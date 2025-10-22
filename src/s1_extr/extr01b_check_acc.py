"""Verifys XBR data from MS Access"""

from rich import print as rprint
from src._registry.acc import main as inst_acc


def main() -> int:
    accdb = inst_acc(db_choice="db")
    conn = accdb[0]
    check = conn.test_connect()
    if check:
        msg: str = f"MS Access connect is ok.\n{accdb[1]}"
        rprint(msg)
    return 0


if __name__ == "__main__":
    main()
