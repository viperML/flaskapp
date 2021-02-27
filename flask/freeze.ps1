& $PSScriptRoot\\env\\Scripts\\activate.ps1
Set-Content -Path requirements.txt -Value (pip freeze | Select-String -Pattern "Flask-Uploads==" -NotMatch) 
Add-Content -Path requirements.txt -Value "git+https://github.com/maxcountryman/flask-uploads.git"