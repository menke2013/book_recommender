import streamlit as st
import pandas as pd
import numpy as np
from itertools import cycle

st.set_page_config(layout="centered")
st.markdown("<h1 style='text-align: center; color: red;font-size: 60px;'>Better Book Nights</h1>", unsafe_allow_html=True)

selected_option_page4 = st.sidebar.radio('Select:', ['Algorithm based on description', 'Algorithm based on author'])

selected_option_2_page4 = st.sidebar.radio('Search in:', ['Title', 'Author'])


if selected_option_page4 == 'Algorithm based on description':
        
    df_all_books = pd.read_csv('cleaned_books_stage_3.csv')
    df_desc = pd.read_csv('google_desc_tfidf.csv')
        
    if selected_option_2_page4 == 'Title':
        user_selected_book = st.sidebar.text_input('Keyword or book title:').lower()
        
        if "selected_book" not in st.session_state:
            st.session_state.selected_book = False
        if len(user_selected_book) < 1:
            st.session_state.selected_book = False
        if len(user_selected_book) > 0:
            df_user_selection_books = df_all_books[df_all_books['title'].str.lower().str.contains(user_selected_book)][['title', 'authors','genres']]
            hide_table_row_index = """
                        <style>
                        tbody th {display:none}
                        .blank {display:none}
                        </style>
                        """
            placeholder = st.empty()
            with placeholder.container():

                if len(df_user_selection_books) < 1:
                    st.header("We couldn't find anything related. Try again.")
                if len(df_user_selection_books) > 0:
                    st.subheader('Book(s) found in our database. Select the preferred one in the menu on the left.')
                    st.markdown(hide_table_row_index, unsafe_allow_html=True)
                    st.table(df_user_selection_books)

            if len(df_user_selection_books) > 0:        
                list_selection_table_books = df_user_selection_books['title'].to_list()

                user_selected_book_exact = st.sidebar.selectbox(
                    'Which book precisely?', (list_selection_table_books))
                df_help_page4 = df_all_books[df_all_books['title']==user_selected_book_exact]
                selected_book_id = df_help_page4['book_id'].iloc[0]

                number_of_suggested_books_page4 = st.sidebar.selectbox(
                'How many books should be suggested to you?', (5,10,15,20))

                start_button = st.sidebar.button('Start')

                if start_button:
                    st.session_state.selected_book = True
                    placeholder.empty()

                    df_select_2 = (df_desc[df_desc['book_id_ref'] ==selected_book_id]).head(number_of_suggested_books_page4)
                    list_books_desc_1 = list(df_select_2['book_id'])
                    df_getting_books_desc = df_all_books[df_all_books['book_id'].isin(list_books_desc_1)]

                    list_url_desc_selected = df_getting_books_desc['image_url'].to_list()
                    list_title_desc_selected = df_getting_books_desc['title'].to_list()
                    list_authors_desc_selected = df_getting_books_desc['authors'].to_list()
                    list_genres_desc_selected = df_getting_books_desc['genres'].to_list()

                    cols_desc_selected = cycle(st.columns(1))
                    #placeholder.empty()
                    for idx, book_cover in enumerate(list_url_desc_selected):
                        col1, mid, col2 = st.columns([1,20,50])
                        with col1:
                            st.image(book_cover, width=100)
                        with col2:
                            st.subheader(list_title_desc_selected[idx])
                            st.write(list_authors_desc_selected[idx])
                            st.write(list_genres_desc_selected[idx])

    
    if selected_option_2_page4 == 'Author':
        user_selected_book = st.sidebar.text_input('Name of author:').lower()
        
        if "selected_book" not in st.session_state:
            st.session_state.selected_book = False
        if len(user_selected_book) < 1:
            st.session_state.selected_book = False
        if len(user_selected_book) > 0:
            df_user_selection_books = df_all_books[df_all_books['authors'].str.lower().str.contains(user_selected_book)][['title', 'authors','genres']]
            hide_table_row_index = """
                        <style>
                        tbody th {display:none}
                        .blank {display:none}
                        </style>
                        """
            placeholder = st.empty()
            with placeholder.container():

                if len(df_user_selection_books) < 1:
                    st.header("We couldn't find anything related. Try again.")
                if len(df_user_selection_books) > 0:
                    st.subheader('Book(s) found in our database. Select the preferred one in the menu on the left.')
                    st.markdown(hide_table_row_index, unsafe_allow_html=True)
                    st.table(df_user_selection_books)

            if len(df_user_selection_books) > 0:        
                list_selection_table_books = df_user_selection_books['title'].to_list()

                user_selected_book_exact = st.sidebar.selectbox(
                    'Which book precisely?', (list_selection_table_books))
                df_help_page4 = df_all_books[df_all_books['title']==user_selected_book_exact]
                selected_book_id = df_help_page4['book_id'].iloc[0]

                number_of_suggested_books_page4 = st.sidebar.selectbox(
                'How many books should be suggested to you?', (5,10,15,20))

                start_button = st.sidebar.button('Start')

                if start_button:
                    st.session_state.selected_book = True
                    placeholder.empty()

                    df_select_2 = (df_desc[df_desc['book_id_ref'] ==selected_book_id]).head(number_of_suggested_books_page4)
                    list_books_desc_1 = list(df_select_2['book_id'])
                    df_getting_books_desc = df_all_books[df_all_books['book_id'].isin(list_books_desc_1)]

                    list_url_desc_selected = df_getting_books_desc['image_url'].to_list()
                    list_title_desc_selected = df_getting_books_desc['title'].to_list()
                    list_authors_desc_selected = df_getting_books_desc['authors'].to_list()
                    list_genres_desc_selected = df_getting_books_desc['genres'].to_list()

                    cols_desc_selected = cycle(st.columns(1))
                    #placeholder.empty()
                    for idx, book_cover in enumerate(list_url_desc_selected):
                        col1, mid, col2 = st.columns([1,20,50])
                        with col1:
                            st.image(book_cover, width=100)
                        with col2:
                            st.subheader(list_title_desc_selected[idx])
                            st.write(list_authors_desc_selected[idx])
                            st.write(list_genres_desc_selected[idx])        
    
