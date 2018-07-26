# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftCiqsModelsGalleryRegexEntry(Model):
    """MicrosoftCiqsModelsGalleryRegexEntry.

    :param regex:
    :type regex: str
    :param flags:
    :type flags: str
    :param error_message:
    :type error_message: str
    """

    _attribute_map = {
        'regex': {'key': 'regex', 'type': 'str'},
        'flags': {'key': 'flags', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
    }

    def __init__(self, regex=None, flags=None, error_message=None):
        super(MicrosoftCiqsModelsGalleryRegexEntry, self).__init__()
        self.regex = regex
        self.flags = flags
        self.error_message = error_message