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

    def __init__(self, name, is_computer):
        self._die_value = None
        self._name = name
        self._is_computer = is_computer
        self._counter = 0


    @property
    def name(self):
        return self._name

    @property
    def die_value(self):
        return self._die_value
    
    @die_value.setter
    def die_value(self, new_value):
        self._die_value = new_value
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        return self._counter
    
    def increment_counter(self, value):
        self._counter += value



class DiceGame:

    def __init__(self):
        self._players = []
    
    @property
    def players(self):
        return self._players

    
    def generate_players(self):

        player_count = int(input("Enter the no. of players to play : "))

        while player_count < 2:
            print("Player should be more than 2 !!!!!!!!! ")
            player_count = int(input("Enter the no. of players to play : "))
        
        for i in range(player_count):
            print(f"-------- Player {i+1} --------")
            name = input("Enter ur name : ")
            ans = input("Are u computer ? 'Y' for yes 'N' for no ").capitalize()[0]
            is_computer = (ans == 'Y')

            self._players.append(Player(name, is_computer))
            

    def welcome_message(self):
        print("\n:::::::::::::::::::::::::::::::::::::::::")
        print("🎲 Welcome to Roll the Dice!")
        print(":::::::::::::::::::::::::::::::::::::::::\n")


    def play(self):
        self.welcome_message()
        self.generate_players()

        no_of_rounds = int(input("\nEnter number of rounds to play : "))

        self.recursive_play(no_of_rounds)
        self.show_final_leaderboard()

    def recursive_play(self, no_of_rounds):
        if no_of_rounds == 0:
            return 
        self.recursive_play(no_of_rounds-1)
        self.play_round(no_of_rounds)


    def play_round(self, round_no):

        self.print_round_welcome(round_no)

        # Roll the dice
        round_die_values = self.roll_dice()

        # Current Round Values
        self.print_round_die_value(round_die_values)


        # Calculate scores : 
        self.calculate_score(round_die_values)

        # show winner 
        self.show_round_winner(round_die_values)

        
        

    def roll_dice(self):

        dice = Die()
        round_die_values = {}

        for player in self.players: 
            if player.is_computer == False:
                print(f"\nPlayer : {player.name}")
                choice = input("Do u want to play ur dice ? Enter 'Y' for yes 'N' for no. ").capitalize()[0]
                if (choice != 'Y'):
                    return
                
            else:
                print(f"\nComputer : {player.name}")
            print(f"\nPlaying {player.name}'s die ... ")
            player.die_value = dice.roll()
            round_die_values[player] = dice.value
                
        return round_die_values

    def print_round_die_value(self, round_die_values):
        print("\n------------- Current round score ------------- \n")
        for person in round_die_values.keys():
            print(f"{person.name} die value : {round_die_values[person]} ")

    def calculate_score(self, round_die_values):
        # round_die_values_sorted = dict(sorted(round_die_values.items(), key=lambda item: item[1]))

        for player,score in round_die_values.items():
            player.increment_counter(score)
    
    def show_round_winner(self, round_die_values):
        round_die_values_sorted = dict(sorted(round_die_values.items(), key=lambda item: item[1],reverse=True))

        winners = []
        top_score_value = 0
        
        # multiple winners
        for player,value in (round_die_values_sorted.items()):
            if top_score_value > value:
                break
            top_score_value = value
            winners.append(player)
        
        print("The round winner are : ")
        for winner in winners:
            print(f"- {winner.name}")
        print(f"With round score value - {top_score_value}")


    def print_round_welcome(self, round_no):
        print(f"\n----------You are entering Round {round_no} ----------")
        # input("🎲 Press any key to roll the dice.🎲\n")

    def get_players_score(self):
        player_scores = {}
        for player in self._players:
            player_scores[player.name] = player.counter
        return player_scores
    
        
    def show_final_leaderboard(self):
    
        print("\n:::::::::::::::::::::::::::::::::::::::")
        print(" G A M E  O V E R ")
        print(":::::::::::::::::::::::::::::::::::::::\n")
        
        print("-----------\t H A L L  O F  F A M E \t-----------")

        player_scores = self.get_players_score()

        player_scores_sorted = dict(sorted(player_scores.items(), key=lambda item: item[1],reverse=True))

        previous_score = None
        position = 0
        index = 1
        print(f"{'Player No.':<15}{'Player Name':<20}{'Player Position':<20}{'Player Score':<15}")


        for player,score in player_scores_sorted.items():
            if previous_score != score:
                position += 1
            print(f"{index:<15}{player:<20}{position:<20}{score:<15}")
            index += 1
            previous_score = score


class OddDiceGame(DiceGame):

    def calculate_score(self, round_die_values):

        for player,value in round_die_values.items():
            if value%2 == 0:
                round_die_values[player] = (value*10)
            else:
                round_die_values[player] = (value*-10)

        return super().calculate_score(round_die_values)
    
    def welcome_message(self):
        super().welcome_message()
        print("\n:::::::::::::::::::::::::::::::::::::::::")
        print("🎲 LUCKY IF YOU DONT GET ODD VALUES ")
        print(":::::::::::::::::::::::::::::::::::::::::\n")

    
class BlackDiceGame(DiceGame):

    BLACK_DIE_VALUES = [3,5]

    def welcome_message(self):
        super().welcome_message()
        print("\n:::::::::::::::::::::::::::::::::::::::::")
        print("🎲 BLACK DICE ☠️  ☠️  ☠️  ☠️  ☠️  ☠️ ")
        print("Score for round is 0 if got 3 or 5 😁")
        print(":::::::::::::::::::::::::::::::::::::::::\n")

    def calculate_score(self, round_die_values):

        for player,value in round_die_values.items():
            if value in BlackDiceGame.BLACK_DIE_VALUES:
                round_die_values[player] = 0
            else:
                round_die_values[player] = (value*10)

        return super().calculate_score(round_die_values)
    



# Create Game
# game = DiceGame()
# game = BlackDiceGame()
game = OddDiceGame()

# Start Game
game.play()


# Task 1 : - Provide number of rounds to play between player and computer
#          - Show playing the number of rounds methods using recursion
# Task 2 : - Creating Multiplayer - ( Addition of Multi Players and Computer Players )
#          - Adding leaderboard ( Hall of Fame ) 
# Task 3 : - Creating custom dices ( Ex : Use Inheritance )