from os import*
from datetime import*
from platform import*
from time import sleep
print("A message to the windows users:")
print("I reccomend that you do not tun this program in the windows shell if you wish to bennefit from some graphics")
forbidden=[" ","-",",",";","+","'",""" " """,""" \ ""","/","#","*","(",")","[","]","{","}","`","¨","^","|","%","!","<",">",".","="," "]
def pause():
    pause=input("Press enter to continue...")
try:
    file=open("CharaterLists.txt","r")
    aa=file.read()
    print(aa)
    file.close()
    print("success")
except:
    file=open("CharaterLists.txt","a")
    file.close()
    print("fail")
pause()
date=datetime.datetime.now()
DATE="{}/{}/{}".format(date.day,date.month,date.year)

def s():
    if d>c:
        if d-c==0 or d-c==1:
            ss=""
        else:
            ss="s"
    elif d<c:
        if c-d==0 or c-d==1:
            ss=""
        else:
            ss="s"
    else:
        ss="This s function is not functionnal due to the fact that either the d or c or both variables are missing.\nMake sure that you have ne changed their name by mistake."
    return ss
def attention():
    attsing="\n           ^\n          / \\\n         / _ \\\n        / | | \\\n       /  | |  \\\n      /   | |   \\\n     /    | |    \\\n    /     | |     \\\n   /      |_|      \\\n  /        _        \\\n /        |_|        \\\n/_____________________\\\n"
    return attsing
def check(listname):
    check=[" ","         _","        //","       //"," _    //"," \\\\  //","  \\\\//","   \\/"]
    X=[" "," __            __"," \ \\          / /","  \ \\        / /","   \ \\      / /","    \ \\    / /","     \ \\  / /","      \ \\/ /","       \  /","       /  \\","      / /\\ \\","     / /  \\ \\","    / /    \\ \\","   / /      \\ \\","  / /        \\ \\"," / /          \\ \\","/_/            \\_\\"]
    lettres={}
    alpha=0
    lenthlist=len(listname)
    length=len(listname)*len(forbidden)
    print("Testing",end=" ")
    while alpha<=lenthlist:
        print()
        for c in listname:
            for i in forbidden:
                #print(i)
                #print(c)
                #check=forbidden[i]
                if c==i:
                    print("X!",end="")
                    liine=17
                    for dd in range(liine):
                        print(X[dd],end="\n")
                    print("\n\n\n\nYou have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\nThe unauthorised symbol was: '{}'".format(listname,i))
                    listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: ~ - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > . £ $ € ¥ ¤ & ° § ? ² @ : \n- You can use theses symbols: µ, ù\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                    lenthlist=len(listname)
                    c=""
                    alpha=i=0
                    print("Testing",end=" ")
                    sleep(0.5)
                else:
                    alpha+=1
                    print(".",end="")
                    sleep(0.5)
                    continue
    line=8
    for rr in range (line):
        print(check[rr],end="\n")
    print("\nSuccess")
    sleep(1)
    pause()
    return listname

listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: ~ - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > . £ $ € ¥ ¤ & ° § ? ² @ : \n- You can use theses symbols: µ, ù\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
if listname=="" or listname=="  " or listname==" ":
    listname="characters="
else:
    check(listname)
print(listname)


