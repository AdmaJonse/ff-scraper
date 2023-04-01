"""
Common utility functions.
"""

def normalize_name(name : str) -> str:
    """
    Normalize player names by removing punctuation and suffixes.
    """
    replace_strings = ["Sr.", "Jr.", "III", "IV", "II", ".", ","]
    name = name.strip()
    for rep in replace_strings:
        name = name.replace(rep, "")
    return name.strip()

def normalize_owner(name : str) -> str:
    """
    Standardize the owner name.
    """
    pairs = {
        "Simon Thomas": "STDK",
        "Jared Duffy": "JDBK"
    }
    if name in pairs:
        return pairs.get(name, "")
    return name.split(" ")[0].capitalize()
