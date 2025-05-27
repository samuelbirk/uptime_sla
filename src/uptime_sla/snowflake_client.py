"""Simple Snowflake client using browser authentication."""
from __future__ import annotations

import os
from typing import List, Tuple

import pandas as pd
import snowflake.connector


class SnowflakeClient:
    """Utility for connecting to Snowflake and executing queries."""

    def __init__(self, account: str, user: str, role: str, warehouse: str, database: str, schema: str) -> None:
        self.account = account
        self.user = user
        self.role = role
        self.warehouse = warehouse
        self.database = database
        self.schema = schema

    def _connect(self):
        """Create a Snowflake connection using external browser authentication."""
        return snowflake.connector.connect(
            account=self.account,
            user=self.user,
            role=self.role,
            warehouse=self.warehouse,
            database=self.database,
            schema=self.schema,
            authenticator="externalbrowser",
        )

    def fetch_dataframe(self, query: str, params: List | Tuple | None = None) -> pd.DataFrame:
        """Execute a query and return the results as a DataFrame."""
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params or [])
                df = cur.fetch_pandas_all()
        return df
