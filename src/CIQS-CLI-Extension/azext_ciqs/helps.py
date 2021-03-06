# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

# Ciqs help

helps['ciqs'] = """
    type: group
    short-summary: Manage CIQS(Cloud Intelligence Quickstart) deployments and gallery
"""

# --------------------------------------------------------------------------------------------
# deployment
# --------------------------------------------------------------------------------------------
helps['ciqs deployment'] = """
    type: group
    short-summary: Manage deployments for CIQS(Cloud Intelligence Quickstart).
"""

helps['ciqs deployment list'] = """
    type: command
    short-summary: List all deployments in a subscription.
"""

helps['ciqs deployment create'] = """
    type: command
    short-summary: Create a deployment in a subscription.
"""

helps['ciqs deployment view'] = """
    type: command
    short-summary: View a specific deployment details.
"""

helps['ciqs deployment delete'] = """
    type: command
    short-summary: Delete a specific deployment.
"""

helps['ciqs deployment send-params'] = """
    type: command
    short-summary: Sends paramters to the exisiting deployment.
    long-summery: >
        This should be used when the deployment status is ActionRequired.
        Cannot use both --parameters and --params-file at the same time.
"""

helps['ciqs deployment view-params'] = """
    type: command
    short-summary: View parameters for current provisioning step.
    long-summery: >
        This should be used when the deployment status is ActionRequired.
"""

helps['ciqs deployment view-provisioning-step'] = """
    type: command
    short-summary: View the current provisioning step.
"""

helps['ciqs deployment view-status'] = """
    type: command
    short-summary: View the current status of the deployment.
"""

helps['ciqs deployment wait-terminal-status'] = """
    type: command
    short-summary: Waits for a terminal status to be reached and then return the status.
"""

# --------------------------------------------------------------------------------------------
# gallery
# --------------------------------------------------------------------------------------------
helps['ciqs template'] = """
    type: group
    short-summary: View templates for CIQS(Cloud Inteligent Quick Start)
"""

helps['ciqs template list'] = """
    type: command
    short-summary: List all templates in the CIQS gallery.
    long-summary: >
        Use a connection string to list also from a private gallery.
"""

helps['ciqs template view'] = """
    type: command
    short-summary: View a specific template in the gallery.
    long-summary: >
        Use a connection string to view a template from a private gallery.
"""

helps['ciqs template locations'] = """
    type: command
    short-summary: List all available locations in a subscription for a solution template
    long-summary: >
        These locations can be used when deploying a solution for the specified template.
"""
