# RunTests.ps1
# This will run all the tests in the testScripts directory
# Each test will output Passed or Failed
# A test will fail if it exits on non zero exit code

$env:CIQS_CLI_TEST="Remote"

$originalColor = $Host.UI.RawUI.ForegroundColor

$numberOfTests = (Get-ChildItem ".\testScripts").count
$numberOfTestsRun = 0

Get-ChildItem ".\testScripts" | ForEach-Object {
    Write-Progress -Activity "Running Tests" -Status "Test $_"
    if($_.Name.endswith(".ps1")){
        & $_.FullName *>$null
        $numberOfTestsRun++
        if ($LASTEXITCODE -ne 0){
            $Host.UI.RawUI.ForegroundColor = "Red"
            Write-Output ("Failed -- Code: " + $LASTEXITCODE + " -- " + $_.Name)
        }
        else {
            $Host.UI.RawUI.ForegroundColor = "DarkGreen"
            Write-Output ("Passed -- " + $_.Name)
        }
    }
    $Host.UI.RawUI.ForegroundColor = $originalColor
}
