# Testing
This is for all tests designed to run against the CIQS CLI Extension.
The tests should be scripts that run various commands on the CIQS CLI Extension.

## Prerequistes
* Azure CLI must be installed
* CIQS-CLI-Extension must be installed to the Azure CLI

## Powershell Test Scripts
Currently all the tests are designed to run in powershell. The tess are designed to give a pass or fail based on the exit code of the test.
### Powershell Test Script Requirements
* All powershell tests should be in the testPowershellScripts directory.
* If a test passed, it should exit with code `0`.
* If a test fails, it should exit with nonzero code.
### Running the Powershell tests
To run the powershell tests run the following command in powershell in this directory:
```Powershell
.\RunPowershellTests.ps1
```
This will output for each test a "Passed" or "Failed" with the exit code.