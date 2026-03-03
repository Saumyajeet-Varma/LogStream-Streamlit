import streamlit as st
import pandas as pd
from datetime import datetime, timezone
from utils import fetch_logs, sanitize_filename, format_export_data

st.set_page_config(
    page_title="LogStream",
    page_icon=":bar_chart:",
    layout="wide",
)
st.title("Log Analyzer")

st.sidebar.header("Source")
target_url = st.sidebar.text_input("Enter the URL of the log file")
from_date = st.sidebar.date_input("Filter from Date", datetime.now())

if target_url:
    df_master = fetch_logs(target_url)
    if isinstance(df_master, pd.DataFrame) and not df_master.empty:
        keyword = st.text_input("Filter by Keyword", "")
        start_dt = from_date.combine(from_date, datetime.min.time()).replace(tzinfo=timezone.utc)
        filtered_df = df_master[df_master['Timestamp'] >= start_dt]
        if keyword:
            filtered_df = filtered_df[filtered_df['Log Message'].str.contains(keyword, case=False)]
        st.dataframe(filtered_df.sort_values("Timestamp", ascending=False), use_container_width=True)
        st.divider()
        fmt = st.selectbox("Export Format", ["CSV", "TXT", "JSON"])
        safe_url = sanitize_filename(target_url)
        filename = f"{safe_url}-{from_date.strftime('%Y%m%d')}-{datetime.now().strftime('%H%M')}"
        out_data, m_type, ext = format_export_data(filtered_df, fmt)
        st.download_button(label=f"Download {ext}", data=out_data, file_name=f"{filename}.{ext}", mime=m_type)
    elif isinstance(df_master, str):
        st.error(f"Error fetching logs: {df_master}")