"""Get XBR data."""

# import src.s0_helpers.richtools as rt
import duckdb as ddb
from config import settings
from typing import Final
from rich import print as rprint

from src._registry.acc import main as acc
from src._registry.tdic import main as get_tdict

from src.s0_helpers.qries.qry_constraints import QryConstraints

duckdb_path = settings.paths.duckdb


def set_constraints(conn: ddb.DuckDBPyConnection, table_nm:str)->None:
    qry_constr = QryConstraints(conn, table_nm=table_nm)
    keys = {
        "qryR_invoices": ['ndx'],
        'qryR_costs_optix': ['parent_item_no', 'cost_type', 'cal_month_id'],
        'qryR_clusters': ['clust', 'cie']
        
    }
    qry_constr.add_primary_key(keys[table_nm])


def main() -> None:
    TDIC_NM:Final[str] = 'main'
    DB_NM: Final[str] = "db"
    acc_conn, _ = acc(db_choice=DB_NM)
    tdict = get_tdict(TDIC_NM)
    
    # print(tdict)
    for line in tdict.lines:
        if line.activ:
            # print(line)
            qry = f"SELECT * FROM {line.table_nm};"
            data = acc_conn.read(qry)
            if data.empty:
                msg = f"Data from table '{line.table_nm}' is empty."
                raise AssertionError(msg)
        with ddb.connect(duckdb_path) as conn:
            qry = f"""
            CREATE OR REPLACE TABLE {line.name} AS
            SELECT * FROM data
            """
            conn.sql(qry)
            rprint(f"Table '{line.name}' created or replaced.")
            set_constraints(conn, table_nm=line.name)
