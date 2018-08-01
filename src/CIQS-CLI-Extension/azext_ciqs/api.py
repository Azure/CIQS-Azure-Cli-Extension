# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from knack.log import get_logger

import json
import http.client
import ssl
import os

logger = get_logger(__name__)

TEST_ENVIRONMENT_VAR = 'CIQS_CLI_TEST'

def getEndpoint():
    logger.info("Using test api...")
    if os.getenv(TEST_ENVIRONMENT_VAR, False) == "Remote":
        base_url = 'https://ciqs-api-test-westus.azurewebsites.net'
        return base_url
    elif os.getenv(TEST_ENVIRONMENT_VAR, False) == "Local":
        logger.info("Using test api...")
        base_url = 'https://localhost:44332'
        return base_url
    else:
        return None
