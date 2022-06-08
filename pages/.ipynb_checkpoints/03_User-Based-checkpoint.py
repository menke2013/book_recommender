import streamlit as st
import pandas as pd
import numpy as np
from itertools import cycle

st.set_page_config(layout="centered")
st.markdown("<h1 style='text-align: center; color: red;font-size: 60px;'>Better Book Nights</h1>", unsafe_allow_html=True)
st.title('')

df_all_books = pd.read_csv('cleaned_books_stage_3.csv')

wishlist_choice_page_3 = ['Yes', 'No']
selected_wishlist_option_page_3 = st.sidebar.radio('Taking your wishlist into consideration?', wishlist_choice_page_3)

if selected_wishlist_option_page_3 == 'Yes':
    df_user_wishlist = pd.read_csv('wishlist_2k_svd.csv')
    list_of_user_ids_2 = list(df_user_wishlist.user_id.unique())
    list_of_user_ids_2.sort()

    user_id_selection = st.sidebar.selectbox(
            'Who are you?', (list_of_user_ids_2))
    
    number_of_suggested_books_page3 = st.sidebar.selectbox(
        'How many books should be suggested to you? Maximum is the number of books on the wishlist.', (5,10,15,20))
    
    df_user_id_wishlist = df_user_wishlist[df_user_wishlist['user_id'] == user_id_selection]

    df_wishlist_books_for_user = df_user_id_wishlist.merge(df_all_books, how='left', on='book_id')



    if len(df_wishlist_books_for_user) < number_of_suggested_books_page3:
        x_number_of_suggested_books = len(df_wishlist_books_for_user)
    else:
        x_number_of_suggested_books = number_of_suggested_books_page3
    
    df_wishlist_books_for_user_2 = df_wishlist_books_for_user.head(x_number_of_suggested_books)
    
    list_url_user_selected_2 = df_wishlist_books_for_user_2['image_url'].to_list()
    list_title_user_selected_2 = df_wishlist_books_for_user_2['title'].to_list()
    list_authors_user_selected_2 = df_wishlist_books_for_user_2['authors'].to_list()
    list_genres_user_selected_2 = df_wishlist_books_for_user_2['genres'].to_list()
    list_rating_user_selected_2 = df_wishlist_books_for_user_2['est_score'].to_list()
    
    cols_desc_selected = cycle(st.columns(1))

    for idx, book_cover in enumerate(list_url_user_selected_2):
        col1, mid, col2 = st.columns([1,20,50])
        with col1:
            st.image(book_cover, width=100)
        with col2:
            st.subheader(list_title_user_selected_2[idx])
            st.write(list_authors_user_selected_2[idx])
            st.write(list_genres_user_selected_2[idx])
            st.write(f'Estimated Rating:   {round(list_rating_user_selected_2[idx],2)}')

if selected_wishlist_option_page_3 == 'No':
    df_user_rating_pred = pd.read_csv('top2k_users_20pred_svd.csv')
    list_of_user_ids_1 = list(df_user_rating_pred.user_id.unique())
    list_of_user_ids_1.sort()

    user_id_selection = st.sidebar.selectbox(
            'Who are you?', (list_of_user_ids_1))
    
    number_of_suggested_books_page3 = st.sidebar.selectbox(
        'How many books should be suggested to you?', (5,10,15,20))
    
    df_books_for_user_id = (df_user_rating_pred[df_user_rating_pred['user_id'] ==user_id_selection]).head(number_of_suggested_books_page3)

    df_books_for_user_id_2 = df_books_for_user_id.merge(df_all_books, how='left', on='book_id')
     
    list_url_user_selected_1 = df_books_for_user_id_2['image_url'].to_list()
    list_title_user_selected_1 = df_books_for_user_id_2['title'].to_list()
    list_authors_user_selected_1 = df_books_for_user_id_2['authors'].to_list()
    list_genres_user_selected_1 = df_books_for_user_id_2['genres'].to_list()
    list_rating_user_selected_1 = df_books_for_user_id_2['est_score'].to_list()
    

    cols_desc_selected = cycle(st.columns(1))

    for idx, book_cover in enumerate(list_url_user_selected_1):
        col1, mid, col2 = st.columns([1,20,50])
        with col1:
            st.image(book_cover, width=100)
        with col2:
            st.subheader(list_title_user_selected_1[idx])
            st.write(list_authors_user_selected_1[idx])
            st.write(list_genres_user_selected_1[idx])
            st.write(f'Estimated Rating:   {round(list_rating_user_selected_1[idx],2)}')