# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

from knack.log import get_logger
from knack.prompting import prompt_pass, NoTTYException
from knack.util import CLIError

from azure.cli.core._profile import Profile
from azure.cli.core.util import in_cloud_console

import json
import http.client

logger = get_logger(__name__)

HOST = 'ciqs-api-westus.azurewebsites.net'

# group ciqs
def locations(cmd):
    print('To be implemented')

# group ciqs deployments

def listDeployments(cmd, subscription=None):
    from azure.cli.core.commands.client_factory import get_subscription_id

    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)

    conn = http.client.HTTPSConnection(HOST, 443)
    path = '/api/deployments/' + subscription
    conn.putrequest('GET', path)
    conn.putheader('Authorization', auth_token[0][0] + ' ' + auth_token[0][1])
    conn.endheaders()
    responseStream = conn.getresponse()

    response = responseStream.read().decode('utf-8')
    responseJSON = json.loads(response)
    #print(json.dumps(responseJSON, sort_keys=True, indent=4, separators=(',', ': ')))
    return responseJSON

def createDeployment(cmd, deploymentObj, subscription=None):
    print('To be implemented')

def deployDeployment(cmd, deploymentId, subscription=None):
    print('To be implemented')

def viewDeployment(cmd, deploymentId, subscription=None):
    print('To be implemented')

def deleteDeployment(cmd, deploymentId, subscription=None):
    print('To be implemented')

# group ciqs gallery

def listTemplates(cmd):
    print('To be implemented')

def getTemplate(cmd, templateId):
    print('To be implemented')