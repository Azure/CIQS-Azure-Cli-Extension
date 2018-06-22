# Description

This repository contains the implementation of CIQS(Cloud Intelligence Quickstart) Azure Cli extension. It help AI solution authoring and provisioning platform (a.k.a CIQS) reach out to a broader set of customers, including data scientists, data engineers, developers and ISVs.

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

# Depdendencies

* Azure CLI 2.0 (install instructions [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest))
* Python 2 or Python 3

# Build Instructions

Navigate to src/CIQS-CLI-Extension.
Run the following command:
```
python setup.py bdist_wheel
```
This will create a `dist` directory containing your `.whl` extension.
The `.whl` file will be used to install the extension.

# Install Instructions

Navigate to src/CIQS-CLI-Extension.

Run the following command where "{FILENAME}.whl" is the file generated when building:
```
az extension add --source ./dist/{FILENAME}.whl
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

# Tutorials

[From beginning to end](end2endTutorial.md)
