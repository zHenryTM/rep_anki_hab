import streamlit as st
from interface.main_page import main_page


st.set_page_config(layout='wide', page_title='Enemaster.app', initial_sidebar_state="expanded", page_icon="🧊",    menu_items={
        'About': "# Feito por *enemaster.app*"
    })


def main():
    main_page()


if __name__ == "__main__":
    main()
