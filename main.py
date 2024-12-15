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
        self._counter = 10

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
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        return self._die.roll()


class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print(":::::::::::::::::::::::::::::::::::::::::")
        print("🎲 Welcome to Roll the Dice!")
        print(":::::::::::::::::::::::::::::::::::::::::")

        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break


    def play_round(self):
        # Welcome the user
        self.print_round_welcome()

        # Roll the dice
        
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        # Show the values
        self.show_dice(player_value, computer_value)

        # Determine winner and Loser
        if player_value > computer_value:
            self.update_counter(winner=self._player, loser=self._computer)
            print("You won the round. 😁")
        elif computer_value > player_value:
            self.update_counter(winner=self._computer, loser=self._player)
            print("Computer has won this round. Try again. 😢")
        else:
            print("Its a tie. 😊")

        # Show counter
        self.show_counters()
        

    def print_round_welcome(Self):
        print("---------- New Round ----------")
        input("🎲 Press any key to roll the dice.🎲")

    def show_dice(self, player_value, computer_value):
        print(f"Your Die  : {player_value}")
        print(f"Computer Die : {computer_value}")

    def update_counter(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def show_counters(self):
        print(f"Your counter : {self._player.counter}")
        print(f"Computer counter : {self._computer.counter}")

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True
        else:
            return False
        
    def show_game_over(self, winner):
        if winner.is_computer:
            print("\n:::::::::::::::::::::::::::::::::::::::")
            print(" G A M E  O V E R ")
            print("The Computer won the game !! Sorry 😢")
            print("\n:::::::::::::::::::::::::::::::::::::::")
        else:
            print("\n:::::::::::::::::::::::::::::::::::::::")
            print(" G A M E  O V E R ")
            print("You won the game !!!! 😁")
            print("\n:::::::::::::::::::::::::::::::::::::::")



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