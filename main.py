firstwin = 0
secondwin = 0
while firstwin <3 and secondwin < 3:
    first = input ("Player 1 choose: rock, paper, or scissors")
    second = input ("Player 2 choose rock, paper, or scissors")

    if first == "rock" and second == "scissors":
        firstwin = firstwin + 1
        print ("first player you won! :)")

    if first == "rock" and second == "paper":
        secondwin = secondwin + 1
        print ("second player you won! :)")

    if first == "rock" and second == "rock":
        print ("tie -_-")

    if first == "paper" and second == "scissors":
        secondwin  = secondwin + 1
        print ("second player you won! :)")

    if first == "paper" and second == "rock":
        firstwin = firstwin + 1
        print ("first player you won! :)")

    if first == "paper" and second == "paper":
        print ("tie -_-")

    if first == "scissors" and second == "paper":
        firstwin = firstwin = 1
        print ("first player you won! :)")

    if first == "scissors" and second == "rock":
        secondwin = secondwin + 1
        print ("second player you won! :)")

    if first == "scissors" and second == "scissors":
        print ("tie -_-")

    if firstwin == 3:
        print("first player you have won the game!! ^_^")
    if secondwin == 3:
        print ("second player you have won the game!! ^_^")