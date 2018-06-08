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
