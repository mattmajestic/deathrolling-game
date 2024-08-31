from flask import Flask, render_template, request, jsonify
from models import Player, GameState
from game_logic import GameLogic

app = Flask(__name__)

game_state = None
game_logic = None
roll_count = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    global game_state, game_logic, roll_count
    data = request.json  # Expect JSON data
    wager_amount = int(data['wager_amount'])
    roll_count = 0

    # Initialize game state
    game_state = GameState(
        player1=Player(name="Player 1", current_roll=wager_amount, is_turn=True),
        player2=Player(name="Player 2", current_roll=wager_amount)
    )
    game_logic = GameLogic(game_state)

    # Since it's Player 1's turn, the current_roll should be set to the wager amount
    player1_initial_roll = game_logic.roll_dice(player=game_state.player1)

    return jsonify({
        'roll_count': roll_count,
        'current_roll': player1_initial_roll,  # Return the correct initial roll
        'status': "Game started!",
        'player1_status': game_state.player1.status,
        'player2_status': game_state.player2.status
    })

@app.route('/roll_dice', methods=['POST'])
def roll_dice():
    global roll_count
    roll_count += 1

    # Roll for the current player
    current_player = game_logic._get_current_player()
    game_logic.roll_dice()

    # Check if the game is over after the roll
    game_over = game_state.game_over
    winner = game_state.winner if game_over else None

    return jsonify({
        'roll_count': roll_count,
        'current_roll': current_player.current_roll,
        'status': f"{current_player.name} rolled {current_player.current_roll}",
        'game_over': game_over,
        'winner': winner
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
