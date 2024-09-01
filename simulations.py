import random
import numpy as np
import json
import os

def death_rolling_simulation(num_games):
    player1_wins = 0
    player2_wins = 0
    rolls_per_game = []

    for _ in range(num_games):
        max_roll = 100
        player1_turn = True
        rolls_in_game = 0

        while max_roll > 1:
            roll = random.randint(1, max_roll)
            rolls_in_game += 1
            if roll == 1:
                if player1_turn:
                    player2_wins += 1
                else:
                    player1_wins += 1
                break
            max_roll = roll
            player1_turn = not player1_turn

        rolls_per_game.append(rolls_in_game)

    return player1_wins, player2_wins, rolls_per_game

# Simulate 100,000,000 games
num_games = 100000000
player1_wins, player2_wins, rolls_per_game = death_rolling_simulation(num_games)

# Calculate proportions
player1_win_probability = player1_wins / num_games
player2_win_probability = player2_wins / num_games

# Calculate basic statistics
average_rolls = float(np.mean(rolls_per_game))  # Convert to native Python float
max_rolls = int(np.max(rolls_per_game))         # Convert to native Python int
min_rolls = int(np.min(rolls_per_game))         # Convert to native Python int

# Prepare the results dictionary
results = {
    "player1_win_probability": player1_win_probability,
    "player2_win_probability": player2_win_probability,
    "average_rolls_per_game": average_rolls,
    "max_rolls_in_game": max_rolls,
    "min_rolls_in_game": min_rolls
}

# Ensure the sims/ directory exists
os.makedirs('sims', exist_ok=True)

# Store results in a JSON file
with open('sims/death_rolling_results.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)

# Print confirmation
print(f"Results saved to 'sims/death_rolling_results.json'")
