# 🇬🇳 Simulateur Économétrique : Rupture Structurelle & Projets Éducatifs

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://votre-lien-streamlit-ici)

**Auteur :** Almamy Kalla BANGOURA – Consultant Data | Candidat au LEP (Poitiers)

---

## 📌 Présentation du Projet
Ce projet propose une analyse économétrique avancée du système éducatif guinéen, centrée sur la **rupture structurelle majeure de 2022**. Suite aux réformes de moralisation des examens nationaux, les trajectoires de réussite ont subi un **choc exogène**, nécessitant de nouveaux outils de modélisation pour la planification stratégique à l'horizon 2026.

L'objectif est de fournir un **simulateur interactif** permettant de visualiser l'interdépendance entre les cycles (CEE, BEPC) et le taux de réussite au Baccalauréat (BAC). Le lien su simulateur https://almamy-bangoura-thesis.streamlit.app/

---

## 🚀 Fonctionnalités
* **Visualisation Historique (2005-2025) :** Mise en évidence graphique du changement de paradigme post-2022.
* **Modélisation Prédictive :** Algorithme basé sur la **Régression de Ridge ($L_2$)** pour traiter la multicolinéarité.
* **Simulation Interactive :** Curseurs dynamiques pour projeter les résultats du BAC 2026.

---

## 📊 Méthodologie Scientifique
Le modèle privilégie les données post-2022 pour capturer la "nouvelle normale". L'utilisation de la régularisation de Ridge stabilise les coefficients sur un échantillon à faible profondeur historique.

**Équation du modèle :**
$$\min_{\beta} \left( \|y - X\beta\|^2_2 + \alpha \|\beta\|^2_2 \right)$$

---

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

---

## 🤝 Contact

**Almamy Kalla BANGOURA** Candidat au Laboratoire d'Économie de Poitiers (LEP)
