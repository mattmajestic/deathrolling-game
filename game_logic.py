import random
from models import GameState

class GameLogic:
    def __init__(self, game_state):
        self.game_state = game_state

    def roll_dice(self, player=None):
        if player is None:
            player = self._get_current_player()

        # Roll the dice
        player.current_roll = random.randint(1, player.current_roll)
        player.is_turn = False

        # Check if game over
        if player.current_roll == 1:
            self.game_state.game_over = True
            self.game_state.winner = self._get_opponent_player().name

        # Switch turns
        self._switch_turns()
        return player.current_roll

    def _get_current_player(self):
        if self.game_state.player1.is_turn:
            return self.game_state.player1
        return self.game_state.player2

    def _get_opponent_player(self):
        if self.game_state.player1.is_turn:
            return self.game_state.player2
        return self.game_state.player1

    def _switch_turns(self):
        self.game_state.player1.is_turn = not self.game_state.player1.is_turn
        self.game_state.player2.is_turn = not self.game_state.player2.is_turn
