# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import defaultdict
from collections import Set

STATUS_DICT = defaultdict(lambda: 'Unknown',
                         {'created': 'Created',
                         'actionrequired': 'Action Required',
                         'parameterssubmitted': 'Parameters Submitted',
                         'provisioning': 'Provisioning',
                         'ready': 'Ready',
                         'failed': 'Failed',
                         'timeout': 'Timed Out',
                         'deleting': 'Deleting',
                         'deleted': 'Deleted',
                         'deletionfailed': 'Deletion Failed',
                         'interrupted': 'Interrupted'})

def provisioningStatusTransform(status):
    """Transforms provisioning status into a human readable form"""
    if status is None:
        return ''
    status = status.lower()
    return STATUS_DICT[status]

TERMINAL_STATUSES = set(['timeout', 'actionRequired', 'failed', 'ready', 'deleted'])
