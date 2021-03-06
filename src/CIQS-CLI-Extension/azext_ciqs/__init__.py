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
import azext_ciqs.validators

class CiqsCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        custom_type = CliCommandType(operations_tmpl='azext_ciqs.custom#{}')
        super(CiqsCommandsLoader, self).__init__(cli_ctx=cli_ctx, custom_command_type=custom_type)

    def load_command_table(self, args):

        with self.command_group('ciqs deployment') as g:
            g.custom_command('list', 'listDeployments', table_transformer=format.transform_deploymentList)
            g.custom_command('create', 'createDeployment')
            g.custom_command('view', 'viewDeployment', table_transformer=format.transform_deploymentView)
            g.custom_command('delete', 'deleteDeployment')
            g.custom_command('send-params', 'sendParameters')
            g.custom_command('view-provisioning-step', 'viewCurrentProvisioningStep', table_transformer=format.transform_provisioningStep)
            g.custom_command('view-status', 'viewDeploymentStatus', table_transformer=format.transform_deploymentViewStatus)
            g.custom_command('view-params', 'getDeploymentParameters', table_transformer=format.transform_deploymentViewParamsList)
            g.custom_command('wait-terminal-status', 'waitForTerminalStatus')

        with self.command_group('ciqs template') as g:
            g.custom_command('list', 'listTemplates', table_transformer=format.transform_templateList)
            g.custom_command('view', 'getTemplate', table_transformer=format.transform_templateView)
            g.custom_command('locations', 'listLocations')

        return self.command_table

    def load_arguments(self, command):
        
        with self.argument_context('ciqs') as c:
            c.argument('templateId', options_list=('--template-id', '-t'), help='Unique ID of a solution template')
            c.argument('subscription', options_list=('--subscription', '-s'), help='Subscription Id. If none is supplied, the default subscription for the account will be used.', completer=get_subscription_id_list)
            c.argument('solutionStorageConnectionString', options_list=('--connection-string',), help='This is the Solution Storage Connection String that is used to access your private gallery.')

        with self.argument_context('ciqs deployment') as c:
            c.argument('deploymentId', options_list=('--deployment-id', '-d'), help='ID of deployment.')
            c.argument('parameters', options_list=('--parameters',), validator=validators.validate_sendParamters_parameters, help='Parameters in JSON format to send to the deployment.', )
            c.argument('parameterFile', options_list=('--param-file',), help='JSON file containing parameters to send.')

        with self.argument_context('ciqs deployment create') as c:
            c.argument('name', options_list=('--name', '-n'), help='Deployment name must be between 3 and 9 characters, start with a lowercase letter, and contain only lowercase letters and numbers.')
            c.argument('location', options_list=('--location', '-l'), help='Location to deploy. See "az ciqs template locations -h"')
            c.argument('description', options_list=('--description',), help='Describe the deployment.')

        with self.argument_context('ciqs deployment wait-terminal-status') as c:
            c.argument('timeout', options_list=('--timeout',), help='Max time to wait for terminal status')

COMMAND_LOADER_CLS = CiqsCommandsLoader
