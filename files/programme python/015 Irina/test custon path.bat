color 0A
echo off
cls
:start
echo.
echo ============================================ Menu Principal ============================================
echo.
echo Si vous voulez aller autre part que dans les dossiers de compte, tapez C dans la question qui suit, sinon tapez U, pour naviguer librement dossier par dossiert tapez nl, pour quitter tapez q :
set /p option=
if %option%==C goto c
if %option%==c goto c
if %option%==U goto u
if %option%==u goto u
if %option%==nl goto nl1
if %option%==nL goto nl1
if %option%==Nl goto nl1
if %option%==NL goto nl1
if %option%==q goto end
if %option%==Q goto end
echo.
echo Merci de ne rentrer soit C ou c pour entrer autre part que dans les dossier d'utilisateurs ou tapez U ou u pour explorer un dossier d'utilisateur, out tapez nl ou Nl ou nL ou NL pour naviguer dossier par dossier, ou tapez Q ou q pour quitter.
echo Vous avez entr‚ %option%
pause
goto start
:u
echo.
echo ============================================ Navigage Guid‚e ============================================
echo.
echo on
echo off
echo.
echo Ou voulez-vous aller? (merci de bien vouloir rentrer le chemin complet en partant du dossier qui suit votre nom de compte
set /p path=
echo.
echo Quel est votre nom de compte?
set /p name=
echo.
echo Quel est le nom de votre lecteur? (le nom de votre lecteur peut etre C:, D:, E:, (F:), n'entrez que la lettre)
set /p device=
echo.
echo Acces a : %device%:\Users\%name%\%path%
echo.
cd %device%:\Users\%name%\%path%
echo on
echo off
echo r‚ussi
pause
dir
pause
echo cr‚‚ par Henry Letellier
pause
echo Vous retournez au menu Principal......................
pause
echo.
echo ============================================ Menu Navigage Guid‚e Exited ============================================
echo.
echo retour au menu principal..................................................................
pause
goto start
:c
echo.
echo ============================================ Navigage Libre Depuis La Source ============================================
echo.
echo on
echo off
echo.
echo Ou voulez-vous aller? (si vous avez un doute, regardez la ligne "C:\le chemin d'acces>" au dessu de cette question)
set /p path=
echo.
echo Acces a: %path%
echo.
cd %path%
echo.
echo on
echo off
pause
dir
pause
echo cr‚‚ par Henry Letellier
pause
echo Vous retournez au menu Principal......................
pause
echo.
echo ============================================ Menu Navigage Libre Depuis La Source Exited  ============================================
echo.
echo retour au menu principal..................................................................
pause
goto start
:nl1
echo.
echo ============================================ nl: Navigage Libre (Dossier par Dossier) ============================================
echo.
rem goto nl
:nl
echo.
echo Pour sortir de la fonction nl, tapez q, sinon tapez le nom du dossier dans lequel vous souhaitez entrer, tapez d pour afficher le contenu du dossier, et tappez s pour lancer un programme
echo.
echo on
echo off
echo.
echo Ou voulez-vous aller? (si vous avez un doute, regardez la ligne "C:\le chemin d'acces>" au dessu de cette question)
set /p path=
if %path%==q goto Q
if %path%==Q goto Q
if %path%==d goto dir
if %path%==D goto dir
if %path%==dir goto dir
if %path%==DIR goto dir
if %path%==dd dir
if %path%==s goto starrt
if %path%==S goto starrt
echo.
echo Acces a: %path%
set fol=%path%
echo.
cd %path%
echo.
echo on
echo off
pause
dir
pause
echo cr‚‚ par Henry Letellier
goto nl
:Q
echo cr‚‚ par Henry Letellier
pause
echo Vous retournez au menu Principal......................
pause
echo.
echo ============================================ Menu nl (naviguer librement) Exited  ============================================
echo.
echo retour au menu principal..................................................................
goto start
goto nl
:starrt
echo quelle fonction voulez-vous utiliser pour demarer un programme, start (s) ou cmd (c), (e) pour sortir.
set /p which=
if %which%==c goto Cmd
if %which%==C goto Cmd
if %which%==s goto starrrt
if %which%==S goto starrrt
if %which%==e goto e
if %which%==E goto e
:e
pause
echo Vous retournez au menu naviguer librement (nl)......................
pause
echo.
echo ============================================ Menu starrt Exited  ============================================
echo.
echo retour au menu nl..................................................................
goto nl
:starrrt
echo start
echo entrez le nom du fichier a ouvrir:
set /p startt=
echo Acces a: %startt%
echo.
start %startt%
echo.
echo on
echo off
pause
dir
pause
echo Cr‚‚ par Henry Letellier
pause
goto starrt
:Cmd
echo Cette rubrique est encore en cour d'edition ainsi que ses balises enfant, faite CS pour sortir

echo (cc) correspond a "cmd/c "le chemin d'acces" " cela demarre un programme dans la meme fenêtre que la ou vous avez tape la commande, quand le program est termine on retourne a l'interface principale (ici: ce programme).
echo.
echo (ck) correspond a "cmd/k "le chemin d'acces" " cela demarre un programme dans la meme fenêtre que la ou vous avez tape la commande, quand le program est termine on ne retourne a l'interface principale (ici: ce programme) mais.
echo.
echo (ch) 
echo.
echo (cs)
echo.
echo (cq)
echo.
echo (cd)
echo.
echo (ca)
echo.
echo (cu)
echo.
echo (ct)
echo.
echo (ceo)
echo.
echo (cef)
echo.
echo (cvo)
echo.
echo (cvf)
echo.
echo (cs)


set /p stat=
if %stat%==cc goto cc
if %stat%==Cc goto cc
if %stat%==cC goto cc
if %stat%==CC goto cc
if %stat%==ch goto ch
if %stat%==Ch goto ch
if %stat%==cH goto ch
if %stat%==CH goto ch
if %stat%==ck goto ck
if %stat%==Ck goto ck
if %stat%==cK goto ck
if %stat%==CK goto ck
if %stat%==cs goto cs
if %stat%==Cs goto cs
if %stat%==cS goto cs
if %stat%==CS goto cs
if %stat%==cq goto cq
if %stat%==Cq goto cq
if %stat%==cQ goto cq
if %stat%==CQ goto cq
if %stat%==cd goto cd
if %stat%==Cd goto cd
if %stat%==cD goto cd
if %stat%==CD goto cd
if %stat%==ca goto ca
if %stat%==Ca goto ca
if %stat%==cA goto ca
if %stat%==CA goto ca
if %stat%==cu goto cu
if %stat%==Cu goto cu
if %stat%==cU goto cu
if %stat%==CU goto cu
if %stat%==ct goto ct
if %stat%==Ct goto ct
if %stat%==cT goto ct
if %stat%==CT goto ct
if %stat%==ceo goto ceo
if %stat%==CEo goto ceo
if %stat%==CEO goto ceo
if %stat%==cEo goto ceo
if %stat%==CeO goto ceo
if %stat%==Ceo goto ceo
if %stat%==cEO goto ceo
if %stat%==cef goto cef
if %stat%==CEf goto cef
if %stat%==CEF goto cef
if %stat%==cEf goto cef
if %stat%==CeF goto cef
if %stat%==Cef goto cef
if %stat%==cEF goto cef
if %stat%==cvo goto cvo
if %stat%==CVo goto cvo
if %stat%==CVO goto cvo
if %stat%==cVo goto cvo
if %stat%==CvO goto cvo
if %stat%==Cvo goto cvo
if %stat%==cVO goto cvo
if %stat%==cvf goto cvf
if %stat%==CVf goto cvf
if %stat%==CVF goto cvf
if %stat%==cVf goto cvf
if %stat%==CvF goto cvf
if %stat%==Cvf goto cvf
if %stat%==cVF goto cvf
if %stat%==cs goto cs
if %stat%==Cs goto cs
if %stat%==cS goto cs
if %stat%==CS goto cs

:cc
echo cc
echo Je suis encore en cour d'edition
echo.
echo Info:
echo.
echo  Execute la commande donnee par la chaine de caracteres puis se termine.
pause
echo entrez le nom du fichier a ouvrir:
set /p startt=
echo.
echo " cmd/c "%startt%" "
echo.
cmd/c "%startt%"
echo.
pause
echo Cr‚‚ par Henry Letellier
pause
goto Cmd

:cvf
echo cvf
echo Je suis encore en cour d'edition
pause
echo Info:
echo.
echo Desactive l’expansion retardee des variables d’environnement.
echo.
echo " cmd/V:OFF  "
cmd/v:Off
echo.
pause
echo Cr‚‚ par Henry Letellier
pause
goto Cmd

:cvo
echo cvo
echo Je suis encore en cour d'edition
pause
echo.
echo Info:
echo.
echo Active l’expansion retardee des variables d’environnement en utilisant ! comme délimiteur. Par exemple, /V:ON permet a !var! de developper la variable var a l’execution. La syntaxe var developpe les variables lorsqu’elles sont entrees, ce qui est different lorsque utilisé à l’interieur d’une boucle FOR.
echo.
echo " cmd/V:ON "
cmd/v:on
pause
echo Cr‚‚ par Henry Letellier
pause
goto Cmd

:cef
echo cef
echo Je suis encore en cour d'edition
pause
echo entrez le nom du fichier a ouvrir:
set /p startt=
echo.
echo Info:
echo.
echo Desactive les extensions de commande (voir ci-dessous).
echo.
pause
echo "cmd/E:off"
cmd/e:off
echo Cr‚‚ par Henry Letellier
pause
goto Cmd

:ceo
echo ceo
echo Je suis encore en cour d'edition
pause
echo entrez le nom du fichier a ouvrir:
set /p startt=
echo.
echo Info:
echo.
echo Active les extensions de commande (voir ci-dessous).
echo.
pause
echo "cmd/E:on"
cmd/e:on
pause
echo Cr‚‚ par Henry Letellier
pause
goto Cmd

:ct
echo ct
echo Je suis encore en cour d'edition
pause
echo entrez le nom du fichier a ouvrir:
set /p startt=
echo.
echo Info:
echo.
echo Change la couleur du premier plan ou de l’arriere-plan (voir aussi COLOR /?).
echo.
pause
echo Quelle est votre premirere couleur, l'ecriture:
set /p f=
echo.
echo Quelle est votre deuxieme couleur, l'arriere-plan:
set /p b=
echo.
echo "cmd/T:fg"
pause
echo "cmd/T:%f%%g% "%startt%""
cmd/T:%f%%g% "%startt%
pause
echo Cr‚‚ par Henry Letellier
pause
goto Cmd

:cu
echo cu
echo Je suis encore en cour d'edition
pause
echo entrez le nom du fichier a ouvrir:
set /p startt=
echo.
echo Info:
echo.
echo  Redirige la sortie de commandes internes vers un canal ou un fichier UNICODE.
echo.
pause
echo "cmd/U"
cmd/u
echo Cr‚‚ par Henry Letellier
pause
goto Cmd

:ca
echo ca
echo Je suis encore en cour d'edition
pause
echo entrez le nom du fichier a ouvrir:
set /p startt=
echo.
echo Info:
echo.
echo Redirige la sortie de commandes internes vers un canal ou un fichier ANSI.
echo.
pause
echo "cmd/A"
cmd/a
pause
echo Cr‚‚ par Henry Letellier
pause
goto Cmd

:cd
echo cd
echo Je suis encore en cour d'edition
pause
echo entrez le nom du fichier a ouvrir:
set /p startt=
echo.
echo Info:
echo.
echo Desactive l’execution d’AutoRun a partir du Registre (voir ci-dessous).
echo.
pause
echo "cmd/D"
cmd/d
pause
echo Cr‚‚ par Henry Letellier
pause
goto Cmd

:cq
echo cq
echo Je suis encore en cour d'edition
pause
echo entrez le nom du fichier a ouvrir:
set /p startt=
echo.
echo Info:
echo.
echo Desactive l’execution d’AutoRun a partir du Registre (voir ci-dessous).
echo.
pause
echo "cmd/D"
cmd/d
pause
echo Cr‚‚ par Henry Letellier
pause
goto Cmd

:cs
echo cs
echo Vouc etes maintenant entrain de sortir du menu cmd....
pause
echo.
echo Vous retournez au menu choix entre la comande start et la comande cmd......................
pause
echo.
echo ============================================ Menu Cmd Exited  ============================================
echo.
echo retour au menu starrt..................................................................
echo.
echo Cr‚‚ par Henry Letellier
pause
goto starrt

:ck
echo ck
echo Je suis encore en cour d'edition
pause
echo entrez le nom du fichier a ouvrir:
set /p startt=
echo Acces a: %startt%
echo.
echo.
echo Info:
echo.
echo Desactive l’execution d’AutoRun a partir du Registre (voir ci-dessous).
echo.
pause
echo "cmd/D"
cmd/d
pause
echo Cr‚‚ par Henry Letellier
pause
goto Cmd

:ch
echo ch
echo Je suis encore en cour d'edition
pause
echo entrez le nom du fichier a ouvrir:
set /p startt=
echo.
echo Info:
echo.
echo Desactive l’execution d’AutoRun a partir du Registre (voir ci-dessous).
echo.
pause
echo "cmd/D"
cmd/d
pause
pause
echo Cr‚‚ par Henry Letellier
pause
goto Cmd


rem/C
rem/K
rem/S
rem/Q
rem/D
rem/A
rem/U
rem/T:fg
rem/E:ON
rem/E:OFF
rem/F:ON
rem/F:OFF
rem/V:ON
rem/V:OFF


echo.
echo Acces a: %path%
set fol=%path%
echo.
cd %path%
echo.
echo on
echo off
pause
dir
pause
echo cr‚‚ par Henry Letellier
pause
goto nl
:dir
echo.
echo ============================================ Affichage du contenu du dossier %fol% ============================================
echo.
dir
echo.
echo ============================================ Fin de l'affichage du contenu du dossier %fol% ============================================
echo.
goto nl
:end
echo Au revoir
echo cr‚‚ par Henry Letellier
echo.
echo " ._____. "
echo " |.   .| "
echo " |  |  | "
echo " |\___/| "
echo " |_____| "
timeout 3
pause
pause