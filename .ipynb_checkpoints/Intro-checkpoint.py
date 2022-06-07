## importing libraries
import streamlit as st
import pandas as pd
import numpy as np
from itertools import cycle



## creating some dataframes and variables

#st.markdown('''
#<img src="https://github.com/menke2013/recommender_film/blob/45af26e59da2fb69ea57fdf4edd2227a6d63ce5a/felix-mooneeram-evlkOfkQ5rE-unsplash.png"   
#    style="width: 100vw;
#    position: center;
#    margin: 0;
#    padding: 0;
#    top: -6rem;
#    filter: brightness(0.2);
#    left: -37.5rem;"><img>
#    ''', unsafe_allow_html=True)
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: red;font-size: 60px;'>Better Book Nights</h1>", unsafe_allow_html=True)
st.title('')
#st.sidebar.markdown("# Main page 🎈")


df_all_books = pd.read_csv('cleaned_books_stage_2.csv') 
df_random_display = df_all_books.sample(32)
list_url = df_random_display['image_url'].to_list()
cols = cycle(st.columns(8))
        
for idx, book_cover in enumerate(list_url):
    next(cols).image(book_cover, width=100)#, caption=list_captions[idx])