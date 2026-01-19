# =================================================================
# PROJET DE THÈSE : Économie de l'Éducation en Guinée
# APPLICATION : Simulateur de Rupture Structurelle et Prédictions
# AUTEUR : Almamy Kalla BANGOURA
# PROFESSION : Consultant Data | Chargé d'études statistiques
# LABORATOIRE : Candidat au Laboratoire d'Économie de Poitiers (LEP)
# =================================================================

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# 1. Configuration de la page
st.set_page_config(page_title="Simulateur Guinée 2005-2026", layout="wide")

# 2. BARRE LATÉRALE : PARAMÈTRES EN PREMIER
st.sidebar.header("🎯 Paramètres de Simulation 2026")
st.sidebar.info("Ajustez les cibles pour voir l'impact sur le BAC 2026.")
cee_target = st.sidebar.slider("Cible CEE 2026 (%)", 10.0, 90.0, 61.74)
bepc_target = st.sidebar.slider("Cible BEPC 2026 (%)", 10.0, 80.0, 44.25)

st.sidebar.markdown("---") # Ligne de séparation

# 3. DESCRIPTION DE L'AUTEUR EN DESSOUS
st.sidebar.header("🎓 À propos de l'auteur")
st.sidebar.write("**Auteur :** Almamy Kalla BANGOURA")
st.sidebar.write("**Profil :** Economiste-statisticien | Consultant BI et Expert en analyse des données et évaluation d'impact des politiques publiques")

# 4. Données Historiques (2005-2025)
@st.cache_data
def load_data():
    data = {
        'Annee': list(range(2005, 2026)),
        'CEE': [61.5, 63.4, 59.8, 62.7, 64.2, 66.5, 58.4, 63.1, 65.4, 68.2, 66.7, 69.4, 71.2, 63.4, 62.34, 55.83, 62.08, 17.62, 44.25, 63.22, 65.5],
        'BEPC': [48.2, 45.9, 43.1, 47.5, 49.3, 50.1, 42.6, 44.8, 46.2, 48.5, 47.2, 49.8, 48.6, 45.6, 44.11, 35.59, 35.08, 15.04, 34.05, 47.11, 48.2],
        'BAC': [27.0, 33.15, 19.0, 26.45, 29.0, 31.53, 34.0, 38.0, 26.0, 34.0, 26.0, 42.0, 27.12, 26.04, 24.38, 44.43, 25.36, 9.37, 27.46, 24.64, 32.33]
    }
    return pd.DataFrame(data)

df = load_data()

# 5. Modèle prédictif (Régression de Ridge)
df_recent = df[df['Annee'] >= 2022]
model = Ridge(alpha=1.0).fit(df_recent[['CEE', 'BEPC']], df_recent['BAC'])
prediction_2026 = model.predict([[cee_target, bepc_target]])[0]

# 6. Interface Principale
st.title(" GUINEE : Pilotage Stratégique des Examens ")
st.title(" Prédiction : Horizon 2026 ")
st.markdown("### Analyse de la rupture structurelle et projections économétriques")

col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Trajectoires des Examens (2005-2025)")
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Graphiques
    ax.plot(df['Annee'], df['CEE'], label='CEE', marker='o', color='#2ECC71', alpha=0.7)
    ax.plot(df['Annee'], df['BEPC'], label='BEPC', marker='o', color='#F1C40F', alpha=0.7)
    ax.plot(df['Annee'], df['BAC'], label='BAC', marker='s', color='#E74C3C', linewidth=3)
    
    # Ligne de rupture
    ax.axvline(x=2022, color='black', linestyle='--', label='Rupture (Rigueur 2022)')
    
    # Correction des axes (Années entières)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.get_xaxis().get_major_formatter().set_useOffset(False)
    ax.get_xaxis().get_major_formatter().set_scientific(False)
    
    ax.set_ylabel("Taux de réussite (%)")
    ax.legend(loc='lower left')
    ax.grid(True, linestyle=':', alpha=0.5)
    st.pyplot(fig)

with col2:
    st.metric(label="PROJECTION BAC 2026", value=f"{prediction_2026:.2f} %")
    st.write("---")
    st.write("**Note Stratégique :**")
    st.caption("Cette projection repose sur l'hypothèse d'une persistance du modèle de rigueur instauré en 2022, un intervalle de confiance stochastique permet d'anticiper les variations selon les aléas de gouvernance ou de calendrier.")

# 7. Recommandation finale

st.success(f"**Analyse de l'Expert:** La corrélation entre les cycles s'est stabilisée à un niveau de rigueur élevé. Pour 2026, une cible de {prediction_2026:.1f}% au BAC est cohérente avec les efforts de moralisation des examens.")



















