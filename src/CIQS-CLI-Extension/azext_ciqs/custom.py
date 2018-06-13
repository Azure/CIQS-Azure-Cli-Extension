# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# TODO: See about making appropriate classes for requests.

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
    """Lists the deployments for the supplied subscription. If no subscription
    is supplied, it will use the default subscription of the current logged in
    user of the Azure CLI.
    subscription[optional]: Provides an alternate subscription to use if desired.
    """
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    path = api.DEPLOYMENT_ENDPOINT + subscription
    return api.makeAPICall('GET', path, auth_token=auth_token)

def createDeployment(cmd, name, location, templateId, description=None, parameters=None, solutionStorageConnectionString=None, subscription=None):
    """Creates a deployment with the specified parameters.
    name: The name of the deployment. (must be alphanumeric lowercase between 3 to 9 characters beginning with a letter)
    location: The location to deploy the solution to.
    templateId: The unique id of the template which the deployment will be bulit from.
    description[optional]: The optional description of the deployment.
    parameters[optional]:
    solutionStorageConnectionString[optional]:
    subscription[optional]: Provides an alternate subscription to use if desired.
    """
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    createDeploymentRequest = api.CreateDeploymentRequest(name,
                                                         location,
                                                         templateId,
                                                         subscription,
                                                         auth_token,
                                                         description=description,
                                                         parameters=parameters,
                                                         solutionStorageConnectionString=solutionStorageConnectionString)
    return createDeploymentRequest.sendRequest()

def deployDeployment(cmd, deploymentId, subscription=None):
    raise CLIError('Not Implemented')

def sendParameters(cmd, deploymentId, parameters, subscription=None):
    """Sends parameters to the existing deployment. This should be used when
    the deployment status is ActionRequired.
    deploymentId: The unique id created at the time the deployment was made.
    parameters: A string in JSON format with key value pairs for the parameters to send.
    subscription[optional]: Provides an alternate subscription to use if desired.
    """
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    path = api.DEPLOYMENT_ENDPOINT + subscription + '/' + deploymentId
    return api.makeAPICall('PUT', path, auth_token=auth_token, refresh_token=True, requestBody=parameters, contentType='application/json')


def viewDeployment(cmd, deploymentId, subscription=None):
    """Returns details about an existing deployment.
    deploymentId: The unique id created at the time the deployment was made.
    subscription[optional]: Provides an alternate subscripton to use if desired.
    """
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    path = api.DEPLOYMENT_ENDPOINT + subscription + '/' + deploymentId
    return api.makeAPICall('GET', path, auth_token=auth_token)

def viewCurrentProvisioningStep(cmd, deploymentId, subscription=None):
    """Returns the current provisioning step.
    deploymentId: The unique id created at the time the deployment was made.
    subscription[optional]: Provides an alternate subscripton to use if desired.
    """
    #TODO: Consider changing this to take an optional provisioning step number to show instead of only current.
    deployment = viewDeployment(cmd=cmd, deploymentId=deploymentId, subscription=subscription)
    currentProvisioningStepNumber = deployment['deployment']['currentProvisioningStep']
    currentProvisioningStep = deployment['provisioningSteps'][currentProvisioningStepNumber]
    return currentProvisioningStep

def viewDeploymentStatus(cmd, deploymentId, subscription=None):
    deployment = viewDeployment(cmd=cmd, deploymentId=deploymentId, subscription=subscription)
    status = deployment['deployment']['status']
    return status

def deleteDeployment(cmd, deploymentId, subscription=None):
    """Deletes a deployment.
    deploymentId: The unique id created at the time the deployment was made.
    subscription[optional]: Provides an alternate subscripton to use if desired.
    """
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    path = api.DEPLOYMENT_ENDPOINT + subscription + '/' + deploymentId
    return api.makeAPICall('DELETE', path, auth_token=auth_token)

#---------------------------------------------------------------------------------------------
# sub-group ciqs gallery
#---------------------------------------------------------------------------------------------

def listTemplates(cmd, solutionStorageConnectionString=None):
    """Lists templates from the gallery"""
    path = api.GALLERY_ENDPOINT
    return api.makeAPICall('GET', path, solutionStorageConnectionString=solutionStorageConnectionString)

def getTemplate(cmd, templateId):
    """Gets details about the specified template from the gallery.
    templateId: The unique id of the template.
    """
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token()
    path = api.GALLERY_ENDPOINT + templateId
    return api.makeAPICall('GET', path, auth_token=auth_token)

def listLocations(cmd, templateId, subscription=None, solutionStorageConnectionString=None):
    """Lists the locations which the specifed templateId may be deployed.
    templateId: The unique id of the template.
    subscription[optional]: Provides an alternate subscription to use if desired.
    """
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    path = api.LOCATIONS_ENDPOINT + templateId + '/' + subscription
    return api.makeAPICall('GET', path, auth_token=auth_token, solutionStorageConnectionString=solutionStorageConnectionString)
