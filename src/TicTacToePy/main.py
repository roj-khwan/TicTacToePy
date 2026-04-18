from TicTacToePy.game import Game

def main():
    game = Game()

    game.Display()
    print('---------')
    print("7 | 8 | 9\n4 | 5 | 6\n1 | 2 | 3")
    while (True):
        slotPlayed = input(": ")
        valid, move = game.TryParseMove(slotPlayed)

        if not valid:
            print("Not valid, reason : " + move)
            continue

        game.Run(move)
        game.Display()

if __name__ == "__main__":
    main()