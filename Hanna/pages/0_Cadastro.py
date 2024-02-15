import streamlit as st
import pandas as pd
import numpy as np

def conn_mysql():
    conn = st.connection('mysql', type='sql')
