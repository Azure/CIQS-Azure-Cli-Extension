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
from azure.cli.core.commands.client_factory import get_subscription_id

from azext_ciqs import api
import json
import http.client

logger = get_logger(__name__)

#---------------------------------------------------------------------------------------------
# group ciqs
#---------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------
# sub-group ciqs deployments
#---------------------------------------------------------------------------------------------

def listDeployments(cmd, subscription=None):
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    path = api.DEPLOYMENT_ENDPOINT + subscription
    return api.makeAPICall('GET', path, auth_token=auth_token)

def createDeployment(cmd, name, location, templateId, description=None, parameters=None, solutionStorageConnectionString=None, subscription=None):
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    path = api.DEPLOYMENT_ENDPOINT
    createData = {}
    createData['name'] = name
    createData['location'] = location
    createData['templateId'] = templateId
    createData['subscription'] = subscription
    if description is not None:
        createData['description'] = description
    else:
        createData['description'] = ''
    if parameters is not None:
        createData['parameters'] = parameters
    if solutionStorageConnectionString is not None:
        createData['solutionStorageConnectionString'] = solutionStorageConnectionString
    createData['environment'] = 'prod'
    createData['referrer'] = 'az ciqs'
    requestBody = json.dumps(createData)
    return api.makeAPICall('POST', path, auth_token=auth_token, requestBody=requestBody, contentType='application/json')

def deployDeployment(cmd, deploymentId, subscription=None):
    raise CLIError('Not Implemented')

def viewDeployment(cmd, deploymentId, subscription=None):
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    path = api.DEPLOYMENT_ENDPOINT + subscription + '/' + deploymentId
    return api.makeAPICall('GET', path, auth_token=auth_token)

def deleteDeployment(cmd, deploymentId, subscription=None):
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    path = api.DEPLOYMENT_ENDPOINT + subscription + '/' + deploymentId
    return api.makeAPICall('DELETE', path, auth_token=auth_token)

#---------------------------------------------------------------------------------------------
# sub-group ciqs gallery
#---------------------------------------------------------------------------------------------

def listTemplates(cmd):
    path = api.GALLERY_ENDPOINT
    return api.makeAPICall('GET', path)

def getTemplate(cmd, templateId):
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token()
    path = api.GALLERY_ENDPOINT + templateId
    return api.makeAPICall('GET', path, auth_token=auth_token)

def listLocations(cmd, templateId, subscription=None):
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    path = api.LOCATIONS_ENDPOINT + templateId + '/' + subscription
    return api.makeAPICall('GET', path, auth_token=auth_token)
