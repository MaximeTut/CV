import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import seaborn as sns
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pages import *

photo = "photo_profil.png"
photo2 = "Photo_profil2.jpg"

st.set_page_config(page_icon = photo2, page_title ="Maxime Le Tutour", layout = "wide",)


def main():
    st.header("Data Scientist | Data Analyst")
    choice = option_menu(
            menu_title = None,
            options = ["Présentation", "Compétence", "Portfolio"],
            icons=["house", "speedometer","book"],
            menu_icon="robot", orientation = "horizontal",
             styles={
                 "container": {"padding": "0!important", "font-size" : "40px"},
        "icon": {"color": "orange", "font-size": "28px"}, 
        "nav-link": {"font-size": "22px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
        )

    with st.sidebar:

        with st.container():
            col1, col2, col3 = st.columns([1,6,1])
            col2.image(photo2, width = 180)
            col2.title("Maxime Le Tutour")
            

        col1, col2, col3 = st.columns([1.2,2,1])
        col1.markdown("**Téléphone:**")
        col2.write("06 77 32 74 01")

        col1.markdown("**Email:**")
        col2.write("maxime.letutour@gmail.com")

        col1.markdown("**Adresse:**")
        col2.write("Bretagne")

        st.markdown("#")


        with st.container():
            col1, col2= st.columns([1,3])
            col1.image("linkedin.png", width = 40)
            col2.subheader("[Compte Linkedin ](https://www.linkedin.com/in/maxime-le-tutour-95994795/)")

            col1.image("github.png", width = 40)
            col2.subheader("[Compte Github ](https://github.com/MaximeTut)")
        
    if choice == "Présentation":
        presentation()
    if choice == "Compétence":
        Competences()
    elif choice == "Portfolio":
        portfolio()



if __name__ == '__main__':
	main()