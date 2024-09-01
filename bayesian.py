import numpy as np
import random
import os
import json
from scipy.stats import beta

def death_rolling_simulation(num_games):
    player1_wins = 0
    player2_wins = 0

    for _ in range(num_games):
        max_roll = 100
        player1_turn = True

        while max_roll > 1:
            roll = random.randint(1, max_roll)
            if roll == 1:
                if player1_turn:
                    player2_wins += 1
                else:
                    player1_wins += 1
                break
            max_roll = roll
            player1_turn = not player1_turn

    return player1_wins, player2_wins

# Parameters for the Beta distribution (prior)
alpha1 = 1
beta1 = 1
alpha2 = 1
beta2 = 1

# Simulate games and update the posterior
num_games = 100000
player1_wins, player2_wins = death_rolling_simulation(num_games)

# Update posterior for player 1
posterior_player1 = beta(alpha1 + player1_wins, beta1 + num_games - player1_wins)

# Update posterior for player 2
posterior_player2 = beta(alpha2 + player2_wins, beta2 + num_games - player2_wins)

# Calculate mean of posterior distributions
player1_win_probability = posterior_player1.mean()
player2_win_probability = posterior_player2.mean()

# Prepare the results dictionary
results = {
    "player1_win_probability": player1_win_probability,
    "player2_win_probability": player2_win_probability
}

# Ensure the sims/ directory exists
os.makedirs('sims', exist_ok=True)

# Store results in a JSON file
with open('sims/death_rolling_bayesian_results.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)

# Print confirmation
print(f"Results saved to 'sims/death_rolling_bayesian_results.json'")

