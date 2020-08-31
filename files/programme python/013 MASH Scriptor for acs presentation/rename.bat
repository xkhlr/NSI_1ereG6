color 0A
echo off
cls
:start
echo (p)arcourir le repertoire/(l)ister le contenu du repertoire/(r)enomer/(q)uitter
set /p choice=
if %choice%==p goto p
if %choice%==l goto l
if %choice%==r goto r
if %choice%==q goto q
if %choice%==P goto p
if %choice%==L goto l
if %choice%==R goto r
if %choice%==Q goto q

:p
dir
REM echo Merci de n'avancer que d'un dossier a la fois sous peine de risquer de faire planter le programe.
REM echo.
REM echo Quand vous avez des dossier qui comprennent des espaces, merci de d'encadrer la ligne par "
echo.
echo "Entrez le dossier(s) (pour reculer d'un dossier, entrez ..):"
set /p folder=
echo %folder%
cd "%folder%"
dir
echo Voulez-vous acceder a un autre dossier? [(o)ui/(n)on]:
set /p parc=
echo Vous avez choisi %rest%
if %parc%==o goto p
if %parc%==O goto p
if %parc%==0 goto P
if %parc%==n goto start
if %parc%==N goto start
else (
	echo Merci de ne rentrer que o ou O ou 0 pour oui ou n ou N pour non.
	echo Vous avez entre %parc%
	pause
	goto p
)
:l
dir
echo.
goto start
:r
echo Si vous renommer un fichier qui a des espaces vous risquerez d'avoir trois lignes qui vont apparaitre une fois l'operation reussie:
echo Les deux premiere ligne sont habituelles:
echo "- Le fichier <nom de votre fichier.l'extension de votre fichier> existe"
echo "- Le fichier <nom de votre fichier.l'extension de votre fichier> a ete renome en <nom de destination de votre fichier.l'extension de destination de votre fichier> avec succes."
echo La derniere ligne peut etre quelque peux deconcertante:
echo "- Le fichier <nom de votre fichier.l'extension de votre fichier> est introuvable.", pourtant l'operation s'est deroulee avec succes, vous pouvez donc ignorer cette ligne.
echo.
echo.
echo Une operation a echouee si vous voyez les quatres lignes suivantes ou que le programme vous affiche Le fichier <nom de votre fichier.l'extension de votre fichier> est introuvable.
echo Les quatres lignes qui montre que le programe a echoue sont:
echo "Le fichier <nom de votre fichier.l'extension de votre fichier> existe."
ren d%.d zz.d
echo "Le fichier <nom de votre fichier.l'extension de votre fichier> a ete renome en <nom de votre fichier.l'extension de votre fichier> avec succes."
echo "Le fichier <nom de votre fichier.l'extension de votre fichier> est introuvable."
echo.
echo.
echo Entrez l'extension de votre fichier (merci de ne pas mettre le point devant l'extension):
set /p ext=
echo L'extension de votre fichier est %ext%.
echo.
echo Entrez l'extension du fichier une fois renome (merci de ne pas mettre le point devant l'extension):
set /p next=
echo L'extension du fichier renome sera %next%.
echo.
echo Entrez le nom du fichier a modifier:
set /p nfile=
echo Le nom du fichier choisi est %nfile%.
echo.
echo Entrez le nouveau nom du fichier:
set /p refile=
echo Le nouveau nom du fichier est %refile%.
echo.

IF EXIST %nfile%.%ext% (
	echo Le fichier %nfile% existe.
	ren "%nfile%.%ext%" "%refile%.%next%"
	echo Le fichier %nfile%.%ext% a ete renome en %refile%.%next% avec succes.
) ELSE (
	echo Le fichier %nfile%.%ext% est introuvable.
)
echo Voulez-vous renomer un nouveau fichier? [(o)ui/(n)on]:
set /p rest=
echo Vous avez choisi %rest%
if %rest%==o goto r
if %rest%==O goto r
if %rest%==0 goto r
if %rest%==n goto start
if %rest%==N goto start
else (
	echo Merci de ne rentrer que o ou O ou 0 pour oui ou n ou N pour non.
	echo Vous avez entre %rest%
	pause
	goto r
)
:q
echo Au revoir et a la prochaine.
echo Cree par Henry Letellier
pause