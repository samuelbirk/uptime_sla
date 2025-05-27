# uptime_sla

This stencil repository fetches uptime SLA statistics from Snowflake and renders
an uptime heatmap. It uses Snowflake's browser-based authentication so it can be
run locally without storing credentials.

## Requirements

- Python 3.9+
- Snowflake user with access to the target tables
- The packages listed in `requirements.txt`

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Running

Invoke the command line script and provide your Snowflake connection
information. A browser window will open for authentication.

```bash
python src/main.py \
  --account <account> \
  --user <user> \
  --role <role> \
  --warehouse <warehouse> \
  --database <database> \
  --schema <schema> \
  --output heatmap.png
```

The script will execute the query defined in `src/main.py` and generate a heatmap
image using the returned data.
