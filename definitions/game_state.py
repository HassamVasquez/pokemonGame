from enum import Enum

class GameState(Enum):
    LISTING = 1,
    FILTERING = 2,
    SINGLE_BATTLE = 3,
    TEAM_BATTLE = 4
