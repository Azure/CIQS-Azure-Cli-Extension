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
import sys

logger = get_logger(__name__)

#---------------------------------------------------------------------------------------------
# group ciqs
#---------------------------------------------------------------------------------------------

HOST = 'ciqs-api-westus.azurewebsites.net'

def _makeAPICall(cmd, method, path, auth_token=None):
    conn = http.client.HTTPSConnection(HOST, http.client.HTTPS_PORT)
    conn.putrequest(method, path)
    if not (auth_token is None):
        conn.putheader('Authorization', auth_token[0][0] + ' ' + auth_token[0][1])
    conn.endheaders()
    responseStream = conn.getresponse()
    response = responseStream.read().decode('utf-8')
    responseJSON = json.loads(response)
    return responseJSON

#---------------------------------------------------------------------------------------------
# sub-group ciqs deployments
#---------------------------------------------------------------------------------------------

def listDeployments(cmd, subscription=None):
    from azure.cli.core.commands.client_factory import get_subscription_id
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    path = '/api/deployments/' + subscription
    return _makeAPICall(cmd, 'GET', path, auth_token=auth_token)

def createDeployment(cmd, deploymentObj, subscription=None):
    print('To be implemented')

def deployDeployment(cmd, deploymentId, subscription=None):
    print('To be implemented')

def viewDeployment(cmd, deploymentId, subscription=None):
    from azure.cli.core.commands.client_factory import get_subscription_id
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    path = '/api/deployments/' + subscription + '/' + deploymentId
    return _makeAPICall(cmd, 'GET', path, auth_token=auth_token)

def deleteDeployment(cmd, deploymentId, subscription=None):
    from azure.cli.core.commands.client_factory import get_subscription_id
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    path = '/api/deployments/' + subscription + '/' + deploymentId
    return _makeAPICall(cmd, 'DELETE', path, auth_token=auth_token)

#---------------------------------------------------------------------------------------------
# sub-group ciqs gallery
#---------------------------------------------------------------------------------------------

def listTemplates(cmd):
    path = '/api/gallery'
    return _makeAPICall(cmd, 'GET', path)

def getTemplate(cmd, templateId):
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token()
    path = '/api/gallery/' + templateId
    return _makeAPICall(cmd, 'GET', path, auth_token=auth_token)

def locations(cmd, templateId, subscription=None):
    from azure.cli.core.commands.client_factory import get_subscription_id
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    path = '/api/locations/' + templateId + '/' + subscription
    return _makeAPICall(cmd, 'GET', path, auth_token=auth_token)