filename=["!!Kitten!!.acs","3dman.acs","486.acs","Actmanii.acs","Agent.acs","Al.acs","Alfred.acs","Alice.acs","Alien.acs","Amreica.acs","Amy.acs","Andrea.acs","AngBao.acs","Angel.acs","Angie.acs","Angie2.acs","Ant.acs","Apollo.acs","Arthur.acs","Athena.acs","Athena1.acs","Audie.acs","Bab.acs","Babe.acs","Balle.acs","Ballno.acs","Ballyes.acs","Balty.acs","Banjo.acs","Baron.acs","Barry.acs","BasicBook.acs","BassClown.acs","Beachballfish.acs","Beachballstrp.acs","Beau.acs","Ben.acs","Benoit.acs","BenPet.acs","BenPetChicken.acs","BenPetCloud.acs","BenPetHelicopter.acs","BenPetShelter.acs","BigZap.acs","Biker.acs","Bill.acs","Bill2.acs","BillG.acs","Birdie.acs","BlackMizi.acs","Blanket.acs","Blinky.acs","Bob.acs","Bobbi.acs","Bobby.acs","Bone.acs","Bone2.acs","Bongo.acs","Bonzi.acs","BoomBox.acs","Breezeb.acs","Brocklee.acs","Bruce2.acs","Bruceextra.acs","Bubbles.acs","Bugs.acs","Bungae.acs","ButterCup.acs","Cameron.acs","Cami.acs","Car.acs","Cassandra.acs","Cathie.acs","Cats.acs","Ceasar.acs","Charfile.acs","Charlie.acs","Check.acs","Christie.acs","Claude.acs","Cliff.acs","Clippit.acs","Clippy.acs","Cloudy.acs","Clown.acs","Coco.acs","ComputerGuy.acs","Cone.acs","Coney.acs","Cookie2.acs","Courtney.acs","CroonerClown.acs","Cruiser.acs","Crystal.acs","Cupid.acs","Cursor.acs","Curt.acs","Cyber.acs","Daffy.acs","Dalila.acs","Darkcarnival.acs","DeepThunk.acs","DejaVu.acs","Dello.acs","Demobian.acs","Denise.acs","Destroyer.acs","Diablo.acs","DiabloII.acs","DinoBB.acs","Disco.acs","DiscoJudd.acs","Dobu1.acs","DoctorMike.acs","Dog.acs","Dogbert.acs","DogFood.acs","Dolphin.acs","Doompuff.acs","Dot.acs","Dragon.acs","Drogon4.acs","Drone.acs","Earl.acs","Earlrev.acs","Earnie.acs","Electra.acs","Elmo.acs","Elvis2.acs","Eman.acs","Enterprise.acs","ErnestT.acs","Ewoman.acs","Eye.acs","F1.acs","FatGuy.acs","Felix.acs","Finfin.acs","FireBob.acs","Firechr.acs","FormerMsPres.acs","Furby.acs","Galaxygirl.acs","GamesAgent.acs","Gar.acs","Genie.acs","Genius.acs","Georgio.acs","Girlsa.acs","Gman.acs","Gnome.acs","Gooddy.acs","Gorge.acs","Gourdy.acs","Grace.acs","Grandpa.acs","Gretchen.acs","GuitarClown.acs","Guy1sa.acs","Guy2sa.acs","Hal9000.acs","Handyandy.acs","Hanz.acs","HappyFace.acs","Harriett.acs","Heather.acs","HeeJun.acs","HeeSuk.acs","Helperwiz.acs","HeMail.acs","Hitode.acs","HomerSimpsonjustthehead.acs","HomerSimpsonThewholebody.acs","Honk.acs","Hoss1.acs","Igaguri.acs","Ike.acs","Impstance.acs","Inguitar.acs","Isabella.acs","Ivan.acs","Jack.acs","JaeWon.acs","Jamesblack.acs","Jameswhite.acs","Janusz.acs","Jenni.acs","Jennifer.acs","Jffc.acs","Joe.acs","JohnnyReb.acs","Josh.acs","Judd.acs","JuddDemo.acs","Justin.acs","Kame.acs","KangTa.acs","Karabas.acs","Kasatka.acs","KatieKaboom.acs","Kel.acs","Khan.acs","Kimi.acs","Kissy.acs","Kitten.acs","Koral.acs","Krabbe.acs","Laetitia.acs","Lalen.acs","LandingBay.acs","LaterLetter.acs","LaterSign.acs","LaurenV1.acs","Legend.acs","Leo.acs","Liberty.acs","Liesl.acs","Liff.acs","Lightning.acs","LittleBear.acs","Lockergnome.acs","Logo.acs","Lokie.acs","Lorette.acs","Makki.acs","Marge.acs","Marge1.acs","Maria.acs","Marine.acs","Marvin.acs","Mary.acs","Mary1.acs","Matchstick.acs","Max.acs","Mediator.acs","Melimelo.acs","Merlin.acs","Micro.acs","Miku.acs","Milton.acs","MissAndrea.acs","MissAngie.acs","MNature.acs","Molly.acs","Monkey.acs","MonkeyKing.acs","Mouth.acs","MovieAgent.acs","MrClean.acs","Msachar.acs","Mumu.acs","Nest.acs","Newbruce.acs","Noa.acs","NorTeeDevilWebAssistant.acs","Notice.acs","Novman1.acs","Offcat.acs","OfficeClown.acs","OffScreenPlayer.acs","OftenLetter.acs","OftenSign.acs","Orin.acs","Oscar.acs","Otto.acs","Ozzar.acs","Ozzie.acs","Paige.acs","Palm.acs","Pat.acs","PCBlue.acs","Pedro.acs","Peedy.acs","Pepe.acs","PepeBrit.acs","Pete.acs","Peter.acs","PetopiaJack.acs","Philip.acs","Phony.acs","PianoClown.acs","Pigeon.acs","Pikachu.acs","PizzaBoy.acs","Plany.acs","PmGreen.acs","Professor.acs","Q1.acs","Qe2.acs","Qmark.acs","Queen.acs","Quitter.acs","Rain.acs","Reaper.acs","Rebecca.acs","RedDog.acs","Reed.acs","Reenie.acs","RevDraco.acs","Ricardo.acs","RightPro.acs","Rini.acs","Robby.acs","Robocop.acs","Rock.acs","Rocky.acs","Ron1g.acs","Rover.acs","Rovingcowboy.acs","RubberballBase.acs","RubberballGold.acs","RubberballRain.acs","Saeko.acs","Sam.acs","Sandra.acs","Santa.acs","SantaCring.acs","SarahJane.acs","SeaLena.acs","Septman.acs","Serge.acs","Shady.acs","Shampoo.acs","Shane.acs","Sharky.acs","ShellBeetle.acs","Shirley.acs","Shotzie.acs","Shrek.acs","Silver.acs","Simba.acs","Simon.acs","Sizlik.acs","Skull.acs","SmallHarp.acs","Smiley.acs","Sniffles.acs","Sniffles1.acs","Sniffles1b.acs","Snow.acs","Snowman.acs","SpaceMan.acs","Spaceman2.acs","Spaceman3.acs","Sparkle.acs","Spectra.acs","Spirou.acs","Squidge.acs","Star.acs","Stockman.acs","StockWiz.acs","StoryHarp.acs","StupyCat.acs","Sunfire.acs","Sunny.acs","Swan.acs","Symi.acs","Talkster.acs","Teasha.acs","Tempest.acs","Test.acs","TestChar.acs","TheInvisibleMan.acs","TheInvisibleWoman.acs","TheSquare.acs","Thunderbolt.acs","Tiger.acs","Tiggie.acs","TiggieDemo.acs","TimBrown.acs","Timothy.acs","Tip.acs","Tommy.acs","Tommy2.acs","Tony.acs","Totem.acs","Tres.acs","Trog.acs","TurkArabasi.acs","UncleSam.acs","Vandrea.acs","Victaur.acs","Victor.acs","Vide.acs","VietnamVet.acs","Vinnie.acs","VRGirl.acs","Wabbit.acs","Wade.acs","Walter.acs","Warning.acs","WartNose.acs","WheeJae.acs","WhisperingWall.acs","Will.acs","Wolfman.acs","Woo.acs","Woodrow.acs","WooHyuck.acs","X1.acs","Yikes.acs","YoungBarry.acs","Zap.acs","Zigreo.acs",
"Zippz.acs"]

