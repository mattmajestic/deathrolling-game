import random
from models import GameState

class GameLogic:
    def __init__(self, game_state: GameState):
        self.game_state = game_state

    def roll_dice(self):
        current_player = self._get_current_player()
        opponent_player = self._get_opponent_player()

        # The current player's roll is between 1 and the opponent's last roll
        new_roll = random.randint(1, opponent_player.current_roll)
        current_player.current_roll = new_roll
        current_player.status = f"{current_player.name} rolled a {new_roll}."

        if new_roll == 1:
            self.game_state.game_over = True
            self.game_state.winner = opponent_player.name
            current_player.status = f"{current_player.name} rolled a 1 and lost the game!"
        else:
            self._switch_turn()

    def _get_current_player(self):
        return self.game_state.player1 if self.game_state.player1.is_turn else self.game_state.player2

    def _get_opponent_player(self):
        return self.game_state.player2 if self.game_state.player1.is_turn else self.game_state.player1

    def _switch_turn(self):
        self.game_state.player1.is_turn = not self.game_state.player1.is_turn
        self.game_state.player2.is_turn = not self.game_state.player2.is_turn
