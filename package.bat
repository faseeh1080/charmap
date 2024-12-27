pyinstaller --icon=assets\icon.ico --name="Faseehs CharMap" --noconsole main.py

set source="assets"
set destination="dist\Faseehs CharMap\assets"

:: Check if the destination folder exists
if not exist %destination% (
    echo The destination folder does not exist. Creating it now...
    mkdir %destination%
)

:: Update the copy of the folder
echo Updating the copy...
xcopy /E /H /Y /D %source% %destination%

echo Success!

pause