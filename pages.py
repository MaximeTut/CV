import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


def presentation():
    st.write("Avec 5 ans d’expérience manipulant au quotidien les données dans \
l’industrie et passionné d'investigation j'ai décidé d'orienter ma carrière vers \
le monde de la data science. Avec mes compétences en programmation Python et mes \
connaissances en statistiques et mise en production de modèle je saurai faire parler \
vos données !")

    df = pd.DataFrame([
    dict(Task="Licence Biologie", Start='2006', Finish='2009', Ecole="Université Bretagne Sud"),
    dict(Task="Master Sciences de l'environnement", Start='2009', Finish='2011', Ecole="Université de La Rochelle"),
    dict(Task="Master Intelligence Artificielle", Start='2020', Finish='2022', Ecole="IA School")])

    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Ecole", height = 240, width = 1100)
    fig.update_yaxes(visible = True)
    fig.update_layout(showlegend=True, yaxis_title=None, font=dict(size=14))

    st.markdown("#### 🎓 Parcours Universitaire")
    st.plotly_chart(fig)

    st.markdown("#### 🔨 Parcours Professionnel")
    st.markdown("#")

    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)

        col1.markdown("##### 2012-2014 ")
        col1.markdown("###### Responsable Qualité\n_Argoat Plastique_")
        col1.write(" ISO 9001 | Gestion de projet")

        col2.markdown("##### 2015-2017")
        col2.markdown("###### Volontaire Workaway à l'internationale\n _(Angleterre, Pérou, Colombie, Mexique, Espagne, Népal, Inde)_")
        col2.write("Apprentissage de l'anglais et de l'espagnol")
        col2.write("[Références](https://www.fichier-pdf.fr/2017/11/24/workawayreferenceletter/?)")

        

        col3.markdown("##### 2018-2020")
        col3.markdown("###### Consultant Qualité au Canada\n_Taghleef Canada_")
        col3.write("Analyse statistique | Gestion de projet")

        col4.markdown("##### 2020-2021")
        col4.markdown("###### Data Analyst\n_Data Scientest_")
        col4.write("Analyse avancée de paris sportifs pour un retour sur investissement maximum grâce au machine learning.")
        col4.write("[Lien du projet](https://github.com/MaximeTut/Beat_the_bookmakers)")

        col5.markdown("##### 2021-2022")
        col5.markdown("###### Data Scientist\n_Bouygues Construction_")
        col5.write("Dataiku | Snowflake | NLP | Machine Learning | Programmation Python")




