# TestHelloFunctionsJsDeployment

$deployment = az ciqs deployment create -t "ciqs-hellofunctions-js" -n "clitest03" -l "East US" | ConvertFrom-Json
if($LASTEXITCODE -ne 0){
    exit 1
}

$deploymentStatus = az ciqs deployment wait-terminal-status --deployment-id $deployment.uniqueId --timeout 180000 | ConvertFrom-Json
if($LASTEXITCODE -ne 0){
    exit 2
}
if ($deploymentStatus.status -ne "actionRequired"){
    exit 3
}

$paramJson = @'
{"""Name""":"""Pikachu"""}
'@

az ciqs deployment send-params --deployment-id $deployment.uniqueId --parameters $paramJson
if($LASTEXITCODE -ne 0){
    exit 4
}

$deploymentStatus = az ciqs deployment wait-terminal-status --deployment-id $deployment.uniqueId --timeout 180000 | ConvertFrom-Json
if ($LASTEXITCODE -ne 0){
    exit 5
}
if ($deploymentStatus.status -ne "ready"){
    exit 6
}

$provisioningStep = az ciqs deployment view-provisioning-step --deployment-id $deployment.uniqueId | ConvertFrom-Json
if($LASTEXITCODE -ne 0){
    exit 7
}
if(-not $provisioningStep.instructions.data.contains("Hello USA!")){
    exit 8
}

az ciqs deployment delete --deployment-id $deployment.uniqueId