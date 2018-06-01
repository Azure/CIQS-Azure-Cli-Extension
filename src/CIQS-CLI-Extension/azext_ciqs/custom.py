# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

from knack.log import get_logger
from knack.prompting import prompt_pass, NoTTYException
from knack.util import CLIError

from azure.cli.core._profile import Profile
from azure.cli.core.util import in_cloud_console

logger = get_logger(__name__)

# group ciqs
def locations(cmd):
    print('To be implemented')

# group ciqs deployments

def listDeployments(cmd, subscription=None):
    print('To be implemented')

def createDeployment(cmd):
    print('To be implemented')

def deployDeployment(cmd):
    print('To be implemented')

def viewDeployment(cmd):
    print('To be implemented')

def deleteDeployment(cmd):
    print('To be implemented')

# group ciqs gallery

def listGallery(cmd):
    print('To be implemented')

def getTemplateFromGallery(cmd):
    print('To be implemented')