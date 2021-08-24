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

# # ______________________________stage 2 of 5________________________________________________
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
# print("======================================================================")
# print("Stock size:", len(stock_dominoes))
# print("Computer pieces:", len(computer_dominoes))
# print()
# for domino in domino_snake:
#     print(domino)
# print("\nYour pieces:")
# i = 1
# for domino in player_dominoes:
#     print(i, ":", domino, sep='')
#     i += 1
# print()
# if status == 'player':
#     print("Status: It's your turn to make a move. Enter your command.")
# elif status == 'computer':
#     print("Status: Computer is about to make a move. Press Enter to continue...")
# else:
#     print("Status: something went wrong")

# ______________________________stage 3 of 5________________________________________________
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


def check_player_choice(choice):
    if choice[0] == '-' and choice[1:].isdigit() and -int(choice) < len(player_dominoes) + 1:
        return True
    if choice.isdigit() and int(choice) < len(player_dominoes) + 1:
        return True
    print("Invalid input. Please try again.")
    return False


def print_info():
    print("======================================================================")
    print("Stock size:", len(stock_dominoes))
    print("Computer pieces:", len(computer_dominoes))
    print()
    if len(domino_snake) < 7:
        for domino in domino_snake:
            print(domino, end='')
    else:
        for i in range(3):
            print(domino_snake[i], end='')
        print("...", end='')
        for i in range(3, 0, -1):
            print(domino_snake[-i], end='')
    print()
    print("\nYour pieces:")
    i = 1
    for domino in player_dominoes:
        print(i, ":", domino, sep='')
        i += 1
    print()


def check_domino_snake():
    num_1 = domino_snake[0][0]
    num_2 = domino_snake[-1][1]
    if num_1 == num_2:
        count = 0
        for domino in domino_snake:
            if domino[0] == num_1:
                count += 1
            if domino[1] == num_1:
                count += 1
        if count == 8:
            return False
    return True


initiation()
while True:
    print_info()
    if status == 'player':
        print("Status: It's your turn to make a move. Enter your command.")
        check = False
        while not check:
            player_choice = input()
            check = check_player_choice(player_choice)
        player_choice = int(player_choice)
        if player_choice == 0:
            if len(stock_dominoes) > 0:
                player_dominoes.append(stock_dominoes.pop(random.randint(0, len(stock_dominoes) - 1)))
                status = 'computer'
            else:
                status = 'draw'
        elif player_choice < 0:
            selected_domino = player_dominoes.pop(-player_choice - 1)
            if len(player_dominoes) == 0:
                print_info()
                print("Status: The game is over. You won!")
                break
            domino_snake.insert(0, selected_domino)
            status = 'computer'
            if not check_domino_snake():
                status = 'draw'
        else:
            selected_domino = player_dominoes.pop(player_choice - 1)
            if len(player_dominoes) == 0:
                print_info()
                print("Status: The game is over. You won!")
                break
            domino_snake.append(selected_domino)
            status = 'computer'
            if not check_domino_snake():
                status = 'draw'
    elif status == 'computer':
        print("Status: Computer is about to make a move. Press Enter to continue...")
        input()
        computer_choice = random.randint(-len(computer_dominoes), len(computer_dominoes))
        if computer_choice == 0:
            if len(stock_dominoes) > 0:
                computer_dominoes.append(stock_dominoes.pop(random.randint(0, len(stock_dominoes) - 1)))
                status = 'player'
            else:
                status = 'draw'
        elif computer_choice < 0:
            selected_domino = computer_dominoes.pop(-computer_choice - 1)
            if len(computer_dominoes) == 0:
                print_info()
                print("Status: The game is over. The computer won!")
                break
            domino_snake.insert(0, selected_domino)
            status = 'player'
            if not check_domino_snake():
                status = 'draw'
        else:
            selected_domino = computer_dominoes.pop(computer_choice - 1)
            if len(computer_dominoes) == 0:
                print_info()
                print("Status: The game is over. You won!")
                break
            domino_snake.append(selected_domino)
            status = 'player'
            if not check_domino_snake():
                status = 'draw'
    elif status == 'draw':
        print("Status: The game is over. It's a draw!")
        break
    else:
        print("Status: something went wrong")
