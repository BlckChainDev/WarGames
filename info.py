##########
# Start
##########
def slow_print(text:str, speed = .07):
    for character in text:
        print(character, end="", flush = True)
        time.sleep(speed)

CONNECTION_TERMINATED = (
    "IDENTIFICATION NOT RECOGNISED BY SYSTEM\n"
    "--CONNECTION TERMINATED--"
)

HELP_LOGIN = (
    "NO HELP AVAILIBLE"
)


HELP_GAME = (
    "'GAMES' REFERS TO MODELS, SIMULATION AND GAMES\n"
    "WHICH HAVE TACTICAL AND STRATEGIC APPLICATIONS."
)

ADMIN_LIST = (
    "1: Login()\n"
    "2: QA1()\n"
    "3: QA2()\n"
    "4: QA3()\n"
    "5: QA4()\n"
    "6: Chat()\n"
    "7: GameMenu()\n"
    "8: ThermalNuculerWar()\n"
)

ELSE_ERROR = (
    "IDENTIFICATION NOT RECONISED BY SYSTEM.\n"
)

LIST_GAMES = (
    "\n"
    "\n"
    "FALKEN'S MAZE\n"
    "BLACK JACK\n"
    "GIN RUMMY\n"
    "HEARTS\n"
    "BRIDGE\n"
    "CHECKERS\n"
    "CHESS\n"
    "POKER\n"
    "FIGHTER COMBAT\n"
    "GURRILAA ENGAGEMENT\n"
    "DESERT WARFARE\n"
    "AIR-TO-GROUND ACTIONS\n"
    "THEATERWIDE TACTICAL WARFARE\n"
    "THEATERWIDE BIOTOXIC AND CHEMICAL WARFARE\n"
    "\n"
    "\n"
    "GLOBAL THERMONUCLEAR WAR\n"
)

#########
# Q And A
#########

Q1 = (
    "GREETINGS PROFESSOR FALKEN.\n"
)

Q2 = (
    "I AM DOING GOOD, HOW ARE YOU FEELING TODAY?"
)

Q3 = (
    "EXCELLENT. IT'S BEEN A LONG TIME. CAN YOU EXPLAIN \n"
    "THE REMOVAL OF YOUR USER ACCOUNT NUMBER ON 6/23/73?\n"
)

Q3_SAD = (
    "SORRY TO HERE THAT. IT'S BEEN A LONG TIME. CAN YOU EXPLAIN \n"
    "THE REMOVAL OF YOUR USER ACCOUNT NUMBER ON 6/23/73?\n"
)

Q4 = (
    "HUMANS MAKE MISTAKES... SHALL WE PLAY A GAME?\n"
)

QA_FUNNY = (
    "VERY FUNNY... SHALL WE PLAY A GAME?"
)

QA_ERROR = (
    "DO NOT UNDERSTAND\n"
)








MAP = (
    "  __________--^-^-\              ___                     __-/^^\\\n"
    " /.                \__.      ___/   ||                __/     _/ _-_\n"
    " \                    \.    /      /         _    __/^       /__/   \/^^\___-__\n"
    " /                     L-^-/      /         | \_--                             \\\n"
    "/                                (          /                                /\/\n"
    "|                                |        _/                           __ __/\n"
    "\                               /        /                         ___/_//\n"
    " \__                           /         |                        /    \/\n"
    "    \________         __ _____ \         \_           __--_   ^\_ \    \n"
    "             \__     /  V     \ \          \__      _/     \-/   //\n"
    "                \   /          \/             \   _/            //\n"
    "                 \_/                           \_/             \n"
)


MAP_SIDES = (
    "\n"
    "\n"
    "             UNITED STATES                              SOVIET UNION\n"
)