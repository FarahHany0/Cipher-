#this_is_kayles_game
#we will start with 20 tokens with 2 players
#each player can remove one or two adjacent tokens
#the player who takes the last token wins!!
tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , 15, 16, 17, 18, 19, 20]
win = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_","_"]
#Displaying the tokens
def display_state():
    global tokens
    print("tokens = ", tokens)
#the turn of the first player
def player1_move(player):
    num_tokens = int(input("player_1, Are you going to remove 1 number or 2 numbers? "))
    if num_tokens == 2 :
        num_1 = int(input("please enter the first number:"))
        while num_1 not in tokens :        #repeating unitll the right number is entered
                num_1 = int(input("please enter a number that hasn't been removed: "))
        num_2 = int(input("please enter the second number: "))
        while num_2  not in tokens:        #repeating unitll the right number is entered
                num_2 = int(input("please enter a number that hasn't been removed: "))
        if num_2 != (num_1+1):      # checking if the two numbers are adjacent
            num_2 = int(input('please enter a number that is adjacent to the first one: '))
            for i in range(len(tokens)):      #replacing the number with (_) which means that the number is removed
                del tokens[num_1 - 1]
                tokens.insert(num_1-1, "_")
                del tokens[num_2-1]
                tokens.insert(num_2-1, "_")
        else:
            for i in range(len(tokens)):
                del tokens[num_1 - 1]
                tokens.insert(num_1 - 1, "_")
                del tokens[num_2 - 1]
                tokens.insert(num_2 - 1, "_")
    else:
        num = int(input("please enter the number you want to delete: "))
        while num not in tokens:
            num = int(input("please enter a number that hasn't been removed: "))
        del tokens[num - 1]
        tokens.insert(num - 1, "_")
# second player's turn
def player2_move(player):
    num_tokens = int(input("player_2, Are you going to remove 1 number or 2 numbers? "))
    if num_tokens == 2 :
        num_1 = int(input("please enter the first number:"))
        while num_1 not in tokens:
                num_1 = int(input("please enter a number that hasn't been removed: "))
        num_2 = int(input("please enter the second number: "))
        while num_2  not in tokens:
                num_2 = int(input("please enter a number that hasn't been removed: "))
        if num_2 != (num_1+1):
            num_2 = int(input('please enter a number that is adjacent to the first one: '))
            for i in range(len(tokens)):
                del tokens[num_1 - 1]
                tokens.insert(num_1-1, "_")
                del tokens[num_2-1]
                tokens.insert(num_2-1, "_")
        else:
            for i in range(len(tokens)):
                del tokens[num_1 - 1]
                tokens.insert(num_1 - 1, "_")
                del tokens[num_2 - 1]
                tokens.insert(num_2 - 1, "_")
    else:
        num = int(input("please enter the number you want to delete: "))
        while num not in tokens:
                num = int(input("please enter a number that hasn't been removed: "))
        del tokens[num - 1]
        tokens.insert(num - 1, "_")
# updating the tokens list
def update_state(deleted_tokens):
    global token
# checking if player took the last numbers and won
def is_A_Winner():
    if tokens == win :
        return True
# playing kayles game
def play_kayles_game():
    display_state()
    while(True):      # repeating till one of them loses
        first = player1_move("first")
        update_state(first)
        display_state()    # displaying the new tokens list
        if (is_A_Winner()):
            print("player_1 won!!!")
            break
        second = player2_move("second")
        update_state(second)
        display_state()
        if (is_A_Winner()):
            print("player_2 won!!!")
            break
play_kayles_game()







