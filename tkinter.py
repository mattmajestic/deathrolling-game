import tkinter as tk
from tkinter import font as tkfont
import time
from models import Player, GameState
from game_logic import GameLogic

class DeathrollingGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Deathrolling Game")
        self.root.configure(bg='#2c2c2c')  # Dark mode background
        self.root.geometry("600x400")  # Larger window size

        # Set up initial state
        self.wager_amount = tk.IntVar(value=1000)
        self.roll_count = tk.IntVar(value=0)
        self.game_state = None
        self.game_logic = None

        self.create_widgets()

    def create_widgets(self):
        title_font = tkfont.Font(family="Helvetica", size=20, weight="bold")
        label_font = tkfont.Font(family="Helvetica", size=14)

        # Title
        self.title_label = tk.Label(self.root, text="Deathrolling Game", font=title_font, bg='#2c2c2c', fg='#ffffff')
        self.title_label.pack(pady=10)

        # Input for Wager Amount
        self.wager_label = tk.Label(self.root, text="Wager Amount $", font=label_font, bg='#2c2c2c', fg='#ffffff')
        self.wager_label.pack(pady=5)

        self.wager_entry = tk.Entry(self.root, textvariable=self.wager_amount, font=label_font, bg='#333333', fg='#ffffff')
        self.wager_entry.pack(pady=5)

        # Confirm button
        self.confirm_button = tk.Button(self.root, text="Confirm", command=self.confirm_wager, font=label_font, bg='#4CAF50', fg='#ffffff')
        self.confirm_button.pack(pady=15)

        # Roll count display
        self.roll_count_label = tk.Label(self.root, text="", font=label_font, bg='#2c2c2c', fg='#ffffff')
        self.roll_count_label.pack(pady=10)

        # Display current roll (hidden initially)
        self.roll_label = tk.Label(self.root, text="", font=label_font, bg='#2c2c2c', fg='#ffffff')
        self.roll_label.pack(pady=10)

        # Status display (hidden initially)
        self.status_label = tk.Label(self.root, text="", font=label_font, bg='#2c2c2c', fg='#ffffff')
        self.status_label.pack(pady=10)

    def confirm_wager(self):
        wager_amount_value = self.wager_amount.get()

        # Initialize game state
        self.game_state = GameState(
            player1=Player(name="Player 1", current_roll=wager_amount_value, is_turn=True),
            player2=Player(name="Player 2", current_roll=wager_amount_value)
        )
        self.game_logic = GameLogic(self.game_state)

        # Update UI
        self.roll_count_label.config(text=f"Roll Count: 0")
        self.roll_label.config(text=f"Current Roll: {self._current_roll_display()}")
        self.status_label.config(text="Game started!")
        self.confirm_button.pack_forget()  # Hide confirm button
        self.wager_entry.config(state="disabled")  # Disable input after confirmation

        self.auto_roll()

    def auto_roll(self):
        if not self.game_state.game_over:
            self.root.after(2000, self.roll_dice)

    def roll_dice(self):
        self.roll_count.set(self.roll_count.get() + 1)
        self.game_logic.roll_dice()

        # Update the roll count, player, and roll labels
        current_player = self.game_logic._get_current_player()
        opponent_player = self.game_logic._get_opponent_player()
        self.roll_count_label.config(text=f"Roll Count: {self.roll_count.get()}")
        self.roll_label.config(text=f"{current_player.name}'s Roll: {self._current_roll_display()}")
        self.status_label.config(text=f"{current_player.status} | {opponent_player.status}")

        if self.game_state.game_over:
            self.status_label.config(text=f"Game Over! {self.game_state.winner} wins!")
        else:
            self.auto_roll()  # Automatically roll again after 2 seconds

    def _current_roll_display(self):
        return self.game_logic._get_current_player().current_roll

if __name__ == "__main__":
    root = tk.Tk()
    app = DeathrollingGameApp(root)
    root.mainloop()
