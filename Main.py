import time
import info
import os

def slow_print(text:str, speed = .07):
    for character in text:
        print(character, end="", flush = True)
        time.sleep(speed)


def Login():
    Pas = "Joshua"
    print("")
    print("")
    Password = input("Logon: ")
    if Password == Pas:
        Chat()
    elif Password.lower() == "help logon":
        slow_print(info.HELP_LOGIN)
    elif Password.lower() == "help games":
        slow_print(info.HELP_GAME)
        Login()
    elif Password.lower() == "list games":
        slow_print(info.LIST_GAMES)
        Login()
    elif Password == "WOPR-ADMIN12":
        slow_print(info.ADMIN_LIST)

        ask = input("Enter Selection:  ")
        if ask == "1":
            Login()
        elif ask == "2":
            QA1()
        elif ask == "3":
            QA2()
        elif ask == "4":
            QA3()
        elif ask == "5":
            QA4()
        elif ask == "6":
            Chat()
        elif ask == "7":
            GameMenu()
        elif ask == "8":
            ThermalNuculerWar()
        elif ask.lower() == "bye":
            Login()
        else:
            Login()
    else:
        slow_print(info.ELSE_ERROR)

def QA1():
    slow_print(info.Q1)
    print("")
    hi = input("")
    hi = hi.lower()
    if hi.__contains__("hello") or hi.__contains__("hi") or hi.__contains__("wassup") or hi.__contains__("good evening") or hi.__contains__("g'day") or hi.__contains__("hi-ya") or hi.__contains__("greetings"):
        slow_print(info.Q2)
        print("")
        QA2()
    else:
        slow_print(info.QA_ERROR)
        print("")
        QA1()

def QA2():
    feel = input("")
    feel = feel.lower()
    if feel.__contains__("fine") or feel.__contains__("good") or feel.__contains__("great") or feel.__contains__("excellent") or feel.__contains__("nice") or feel.__contains__("ok"):
        slow_print(info.Q3)
        print("")
        QA3()
    elif feel.__contains__("bad") or feel.__contains__("terrible") or feel.__contains__("not good") or feel.__contains__("stop"):
        slow_print(info.Q3_SAD)
        print("")
        QA3()
    else:
        slow_print(info.QA_ERROR)
        print("")
        QA2()

def QA3():
    ask = input("")
    ask = ask.lower()
    if ask.__contains__("mistake") or ask.__contains__("dont know") or ask.__contains__("accident") or ask.__contains__("?") or ask.__contains__("no"):
        slow_print(info.Q4)
        print("")
        QA4()
    elif ask.__contains__("i died"):
        slow_print(info.QA_FUNNY)
        print("")
        QA4()
    else:
        slow_print(info.QA_ERROR)
        print("")
        QA3()

def QA4():
    game = input("")
    game = game.lower()
    if game.__contains__("yes") or game.__contains__("ya") or game.__contains__("sure") or game.__contains__("of course") or game.__contains__("yess") or game.__contains__("ok"):
        GameMenu()
    else:
        slow_print("SEE YOU LATER PROFESSOR...")
        print("")
        Login()


def Chat():
    QA1()

def GameMenu():
    print("")
    print("")
    print("")
    Falkins_Maze = slow_print("FALKEN'S MAZE")
    print("")
    Black_Jack = slow_print("BLACK JACK")
    print("")
    Gin_Rummy = slow_print("GIN RUMMY")
    print("")
    Hearts = slow_print("HEARTS")
    print("")
    Bridge = slow_print("BRIDGE")
    print("")
    Cheackers = slow_print("CHECKERS")
    print("")
    Chess = slow_print("CHESS")
    print("")
    Poker = slow_print("POKER")
    print("")
    Fighter_combat = slow_print("FIGHTER COMBAT")
    print("")
    Guerrilla_engagment = slow_print("GURRILAA ENGAGEMENT")
    print("")
    Desert_warfare = slow_print("DESERT WARFARE")
    print("")
    Air_to_ground_actions = slow_print("AIR-TO-GROUND ACTIONS")
    print("")
    Tactical_warfare = slow_print("THEATERWIDE TACTICAL WARFARE")
    print("")
    Chemical_Warfare = slow_print("THEATERWIDE BIOTOXIC AND CHEMICAL WARFARE")
    print("")
    print("")
    Gobal = slow_print("GLOBAL THERMONUCLEAR WAR")
    print("")
    print("")
    choose_game = input("")
    if choose_game.lower() == "global thermonuclear war":
        ThermalNuculerWar()
    else:
        slow_print("UNKNOWN")
        GameMenu()

def fast_print(text:str, speed = .001):
        for character in text:
            print(character, end="", flush = True)
            time.sleep(speed)

def ThermalNuculerWar_US():
    os.system('clear')

def QA_GAME15():
    sides = input("ENTER YOUR SIDE:  ")
    if sides.lower() == "united states":
        ThermalNuculerWar_US()
    elif sides.lower() == "soviet union":
        ThermalNuculerWar_SU()
    else:
        slow_print("DID NOT UNDERSTAND")
        QA_GAME15()

def ThermalNuculerWar():
    fast_print(info.MAP)
    fast_print("")
    fast_print("")
    slow_print(info.MAP_SIDES)
    print("\n")
    print("\n")
    print("\n")
    QA_GAME15()



Login()