def Competences():

    with st.expander("🧑‍💻 Data Science") :

        with st.container():
            col1, col2 = st.columns(2)
            with col1:

                techno = ['Python','Dashboarding','Base de données','Machine learning | Deep learning', 'Big Data', 'Statistiques', 'Mise en production']
                notes = [4.6, 4, 3.8, 3.9, 2.7, 4, 4]

                df = pd.DataFrame()
                df["techno"] = techno
                df["notes"] = notes

                fig = px.line_polar(df, r='notes', theta='techno',range_r = [0,5], line_close=True,
                                color_discrete_sequence = ["darkseagreen"], width=430,
                height=400,title="Compétences Générales")

                fig.update_traces(fill='toself')
                fig.update_layout(polar = dict(radialaxis = dict(showticklabels = False)))
                fig.update_layout(polar = dict(radialaxis = dict(visible = False)))
                fig.update_layout(width = 500)
                st.plotly_chart(fig)

            with col2 :
                df = pd.DataFrame()

                competences = ["Python", "Python", "IA", "IA", "IA",
                            "IA", "IA" ,"IA","Python", "Python", "Business Intelligence",
                            "Business Intelligence","Big Data", "ML Ops", "ML Ops", "ML Ops",
                            "ML Ops", "ML Ops",
                            "ML Ops", "Big Data", "Big Data"]


                librairies = ["Data analyse", "Data analyse", "TensorFlow/Keras", "TensorFlow/Keras", "TensorFlow/Keras",
                            'Scikit-Learn', 'Scikit-Learn', 'Scikit-Learn', 'Data visualisation', 'Data visualisation',
                            'PowerBI', 'Tableau','Pyspark', 'API', 'API',
                            'Contener', 'Versioning', "Cloud", "Tests Unitaires", "Dataiku", "SQL"]

                df["Compétence"] = competences
                df["Librairies"] = librairies
                df["Détails"] = ["Pandas", "Numpy", "Réseau de convolution", "Natural Language Processing", "Time Series", "Apprentissage Supervié",
                                "Clustering", "Apprentissage semi-supervisé", "Matplotlib/Seaborn", "Plotly", None, None, None, "Flask", "FastAPI", "Docker",
                                "Git/Github", "Azure", "Pytest", None, None]

                fig = px.sunburst(df, path=['Compétence', 'Librairies', 'Détails'], title = "Compétences détaillées")
                fig.update_layout(width = 500)

                st.plotly_chart(fig)
                st.markdown("##### Cliquez sur le graphe pour dérouler 👆 ")
    
    with st.expander(" 💬 Langues"):
        col1, col2, col3 = st.columns(3)
        with col1:
            fig = go.Figure(go.Indicator(
                    mode = "gauge",
                    value = 10,
                    title = {'text': "Français"},
                    gauge = {'axis': {'range': [0, 10]},
                            'bar': {'color': "seashell"},
                            'steps' : [{'range': [0, 10], 'color': "steelblue"}] }))
                
            fig.update_layout(autosize=False, width=300, height=300)
            fig.update_xaxes(showticklabels=False, visible=False)
            fig.update_yaxes(showticklabels=False, visible=False)

            fig.update_layout(
                annotations = list(fig.layout.annotations) + 
                [go.layout.Annotation(
                        x=0.5,
                        y=0.25,
                        font=dict(
                            size=20, color = 'blue'
                        ),
                        showarrow=False,
                        text="Langue maternelle",
                        textangle=0,
                        xref="paper",
                        yref="paper")])

            fig.update_layout(margin=dict(
                        l=0,
                        r=0,
                        b=0,
                        t=0))
            st.plotly_chart(fig)
        
        with col2:
                fig = go.Figure(go.Indicator(
                        mode = "gauge",
                        value = 9,
                        title = {'text': "Anglais"},
                        gauge = {'axis': {'range': [0, 10]},
                                'bar': {'color': "red"},
                                'steps' : [{'range': [0, 9], 'color': "blue"}] }))
                    
                fig.update_layout(autosize=False, width=300, height=300)
                fig.update_xaxes(showticklabels=False, visible=False)
                fig.update_yaxes(showticklabels=False, visible=False)

                fig.update_layout(
                    annotations = list(fig.layout.annotations) + 
                    [go.layout.Annotation(
                            x=0.5,
                            y=0.25,
                            font=dict(
                                size=20, color = 'blue'
                            ),
                            showarrow=False,
                            text="Avancé (C1)",
                            textangle=0,
                            xref="paper",
                            yref="paper")])

                fig.update_layout(margin=dict(
                            l=0,
                            r=0,
                            b=0,
                            t=0))
                st.plotly_chart(fig)

        with col3:
                fig = go.Figure(go.Indicator(
                    mode = "gauge",
                    value = 7,
                    title = {'text': "Espagnol"},
                    gauge = {'axis': {'range': [0, 10]},
                            'bar': {'color': "red"},
                            'steps' : [{'range': [0, 7], 'color': "yellow"}] }))
    
                fig.update_layout(autosize=False, width=300, height=300)
                fig.update_xaxes(showticklabels=False, visible=False)
                fig.update_yaxes(showticklabels=False, visible=False)

                fig.update_layout(
                    annotations = list(fig.layout.annotations) + 
                    [go.layout.Annotation(
                            x=0.5,
                            y=0.25,
                            font=dict(
                                size=20, color = 'red'
                            ),
                            showarrow=False,
                            text="Intermédiaire (B2)",
                            textangle=0,
                            xref="paper",
                            yref="paper")])

                fig.update_layout(margin=dict(
                            l=0,
                            r=0,
                            b=0,
                            t=0))
                
                st.plotly_chart(fig)
        col2.markdown("󠁧󠁢**Volontariat en Angleterre et au Népal : ** 1 an")
        col3.markdown("**Volontariat en Amérique Latine et en Espagne :** 10 mois")


    col1, col2 = st.columns(2)

    with col1.expander("💡 Soft Skills"):
        quali = ['Curiosité','Créativité', 'Sociabilité','Analytique','Pédagogie', 'Communication']
        notes = [4.6, 4.3, 4.5, 4, 3.8, 3.9]


        df = pd.DataFrame()
        df["quali"] = quali
        df["notes"] = notes

        fig = px.line_polar(df, r='notes', theta='quali',range_r = [0,5], line_close=True,
                            color_discrete_sequence = ["blue"], width=200,
            height=400,title="Soft Skills")

        fig.update_traces(fill='toself')
        fig.update_layout(polar = dict(radialaxis = dict(showticklabels = False)))
        fig.update_layout(polar = dict(radialaxis = dict(visible = False)))
        fig.update_layout(width = 500)
        st.plotly_chart(fig)

    with col2.expander(" 🎓 Certifications"):
        st.markdown("**Dataiku :** Core Designer | ML Practitioner | Advanced Designer | Developer | ML Ops")
        st.markdown("**Azure :** AZ-900: Microsoft Azure Fundamentals | DP-100: Designing and Implementing a Data Science Solution on Azure\
         | AI-900: Microsoft Azure AI Fundamentals")
    
    with st.expander("Centres d'intérêts"):
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([2,3,1,4,1,4,1,3])
        col1.image("compostelle.png", width = 100)
        col2.markdown("**Randonnée :** \n Randonnée de\
            Saint-Jacques de Compostelle. 865 km de Saint-Jean-Pied-de-Port\
            jusque Finistera.")
        with col4 :
            st.markdown("**Actualité IA et scientifique** \n Abonné à :" )
            st.image("magasine.png", width=200)
        with col6:
            st.markdown("**Jeux de société** :")
            st.image("catan.png", width=115)
        with col8:
            st.markdown("🎸 **Guitare** \n Je joue essentiellement avec une folk. Je compose et enregistre de temps en temps\
                de façon très modeste :)")
        



