from dataclasses import dataclass



@dataclass
class FantasyTeam:
    id: int
    name : str
    pg_player_id : int
    sf_player_id : int
    sg_player_id : int
    pf_player_id : int
    c_player_id : int
