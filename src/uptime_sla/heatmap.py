"""Functions for generating heatmaps from Snowflake data."""
from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def generate_heatmap(df: pd.DataFrame, output: str = "heatmap.png") -> None:
    """Generate and save a heatmap image from a DataFrame.

    The DataFrame is expected to have columns ``day`` and ``hour`` representing the
    time period of the SLA metric and a column ``uptime`` representing the
    percentage uptime.
    """
    pivot = df.pivot("day", "hour", "uptime")
    plt.figure(figsize=(12, 7))
    sns.heatmap(pivot, annot=True, fmt=".1f", cmap="YlGnBu")
    plt.title("Uptime SLA Heatmap")
    plt.tight_layout()
    plt.savefig(output)
    print(f"Heatmap saved to {output}")
