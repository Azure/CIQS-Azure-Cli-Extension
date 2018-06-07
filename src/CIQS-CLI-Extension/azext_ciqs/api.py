# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

import json
import http.client
import os

HOST = 'ciqs-api-westus.azurewebsites.net'
TEST_HOST = 'ciqs-api-test-westus.azurewebsites.net'
API_BASE_ENDPOINT = '/api/'
DEPLOYMENT_ENDPOINT = API_BASE_ENDPOINT + 'deployments/'
GALLERY_ENDPOINT = API_BASE_ENDPOINT + 'gallery/'
LOCATIONS_ENDPOINT = API_BASE_ENDPOINT + 'locations/'
TEST_ENVIRONMENT_VAR = 'CIQS_CLI_TEST'

def makeAPICall(method, path, auth_token=None, refresh_token=False, requestBody=None, contentType=None):
    # How do you add a config file to an Azure CLI extension?
    # Would like to take HOST info from config file.
    host = HOST
    if os.getenv(TEST_ENVIRONMENT_VAR, False) == "True":
        host = TEST_HOST
        print('Using test api...')
    headers = {'Accept': 'application/json'}
    if not (auth_token is None):
        headers['Authorization'] = auth_token[0][0] + ' '+ auth_token[0][1]
    if not (contentType is None):
        headers['Content-Type'] = contentType
    if refresh_token == True:
        headers['MS-AsmRefreshToken'] = auth_token[0][2]['refreshToken']
    conn = http.client.HTTPSConnection(host)
    conn.request(method, path, body=requestBody, headers=headers)
    response = conn.getresponse()
    responseStatus = response.status
    responseBody = response.read().decode('utf-8')
    if responseStatus != 200:
        raise CLIError("Error: Response code " + str(responseStatus) + ": " + responseBody)
    responseBodyJSON = json.loads(responseBody)
    return responseBodyJSON
