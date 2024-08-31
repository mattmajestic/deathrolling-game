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

    return jsonify({
        'roll_count': roll_count,
        'current_roll': game_state.player1.current_roll,
        'status': "Game started!",
        'player1_status': game_state.player1.status,
        'player2_status': game_state.player2.status
    })

@app.route('/roll_dice', methods=['POST'])
def roll_dice():
    global roll_count
    roll_count += 1
    game_logic.roll_dice()

    current_player = game_logic._get_current_player()
    opponent_player = game_logic._get_opponent_player()

    return jsonify({
        'roll_count': roll_count,
        'current_roll': current_player.current_roll,
        'status': f"{current_player.status} | {opponent_player.status}",
        'game_over': game_state.game_over,
        'winner': game_state.winner
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