vname=["!!Kitten!!","3dman","486","Actmanii","Agent","Al","Alfred","Alice","Alien","Amreica","Amy","Andrea","AngBao","Angel","Angie","Angie2","Ant","Apollo","Arthur","Athena","Athena1","Audie","Bab","Babe","Balle","Ballno","Ballyes","Balty","Banjo","Baron","Barry","BasicBook","BassClown","Beachballfish","Beachballstrp","Beau","Ben","Benoit","BenPet","BenPetChicken","BenPetCloud","BenPetHelicopter","BenPetShelter","BigZap","Biker","Bill","Bill2","BillG","Birdie","BlackMizi","Blanket","Blinky","Bob","Bobbi","Bobby","Bone","Bone2","Bongo","Bonzi","BoomBox","Breezeb","Brocklee","Bruce2","Bruceextra","Bubbles","Bugs","Bungae","ButterCup","Cameron","Cami","Car","Cassandra","Cathie","Cats","Ceasar","Charfile","Charlie","Check","Christie","Claude","Cliff","Clippit","Clippy","Cloudy","Clown","Coco","ComputerGuy","Cone","Coney","Cookie2","Courtney","CroonerClown","Cruiser","Crystal","Cupid","Cursor","Curt","Cyber","Daffy","Dalila","Darkcarnival","DeepThunk","DejaVu","Dello","Demobian","Denise","Destroyer","Diablo","DiabloII","DinoBB","Disco","DiscoJudd","Dobu1","DoctorMike","Dog","Dogbert","DogFood","Dolphin","Doompuff","Dot","Dragon","Drogon4","Drone","Earl","Earlrev","Earnie","Electra","Elmo","Elvis2","Eman","Enterprise","ErnestT","Ewoman","Eye","F1","FatGuy","Felix","Finfin","FireBob","Firechr","FormerMsPres","Furby","Galaxygirl","GamesAgent","Gar","Genie","Genius","Georgio","Girlsa","Gman","Gnome","Gooddy","Gorge","Gourdy","Grace","Grandpa","Gretchen","GuitarClown","Guy1sa","Guy2sa","Hal9000","Handyandy","Hanz","HappyFace","Harriett","Heather","HeeJun","HeeSuk","Helperwiz","HeMail","Hitode","HomerSimpsonjustthehead","HomerSimpsonThewholebody","Honk","Hoss1","Igaguri","Ike","Impstance","Inguitar","Isabella","Ivan","Jack","JaeWon","Jamesblack","Jameswhite","Janusz","Jenni","Jennifer","Jffc","Joe","JohnnyReb","Josh","Judd","JuddDemo","Justin","Kame","KangTa","Karabas","Kasatka","KatieKaboom","Kel","Khan","Kimi","Kissy","Kitten","Koral","Krabbe","Laetitia","Lalen","LandingBay","LaterLetter","LaterSign","LaurenV1","Legend","Leo","Liberty","Liesl","Liff","Lightning","LittleBear","Lockergnome","Logo","Lokie","Lorette","Makki","Marge","Marge1","Maria","Marine","Marvin","Mary","Mary1","Matchstick","Max","Mediator","Melimelo","Merlin","Micro","Miku","Milton","MissAndrea","MissAngie","MNature","Molly","Monkey","MonkeyKing","Mouth","MovieAgent","MrClean","Msachar","Mumu","Nest","Newbruce","Noa","NorTeeDevilWebAssistant","Notice","Novman1","Offcat","OfficeClown","OffScreenPlayer","OftenLetter","OftenSign","Orin","Oscar","Otto","Ozzar","Ozzie","Paige","Palm","Pat","PCBlue","Pedro","Peedy","Pepe","PepeBrit","Pete","Peter","PetopiaJack","Philip","Phony","PianoClown","Pigeon","Pikachu","PizzaBoy","Plany","PmGreen","Professor","Q1","Qe2","Qmark","Queen","Quitter","Rain","Reaper","Rebecca","RedDog","Reed","Reenie","RevDraco","Ricardo","RightPro","Rini","Robby","Robocop","Rock","Rocky","Ron1g","Rover","Rovingcowboy","RubberballBase","RubberballGold","RubberballRain","Saeko","Sam","Sandra","Santa","SantaCring","SarahJane","SeaLena","Septman","Serge","Shady","Shampoo","Shane","Sharky","ShellBeetle","Shirley","Shotzie","Shrek","Silver","Simba","Simon","Sizlik","Skull","SmallHarp","Smiley","Sniffles","Sniffles1","Sniffles1b","Snow","Snowman","SpaceMan","Spaceman2","Spaceman3","Sparkle","Spectra","Spirou","Squidge","Star","Stockman","StockWiz","StoryHarp","StupyCat","Sunfire","Sunny","Swan","Symi","Talkster","Teasha","Tempest","Test","TestChar","TheInvisibleMan","TheInvisibleWoman","TheSquare","Thunderbolt","Tiger","Tiggie","TiggieDemo","TimBrown","Timothy","Tip","Tommy","Tommy2","Tony","Totem","Tres","Trog","TurkArabasi","UncleSam","Vandrea","Victaur","Victor","Vide","VietnamVet","Vinnie","VRGirl","Wabbit","Wade","Walter","Warning","WartNose","WheeJae","WhisperingWall","Will","Wolfman","Woo","Woodrow","WooHyuck","X1","Yikes","YoungBarry","Zap","Zigreo",
"Zippz"]

