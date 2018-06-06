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
from . import api

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
    return api.makeAPICall(cmd, 'GET', path, auth_token=auth_token)

def createDeployment(cmd, deploymentObj, subscription=None):
    raise CLIError('Not Implemented')

def deployDeployment(cmd, deploymentId, subscription=None):
    raise CLIError('Not Implemented')

def viewDeployment(cmd, deploymentId, subscription=None):
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    path = api.DEPLOYMENT_ENDPOINT + subscription + '/' + deploymentId
    return api.makeAPICall(cmd, 'GET', path, auth_token=auth_token)

def deleteDeployment(cmd, deploymentId, subscription=None):
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    path = api.DEPLOYMENT_ENDPOINT + subscription + '/' + deploymentId
    return api.makeAPICall(cmd, 'DELETE', path, auth_token=auth_token)

#---------------------------------------------------------------------------------------------
# sub-group ciqs gallery
#---------------------------------------------------------------------------------------------

def listTemplates(cmd):
    path = api.GALLERY_ENDPOINT
    return api.makeAPICall(cmd, 'GET', path)

def getTemplate(cmd, templateId):
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token()
    path = api.GALLERY_ENDPOINT + templateId
    return api.makeAPICall(cmd, 'GET', path, auth_token=auth_token)

def locations(cmd, templateId, subscription=None):
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    path = api.LOCATIONS_ENDPOINT + templateId + '/' + subscription
    return api.makeAPICall(cmd, 'GET', path, auth_token=auth_token)
