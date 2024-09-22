from dataclasses import dataclass



@dataclass
class FantasyTeam:
    name : str
    pg_player_id : str
    sf_player_id : str
    sg_player_id : str
    pf_player_id : str
    c_player_id : str
    id: int = None
