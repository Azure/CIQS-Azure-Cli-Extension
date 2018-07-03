# TestHelloWorldAndDeletingDeployment

$env:CIQS_CLI_TEST="Remote"
$deployment = az ciqs deployment create -l "East US" -n "testcli01" -t "ciqs-helloworld" | ConvertFrom-Json

Start-Sleep -Seconds 5

if (-not $deployment.status -eq "ready") {
    exit 1
}

$deleteStatus = az ciqs deployment delete -d $deployment.uniqueId | ConvertFrom-Json

if (-not $deleteStatus.isSucceeded -eq $true) {
    exit 2
}

exit 0
