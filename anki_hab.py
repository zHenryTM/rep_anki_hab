import time
import plotly.express as px
import streamlit as st
import numpy as np
import requests
from io import BytesIO
import streamlit.components.v1 as components
from PIL import Image
import string
import os
import matplotlib.pyplot as plt
import zipfile
from barcode.writer import ImageWriter


# Minhas imports
from business.Functions.generate_link_to_youtube import generate_link_to_youtube
from business.Functions.remove_invalid_characters import remove_invalid_characters
from business.Functions.get_enem_subjects_acronym import get_enem_subjects_acronym
from interface.main_page import main_page


st.set_page_config(layout='wide', page_title='Enemaster.app', initial_sidebar_state="expanded", page_icon="🧊",    menu_items={
        'About': "# Feito por *enemaster.app*"
    })


def main():
    main_page()


if __name__ == "__main__":
    main()
