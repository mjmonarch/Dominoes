# # ______________________________stage 1 of 5________________________________________________
# import random
#
# player_dominoes = []  # set of player's dominoes
# computer_dominoes = []  # set of computer's dominoes
# stock_dominoes = []  # set of stock dominoes
# domino_snake = []  # 1 starting domino
# status = None  # the player that goes first
#
#
# def initiation():
#     # initiating full domino set
#     full_domino = []
#     for i in range(7):
#         for j in range(i, 7):
#             full_domino.append([i, j])
#     left_domino = full_domino[:]
#
#     # initiating Player pieces
#     global player_dominoes
#     player_dominoes = random.sample(left_domino, 7)
#     for domino in player_dominoes:
#         left_domino.remove(domino)
#
#     # initiating Computer pieces
#     global computer_dominoes
#     computer_dominoes = random.sample(left_domino, 7)
#     for domino in computer_dominoes:
#         left_domino.remove(domino)
#
#     # initiating Stock pieces
#     global stock_dominoes
#     stock_dominoes = left_domino[:]
#     check_initiation()
#
#
# def check_initiation():
#     success = False
#     global status
#     for i in range(7, 0, -1):
#         if [i, i] in player_dominoes:
#             domino_snake.append([i, i])
#             player_dominoes.remove([i, i])
#             status = 'computer'
#             success = True
#             break
#         elif [i, i] in computer_dominoes:
#             domino_snake.append([i, i])
#             computer_dominoes.remove([i, i])
#             status = 'player'
#             success = True
#             break
#     while not success:
#         initiation()
#
#
# initiation()
# print("Stock pieces: ", stock_dominoes)
# print("Computer pieces: ", computer_dominoes)
# print("Player pieces: ", player_dominoes)
# print("Domino snake: ", domino_snake)
# print("Status: ", status)

# ______________________________stage 2 of 5________________________________________________
import random

player_dominoes = []  # set of player's dominoes
computer_dominoes = []  # set of computer's dominoes
stock_dominoes = []  # set of stock dominoes
domino_snake = []  # 1 starting domino
status = None  # the player that goes first


def initiation():
    # initiating full domino set
    full_domino = []
    for i in range(7):
        for j in range(i, 7):
            full_domino.append([i, j])
    left_domino = full_domino[:]

    # initiating Player pieces
    global player_dominoes
    player_dominoes = random.sample(left_domino, 7)
    for domino in player_dominoes:
        left_domino.remove(domino)

    # initiating Computer pieces
    global computer_dominoes
    computer_dominoes = random.sample(left_domino, 7)
    for domino in computer_dominoes:
        left_domino.remove(domino)

    # initiating Stock pieces
    global stock_dominoes
    stock_dominoes = left_domino[:]
    check_initiation()


def check_initiation():
    success = False
    global status
    for i in range(7, 0, -1):
        if [i, i] in player_dominoes:
            domino_snake.append([i, i])
            player_dominoes.remove([i, i])
            status = 'computer'
            success = True
            break
        elif [i, i] in computer_dominoes:
            domino_snake.append([i, i])
            computer_dominoes.remove([i, i])
            status = 'player'
            success = True
            break
    while not success:
        initiation()


initiation()
print("======================================================================")
print("Stock size:", len(stock_dominoes))
print("Computer pieces:", len(computer_dominoes))
print()
for domino in domino_snake:
    print(domino)
print("\nYour pieces:")
i = 1
for domino in player_dominoes:
    print(i, ":", domino, sep='')
    i += 1
print()
if status == 'player':
    print("Status: It's your turn to make a move. Enter your command.")
elif status == 'computer':
    print("Status: Computer is about to make a move. Press Enter to continue...")
else:
    print("Status: something went wrong")
