import pytest
import repository.player_repository as p
import repository.season_details_repository as s
import repository.fantasy_team_repository as f
from models.FantasyTeam import FantasyTeam
from models.Player import Player
from models.SeasonDetails import SeasonDetails
from service.seed import seed
from repository.database import create_all_tables, get_db_connection


@pytest.fixture(scope="module")
def setup_database():
    create_all_tables()
    seed()
    yield
    # tear down - happens after test finished
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DROP TABLE nba_teams")
    conn.commit()
    cur.close()
    conn.close()


def test_create_all_tables(setup_database):
    check = create_all_tables()
    assert check

def test_seed(setup_database):
    check = seed()
    assert check

def test_create_player_to_db(setup_database):
    check = p.create_player_to_db(Player(id='murkead01', name='ariel'))
    assert check

def test_get_all_players(setup_database):
    check = p.get_all_players()
    assert check

def test_get_player_by_id_db(setup_database):
    check = p.get_player_by_id_db('murkead01')
    assert check

def test_get_player_name_by_player_id(setup_database):
    check = p.get_player_name_by_player_id('murkead01')
    assert check

def test_get_all_season_details(setup_database):
    check = s.get_all_season_details(2024)
    assert check

def test_get_season_details_by_player_id(setup_database):
    check = s.get_season_details_by_player_id('murkead01', 2024)
    assert check

def test_create_season_details_db(setup_database):
    check = s.create_season_details_db(SeasonDetails(player_id='murkead09', team='chi', position='sf', games=25, points=250,
                                                     two_percent=45, three_percent=30, atr=4.23), 2024)
    assert check

def test_add_ppg_ratio_to_player(setup_database):
    check = s.add_ppg_ratio_to_player(SeasonDetails(player_id='murkead09', team='chi', position='sf', games=25, points=250,
                                                    two_percent=45, three_percent=30, atr=4.23), 15.125, 2024)
    assert check

def test_get_all_fantasy_teams_db(setup_database):
    check = f.get_all_fantasy_teams_db()
    assert check

def test_get_fantasy_teams_by_id_db(setup_database):
    check = f.get_fantasy_teams_by_id_db(3)
    assert check


def test_create_fantasy_team_to_db(setup_database):
    check = f.create_fantasy_team_to_db(FantasyTeam(name='ariel', c_player_id="greenaj01", sf_player_id='lawsoaj01',
                                           sg_player_id='griffaj01', pf_player_id='gordoaa01', pg_player_id='holidaa01'))
    assert check

def test_update_fantasy_team_dc(setup_database):
    check = f.update_fantasy_team_dc(FantasyTeam(name='ariel', c_player_id="greenaj01", sf_player_id='lawsoaj01',
                                           sg_player_id='griffaj01', pf_player_id='gordoaa01', pg_player_id='holidaa01'))
    assert check

def test_delete_fantasy_team_db(setup_database):
    check = f.delete_fantasy_team_db('ariel')
    assert check

