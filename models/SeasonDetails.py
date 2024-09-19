from dataclasses import dataclass



@dataclass
class SeasonDetails:
    player_id: int
    team: str
    position: str
    games: int
    points: int
    two_percent: float
    three_percent: float

