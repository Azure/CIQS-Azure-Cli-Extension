# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# TODO: See about making appropriate classes for requests.

from __future__ import print_function

from knack.log import get_logger
from knack.prompting import prompt_pass, NoTTYException
from knack.util import CLIError
from msrest import authentication

from azure.cli.core._profile import Profile
from azure.cli.core.util import in_cloud_console
from azure.cli.core.commands.client_factory import get_subscription_id

from azext_ciqs import api
from azext_ciqs import validators
from azext_ciqs import util
from cloudintelligencequickstart import models
from cloudintelligencequickstart import ciqs_api
import json
import http.client
import msrest.exceptions

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
        logger.info("Using default subscription: " + subscription)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    creds = authentication.BasicTokenAuthentication({'access_token': auth_token[0][1]})
    ciqsapi = ciqs_api.CiqsApi(creds=creds, base_url=api.getEndpoint())
    try:
        logger.info("Sending request.")
        deployments = ciqsapi.get_api_deployments_by_subscription_id(subscription)
    except msrest.exceptions.HttpOperationError as e:
        message = e.response.json()
        raise CLIError(message)
    return deployments

def createDeployment(cmd, name, location, templateId, description=None, parameters=None, parameterFile=None, solutionStorageConnectionString=None, subscription=None):
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
        logger.info("Using default subscription: " + subscription)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    if parameters is not None and parameterFile is not None:
        raise CLIError("May not have parameters and a parameters file at the same time.")
    elif parameterFile is not None:
        logger.info("Using parameter file: " + parameterFile)
        try:
            with open(parameterFile) as jsonfile:
                parameters = json.load(jsonfile)
            logger.info("Parameters loaded.")
        except IOError:
            raise CLIError("Could not open file.")
    elif parameters is not None:
        logger.info("Using parameters from commandline argument.")
        validators.validate_json_arg(parameters)
        parameters = json.loads(parameters)
        logger.info("Parameters loaded")
    creds = authentication.BasicTokenAuthentication({'access_token': auth_token[0][1]})
    ciqsapi = ciqs_api.CiqsApi(creds=creds, base_url=api.getEndpoint())
    request = models.MicrosoftCiqsModelsDeploymentCreateDeploymentRequest(name,
                                                                          location,
                                                                          template_id=templateId,
                                                                          subscription=subscription,
                                                                          description=description,
                                                                          referrer='az ciqs',
                                                                          solution_storage_connection_string=solutionStorageConnectionString,
                                                                          parameters=parameters)
    try:
        logger.info("Sending request.")
        response = ciqsapi.post_api_deployments_by_subscription_id_by_template_id(subscription_id=subscription,
                                                                                  template_id=templateId,
                                                                                  body=request,
                                                                                  ms_asm_refresh_token=auth_token[0][2]['refreshToken'])
    except msrest.exceptions.HttpOperationError as e:
        message = e.response.json()
        raise CLIError(message)
    return response

def getDeploymentParameters(cmd, deploymentId, subscription=None):
    """Gets the parameters required by the user at Action Required status.
    deploymentId: The unique id created at the time the deployment was made.
    subscription[optional]: Provides an alternate subscripton to use if desired.
    """
    currentProvisioningStep = viewCurrentProvisioningStep(cmd, deploymentId, subscription=subscription)
    parameters = currentProvisioningStep.parameters
    parameters = [parameter for parameter in parameters if parameter.hidden != True]
    return parameters

def sendParameters(cmd, deploymentId, parameters=None, parameterFile=None, subscription=None):
    """Sends parameters to the existing deployment. This should be used when
    the deployment status is ActionRequired.
    deploymentId: The unique id created at the time the deployment was made.
    parameters: A string in JSON format with key value pairs for the parameters to send.
    subscription[optional]: Provides an alternate subscription to use if desired.
    """
    if parameters is not None and parameterFile is not None:
        raise CLIError("May not have parameters and a parameters file at the same time.")
    elif parameterFile is not None:
        logger.info("Using parameter file: " + parameterFile)
        try:
            with open(parameterFile) as jsonfile:
                parameters = json.load(jsonfile)
            logger.info("Parameters loaded.")
        except IOError:
            raise CLIError("Could not open file.")
    elif parameters is not None:
        logger.info("Using parameters from commandline argument.")
        validators.validate_sendParameters(cmd, parameters, subscription, deploymentId)
        parameters = json.loads(parameters)
        logger.info("Parameters loaded.")
    else:
        logger.info("No parameters received, building empty json body.")
        parameters = '{}'
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
        logger.info("Using default subscription: " + subscription)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    creds = authentication.BasicTokenAuthentication({'access_token': auth_token[0][1]})
    ciqsapi = ciqs_api.CiqsApi(creds, api.getEndpoint())
    try:
        logger.info("Sending request.")
        response = ciqsapi.put_api_deployments_by_subscription_id_by_deployment_id(subscription, deploymentId, parameters)
    except msrest.exceptions.HttpOperationError as e:
        message = e.response.json()
        raise CLIError(message)
    return response


def viewDeployment(cmd, deploymentId, subscription=None):
    """Returns details about an existing deployment.
    deploymentId: The unique id created at the time the deployment was made.
    subscription[optional]: Provides an alternate subscripton to use if desired.
    """
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
        logger.info("Using default subscription: " + subscription)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    creds = authentication.BasicTokenAuthentication({'access_token': auth_token[0][1]})
    ciqsapi = ciqs_api.CiqsApi(creds=creds, base_url=api.getEndpoint())
    try:
        logger.info("Sending request.")
        deployment = ciqsapi.get_api_deployments_by_subscription_id_by_deployment_id(subscription, deploymentId)
    except msrest.exceptions.HttpOperationError as e:
        message = e.response.json()
        raise CLIError(message)
    return deployment

