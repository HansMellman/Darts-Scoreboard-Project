

### Obtain number of players and player names - populate player_names list. ####
def get_player_info():
    player_names = []
    players = int(input("How many players are there?: "))
    p_count = 0
    for i in range(players):
        p_count += 1
        player_name = input(f"Please enter name for player {p_count}: ")
        player_names.append(player_name)
    return player_names

player_names = get_player_info()
players = len(player_names)

###### Game score setup ######
def game_score_setup(player_names, players):
    while True:
        try:
            game_score = int(input("Please choose the game, enter 301 or 501: "))
            if game_score in [301, 501]:
                if players == 2:
                    print(f"{player_names[0]} vs {player_names[1]}")
                print(f"\nGame begins!")
                break
            else:
                print("Sorry, you've entered an incorrect number for the game score, please enter either 301 or 501.")
        except ValueError:
            print("Please enter a number for the game score, either 301 or 501.")
    return game_score


game_score = game_score_setup(player_names, players)
game_scores = [game_score] * players  # sets a game score for each player.
darts_thrown = [0] * players

##### Main game loop #####
player_won = False # Game loop flag
while not player_won:
    for i in range(len(player_names)):
        player_name = player_names[i]
        p_score = int(input(f"\nPlease enter {player_name}'s score: "))
        darts_thrown[i] += 3
        if p_score <= game_scores[i]: # This check stops it going below 0.
            game_scores[i] -= p_score
        else:
            print("\nYou're bust!!")
        if game_scores[i] == 0:
            print("\nYou've won!!")
            player_won = True
            break
        else:
            print(game_scores[i].__str__() + " remaining")

#### Calculate player average ####
for i in range(len(player_names)):
    average = (game_score - game_scores[i]) / darts_thrown[i]
    average = round(average)
    print(f"\nWell done {player_names[i]}, your average for this game was {average}.")


