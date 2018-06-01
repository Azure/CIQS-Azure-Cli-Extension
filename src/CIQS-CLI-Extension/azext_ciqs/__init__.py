# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# 
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

from azure.cli.core import AzCommandsLoader
from azure.cli.core.commands import CliCommandType

import azext_ciqs.helps


class CiqsCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        custom_type = CliCommandType(operations_tmpl='azext_ciqs.custom#{}')
        super(CiqsCommandsLoader, self).__init__(cli_ctx=cli_ctx, custom_command_type=custom_type)

    def load_command_table(self, args):
        #with self.command_group('ciqs') as g:

        with self.command_group('ciqs deployment') as g:
            g.custom_command('list', 'listDeployments')
            g.custom_command('create', 'createDeployment')
            g.custom_command('deploy', 'deployDeployment')
            g.custom_command('view', 'viewDeployment')
            g.custom_command('delete', 'deleteDeployment')

        with self.command_group('ciqs gallery') as g:
            g.custom_command('list', 'listGallery')
            g.custom_command('view', 'getTemplateFromGallery')
            g.custom_command('locations', 'locations')

        return self.command_table

    def load_arguments(self, _):
        pass

COMMAND_LOADER_CLS = CiqsCommandsLoader
