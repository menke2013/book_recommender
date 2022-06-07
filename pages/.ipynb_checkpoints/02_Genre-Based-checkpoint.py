import streamlit as st
import pandas as pd
import numpy as np
from itertools import cycle

st.set_page_config(layout="centered")
st.markdown("<h1 style='text-align: center; color: red;font-size: 60px;'>Better Book Nights</h1>", unsafe_allow_html=True)

df_best_books = pd.read_csv('best_books_genres.csv')

genre_choice = st.sidebar.selectbox(
 'Which genre are you interested in?',
 ("Art", "Biography", "Business", "Chick-Lit", "Children", "Christian", "Classics",
          "Comics", "Contemporary", "Cookbooks", "Crime", "Ebooks", "Erotica", "Fantasy", "Fiction",
          "Gay and Lesbian", "Graphic Novels", "Historical Fiction", "History", "Horror",
          "Humor", "Manga", "Memoir", "Music", "Mystery", "Nonfiction", "Paranormal",
          "Philosophy", "Poetry", "Psychology", "Religion", "Romance", "Science", "Science Fiction", 
          "Self Help", "Suspense", "Spirituality", "Sports", "Steampunk","Thriller", "Travel", "Young-Adult"))
genre_choice2 = []
genre_choice_3 = genre_choice
genre_choice = genre_choice.lower()
genre_choice2.append(genre_choice)

number_of_top_books = st.sidebar.selectbox(
'How many books should be suggested to you?', (5,10,15,20))

df_genre_selected = ((df_best_books[df_best_books['genres'].str.contains(genre_choice)]).sort_values(by='average_rating', ascending=False).head(number_of_top_books))

col1, center_writing, col2 = st.columns([1,5,1])
with center_writing:
#    genre_choice_3 = genre_choice.upper()
    st.subheader(f'The {number_of_top_books} best books in the {genre_choice_3} category')

list_url_genre_selected = df_genre_selected['image_url'].to_list()
list_title_genre_selected = df_genre_selected['title'].to_list()
list_authors_genre_selected = df_genre_selected['authors'].to_list()
list_rating_genre_selected = df_genre_selected['average_rating'].to_list()

cols_genre_selected = cycle(st.columns(1))

for idx, book_cover in enumerate(list_url_genre_selected):
    col1, mid, col2 = st.columns([1,20,50])
    with col1:
        st.image(book_cover, width=100)
    with col2:
        st.write(list_title_genre_selected[idx])
        st.write(list_authors_genre_selected[idx])
        st.write(list_rating_genre_selected[idx])

