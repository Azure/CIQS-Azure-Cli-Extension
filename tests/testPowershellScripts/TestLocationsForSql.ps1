# TestLocationsForSql

$env:CIQS_CLI_TEST="Remote"

$locations = az ciqs template locations -t ciqs-hellosql | ConvertFrom-Json

if (-not $locations.Length -gt 0){
    exit 1
}

exit 0
