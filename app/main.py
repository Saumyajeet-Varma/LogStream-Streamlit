import streamlit as st

st.set_page_config(
    page_title="LogStream",
    page_icon=":bar_chart:",
    layout="wide",
)
st.title("Log Analyzer")

st.sidebar.header("Source")
target_url = st.sidebar.text_input("Enter the URL of the log file")
from_date = st.sidebar.date_input("Filter from Date", datetime.now())