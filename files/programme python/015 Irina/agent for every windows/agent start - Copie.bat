color 0A
echo off
:start
cls
echo Si votre nom de compte est User, vous rentrerez User.
echo Pour trouver votre nom de compte, il est generalement affiche sur l'ecran de connexion.
echo votre nom de compte se trouve aussi dans "C:\Users\votre nom de compte\le chemin d'acces au dossier contenant le fichier>"
echo on
echo off
echo Avant de commencer, merci de rentrer le nom du compte que vous utilisez actuellement pour vous garantir le bon fonctionnement du programme.
set /p account=

echo Voulez-vous definir un programme a demarer automatiquement ou empecher un programe a demarer automatiquement? (d) pour definir/ (e) pour emecher ou r pour recommencer.
set /p mainchoice=
if %mainchoice%==d goto d
if %mainchoice%==D goto d
if %mainchoice%==e goto e
if %mainchoice%==E goto e
if %mainchoice%==r goto start
if %mainchoice%==R goto start
echo Mercie de ne rentrer que d ou D pour definir ou e ou E pour empecher.
echo Vous avez entre %mainchoice%
goto start
:d
echo Avant de commencer, assurez-vous que le fichier que vous voulez definire en demarage automatique est dans le meme dossier que le petit programme (ou l'inverse, le programme dans le dossier du fichier a copier)
echo S'il vous plait, entrez le nom du fichier a copier exemple: "exemple.png":
set /p choice=
copy %choice% C:\Users\%account%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

echo Merci.
echo Vous devriez voir le fichier dans l'explorateur
timeout 1
start C:\Users\%account%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
goto end

:e
start C:\Users\%account%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs
cd C:\Users\%account%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs
echo Dans la liste de fichiers que vous voyez, lequel voulez-vous supprimer?
echo Entrez ici le nom, si c'est un dossier, entrez d
set /p choice=
if %choice%==d goto dos
if %choice%==D goto dos
echo Suppression du fichier...............................................................................................................
del %choice%
echo Le fichier a ete supprime.
goto end
:dos
echo Merci de rentrer le nom du dossier:
set /p doschoice=
echo Supression du dossier................................................................................................................
rmdir /s %doschoice%
echo Le fichier a ete supprime.
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