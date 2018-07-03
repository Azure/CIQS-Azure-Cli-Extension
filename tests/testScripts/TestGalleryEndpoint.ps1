# TestGalleryEndpointIsAvailableAndAnonymous

$env:CIQS_CLI_TEST="Remote"
$templates = az ciqs template list | ConvertFrom-Json

if (-not $templates.Length -gt 0){
    exit 1
}

exit 0
