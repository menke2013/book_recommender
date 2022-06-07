## importing libraries
import streamlit as st
import pandas as pd
import numpy as np
from itertools import cycle





st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: red;font-size: 60px;'>Better Book Nights</h1>", unsafe_allow_html=True)
st.title('')



df_all_books = pd.read_csv('cleaned_books_stage_3.csv') 
df_random_display = df_all_books.sample(32)
list_url = df_random_display['image_url'].to_list()
cols = cycle(st.columns(8))
        
for idx, book_cover in enumerate(list_url):
    next(cols).image(book_cover, width=100)