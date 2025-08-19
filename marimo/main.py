import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import marimo as mo
    import matplotlib.pyplot as plt
    import uuid
    return mo, pd, plt


@app.cell
def _(mo):
    mo.md(
        r"""
    # 01 - Query Data
    Example showing how to query data from QuixLake into a pandas DataFrame.
    """
    )
    return


@app.cell
def _():
    from quixlake import QuixLakeClient
    client = QuixLakeClient(base_url="https://quixlake-peter-quixlake-webinar.app-staging.quix.io")
    return (client,)


@app.cell
def _(mo):
    sql_query =  """
    SELECT
        DATE_TRUNC('minute', ts_ms) AS time_bucket,
        machine, 
        mean(BED_TEMPERATURE), 
        min(BED_TEMPERATURE),
        max(BED_TEMPERATURE),
    FROM sensortable
    WHERE machine = '3D_PRINTER_1'
    GROUP BY time_bucket, machine
    ORDER BY time_bucket
    """

    # Render the query from when deploying this notebook as a webapp
    mo.md(f"""```sql
    {sql_query}
    ```""")
    return (sql_query,)


@app.cell
def _(client, sql_query):
    df = client.query(sql_query)

    df
    return (df,)


@app.cell
def _(mo):
    mo.md(
        r"""
    # 02 - Visualise Data
    Example showing how to visualise the queried data.
    """
    )
    return


@app.cell
def _(df, pd, plt):
    import matplotlib.dates as mdates

    # --- Prepare timestamp column ---
    # Handles epoch ms (int/float) or string timestamps; leaves datetime as-is.
    _ts = df["time_bucket"]
    if pd.api.types.is_integer_dtype(_ts) or pd.api.types.is_float_dtype(_ts):
        ts = pd.to_datetime(_ts, unit="ms", utc=True).tz_convert("Europe/Prague")
    else:
        ts = pd.to_datetime(_ts)  # pandas will infer tz/naive

    # --- Plot (dark theme first!) ---
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot only numeric columns (skip the timestamp and any helper cols)
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    cols_to_plot = [c for c in numeric_cols if c not in {"time_bucket"}]

    for col in cols_to_plot:
        ax.plot(ts, df[col], label=col)

    # --- Time axis formatting ---
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))
    for label in ax.get_xticklabels():
        label.set_rotation(45)
        label.set_horizontalalignment("right")

    ax.set_title("Overlayed Time Series of Sensors")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    # For marimo Present mode: return the figure as the last expression
    fig
    return


if __name__ == "__main__":
    app.run()