if selected_option_page4 == 'Algorithm based on author':
    df_all_books = pd.read_csv('cleaned_books_stage_3.csv')
    df_author_simal = pd.read_csv('df_authors_simal.csv')

    if selected_option_2_page4 == 'Title':
        user_selected_book = st.sidebar.text_input('Keyword or book title:').lower()

        if "selected_book" not in st.session_state:
            st.session_state.selected_book = False
        if len(user_selected_book) < 1:
            st.session_state.selected_book = False
        if len(user_selected_book) > 0:
            df_user_selection_books = df_all_books[df_all_books['title'].str.lower().str.contains(user_selected_book)][['title', 'authors','genres']]
            hide_table_row_index = """
                        <style>
                        tbody th {display:none}
                        .blank {display:none}
                        </style>
                        """         
            placeholder = st.empty()
            with placeholder.container():
                if len(df_user_selection_books) < 1:
                    st.header("We couldn't find anything related. Try again.")
                if len(df_user_selection_books) > 0:
                    st.subheader('Book(s) found in our database. Select the preferred one in the menu on the left.')
                    st.markdown(hide_table_row_index, unsafe_allow_html=True)
                    st.table(df_user_selection_books)

            if len(df_user_selection_books) > 0:   
                list_selection_table_books = df_user_selection_books['title'].to_list()

                user_selected_book_exact = st.sidebar.selectbox(
                    'Which book precisely?', (list_selection_table_books))
                if len(user_selected_book_exact) > 0:
                        selected_book = True
                df_help_page4 = df_all_books[df_all_books['title']==user_selected_book_exact]
                selected_book_id = df_help_page4['book_id'].iloc[0]

                number_of_suggested_books_page4_2 = st.sidebar.selectbox(
                'How many books should be suggested to you?', (5,10,15,20))

                start_button = st.sidebar.button('Start')

                if start_button:
                    st.session_state.selected_book = True
                    placeholder.empty()

                    df_select_2_2 = (df_author_simal[df_author_simal['book_id_ref'] ==selected_book_id]).head(number_of_suggested_books_page4_2)
                    list_books_auth_1 = list(df_select_2_2['book_id'])
                    df_getting_books_auth = df_all_books[df_all_books['book_id'].isin(list_books_auth_1)]

                    list_url_auth_selected = df_getting_books_auth['image_url'].to_list()
                    list_title_auth_selected = df_getting_books_auth['title'].to_list()
                    list_authors_auth_selected = df_getting_books_auth['authors'].to_list()
                    list_genres_auth_selected = df_getting_books_auth['genres'].to_list()

                    cols_desc_selected = cycle(st.columns(1))

                    for idx, book_cover in enumerate(list_url_auth_selected):
                        col1, mid, col2 = st.columns([1,20,50])
                        with col1:
                            st.image(book_cover, width=100)
                        with col2:
                            st.subheader(list_title_auth_selected[idx])
                            st.write(list_authors_auth_selected[idx])
                            st.write(list_genres_auth_selected[idx])
         
    if selected_option_2_page4 == 'Author':
        user_selected_book = st.sidebar.text_input('Name of author:').lower()

        if "selected_book" not in st.session_state:
            st.session_state.selected_book = False
        if len(user_selected_book) < 1:
            st.session_state.selected_book = False
        if len(user_selected_book) > 0:
            df_user_selection_books = df_all_books[df_all_books['authors'].str.lower().str.contains(user_selected_book)][['title', 'authors','genres']]
            hide_table_row_index = """
                        <style>
                        tbody th {display:none}
                        .blank {display:none}
                        </style>
                        """         
            placeholder = st.empty()
            with placeholder.container():
                if len(df_user_selection_books) < 1:
                    st.header("We couldn't find anything related. Try again.")
                if len(df_user_selection_books) > 0:
                    st.subheader('Book(s) found in our database. Select the preferred one in the menu on the left.')
                    st.markdown(hide_table_row_index, unsafe_allow_html=True)
                    st.table(df_user_selection_books)

            if len(df_user_selection_books) > 0:   
                list_selection_table_books = df_user_selection_books['title'].to_list()

                user_selected_book_exact = st.sidebar.selectbox(
                    'Which book precisely?', (list_selection_table_books))
                if len(user_selected_book_exact) > 0:
                        selected_book = True
                df_help_page4 = df_all_books[df_all_books['title']==user_selected_book_exact]
                selected_book_id = df_help_page4['book_id'].iloc[0]

                number_of_suggested_books_page4_2 = st.sidebar.selectbox(
                'How many books should be suggested to you?', (5,10,15,20))

                start_button = st.sidebar.button('Start')

                if start_button:
                    st.session_state.selected_book = True
                    placeholder.empty()

                    df_select_2_2 = (df_author_simal[df_author_simal['book_id_ref'] ==selected_book_id]).head(number_of_suggested_books_page4_2)
                    list_books_auth_1 = list(df_select_2_2['book_id'])
                    df_getting_books_auth = df_all_books[df_all_books['book_id'].isin(list_books_auth_1)]

                    list_url_auth_selected = df_getting_books_auth['image_url'].to_list()
                    list_title_auth_selected = df_getting_books_auth['title'].to_list()
                    list_authors_auth_selected = df_getting_books_auth['authors'].to_list()
                    list_genres_auth_selected = df_getting_books_auth['genres'].to_list()

                    cols_desc_selected = cycle(st.columns(1))

                    for idx, book_cover in enumerate(list_url_auth_selected):
                        col1, mid, col2 = st.columns([1,20,50])
                        with col1:
                            st.image(book_cover, width=100)
                        with col2:
                            st.subheader(list_title_auth_selected[idx])
                            st.write(list_authors_auth_selected[idx])
                            st.write(list_genres_auth_selected[idx])

        