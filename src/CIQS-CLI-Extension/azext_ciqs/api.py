# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from knack.log import get_logger

import json
import http.client
import ssl
import os

logger = get_logger(__name__)

HOST = 'ciqs-api-westus.azurewebsites.net'
PORT = http.client.HTTPS_PORT
TEST_HOST_REMOTE = 'ciqs-api-test-westus.azurewebsites.net'
TEST_HOST_LOCAL = 'localhost'
TEST_PORT_LOCAL = 44332
API_BASE_ENDPOINT = '/api/'
DEPLOYMENT_ENDPOINT = API_BASE_ENDPOINT + 'deployments/'
GALLERY_ENDPOINT = API_BASE_ENDPOINT + 'gallery/'
LOCATIONS_ENDPOINT = API_BASE_ENDPOINT + 'locations/'
TEST_ENVIRONMENT_VAR = 'CIQS_CLI_TEST'

def makeAPICall(method, path, auth_token=None, refresh_token=False, requestBody=None, contentType=None, solutionStorageConnectionString=None):
    """Makes a call to the api with through the given method to the path endpoint provided
    method: The http method to use when making the call.
    path: The path of the endpoint to make the api call.
    auth_token[optional]: The authorization token provided by the Azure CLI.
    refresh_token[optional]: Boolean flag of whether to send a refresh token. Can only be true
        if there is a valid auth_token.
    requestBody[optional]: The request body to send with the call.
    contentType[optional]: Should be used to specify what type of data the request body is.
    solutionStorageConnectionString[optional]: Used if needed to add connection string as a header.
    """
    # How do you add a config file to an Azure CLI extension?
    # Would like to take HOST info from config file.
    host = HOST
    port = PORT
    # Use the environment variable to run api calls against the test api instead of production api.
    if os.getenv(TEST_ENVIRONMENT_VAR, False) == "Remote":
        host = TEST_HOST_REMOTE
        #logger.warning('Using test api...')
    elif os.getenv(TEST_ENVIRONMENT_VAR, False) == "Local":
        host = TEST_HOST_LOCAL
        port = TEST_PORT_LOCAL
        #logger.warning('Running local api...')
    # Build the appropriate headers:
    headers = {'Accept': 'application/json'}
    # Check to see if specific headers should be added.
    if not (auth_token is None):
        headers['Authorization'] = auth_token[0][0] + ' '+ auth_token[0][1]
    if not (contentType is None):
        headers['Content-Type'] = contentType
    if refresh_token == True:
        headers['MS-AsmRefreshToken'] = auth_token[0][2]['refreshToken']
    if not (solutionStorageConnectionString is None):
        headers['SolutionStorageConnectionString'] = solutionStorageConnectionString
    if requestBody is not None and contentType is None:
        raise CLIError('Header "Content-Type" is missing.')
    # Make the https connection, send the request, and get the response
    # If we are testing locally, we can't verify the certificate, so we will ignore it.
    if os.getenv(TEST_ENVIRONMENT_VAR, False) == "Local":
        conn = http.client.HTTPSConnection(host, port=port, context=ssl._create_unverified_context())
    else:
        conn = http.client.HTTPSConnection(host, port=port)
    conn.request(method, path, body=requestBody, headers=headers)
    response = conn.getresponse()
    responseStatus = response.status
    responseBody = response.read().decode('utf-8')
    # Handle response if not a 200
    if responseStatus != 200:
        raise CLIError("Error: Response code " + str(responseStatus) + ": " + responseBody)
    try:
        responseBodyJSON = json.loads(responseBody)
    except json.JSONDecodeError:
        raise CLIError("Could not decode response from server.")
    return responseBodyJSON


class CreateDeploymentRequest:
    """Object to build and send a deployment create request."""

    def __init__(self,
                name,
                location,
                templateId,
                subscription,
                auth_token,
                description=None,
                parameters=None,
                solutionStorageConnectionString=None):
        """Creates an instance of the class.
        name: The name of the deployment. (must be alphanumeric lowercase between 3 to 9 characters beginning with a letter)
        location: The location to deploy the solution to.
        templateId: The unique id of the template which the deployment will be bulit from.
        subscription: The subscription in which to create a deployment to.
        auth_token: The authentication token from the Azure CLI.
        description[optional]: The optional description of the deployment.
        parameters[optional]:
        solutionStorageConnectionString[optional]:
        """
        self.name = name
        self.location = location
        self.templateId = templateId
        self.subscription = subscription
        self.auth_token = auth_token
        self.description = description
        if parameters is not None:
            self.parameters = json.loads(parameters)
        else:
            self.parameters = None
        self.solutionStorageConnectionString = solutionStorageConnectionString

    def _buildRequestBody(self):
        """Used to build the request body to send to the API."""
        data = {}
        data['name'] = self.name
        data['location'] = self.location
        data['templateId'] = self.templateId
        data['subscription'] = self.subscription
        if self.description is not None:
            data['description'] = self.description
        else:
            data['description'] = ''
        if self.parameters is not None:
            data['parameters'] = self.parameters
        if self.solutionStorageConnectionString is not None:
            data['solutionStorageConnectionString'] = self.solutionStorageConnectionString
        data['environment'] = 'prod'
        data['referrer'] = 'az ciqs'
        requestBody = json.dumps(data)
        logger.debug("Request Body:\n" + requestBody)
        return requestBody

    def sendRequest(self):
        """Sends the request. Returns the response."""
        path = DEPLOYMENT_ENDPOINT + '/' + self.subscription + '/' + self.templateId
        requestBody = self._buildRequestBody()
        return makeAPICall('POST',
                          path,
                          auth_token=self.auth_token,
                          requestBody=requestBody,
                          contentType='application/json')
