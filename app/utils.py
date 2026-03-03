import requests
import re
import pandas as pd
from datetime import timezone
from dateutil.parser import parse

def fetch_logs(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        lines = response.text.splitlines()
        data = []
        for line in lines:
            try:
                dt = parse(line[:35], fuzzy=True)
                if dt.tzinfo is None:
                    dt.replace(tzinfo=timezone.utc)
                data.append({"Timestamp": dt, "Log Message": line})
            except(ValueError, OverflowError):
                continue
        return pd.DataFrame(data)
    except Exception as e:
        return str(e)

def sanitize_filename(url):
    clean = re.sub(r'https?://', '', url)
    return re.sub(r'[^a-zA-Z0-9]', '_', clean).strip('_')

def format_export_data(df, fmt):
    if fmt == 'csv':
        content = df.to_csv(index=False).encode('utf-8')
        MIME_type = "text/csv"
        extension = "csv"
    elif fmt == 'json':
        content = df.to_json(orient='records', indent=4).encode('utf-8')
        MIME_type = "application/json"
        extension = "json"
    elif fmt == 'txt':
        content = "\n".join(df['Log Message'].tolist()).encode('utf-8')
        MIME_type = "text/plain"
        extension = "txt"
    else:
        content, MIME_type, extension = None, None, None
    return content, MIME_type, extension