# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

import configparser

import json
import http.client
import os

HOST = 'ciqs-api-westus.azurewebsites.net'
TEST_HOST = 'ciqs-api-test-westus.azurewebsites.net'
API_BASE_ENDPOINT = '/api/'
DEPLOYMENT_ENDPOINT = API_BASE_ENDPOINT + 'deployments/'
GALLERY_ENDPOINT = API_BASE_ENDPOINT + 'gallery/'
LOCATIONS_ENDPOINT = API_BASE_ENDPOINT + 'locations/'

def makeAPICall(cmd, method, path, auth_token=None):
    # How do you add a config file to an Azure CLI extension?
    # Would like to take HOST info from config file.
    host = HOST
    if os.getenv('CIQS_CLI_TEST', False) == "True":
        host = TEST_HOST
        print('Using test api...')
    conn = http.client.HTTPSConnection(host, http.client.HTTPS_PORT)
    conn.putrequest(method, path)
    if not (auth_token is None):
        conn.putheader('Authorization', auth_token[0][0] + ' ' + auth_token[0][1])
    conn.endheaders()
    response = conn.getresponse()
    responseStatus = response.status
    responseBody = response.read().decode('utf-8')
    if responseStatus != 200:
        raise CLIError("Error: Response code " + str(responseStatus) + ": " + responseBody)
    responseBodyJSON = json.loads(responseBody)
    return responseBodyJSON
