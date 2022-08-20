game = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

def create_board(game):
    print(game[0] + "|" + game[1] + "|" + game[2])
    print("--" + "--" + "--")
    print(game[3] + "|" + game[4] + "|" + game[5])
    print("--" + "--" + "--")
    print(game[6] + "|" + game[7] + "|" + game[8])



def game_play(game, tries = 0):
    lst = []
    for i in range(9):
        if tries % 2 == 0:
            player = "x"
        else:
            player = "o"
        box = int(input(f"Select a position to place {player} (1 to 9): ")) - 1
        if box in lst:
            print("Number has already been inputed")
        else:
            if box >= 0 and box <= 9:
                game[box] = player
                tries += 1
                create_board(game)
                lst.append(box)
                if tries >= 5:
                    if game[0] == game[1] == game[2] and game[0] != "-":
                        print(f"Yay {player} won")
    
                    if game[0] == game[4] == game[8] and game[0] != "-":
                        print(f"Yay {player} won")

                    if game[1] == game[4] == game[7] and game[1] != "-":
                        print(f"Yay {player} won")
                    
                    if game[2] == game[4] == game[6] and game[2] != "-":
                        print(f"Yay {player} won")

                    if game[2] == game[5] == game[8] and game[2] != "-":
                        print(f"Yay {player} won")

                    if game[3] == game[4] == game[5] and game[3] != "-":
                        print(f"Yay {player} won")

                    if game[6] == game[7] == game[8] and game[6] != "-":
                        print(f"Yay {player} won")

                    if tries == 9:
                        print("It's a tie") 
                    retry = input("Would you like to play again? Enter Yes or No: ")
                    if retry == "Yes":
                        for i in range(len(game)):
                            game[i] = "-"
                        game_play(game, tries = 0) 
                        break 
                    elif retry == "No":
                        break
                    else:
                        print("Print enter Yes or No")
            else:
                print("Number out of range")
      
game_play(game)
