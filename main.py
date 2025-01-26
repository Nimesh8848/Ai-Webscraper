import streamlit as st
from scrape import scrape_website 

st.title('AI WebScraper')
url = st.text_input('Enter Website URL')

if st.button('Scrape'):
    st.write('Scraping...')
    result=scrape_website(url)
    print (result)