def viewCurrentProvisioningStep(cmd, deploymentId, subscription=None):
    """Returns the current provisioning step.
    deploymentId: The unique id created at the time the deployment was made.
    subscription[optional]: Provides an alternate subscripton to use if desired.
    """
    # TODO: Consider changing this to take an optional provisioning step number to show instead of only current.
    deployment = viewDeployment(cmd=cmd, deploymentId=deploymentId, subscription=subscription)
    currentProvisioningStepNumber = deployment.deployment.current_provisioning_step
    currentProvisioningStep = deployment.provisioning_steps[currentProvisioningStepNumber]
    return currentProvisioningStep

def viewDeploymentStatus(cmd, deploymentId, subscription=None):
    """Returns the status of the specified deployment.
    deploymentId: The unique id created at the time the deployment was made.
    subscription[optional]: Provides an alternate subscription to use if desired.
    """
    deployment = viewDeployment(cmd=cmd, deploymentId=deploymentId, subscription=subscription)
    status = deployment.deployment.status
    return {'status': status}

def deleteDeployment(cmd, deploymentId, subscription=None):
    """Deletes a deployment.
    deploymentId: The unique id created at the time the deployment was made.
    subscription[optional]: Provides an alternate subscripton to use if desired.
    """
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
        logger.info("Using default subscription: " + subscription)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    creds = authentication.BasicTokenAuthentication({'access_token': auth_token[0][1]})
    ciqsapi = ciqs_api.CiqsApi(creds=creds, base_url=api.getEndpoint())
    try:
        logger.info("Sending request.")
        deleteResponse = ciqsapi.delete_api_deployments_by_subscription_id_by_deployment_id(subscription, deploymentId)
    except msrest.exceptions.HttpOperationError as e:
        message = e.response.json()
        raise CLIError(message)
    return deleteResponse

def waitForTerminalStatus(cmd, deploymentId, subscription=None, timeout=None):
    """Wait for a deployment to reach a terminal status
    deploymentId: The unique id created at the time the deployment was made.
    subscription[optional]: Provides an alternate subscripton to use if desired.
    timeout[optional]: Amount of time before call times out (in second).
    """
    import time
    if timeout is not None:
        logger.info("Parsing timeout.")
        #TODO: Validate that if the timeout exists that it is a float.
        timeout=float(timeout)
    start = time.time()
    status = viewDeploymentStatus(cmd, deploymentId, subscription=subscription)
    while status['status'] not in util.TERMINAL_STATUSES:
        if timeout is not None and time.time() - start > timeout:
            raise CLIError('Call timedout')
        try:
            logger.info("Getting status...")
            status = viewDeploymentStatus(cmd, deploymentId, subscription=subscription)
            logger.info("Status is " + status['status'])
        except CLIError:
            logger.info("Could not find deployement, assume it is deleted.")
            status['status'] = 'deleted'
        time.sleep(5)
    return status

#---------------------------------------------------------------------------------------------
# sub-group ciqs gallery
#---------------------------------------------------------------------------------------------

def listTemplates(cmd, solutionStorageConnectionString=None):
    """Lists templates from the gallery"""
    ciqsapi = ciqs_api.CiqsApi(None, base_url=api.getEndpoint())
    try:
        logger.info("Sending request.")
        templates = ciqsapi.get_api_gallery(solution_storage_connection_string=solutionStorageConnectionString)
    except msrest.exceptions.HttpOperationError as e:
        message = e.response.json()
        raise CLIError(message)
    return templates

def getTemplate(cmd, templateId, solutionStorageConnectionString=None):
    """Gets details about the specified template from the gallery.
    templateId: The unique id of the template.
    """
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token()
    creds = authentication.BasicTokenAuthentication({'access_token': auth_token[0][1]})
    ciqsapi = ciqs_api.CiqsApi(creds=creds, base_url=api.getEndpoint())
    try:
        logger.info("Sending request.")
        template = ciqsapi.get_api_gallery_by_template_id(templateId, solution_storage_connection_string=solutionStorageConnectionString)
    except msrest.exceptions.HttpOperationError as e:
        message = e.response.json()
        raise CLIError(message)
    return template

def listLocations(cmd, templateId, subscription=None, solutionStorageConnectionString=None):
    """Lists the locations which the specifed templateId may be deployed.
    templateId: The unique id of the template.
    subscription[optional]: Provides an alternate subscription to use if desired.
    solutionStorageConnectionString[optional]: Connection string for user's storage account for private solutions.
    """
    if subscription is None:
        subscription = get_subscription_id(cmd.cli_ctx)
        logger.info("Using default subscription: " + subscription)
    profile = Profile(cli_ctx=cmd.cli_ctx)
    auth_token = profile.get_raw_token(subscription=subscription)
    creds = authentication.BasicTokenAuthentication({'access_token': auth_token[0][1]})
    ciqsapi = ciqs_api.CiqsApi(creds=creds, base_url=api.getEndpoint())
    try:
        logger.info("Sending request.")
        locations = ciqsapi.get_api_locations_by_subscription_id_by_template_id(templateId, subscription, solution_storage_connection_string=solutionStorageConnectionString)
    except msrest.exceptions.HttpOperationError as e:
        message = e.response.json()
        raise CLIError(message)
    return locations
