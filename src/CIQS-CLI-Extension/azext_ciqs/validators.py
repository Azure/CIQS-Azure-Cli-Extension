# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

import json

def validate_json_arg(arg):
    print(arg)
    try:
        arg = json.loads(arg)
    except ValueError:
        raise CLIError('Not valid JSON')
    except:
        raise CLIError('Unknown Error')
    return arg

def validate_sendParamters_parameters(ns):
    if ns.parameters:
        return validate_json_arg(ns.parameters)
