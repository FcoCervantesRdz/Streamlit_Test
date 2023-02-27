import os
import streamlit as st
from PIL import Image
st.markdown("""
    # Manga Downloader with Web Scrapping!
    There are free options to read manga online, but in some of them, we aren't able to download a PDF version of it to read it later. This is the case of manganelo.tv (https://ww5.manganelo.tv/), where we can just read manga in the page from images loading in the web page.

    These are links examples for diferent mangas:
    * "*Beyond The Sky*": https://ww5.manganelo.tv/manga/manga-ne990439.
    * "*My Wife Is A Fox Spirit*": https://ww5.manganelo.tv/manga/manga-hr984452.
    * "*Fight Class 3*": https://ww5.manganelo.tv/manga/manga-cd980038.

    In this URL structure, we are able to notice that "*ne990439*", "*hr984452*" & "*cd980038*" represents the manga's unique codes.

    Inside every manga's page, we have acces to the list of chapters and their information, as we can see in the next screeshot from the "Beyond The Sky"'s page:
""")
st.image(Image.open('./../manga_ss.PNG'), caption='Manga SS')