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
    client = QuixLakeClient(base_url="https://quixlake-peter-quixlake-iceberg.app-staging.quix.io")
    return (client,)


@app.cell
def _(mo):
    sql_query =  """
    SELECT ts_ms,PRINT_SPEED,FAN_SPEED 
    FROM iceberg 
    LIMIT 10
    """

    # Render the query from when deploying this notebook as a webapp
    mo.md(f"""```sql
    {sql_query}
    ```""")
    return (sql_query,)


@app.cell
def _(client, pd, sql_query):
    df = client.query(sql_query)
    df["ts_ms"] = pd.to_datetime(df["ts_ms"])
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
def _(df, plt):
    import matplotlib.dates as mdates

    plt.figure(figsize=(12, 6))

    # Overlay lines
    for col in df.columns:
        if col != "ts_ms":
            plt.plot(df["ts_ms"], df[col], label=col)

    # Format x-axis
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())   # auto spacing
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))  # format

    # Use dark style
    plt.style.use("dark_background")

    plt.xticks(rotation=45, ha="right")  # rotate for readability
    plt.title("Overlayed Time Series of Sensors")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return


if __name__ == "__main__":
    app.run()
