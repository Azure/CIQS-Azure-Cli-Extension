# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftCiqsModelsGalleryContent(Model):
    """MicrosoftCiqsModelsGalleryContent.

    :param format:
    :type format: str
    :param data:
    :type data: str
    :param title:
    :type title: str
    :param internal:
    :type internal: bool
    """

    _attribute_map = {
        'format': {'key': 'format', 'type': 'str'},
        'data': {'key': 'data', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'internal': {'key': 'internal', 'type': 'bool'},
    }

    def __init__(self, format=None, data=None, title=None, internal=None):
        super(MicrosoftCiqsModelsGalleryContent, self).__init__()
        self.format = format
        self.data = data
        self.title = title
        self.internal = internal
