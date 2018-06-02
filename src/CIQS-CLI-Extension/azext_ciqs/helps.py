# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

# Ciqs help

helps['ciqs'] = """
    type: group
    short-summary: Manage CIQS deployments and gallery
"""

helps['ciqs locations'] = """
    type: command
    short-summary: List available locations for templates
"""

# deployment

helps['ciqs deployment'] = """
    type: group
    short-summary: Manage deployments for CIQS
"""

helps['ciqs deployment list'] = """
    type: command
    short-summary: List all deployments in a subscription
"""

helps['ciqs deployment create'] = """
    type: command
    short-summary: Create a deployment in a subscription
"""

helps['ciqs deployment deploy'] = """
    type: command
    short-summary: Execute a specific deployment
"""

helps['ciqs deployment view'] = """
    type: command
    short-summary: View a specific deployment details
"""

helps['ciqs deployment delete'] = """
    type: command
    short-summary: Delete a specific deployment
"""

# gallery

helps['ciqs template'] = """
    type: group
    short-summary: View public templates for CIQS (Cloud Inteligent Quick Start)
"""

helps['ciqs template list'] = """
    type: command
    short-summary: List all templates in the public gallery
"""

helps['ciqs template view'] = """
    type: command
    short-summary: View a specific template in the gallery
"""