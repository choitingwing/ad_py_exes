from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.round = 1        
        self.wins = 0
        self.loses = 0
        self.c = 0

    def roll(self):
        self.dice = Die.create_dice(5)

    def reset(self):
        self.round = 1        
        self.wins = 0
        self.loses = 0
        self.c = 0


    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        
        
        runner = cls()
        while True:
            runner.roll()
            print("-------------------- Round {}----------------------\n".format(runner.round))   
            for die in runner.dice:
                print(die.show())
            print(runner.answer())
            while True:
                guess = input("Sigh. What is your guess?: ")
                if guess.isdigit():
                    guess = int(guess)
                    break
                else:
                    print("Not integer, try again!")

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                runner.c += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                runner.c = 0
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round += 1

            if runner.c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                prompt = input("Would you like to play again?[Y/n]: ")
                if prompt == 'y' or prompt == '':
                    runner.reset()
                    continue
                else:
                    i_just_throw_an_exception()
                # break
            


            


