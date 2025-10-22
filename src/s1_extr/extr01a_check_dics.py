"""Verify the table and data dictionaries."""
from rich import print as rprint
# from typing import Final

from src._registry.tdic import main as tdic


def main() -> int:
    """This serves as a test to validate if the dics instantiate properly."""
    for name in ("main",):
        a_tdic = tdic(name)
        n = len(a_tdic.lines)
        msg = f"The '{name}' tdic instantiated with {n} lines."
        rprint(msg)
    # for name in ("xbr", "main"):
    #     a_ddic = ddic(name)
    #     n = len(a_ddic.lines)
    #     msg = f"The '{name}' ddic instantiated with {n} lines."
    #     rprint_msg(msg)
    return 1
