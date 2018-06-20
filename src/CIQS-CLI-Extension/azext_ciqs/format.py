# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict
from collections import defaultdict

from azext_ciqs import util

def transform_templateListItem(result):
    """Transforms an item from a template list into a row in a table"""
    result = OrderedDict([('Template Id', result['id']),
                        ('Title', result['title']),
                        ('Category', result['category'])])
    return result

def transform_templateList(template_list):
    """Transforms a template list into a table in human readable form"""
    return [transform_templateListItem(i) for i in template_list]

def transform_templateView(result):
    """Transforms a single template into a one row table"""
    result = OrderedDict([('Title', result['title']),
                        ('Template Id', result['id']),
                        ('Category', result['category']),
                        ('Estimated Time', result['estimatedTime']),
                        ('Description', result['description'])])
    return result

def transform_deploymentListItem(result):
    """Transforms an item from a deployment list into a row in a table"""
    result = OrderedDict([('Deployment Id', result['uniqueId']),
                        ('Deployment Name', result['name']),
                        ('Location', result['location']),
                        ('Status', util.provisioningStatusTransform(result['status'])),
                        ('Created By User', result['createdByUserFriendlyName']),
                        ('Created By Email', result['createdByUserEmail'])])
    return result

def transform_deploymentList(deployment_list):
    """Transforms the deployment list into a human readable table"""
    return [transform_deploymentListItem(i) for i in deployment_list]

def transform_deploymentView(result):
    """Transforms the output of a deployment into human readable format"""
    result = transform_deploymentListItem(result['deployment'])
    return result

def transform_deploymentParam(result):
    """Transforms a paramter into a row for a table"""
    result = OrderedDict([('Description', result['description']),
                        ('Name', result['name']),
                        ('Type', result['type']),
                        ('Lists Allowed Values', 'Yes' if 'allowedValues' in result else 'No'),
                        ('Default', result['defaultValue'] if 'defaultValue' in result else '')])
    return result

def transform_deploymentViewParamsList(param_list):
    return [transform_deploymentParam(i) for i in param_list]

def transform_deploymentViewStatus(result):
    return OrderedDict([('Status', util.provisioningStatusTransform(result['status']))])
