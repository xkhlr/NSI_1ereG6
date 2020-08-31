forbidden=[" ","£","$","€","¥","¤","&","°","§","?","²","@","~","-",",",";","+","'","""" """,""" \ ""","/","#","*","(",")","[","]","{","}","`","¨","^","|","%","!","<",">",".","="," ",":"]
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
    #I=i=1
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
                else:
                    alpha+=1
                    print(".",end="")
                    continue
    line=8
    for rr in range (line):
        print(check[rr],end="\n")
    print("\nSuccess")
    return listname



def check2(listname):
    lettres={}
    alpha=0
    lenthlist=len(listname)
    I=i=1
    while alpha<=lenthlist:
        for c in listname:
            if c!=" ":
                if c!="-":
                    if c!=",":
                        if c!=";":
                            if c!="+":
                                if c!="'":
                                    if c!=""" " """:
                                        if c!=""" \ """:
                                            if c!="/":
                                                if c!="#":
                                                    if c!="*":
                                                        if c!="(":
                                                            if c!=")":
                                                                if c!="[":
                                                                    if c!="]":
                                                                        if c!="{":
                                                                            if c!="}":
                                                                                if c!="`":
                                                                                    if c!="¨":
                                                                                        if c!="^":
                                                                                            if c!="|":
                                                                                                if c!="%":
                                                                                                    if c!="!":
                                                                                                        if c!="<":
                                                                                                            if c!=">":
                                                                                                                if c!=".":
                                                                                                                    if c!="=":
                                                                                                                        if c!=" ":
                                                                                                                            alpha+=1
                                                                                                                        else:
                                                                                                                            c=""
                                                                                                                            alpha=0
                                                                                                                            print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '='".format(listname))
                                                                                                                            listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                                                                                            lenthlist=len(listname)
                                                                                                                    else:
                                                                                                                        c=""
                                                                                                                        alpha=0
                                                                                                                        print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '='".format(listname))
                                                                                                                        listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                                                                                        lenthlist=len(listname)
                                                                                                                else:
                                                                                                                    c=""
                                                                                                                    alpha=0
                                                                                                                    print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '.'".format(listname))
                                                                                                                    listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                                                                                    lenthlist=len(listname)
                                                                                                            else:
                                                                                                                c=""
                                                                                                                alpha=0
                                                                                                                print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '>'".format(listname))
                                                                                                                listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                                                                                lenthlist=len(listname) 
                                                                                                        else:
                                                                                                            c=""
                                                                                                            alpha=0
                                                                                                            print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '<'".format(listname))
                                                                                                            listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                                                                            lenthlist=len(listname)
                                                                                                    else:
                                                                                                        c=""
                                                                                                        alpha=0
                                                                                                        print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '!'".format(listname))
                                                                                                        listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                                                                        lenthlist=len(listname)
                                                                                                else:
                                                                                                    c=""
                                                                                                    alpha=0
                                                                                                    print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '%'".format(listname))
                                                                                                    listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                                                                    lenthlist=len(listname)
                                                                                            else:
                                                                                                c=""
                                                                                                alpha=0
                                                                                                print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '|'".format(listname))
                                                                                                listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                                                                lenthlist=len(listname)
                                                                                        else:
                                                                                            c=""
                                                                                            alpha=0
                                                                                            print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '^'".format(listname))
                                                                                            listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                                                            lenthlist=len(listname)
                                                                                    else:
                                                                                        c=""
                                                                                        alpha=0
                                                                                        print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '¨'".format(listname))
                                                                                        listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                                                        lenthlist=len(listname)
                                                                                else:
                                                                                    c=""
                                                                                    alpha=0
                                                                                    print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '`'".format(listname))
                                                                                    listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                                                    lenthlist=len(listname)
                                                                            else:
                                                                                c=""
                                                                                alpha=0
                                                                                print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '}'".format(listname))
                                                                                listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                                                lenthlist=len(listname)
                                                                        else:
                                                                            c=""
                                                                            alpha=0
                                                                            print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '{'".format(listname))
                                                                            listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                                            lenthlist=len(listname)
                                                                    else:
                                                                        c=""
                                                                        alpha=0
                                                                        print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: ']'".format(listname))
                                                                        listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                                        lenthlist=len(listname)
                                                                else:
                                                                    c=""
                                                                    alpha=0
                                                                    print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '['".format(listname))
                                                                    listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                                    lenthlist=len(listname)
                                                            else:
                                                                c=""
                                                                alpha=0
                                                                print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: ')'".format(listname))
                                                                listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                                lenthlist=len(listname)
                                                        else:
                                                            c=""
                                                            alpha=0
                                                            print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '('".format(listname))
                                                            listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                            lenthlist=len(listname)
                                                    else:
                                                        c=""
                                                        alpha=0
                                                        print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '*'".format(listname))
                                                        listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                        lenthlist=len(listname)
                                                else:
                                                    c=""
                                                    alpha=0
                                                    print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '#'".format(listname))
                                                    listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                    lenthlist=len(listname)
                                            else:
                                                c=""
                                                alpha=0
                                                print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '/'".format(listname))
                                                listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                                lenthlist=len(listname)
                                        else:
                                            c=""
                                            alpha=0
                                            print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '\'".format(listname))
                                            listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                            lenthlist=len(listname)
                                    else:
                                        c=""
                                        alpha=0
                                        print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '\"'".format(listname))
                                        listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                        lenthlist=len(listname)
                                else:
                                    c=""
                                    alpha=0
                                    print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: ' ' '".format(listname))
                                    listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                    lenthlist=len(listname)
                            else:
                                c=""
                                alpha=0
                                print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '+'".format(listname))
                                listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                                lenthlist=len(listname)
                        else:
                            c=""
                            alpha=0
                            print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: ';'".format(listname))
                            listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                            lenthlist=len(listname)
                    else:
                        c=""
                        alpha=0
                        print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: ','".format(listname))
                        listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                        lenthlist=len(listname)
                else:
                    c=""
                    alpha=0
                    print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '-'".format(listname))
                    listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                    lenthlist=len(listname)
            else:
                c=""
                alpha=0
                print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: '='".format(listname))
                listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
                lenthlist=len(listname)
        else:
            c=""
            alpha=0
            print("You have put an unauthorised symbol, please rename the list without the symbol.\nYour name was: {}\n The unauthorised symbol was: ' '".format(listname))
            listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > .\n- You can use theses symbols: £, $, €, ¥, ~, &, °, µ, ù, ¤, §, ?, ², @\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
            lenthlist=len(listname)
listname=input("{}\nImportant!:\nIn the name of the list itself:\n- Do not include spaces\n- Do not include signs such as: ~ - , ; + ' \" \ / # * () [] {}{} ` ¨ ^ | % ! < > . £ $ € ¥ ¤ & ° § ? ² @ : \n- You can use theses symbols: µ, ù\n- To make a space, you can use this symbol: _ \n- It is not recomended to use accents in the name\n- You can use numbers, capsizes, lowercases\n\nPlease do not put a = sign in the name of you're list or you're list will not work.\nHow do you whant to name your character list (The by default name will be characters):".format(attention(),"{","}"))
if listname=="" or listname=="  " or listname==" ":
    listname="characters="
else:
    check(listname)
    listname+="="
print(listname)
