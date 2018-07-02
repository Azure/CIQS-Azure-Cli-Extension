# TestHelloFunctionsDeployment
$env:AZURE_EXTENSION_DIR="C:\Users\t-jahill\.azure\devcliextensions"
$env:CIQS_CLI_TEST="Remote"
function isTerminalStatus ($status) {
    if ($status -eq "timeout"){
        return $true
    }
    elseif ($status -eq "actionRequired"){
        return $true
    }
    elseif ($status -eq "failed"){
        return $true
    }
    elseif ($status -eq "ready"){
        return $true
    }
    elseif ($status -eq "deleted"){
        return $true
    }
    else {
        return $false
    }
}

function waitForTerminalStatus ($deploymentId, $timeout) {
    $stopwatch = New-Object System.Diagnostics.Stopwatch
    $stopwatch.Start()
    $status = $null
    do {
        if($stopwatch.ElapsedMilliseconds > $timeout){
            $stopwatch.Stop()
            exit 1
        }
        $response = az ciqs deployment view --deployment-id $deploymentId | ConvertFrom-Json *>$null
        if($LASTEXITCODE -ne 0){
            $status = "deleted"
        }
        else {
            $status = $response.status
        }
        Start-Sleep -Seconds 2
        $isTerminal = isTerminalStatus($status)
    }
    while (-not $isTerminal)
    $stopwatch.Stop()
    return $status
}

$deployment = az ciqs deployment create -t "ciqs-hellofunctions" -l "East US" -n "testcli02" | ConvertFrom-Json

$deploymentStatus = waitForTerminalStatus -deploymentId $deployment.uniqueId -timeout 120000
if($LASTEXITCODE -ne 0){
    exit 1
}
if(-not $deploymentStatus -eq "actionRequired"){
    exit 2
}

$paramJson = @'
{"Name":"Pikachu"}
'@

az ciqs deployment send-params --deployment-id $deployment.uniqueId --parameters $paramJson
$deploymentStatus = waitForTerminalStatus($deployment.uniqueId, 120000)
if($LASTEXITCODE -ne 0){
    exit 3
}
if(-not $deploymentStatus -eq "ready"){
    exit 4
}

az ciqs deployment delete --deployment-id $deployment.uniqueId