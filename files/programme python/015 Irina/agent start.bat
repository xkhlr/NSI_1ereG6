color 0A
echo off
:start
cls
echo on
echo off
echo Veux-tu definir un programme a demarer automatiquement ou empecher un programe a demarer automatiquement? (d) pour definir/ (e) pour emecher
set /p mainchoice=
if %mainchoice%==d goto d
if %mainchoice%==D goto d
if %mainchoice%==e goto e
if %mainchoice%==E goto e
echo mercie de ne rentrer que d ou D pour definir ou e ou E pour empecher.
echo vous avez entre %mainchoice%
goto start
:d
echo Avant de commencer, assure-toi que le fichier que tu veux définire en démarage automatique est dans le même dossier que le petit programme (ou l'inverse, le programme dans le dossier du fichier a copier)
echo S'il te plait, entre le nom du fichier à copier exemple: "exemple.png":
set /p choice=
copy %choice% C:\Users\oshkurat\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

echo Merci.
echo tu devrai voir le fichier dans l'explorateur
timeout 1
start C:\Users\oshkurat\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
goto end

:e
start C:\Users\oshkurat\AppData\Roaming\Microsoft\Windows\Start Menu\Programs
cd C:\Users\oshkurat\AppData\Roaming\Microsoft\Windows\Start Menu\Programs
echo Dans la liste de fichiers que tu vois, lequel veux-tu supprimer?
echo entre ici le nom, si c'est un dossier, entre d
set /p choice=
if %choice%==d goto dos
if %choice%==D goto dos
echo supperession du fichier
del %choice%
echo le fichier a ete supprime
goto end
:dos
echo merci de rentrer le nom du dossier:
set /p doschoice=
echo supression du dossier
rmdir /s %doschoice%
echo le fichier a ete supprime
goto end
:end
echo Au revoir
echo cr‚‚ par Henry Letellier
echo " ._____. "
echo " |.   .| "
echo " |  |  | "
echo " |\___/| "
echo " |_____| "
timeout 3
pause
pause
pause
pause