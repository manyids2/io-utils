"""
Read, write with sqlite3 databases and pandas DataFrames.
"""

from typing import Union, Literal, List
from pathlib import Path
import sqlite3
import pandas as pd


def save_db(
    df: pd.DataFrame,
    db_path: Union[Path, str],
    table: str,
    if_exists: Literal["fail", "replace", "append"] = "replace",
    index: bool = False,
    verbose: bool = False,
) -> None:
    """Save DataFrame to sqlite3 db as specified table.
    NOTE : default behaviour is to replace the table if it exists."""
    conn = sqlite3.connect(str(db_path))

    if len(df.columns) == 0:
        print(f"Cannot save empty df ->\n{df}")
        return

    df.to_sql(table, conn, if_exists=if_exists, index=index)
    if verbose:
        print(df)
        print(df.columns)
        print(f"Saved to => {table} => {db_path}")


def load_db(
    db_path: Union[Path, str],
    table: str,
    verbose: bool = False,
) -> pd.DataFrame:
    """Read sqlite3 db, return all rows from specified table."""
    conn = sqlite3.connect(str(db_path))
    df = pd.read_sql_query(f"SELECT * from '{table}'", conn)
    if verbose:
        print(df)
        print(df.columns)
    return df


def get_tables(
    db_path: Union[Path, str],
    verbose: bool = False,
) -> List[str]:
    """Read sqlite3 db, return table names."""
    conn = sqlite3.connect(str(db_path))
    df = pd.read_sql_query('SELECT name FROM sqlite_master WHERE type = "table"', conn)
    if verbose:
        print(df)
    return list(df.name)


def update_item(
    col: str,
    value: Union[str, int],
    primary_key: str,
    primary_key_col: str,
    db_path: Union[Path, str],
    table: str,
) -> None:
    """Update single column, given primary key."""
    conn = sqlite3.connect(str(db_path))
    conn.execute(
        f"UPDATE {table} SET {col}={value} WHERE {primary_key_col} = '{primary_key}'",
    )
    conn.commit()
    conn.close()
