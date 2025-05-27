"""Command-line interface for generating an uptime SLA heatmap."""
from __future__ import annotations

import argparse
import os

from uptime_sla import SnowflakeClient, generate_heatmap

QUERY = (
    "SELECT day, hour, uptime FROM sla.uptime_stats ORDER BY day, hour"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--account", required=True, help="Snowflake account identifier"
    )
    parser.add_argument("--user", required=True, help="Snowflake user name")
    parser.add_argument("--role", required=True, help="Role to use")
    parser.add_argument(
        "--warehouse", required=True, help="Warehouse to run the query"
    )
    parser.add_argument(
        "--database", required=True, help="Database containing the data"
    )
    parser.add_argument("--schema", required=True, help="Schema containing the data")
    parser.add_argument(
        "--output",
        default="heatmap.png",
        help="File name for the generated heatmap",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    client = SnowflakeClient(
        account=args.account,
        user=args.user,
        role=args.role,
        warehouse=args.warehouse,
        database=args.database,
        schema=args.schema,
    )

    df = client.fetch_dataframe(QUERY)
    generate_heatmap(df, args.output)


if __name__ == "__main__":
    main()
