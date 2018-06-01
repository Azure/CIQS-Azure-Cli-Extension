# Description
This repository contains the implementation of CIQS(Cloud Intelligence Quickstart) Azure Cli extension. It help AI solution authoring and provisioning platform (a.k.a CIQS) reach out to a broader set of customers, including data scientists, data engineers, developers and ISVs.

# Build Instructions
In src/CIQS-CLI-Extension run the following command:
```
python setup.py bdist_wheel
```
This will create a `dist` directory containing your `.whl` extension.

# Install Instructions
In the Azure CLI run the following command:
```
az extension add --source ~/location_of_wheel_file/FILENAME.whl
```
See https://docs.microsoft.com/en-us/cli/azure/azure-cli-extensions-overview?view=azure-cli-latest for details of installing extensions.

# Run Instructions
Now the extension should be install directly into the Azure CLI.
To see availabe subgroups and commands run the following command:
```
az ciqs --help
```
An example command that would list all deployments in a given subsciption would be as follows:
```
az ciqs deployment list --subscription "xxxx-xxxx-xxxx-xxxx"
```
