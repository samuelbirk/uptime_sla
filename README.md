# uptime_sla

This StencilJS project displays an uptime SLA heatmap based on data from Snowflake. It uses browser-based authentication and provides a search box to filter results.

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```
2. Start the dev server:
   ```bash
   npm start
   ```

## Snowflake Integration

The project contains a placeholder data file (`src/assets/data.json`). Replace the logic in `fetchSlaData` with a call to your Snowflake instance using browser OAuth. The Snowflake query should return service names and uptime percentages.

You may use `snowflake-sdk` with OAuth credentials or expose an API that the frontend fetches from.

## Searchable SLA

Use the search box at the top of the page to filter services by name. The heatmap colors change from green (high uptime) to red (low uptime).

## Query Example

Replace the query in `fetchSlaData` with your actual Snowflake SQL. Example placeholder:
```sql
SELECT service_name AS name, uptime_percentage AS uptime
FROM my_schema.service_uptime_daily
WHERE date >= CURRENT_DATE - 30
```
