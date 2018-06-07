# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

from azure.cli.core import AzCommandsLoader
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.profile._completers import get_subscription_id_list

import azext_ciqs.helps
import azext_ciqs.format

class CiqsCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        custom_type = CliCommandType(operations_tmpl='azext_ciqs.custom#{}')
        super(CiqsCommandsLoader, self).__init__(cli_ctx=cli_ctx, custom_command_type=custom_type)

    def load_command_table(self, args):

        with self.command_group('ciqs deployment') as g:
            g.custom_command('list', 'listDeployments', table_transformer=format.transform_deploymentList)
            g.custom_command('create', 'createDeployment')
            g.custom_command('deploy', 'deployDeployment')
            g.custom_command('view', 'viewDeployment')
            g.custom_command('delete', 'deleteDeployment')

        with self.command_group('ciqs template') as g:
            g.custom_command('list', 'listTemplates', table_transformer=format.transform_templateList)
            g.custom_command('view', 'getTemplate', table_transformer=format.transform_templateView)
            g.custom_command('locations', 'listLocations')

        return self.command_table

    def load_arguments(self, command):
        
        with self.argument_context('ciqs') as c:
            c.argument('templateId', options_list=('--template-id', '-t'), help='ID of template to use')
            c.argument('subscription', options_list=('--subscription', '-s'), help='Name or ID of subscription. If none is supplied, the default subscription for the account will be used.', completer=get_subscription_id_list)

        with self.argument_context('ciqs deployment') as c:
            c.argument('deploymentId', options_list=('--deployment-id',), help='ID of deployment.')
        
        with self.argument_context('ciqs deployment create') as c:
            c.argument('name', options_list=('--name', '-n'), help='Deployment name must be between 3 and 9 characters, start with a lowercase letter, and contain only lowercase letters and numbers.')
            c.argument('location', options_list=('--location', '-l'), help='Location to deploy. See "az ciqs template locations -h"')
            c.argument('description', options_list=('--description', '-d'), help='Describe the deployment.')


COMMAND_LOADER_CLS = CiqsCommandsLoader
