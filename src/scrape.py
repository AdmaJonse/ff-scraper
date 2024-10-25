"""
TODO
"""

from typing import List
from espn_api.football import League

from src import utils

league_id : int = 95612
teams     : int = 12

def get_league(year : int) -> League:
    """
    Return the league for the given year.
    """
    return League(league_id, year)


def get_all_players(year : int) -> List:
    """
    Scrape the list of rostered players from the given year.
    """
    league      = get_league(year)
    all_players = []

    for team_id in range(1, teams+1):
        team = league.get_team_data(team_id)
        for player in team.roster:
            item = {
                "player": utils.normalize_name(player.name),
                "owner": utils.normalize_owner(team.owners),
                "team": player.proTeam,
                "position": player.position
            }
            all_players.append(item)
    return all_players


def get_draft_picks(year : int) -> List:
    """
    Scrape draft picks from the given year.
    """
    league = get_league(year)
    picks  = []

    for pick in league.draft:
        player = league.player_info(playerId=pick.playerId)
        item = {
            "player": utils.normalize_name(pick.playerName),
            "team": "-" if player.proTeam is None else player.proTeam,
            "position": player.position,
            "year": "-" if bool(pick.keeper_status) else year,
            "round": pick.round_num,
            "pick": (pick.round_num - 1) * 12 + pick.round_pick,
            "keeper": "Y" if bool(pick.keeper_status) else "N",
            "owner": utils.normalize_owner(pick.team.owners)
        }
        picks.append(item)

    return picks
