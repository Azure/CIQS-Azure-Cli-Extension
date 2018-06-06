# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict
from collections import defaultdict

def transform_templateListItem(result):
    result = OrderedDict([('Template Id', result['id']),
                        ('Title', result['title']),
                        ('Category', result['category'])])
    return result

def transform_templateList(template_list):
    return [transform_templateListItem(i) for i in template_list]

def transform_templateView(result):
    result = OrderedDict([('Title', result['title']),
                        ('Category', result['category']),
                        ('Estimated Time', result['estimatedTime']),
                        ('Description', result['description'])])
    return result

STATUS_DICT = defaultdict(lambda: 'Unknown',
                         {'actionRequired': 'Action Required',
                         'ready': 'Ready',
                         'failed': 'Failed',
                         'provisioning': 'Provisioning'})

def transform_deploymentListItem(result):
    result = OrderedDict([('Deployment Id', result['uniqueId']),
                        ('Deployment Name', result['name']),
                        ('Location', result['location']),
                        ('Status', STATUS_DICT[result['status']]),
                        ('Created By User', result['createdByUserFriendlyName']),
                        ('Created By Email', result['createdByUserEmail'])])
    return result

def transform_deploymentList(deployment_list):
    return [transform_deploymentListItem(i) for i in deployment_list]
