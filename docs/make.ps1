
Write-Host "Creating Documentation"
&sphinx-build.exe  -b html ./source ./build

$documentation_project_location = "..\..\aurora-amun-python-sdk-docs\"
Write-Host "Copying docs to '$documentation_project_location'"
copy -Recurse -Force  .\build\*  $documentation_project_location

