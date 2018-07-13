# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

import json

from azext_ciqs import custom

def validate_json_arg(arg):
    try:
        arg = json.loads(arg)
    except ValueError:
        raise CLIError('Not valid JSON')
    return arg

def validate_sendParamters_parameters(ns):
    if ns.parameters:
        return validate_json_arg(ns.parameters)

def validate_sendParameters(cmd, parameters, subscription, deploymentId):
    requiredParams = custom.getDeploymentParameters(cmd, deploymentId, subscription=subscription)
    validate_json_arg(parameters)
    parametersJson = json.loads(parameters)
    for key in parametersJson:
        for i in range(0, len(requiredParams)):
            if requiredParams[i]['name'] == key and 'allowedValues' in requiredParams[i]:
                if not (parametersJson[key] in requiredParams[i]['allowedValues']):
                    message = "Parameter " + str(parametersJson[key]) + " is not an allowed value for " + key + ".\n" + "Allowed Values are: " + ', '.join(requiredParams[i]['allowedValues'])
                    raise CLIError(message)
