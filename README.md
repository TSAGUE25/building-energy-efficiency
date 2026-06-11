# Efficacité Énergétique des Bâtiments

> **Segmentation et prédiction de consommation énergétique par Machine Learning**

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Domaine](https://img.shields.io/badge/Domaine-Énergie-green)
![Statut](https://img.shields.io/badge/Statut-Portfolio-orange)
![Données](https://img.shields.io/badge/Données-Simulées%2FAnonymisées-lightgrey)

---

## Contexte métier

Dans le secteur de l'énergie, l'optimisation de la consommation des bâtiments représente un enjeu économique et environnemental majeur. Un parc immobilier peut comporter des centaines de sites avec des profils de consommation très hétérogènes.

---

## Problème traité

Identifier les bâtiments énergivores, segmenter les sites par profil de consommation et prédire l'IEP (Indicateur d'Efficacité énergétique en kWh/m²) pour prioriser les actions d'amélioration.

---

## Solution proposée

KMeans clustering pour la segmentation (méthode du coude + silhouette), LinearRegression et RandomForestRegressor pour la prédiction, score de priorité composite combinant IEP, surface et ancienneté.

---

## Technologies utilisées

| Outil | Usage |
|-------|-------|
| Python 3.10+ | Langage principal |
| pandas / numpy | Manipulation des données |
| scikit-learn | Machine Learning & preprocessing |
| matplotlib / seaborn | Visualisation |
| Jupyter Notebook | Exploration interactive |

> Voir `requirements.txt` pour la liste complète.

---

## Structure du projet

```
building-energy-efficiency/
├── README.md              ← Ce fichier
├── PORTFOLIO.md           ← Documentation complète du cas d'usage
├── .gitignore
├── requirements.txt
├── notebooks/             ← Jupyter Notebooks d'exploration
├── src/                   ← Code Python modulaire
├── data_sample/           ← Données simulées (anonymisées)
├── figures/               ← Graphiques et visualisations
├── reports/               ← Rapports et synthèses
└── docs/                  ← Documentation complémentaire
```

---

## Installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/TSAGUE25/building-energy-efficiency.git
cd building-energy-efficiency

# 2. Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate    # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer Jupyter
jupyter notebook
```

---

## Métriques clés (données simulées)

```
R², RMSE, MAE, IEP (kWh/m²), Silhouette Score
```

---

## Valeur métier

Réduction de 15-20 % de la consommation énergétique sur les sites prioritaires (simulé).

---

## Limites

Données météo simplifiées. Absence de données d'occupation réelles.

---

## Prochaines améliorations

Intégration DJC réels. Modèle time-series pour la prédiction mensuelle. Power BI dashboard.

---

## Avertissement — Confidentialité

> **Toutes les données utilisées dans ce projet sont simulées, synthétiques ou anonymisées.**
> Aucune donnée réelle, confidentielle ou propriétaire n'est présente dans ce dépôt.
> Ce projet est un cas d'usage pédagogique à destination du portfolio professionnel d'Emmanuel TSAGUE.

---

## Contributors

**TSAGUE Emmanuel** — Data Scientist / Data Analyst
Domaine : Énergie · Performance opérationnelle · Data Science
GitHub : [TSAGUE25](https://github.com/TSAGUE25)

> Voir [PORTFOLIO.md](PORTFOLIO.md) pour la documentation complète du cas d'usage (24 sections).
