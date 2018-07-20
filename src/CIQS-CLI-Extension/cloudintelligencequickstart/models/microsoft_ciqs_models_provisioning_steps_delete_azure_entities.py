# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftCiqsModelsProvisioningStepsDeleteAzureEntities(Model):
    """MicrosoftCiqsModelsProvisioningStepsDeleteAzureEntities.

    :param resource_groups:
    :type resource_groups:
     list[~microsoft.swagger.codegen.cloudintelligencequickstart.models.MicrosoftCiqsModelsProvisioningStepsAzureResourceGroup]
    :param resources:
    :type resources:
     list[~microsoft.swagger.codegen.cloudintelligencequickstart.models.MicrosoftCiqsModelsProvisioningStepsAzureResourceList]
    :param applications:
    :type applications:
     list[~microsoft.swagger.codegen.cloudintelligencequickstart.models.MicrosoftCiqsModelsProvisioningStepsAadApplication]
    :param user_input_required:
    :type user_input_required: bool
    :param standalone:
    :type standalone: bool
    :param parameters:
    :type parameters:
     list[~microsoft.swagger.codegen.cloudintelligencequickstart.models.MicrosoftCiqsModelsGalleryParameter]
    :param title:
    :type title: str
    :param instructions:
    :type instructions:
     ~microsoft.swagger.codegen.cloudintelligencequickstart.models.MicrosoftCiqsModelsGalleryContent
    :param retriable:
    :type retriable: bool
    :param auto_retry_count:
    :type auto_retry_count: int
    :param timeout:
    :type timeout: int
    """

    _attribute_map = {
        'resource_groups': {'key': 'resourceGroups', 'type': '[MicrosoftCiqsModelsProvisioningStepsAzureResourceGroup]'},
        'resources': {'key': 'resources', 'type': '[MicrosoftCiqsModelsProvisioningStepsAzureResourceList]'},
        'applications': {'key': 'applications', 'type': '[MicrosoftCiqsModelsProvisioningStepsAadApplication]'},
        'user_input_required': {'key': 'userInputRequired', 'type': 'bool'},
        'standalone': {'key': 'standalone', 'type': 'bool'},
        'parameters': {'key': 'parameters', 'type': '[MicrosoftCiqsModelsGalleryParameter]'},
        'title': {'key': 'title', 'type': 'str'},
        'instructions': {'key': 'instructions', 'type': 'MicrosoftCiqsModelsGalleryContent'},
        'retriable': {'key': 'retriable', 'type': 'bool'},
        'auto_retry_count': {'key': 'autoRetryCount', 'type': 'int'},
        'timeout': {'key': 'timeout', 'type': 'int'},
    }

    def __init__(self, resource_groups=None, resources=None, applications=None, user_input_required=None, standalone=None, parameters=None, title=None, instructions=None, retriable=None, auto_retry_count=None, timeout=None):
        super(MicrosoftCiqsModelsProvisioningStepsDeleteAzureEntities, self).__init__()
        self.resource_groups = resource_groups
        self.resources = resources
        self.applications = applications
        self.user_input_required = user_input_required
        self.standalone = standalone
        self.parameters = parameters
        self.title = title
        self.instructions = instructions
        self.retriable = retriable
        self.auto_retry_count = auto_retry_count
        self.timeout = timeout
