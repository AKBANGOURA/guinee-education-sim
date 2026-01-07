# 🇬🇳 Simulateur Économétrique : Rupture Structurelle & Projets Éducatifs

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://votre-lien-streamlit-ici)

**Auteur :** Almamy Kalla BANGOURA – Consultant Data | Candidat au LEP (Poitiers)

---

## 📌 Présentation du Projet
Ce projet propose une analyse économétrique avancée du système éducatif guinéen, centrée sur la **rupture structurelle majeure de 2022**. Suite aux réformes de moralisation des examens nationaux, les trajectoires de réussite ont subi un **choc exogène**, nécessitant de nouveaux outils de modélisation pour la planification stratégique à l'horizon 2026.

L'objectif est de fournir un **simulateur interactif** permettant de visualiser l'interdépendance entre les cycles (CEE, BEPC) et le taux de réussite au Baccalauréat (BAC). Le lien su simulateur 

## 🚀 Simulateur Interactif
L'application est déployée sur Streamlit Cloud. Vous pouvez tester différents scénarios de réussite ici :
👉 **https://almamy-bangoura-thesis.streamlit.app/**
---

## 🚀 Fonctionnalités
* **Visualisation Historique (2005-2025) :** Mise en évidence graphique du changement de paradigme post-2022.
* **Données :** Taux de réussite nationaux (CEE, BEPC, BAC) consolidés sur la période 2005-2025.
* **Analyse :** Comparaison de matrices de corrélation avant/après réforme pour prouver la stabilisation structurelle.
* **Modélisation Prédictive :** Algorithme basé sur la **Régression de Ridge ($L_2$)** pour traiter la multicolinéarité.
* Régression de Ridge (Pénalisation $L_2$) pour gérer la multicolinéarité et la faible profondeur historique post-2022
* **Simulation Interactive :** Curseurs dynamiques pour projeter les résultats du BAC 2026.

## 📊 Méthodologie Scientifique
Le modèle privilégie les données post-2022 pour capturer la "nouvelle normale". L'utilisation de la régularisation de Ridge stabilise les coefficients sur un échantillon à faible profondeur historique.

**Équation du modèle :**
$$\min_{\beta} \left( \|y - X\beta\|^2_2 + \alpha \|\beta\|^2_2 \right)$$

---

## 📂 Structure du Dépôt
- `app.py` : Script principal de l'application Streamlit.
- `data_cleaned.csv` : Dataset consolidé et nettoyé.
- `requirements.txt` : Liste des dépendances Python (Pandas, Scikit-Learn, Plotly/Matplotlib).
- `article_guinee_2026.pdf` : L'article scientifique complet de 7 pages.

## 🛠️ Stack Technique
* **Langage :** Python 3.9+
* **Interface :** Streamlit
* **Machine Learning :** Scikit-Learn
* **Data :** Pandas, NumPy, Matplotlib

---

## 🚀 Roadmap
* Analyse régionale par préfecture.
* Étude de la déperdition (Leakage Analysis).
* Corrélation budgets/infrastructures et réussite.


## 🛠️ Installation Locale
1. Cloner le dépôt :
   ```bash
   git clone [https://github.com/votre-nom/guinee-education-sim.git](https://github.com/votre-nom/guinee-education-sim.git)
---

## 🤝 Contact

**Almamy Kalla BANGOURA** Candidat au Laboratoire d'Économie de Poitiers (LEP)

