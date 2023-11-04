# -*- coding: iso-8859-2 -*-

import urllib.request

d = ""
tra = True
while tra == True:
    print ("This is the bater-anglysh-lagguage translator")
    print ("please choose the translation of your choice")
    print ("write 'a-e' for translating to english,")
    print ("and 'e-a' to translate to bater-anglysh.")
    print ("To leave enter 'quit'")
    newresult = ""
    lan = input(">>> ")
    if lan == "e-a":
        while d == "":
            print ("Please select the dialect you want to translate into.")
            print ("If you need a full list please type '/list'")
            d = input(">>> ")
            if d == "/list":
                print ("Common language = '0'")
                print ("Agepaz dialect = 'a'")
                print ("Bembulott's dialect = 'b'")
                print ("Gnadaf's dialect = 'c'")
                d = ""
            if d == "0":
                di = 0
            if d == "a":
                di = 1
            if d == "b":
                di = 2
            if d == "c":
                di = 3
            else:
                di = ""
        print ("Now type in the text to translate")
        txt = input (">>> ")+ " "
        print ("")
        datei = urllib.request.urlopen("https://github.com/RealBamboolord/Bater-Anglysh-muud/raw/main/Dicchionarri.txt")
        news = datei.read()
        news = str(news)
        news = news[2:]
        while txt != "":
            a = txt.find(" ")
            wodd = txt[:a]
            wodd = wodd.capitalize()
            txt = txt[a+1:]
            wodds = "n" + wodd + " = "
            word = news.find(wodds) + len(wodds)
            tran = news[word:]
            find = tran.find("\\")
            if word - len(wodds) != -1:
                result = news[word:(word+find)]
                for dia in range(0,di):
                    dial = result.find("; ")
                    if dial != -1:
                        result = result[dial+2:]
                diale = result.find("; ")
                if diale != -1:
                    result = result[:diale]
            else:
                result = "["+wodd+"]"
            newresult = newresult + result + " "
        newresult = newresult.capitalize()
        print (newresult)
        input("")
    elif lan == "quit":
        tra = False
