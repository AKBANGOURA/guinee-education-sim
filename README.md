🇬🇳 Simulateur Économétrique : Rupture Structurelle & Projets Éducatifs (Guinée 2026)

Auteur : Almamy Kalla BANGOURA – Consultant Data

📌 Présentation du Projet

Ce projet propose une analyse économétrique avancée du système éducatif guinéen, centrée sur la rupture structurelle majeure de 2022. Suite aux réformes de moralisation des examens nationaux, les trajectoires de réussite ont subi un choc exogène, nécessitant de nouveaux outils de modélisation pour la planification stratégique à l'horizon 2026.

L'objectif est de fournir aux décideurs et chercheurs un simulateur interactif permettant de visualiser l'interdépendance entre les cycles (CEE, BEPC) et le taux de réussite au Baccalauréat (BAC).

🚀 Fonctionnalités Visualisation Historique (2005-2025) : Analyse des séries temporelles mettant en évidence le changement de paradigme post-2022.

Modélisation Prédictive : Algorithme basé sur la Régression de Ridge ($L_2$) pour traiter la multicolinéarité des variables éducatives.
Simulation Interactive : Sliders permettant d'ajuster les cibles du CEE et du BEPC pour projeter les résultats du BAC 2026 en temps réel.

🛠️ Stack TechniqueLangage : Python 3.9+Framework Web : StreamlitAnalyse de données : Pandas, NumPyMachine Learning : Scikit-Learn (Ridge Regression)Visualisation : Matplotlib
📊 Méthodologie ScientifiqueLe modèle privilégie les données post-2022 pour capturer la "nouvelle normale" du système scolaire guinéen. 
L'utilisation de la régularisation de Ridge est justifiée par la nécessité de stabiliser les coefficients de régression sur un échantillon à faible profondeur historique mais à haute fidélité institutionnelle.Extrait de code\min_{\beta} \left( \|y - X\beta\|^2_2 + \alpha \|\beta\|^2_2 \right)

📦 Installation et Utilisation LocaleCloner le dépôt :Bashgit clone https://github.com/votre-username/guinee-education-sim.git

cd guinee-education-sim
Installer les dépendances :Bashpip install -r requirements.txt
Lancer l'application :Bashstreamlit run app.py

📄 Licence & Citations

Ce projet est développé dans le cadre d'un travail de recherche en économie de l'éducation. Pour toute citation ou utilisation des données dans un cadre académique, merci de contacter l'auteur.Contact : Almamy Kalla BANGOURALaboratoire : Candidat au Laboratoire d'Économie de Poitiers (LEP)

🚀 Roadmap & Perspectives de Recherche

Cette section détaille les évolutions prévues pour le projet dans le cadre de mes travaux doctoraux au sein du Laboratoire d'Économie de Poitiers (LEP) :

Intégration des données régionales : Analyse fine par préfectures pour identifier les disparités géographiques de rendement scolaire.

Modélisation de la déperdition (Leakage Analysis) : Étude des flux d'élèves entre le BEPC et le BAC pour quantifier l'impact de l'abandon scolaire sur la performance nationale.

Analyse de l'efficacité des intrants : Corrélation entre les budgets alloués aux infrastructures et l'évolution des scores de Ridge par zone.

Développement d'un API : Mise à disposition des prédictions pour les services de planification du Ministère de l'Enseignement Pré-Universitaire (MEPU-A).

🤝 Contributions et Collaboration

Les contributions sont les bienvenues, particulièrement sur les axes suivants :

Amélioration du Modèle : Test d'autres techniques de régularisation (Lasso, ElasticNet) pour comparer les performances avec le modèle Ridge actuel.

Visualisation : Développement de cartes interactives (Geopandas) pour la représentation spatiale des données.

Data Cleaning : Enrichissement de la base de données historique avec les rapports d'inspection annuels.