iid=["&h409"]

characters=[]
z="{}[".format(listname)

d=len(filename)
c=len(vname)
#c=4000
print("filname={} vname={}".format(d,c))

if d==c:
    for i in range(d):
        character={}
        Filename=filename[i]
        Vname=vname[i]
        Iid=iid[0]
        character["filename"]=Filename
        character["vname"]=Vname
        character["id"]=Iid
        print(character)
        characters.append(character)
        if i==d-1:
            z+="{}]".format(character)
        else:
            z+="{},\n".format(character)
    print("{}{}".format(listname,characters))

    file=open("CharaterLists.txt", "a")
    file.write("###########################################################\n###########################################################\n###########################################################\n###########################################################\n=========== Begining of the log of the {} ======================\n\n=========== A few stats ======================\nFile path:{}\nDate of the creation of the dictionnary:{}\nos:{}\n=========== End of a few stats ======================\n\n=========== The dictionnary ======================\n----------- The dictionnary (Condensed) ----------------------\n{}{}\n----------- End of the condensed dictionnary  ----------------------\n\n----------- The dictionnary (Expanded) ----------------------\n{}\n----------- End of the expanded dictionnary  ----------------------\n\n=========== End of the dictionnary ======================\n\n=========== End of the current log ======================\n\n".format(DATE, os.getcwd(), DATE, platform.system(),listname,characters,z))
    file.close()
    pause()
    pause()
