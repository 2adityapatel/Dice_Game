import random


class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value
    

class Player:

    def __init__(self, die, is_computer=False ):
        self._die = die
        self._is_computer = is_computer
        self._counter = 0

    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        return self._counter
    
    def increment_counter(self):
        self._counter += 3


    def roll_die(self):
        return self._die.roll()


class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("\n:::::::::::::::::::::::::::::::::::::::::")
        print("🎲 Welcome to Roll the Dice!")
        print(":::::::::::::::::::::::::::::::::::::::::\n")
        no_of_rounds = int(input("Enter number of rounds to play : "))

        self.recursive_play(no_of_rounds)
        self.check_game_over()

    def recursive_play(self, no_of_rounds):
        if no_of_rounds == 0:
            return 
        self.recursive_play(no_of_rounds-1)
        self.play_round(no_of_rounds)


    def play_round(self, round_no):

        self.print_round_welcome(round_no)

        # Roll the dice
        
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        # Show the values
        self.show_dice(player_value, computer_value)

        # Determine winner and Loser
        if player_value > computer_value:
            self.update_counter(winner=self._player)
            print("You won the round. 😁")
        elif computer_value > player_value:
            self.update_counter(winner=self._computer)
            print("Computer has won this round. Try again. 😢")
        else:
            print("Its a tie. 😊")

        # Show counter
        self.show_counters()
        

    def print_round_welcome(self, round_no):
        print(f"\n---------- Round {round_no} ----------")
        input("🎲 Press any key to roll the dice.🎲\n")

    def show_dice(self, player_value, computer_value):
        print(f"\nYour Die  : {player_value}")
        print(f"Computer Die : {computer_value}\n")

    def update_counter(self, winner):
        winner.increment_counter()

    def show_counters(self):
        print(f"\nYour counter : {self._player.counter}")
        print(f"Computer counter : {self._computer.counter}\n")

    def check_game_over(self):
        if self._player.counter > self._computer.counter :
            self.show_game_over(self._player)
            return True
        elif self._computer.counter > self._player.counter:
            self.show_game_over(self._computer)
            return True
        else:
            self.show_game_over(tie=True)
            return False
        
    def show_game_over(self, winner=None,tie=False):
        if tie == True:
            print("\n:::::::::::::::::::::::::::::::::::::::")
            print(" G A M E  O V E R ")
            print(" IT'S a T I E ..... ")
            print(":::::::::::::::::::::::::::::::::::::::\n")
        elif winner.is_computer:
            print("\n:::::::::::::::::::::::::::::::::::::::")
            print(" G A M E  O V E R ")
            print("The Computer won the game !! Sorry 😢")
            print(":::::::::::::::::::::::::::::::::::::::\n")
        else:
            print("\n:::::::::::::::::::::::::::::::::::::::")
            print(" G A M E  O V E R ")
            print("You won the game !!!! 😁")
            print(":::::::::::::::::::::::::::::::::::::::\n")



# Create Die
player_die = Die()
computer_die = Die()

# Create Players
my_player = Player(player_die, False)
c_player = Player(computer_die, True)

# Create Game
game = DiceGame(my_player, c_player)

# Start Game
game.play()


# Task 1 : - Provide number of rounds to play between player and computer
#          - Show playing the number of rounds methods using recursion
# Task 2 : - Creating Multiplayer - ( Addition of Multi Players and Computer Players )
#          - Adding leaderboard ( Hall of Fame ) 
# Task 3 : - Creating custom dices ( Ex : Use Inheritance )