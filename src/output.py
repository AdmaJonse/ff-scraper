"""
Generate a .csv file from the given data.
"""

import csv
from typing import Dict, List

OUTPUT_FILENAME = "output.csv"

def write_csv(data : List[Dict[str,str]], filename : str = OUTPUT_FILENAME) -> None:
    """
    Write the given list of dictionaries to a .csv file.
    """
    keys = data[0].keys()

    with open(filename, 'w', newline='', encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, keys)
        writer.writeheader()
        writer.writerows(data)


def print_players(data : List[Dict[str,str]]) -> None:
    """
    Print the given list of dictionaries as a table.
    """
    format_string : str = "{:<25} {:<15} {:<5} {:<5}"
    print(format_string.format("Player", "Owner", "Team", "Pos"))
    for item in data:
        name     : str = item.get("player", "")
        owner    : str = item.get("owner", "")
        team     : str = item.get("team", "")
        position : str = item.get("position", "")
        print(format_string.format(name, owner, team, position))


def print_draft(data : List[Dict[str,str]]) -> None:
    """
    Print the given list of dictionaries as a table.
    """
    format_string : str = "{:<25} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<15}"
    print(format_string.format("Player", "Team", "Pos", "Year", "Round", "Pick", "Keep", "Owner"))
    for item in data:
        name     : str = item.get("player", "")
        team     : str = item.get("team", "")
        position : str = item.get("position", "")
        year     : str = str(item.get("year", 0))
        rnd      : str = str(item.get("round", 0))
        pick     : str = str(item.get("pick", 0))
        keeper   : str = item.get("keeper", "N")
        owner    : str = item.get("owner", "")
        print(format_string.format(name, team, position, year, rnd, pick, keeper, owner))
