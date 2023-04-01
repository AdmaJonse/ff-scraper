"""
Mainline execution of the scraping application.

Offer the user possible scraping options and perform one according to their selection.
"""

from src import output
from src import scrape

print("Options:")
print("  1. Player List")
print("  2. Draft Picks")

try:

    option : int = int(input("Select option: "))
    year   : int = int(input("Enter year: "))

    if option == 1:
        players = scrape.get_all_players(year)
        output.print_players(players)
        output.write_csv(players, "players.csv")
    elif option == 2:
        picks = scrape.get_draft_picks(year)
        output.print_draft(picks)
        output.write_csv(picks, "picks.csv")
    else:
        print("invalid option.")

except ValueError:
    print("invalid option.")
