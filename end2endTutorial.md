# From Beginning to End

This tutorial will walk you through how to use CIQS extension of Azure CLI.
When finished with this tutorial, you should be able to do the following tasks:
1. View a list of all solution templates in the CIQS public gallery.
2. View details of a specific solution template in the CIQS public gallery.
3. Create a CIQS deployment from a template in the CIQS public gallery.
4. Run through provisioning steps and sending appropriate parameters.
5. Delete a deployment.

The CIQS Extension is built into 2 subgroups:
1. deployment
   This is used to create, maintain, and delete deployments
2. template
   This is used to view templates used to deploy solutions

**This tutorial assumes you have already installed the Azure CLI and the CIQS extension.**

## First, we must login to the Azure CLI.

There are a few ways to do this. This tutorial will only go through one way.
You can find more about loging in with Azure [here](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest).

To login:
1. Run the following command into the command line:  
   ```Azure CLI
   az login
   ```
   You get a code to use in the next step.
2. Use a web browser to open the page [https://aka.ms/devicelogin] and enter the code to authenticate.
3. Log in with your account credentials in the browser.

You are now logged in.

You can set your default subscription in the Azure CLI.

If your subscription id was 01234567-89ab-cdef-ghij-456789abcdef0, then this would be the command:
```Azure CLI
az account set 01234567-89ab-cdef-0123-456789abcdef0
```

By default the CIQS extension will use this subscription.
You can add a parameter to CIQS commands to specfify to use a different subscription.

## View a list of all solution templates in the CIQS public gallery

Run the following command:
```Azure CLI
az ciqs template list
```
This will give the details of each template in the CIQS public gallery.

To see a simplified list in a human readable table, run the following command:
```Azure CLI
az ciqs template -o table
```
This will give the template id, title, and category.

## View details of a specific solution template in the CIQS public gallery

We need to know which template we want details with before we can see the details of it.
We can select any of the templates from the list in the previous section.

For this tutorial we will use Anomaly Detection in Real-time Data Streams.
Its template id is anomalydetectionpcsv2.

Run the following command to see the details of this template:
```Azure CLI
az ciqs template view --template-id anomalydetectionpcsv2
```

This will give us a lot infomation regarding the template.
In order to deploy a solution with this template, we only need the template id.

## Create a CIQS deployment from a template in the CIQS public gallery

Before we create the deployment, we must first find out what valid locations this template can deployed to.

To do this, we will use the template id to ask ciqs where we can deploy to.
Run the following command:
```Azure CLI
az ciqs template locations --template-id anomalydetectionpcsv2
```
This lists all locations for the template to be deployed on.

We will select a location for the next step.

We need 3 things to create the deployment.
1. Location
2. Name
3. Template

For location we will use "South Central US".
For name we will use "tutorial1".
For the template we will use "anomalydetectionpcsv2".

To create this deployment, we will run the following command:
```Azure CLI
az ciqs deployment create --location "South Central US" --name tutorial1 --template-id anomalydetectionpcsv2
```
If successful, we will see some output. Keep note of the uniqueId, we will use it from this point on.
Through this tutorial I will use the uniqueId "1234567890-abcd-efgh-ijkl-mnopqrstuvw".

## Run through provisioning steps and sending appropriate parameters

First we should find out the status of our deployment.
Run the following command:
```Azure CLI
az ciqs deployment view-status --deployment-id 1234567890-abcd-efgh-ijkl-mnopqrstuvw
```
You should get a status of "actionRequired".
This is because user action is needed. We need to enter some parameters.

To view required parameters, run the following:
```Azure CLI
az ciqs deployment view-params --deployment-id 1234567890-abcd-efgh-ijkl-mnopqrstuvw
```
We should see 3 objects in response. It will tell us what valid input is, what the names of parameters, and other info.

To send the values for the parameters, we need to give a JSON string into a command.
There are two options:
1. Pass in a JSON filename as a commandline arg
2. Pass the JSON string as a command line arg

*To pass a JSON string as a command line requires escape characters and varies depending on the command line being used*

For this tutorial, we will use a JSON file.

Create the following file params1.json:
```json
{
    "mLParams": "{\"tspikedetector.sensitivity\":\"3\",\"zspikedetector.sensitivity\":\"3\",\"trenddetector.sensitivity\":\"3.25\",\"bileveldetector.sensitivity\":\"3.25\"}",
    "sqlServerUserName": "fakeuser",
    "sqlServerPassword": "F#kePa55w0Rd"
}
```

Now we will send the parameters with the following command:
```Azure CLI
az ciqs deployment send-params --deployment-id 1234567890-abcd-efgh-ijkl-mnopqrstuvw --parameterFile params1.json
```
We should see a status of "parametersSubmitted" in the response. If it is "actionRequried", then some parameters were invalid.

When we run view-status again, we should see the status has changed to "provisioning."
When the status changes to "actionRequired" we again view the parameters and input them in the same manner.

## Delete a deployment

When it is time for a deployment to be deleted, simply run the following command:
```Azure CLI
ciqs deployment delete --deployment-id 1234567890-abcd-efgh-ijkl-mnopqrstuvw
```

## Conclusion

Now you have successfully ran CIQS from end to end.