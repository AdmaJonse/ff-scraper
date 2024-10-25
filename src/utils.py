"""
Common utility functions.
"""

from typing import List

def normalize_name(name : str) -> str:
    """
    Normalize player names by removing punctuation and suffixes.
    """
    replace_strings = ["Sr.", "Jr.", "III", "IV", "II", ".", ","]
    name = name.strip()
    for rep in replace_strings:
        name = name.replace(rep, "")
    return name.strip()

def normalize_owner(names : List[dict]) -> str:
    """
    Standardize the owner name.
    """
    pairs = {
        "Simon":   "STDK",
        "Jared":   "JDBK",
        "Brendan": "JDBK"
    }
    name : str = names[0].get("firstName","")
    if name in pairs:
        return pairs.get(name, "")
    return name
