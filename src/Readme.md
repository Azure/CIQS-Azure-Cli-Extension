# Description
This repository contains the implementation of CIQS(Cloud Intelligence Quickstart) Azure Cli extension. It help AI solution authoring and provisioning platform (a.k.a CIQS) reach out to a broader set of customers, including data scientists, data engineers, developers and ISVs.

# Build Instructions
In src/CIQS-CLI-Extension run the following command:
```
python setup.py bdist_wheel
```
This will create a `dist` directory containing your `.whl` extension.

# Install instructions
In the Azure CLI runn the following command:
```
az extension add --source ~/location_of_wheel_file/FILENAME.whl
```
See https://docs.microsoft.com/en-us/cli/azure/azure-cli-extensions-overview?view=azure-cli-latest for details of installing extensions.