elif d>c:
    print("###########################################################\n###########################################################\n###########################################################\n###########################################################\n=========== Begining of the log of the {} ======================\n{}\n=========== Fatal Error! ======================\n{} element{} are missing in the vname list.\nMake sure that you have not forgotten to put the name of the new character{} in the vname list\n=========== End of the Fatal Error! ======================\n\n=========== End of the current log ======================\n\n".format(DATE,attention(),d-c,s(),s()))
    file=open("CharaterLists.txt", "a")
    file.write("###########################################################\n###########################################################\n###########################################################\n###########################################################\n=========== Begining of the log of the {} ======================\n\n=========== A few stats ======================\nFile path:{}\nDate of the creation of the dictionnary:{}\nos:{}\n=========== End of a few stats ======================\n{}\n=========== Fatal Error! ======================\n{} element{} are missing in the vname list.\nMake sure that you have not forgotten to put the name of the new chraracter{} in the vname list\n=========== End of the Fatal Error! ======================\n\n=========== End of the current log ======================\n\n".format(DATE, os.getcwd(), DATE, platform.system(),attention(),d-c,s(),s()))
    file.close()
    pause()
    pause()
elif d<c:
    print("###########################################################\n###########################################################\n###########################################################\n###########################################################\n=========== Begining of the log of the {} ======================\n{}\n=========== Fatal Error! ======================\n{} element{} are missing in the filename list.\nMake sure that you have not forgotten to put the name of the new character{} in the filename list\n=========== End of the Fatal Error! ======================\n\n=========== End of the current log ======================\n\n".format(DATE,attention(),c-d,s(),s()))
    file=open("CharaterLists.txt", "a")
    file.write("###########################################################\n###########################################################\n###########################################################\n###########################################################\n=========== Begining of the log of the {} ======================\n\n=========== A few stats ======================\nFile path:{}\nDate of the creation of the dictionnary:{}\nos:{}\n=========== End of a few stats ======================\n{}\n=========== Fatal Error! ======================\n{} element{} are missing in the filename list.\nMake sure that you have not forgotten to put the name of the new character{} in the filename list\n=========== End of the Fatal Error! ======================\n\n=========== End of the current log ======================\n\n".format(DATE, os.getcwd(), DATE, platform.system(),attention(),c-d,s(),s()))
    file.close()
    pause()
    pause()
else:
    print("Whoops, Something is wrong but I don't know what. Have a look at the program to try and fix it or download it again from this website: ")
    pause()
    pause()