from pydantic import BaseModel, Field
from typing import Optional, List

class Player(BaseModel):
    name: str
    current_roll: int = Field(..., gt=0, description="The current roll value, must be greater than 0.")
    is_turn: bool = Field(False, description="Indicates if it's the player's turn.")
    status: Optional[str] = Field(None, description="The current status of the player.")

class GameState(BaseModel):
    player1: Player
    player2: Player
    game_over: bool = Field(False, description="Flag indicating if the game is over.")
    winner: Optional[str] = Field(None, description="Name of the winning player.")

# Troll Dice Player Model
class td_Player(BaseModel):
    name: str
    score: int = 0

# Troll Dice Roll Result Model
class td_RollResult(BaseModel):
    player: str
    dice_roll: int

# Troll Dice Game State Model
class td_GameState(BaseModel):
    players: List[td_Player]
    current_turn: int = 0
    last_roll: td_RollResult = None