def portfolio():
    col1, col2, col3 = st.columns(3)
    st.markdown(
        """
    <style>
    .streamlit-expanderHeader {
        font-size: 20px;
        font-weight : bold;
        background-color: rgb(255, 255, 255);
    }
    .streamlit-expander {background-color: rgb(255, 255, 255)}
    </style>
    """,
        unsafe_allow_html=True,
    )

    with col1.expander("NLP", expanded= True ):
        st.image("img_nlp.png", width=100)
        style  = '<p style="font-family:sans-serif; font-weight : bold; color:Green; font-size: 15px;">Topic Modeling & Analyse de sentiment</p>'
    
        st.markdown(style, unsafe_allow_html=True)
        st.write(" Analyse de sentiment et Topic modeling d'une application Smart City utilisée par les\
            habitants pour détecter des causes de mécontentements.")
        st.markdown("**#Transformers #Python**")


    with col2.expander("Dashboarding", expanded = True ):
        st.image("poleemploi.png", width=180)
        style  = '<p style="font-family:sans-serif; font-weight : bold; color:Green; font-size: 15px;">Analyse des données de Pôle Emploi</p>'
        st.markdown(style, unsafe_allow_html=True)
        st.write("Analyser facilement les pénuries de talents selon les régions.")
        st.markdown("######")
        st.markdown("**#Seaborn #Plotly**")
        st.write("[**Lien de la webapp**](https://share.streamlit.io/maximetut/emploi2021/main/emploi2021.py)")


    with col3.expander("Statistique et prédiction", expanded= True):
        st.image("turnover.png", width=220)
        style  = '<p style="font-family:sans-serif; font-weight : bold; color:Green; font-size: 15px;">Analyse Turn-Over</p>'
        st.markdown(style, unsafe_allow_html=True)
        st.write("Analyse statistique des causes du turn-over, proposition d'un plan de rétention des talents\
            et prédiction des fuites des salariés")
        st.markdown("**#shap #statistique #scikit-learn**")
        st.write("[**Lien du Notebook**](https://github.com/MaximeTut/Analyse_Turn_Over/blob/main/Analyse_Turn_Over.ipynb)")
    
    col1, col2, col3 = st.columns(3)
    with col1.expander("Data visualisation", expanded= True ):
        st.image("accident.png", width=240)
        style  = '<p style="font-family:sans-serif; font-weight : bold; color:Green; font-size: 15px;">Réduction des accidents de la route</p>'
        st.markdown(style, unsafe_allow_html=True)
        st.write("Analyse des taux d'accidents du Royaume-Unis, identification des causes et recommandations pour les réduire.")
        st.markdown("**#Seaborn #Matplotlib**")
        st.write("[**Lien du Notebook**](https://github.com/MaximeTut/Analyse_accident/blob/main/accident_ru.ipynb)")


    with col2.expander("Text Generating", expanded = True ):
        st.image("robot.png", width=150)
        style  = '<p style="font-family:sans-serif; font-weight : bold; color:Green; font-size: 15px;">Discussion avec un robot</p>'
        st.markdown(style, unsafe_allow_html=True)
        st.write("Déploiement de l'algorithme GPT-2 sous la forme de question/réponse")
        st.markdown("**#NLP #GTP-2**")
        st.write("[**Lien de la webapp**](https://share.streamlit.io/maximetut/robot/main/app.py)")

    with col3.expander("Machine Learning", expanded = True ):
        st.image("pari.png", width=180)
        style  = '<p style="font-family:sans-serif; font-weight : bold; color:Green; font-size: 15px;">Beat the Bookmakers</p>'
        st.markdown(style, unsafe_allow_html=True)
        st.write("Etablir une stratégie de pari sur des matchs de tennis pour générer un maximum de ROI. ROI : 14%")
        st.markdown("**#XGBoost #Scikit-Learn**")
        st.write("[**Lien de la webapp**](https://github.com/MaximeTut/Beat_the_bookmakers)")

    col1, col2, col3 = st.columns(3)
    with col1.expander("Computer vision", expanded= True):
        st.image("computervision.png", width= 100)
        style  = '<p style="font-family:sans-serif; font-weight : bold; color:Green; font-size: 15px;">Détection de maladie</p>'
        st.markdown(style, unsafe_allow_html=True)
        st.write("Utilisation des réseaux de convolution pour diagnostiquer des maladies sur des \
            radiographies de la poitrine.")
        st.markdown("**#Tensorflow #Keras**")
        st.write("[**Lien du Notebook**](https://www.kaggle.com/code/maximetut/cnn-x-ray-images/notebook)")
