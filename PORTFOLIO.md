# CAS D'USAGE 1 — Efficacité énergétique des bâtiments
## Analyse de l'efficacité énergétique pour identifier les leviers de réduction de consommation

> **Auteur :** TSAGUE EMMANUEL — Data Scientist / Data Analyst  
> **Domaine :** Énergie, Performance opérationnelle, Pilotage par les indicateurs  
> **Repository GitHub :** `building-energy-efficiency-analytics`  
> **Statut :** Portfolio — données simulées  
> **Date :** Juin 2026

---
## 1. TITRE ET RÉSUMÉ EXÉCUTIF

### Titre complet

**"Analyse de l'efficacité énergétique des bâtiments pour identifier les leviers de réduction de consommation et prioriser les actions correctives"**

### Résumé exécutif (Executive Summary)

> Un résumé exécutif est un texte court qui explique l'essentiel du projet en quelques lignes, destiné à un décideur qui n'a pas le temps de tout lire.

Dans ce projet, une organisation exploitant un parc de bâtiments (bureaux, entrepôts, sites industriels, logements sociaux) souhaite comprendre et réduire ses consommations énergétiques. Les données proviennent de compteurs intelligents, de capteurs de température intérieure/extérieure, de systèmes de gestion technique des bâtiments (GTB) et de relevés manuels. L'analyse permet d'identifier les bâtiments les plus énergivores, d'expliquer les causes de sur-consommation, de détecter les dérives et de prioriser les investissements d'amélioration.

**Résultats hypothétiques (simulés pour portfolio) :**
- Identification de 15 % des bâtiments responsables de 40 % de la sur-consommation
- Gain potentiel estimé entre 10 % et 25 % sur la facture énergétique annuelle
- Tableau de bord Power BI opérationnel pour le suivi mensuel des indicateurs

---
## 2. CONTEXTE MÉTIER

### Qui est concerné ?

Les organisations suivantes sont directement concernées par ce type de projet :
- **Collectivités territoriales** gérant un parc immobilier public (écoles, mairies, gymnases)
- **Bailleurs sociaux** supervisant des centaines de logements
- **Entreprises industrielles** cherchant à réduire leur facture énergétique
- **Exploitants d'énergie** (type EDF, Enedis, Veolia, Dalkia) vendant des services d'efficacité énergétique
- **Property managers** gérant des immeubles de bureaux

### Contexte opérationnel

Depuis 2020, les réglementations européennes (directive sur l'efficacité énergétique) et nationales (décret tertiaire en France) imposent aux bâtiments tertiaires de réduire leur consommation d'énergie de **40 % d'ici 2030** et de **60 % d'ici 2050** par rapport à une année de référence.

> **Décret tertiaire :** réglementation française qui oblige les propriétaires et exploitants de bâtiments tertiaires de plus de 1 000 m² à déclarer leurs consommations et à respecter des objectifs de réduction.

Dans ce contexte, les organisations doivent :
1. Mesurer précisément leurs consommations actuelles
2. Identifier les bâtiments "passoires énergétiques"
3. Comprendre les causes de sur-consommation
4. Prioriser les travaux et les actions correctives
5. Suivre les progrès dans le temps

### Données disponibles

Les organisations disposent généralement de :
- **Factures d'énergie** (électricité, gaz, chaleur) — données mensuelles ou annuelles
- **Compteurs communicants** — données horaires ou à la demi-heure
- **Capteurs GTB** (Gestion Technique du Bâtiment) — température, occupation, horaires
- **Données météo** — température extérieure, ensoleillement, degré-jours climatiques

> **Degré-jour climatique (DJC) :** indicateur qui mesure l'écart entre la température extérieure et une température de référence (souvent 18°C). Plus les DJC sont élevés, plus le chauffage est nécessaire. Cela permet de comparer des consommations d'années climatiquement différentes.

---
## 3. POURQUOI CE SUJET EXISTE DANS L'ORGANISATION

### La réponse directe

Ce sujet existe parce que **l'énergie coûte cher, les réglementations sont plus strictes, et les données pour agir existent mais ne sont pas exploitées**.

### Les 5 raisons concrètes

| Raison | Explication | Impact si non traité |
|--------|-------------|----------------------|
| **Coût financier** | L'énergie représente 3 à 8 % du budget d'exploitation d'un bâtiment | Factures en hausse non maîtrisées |
| **Obligation réglementaire** | Décret tertiaire, ISO 50001, reporting ESG | Amendes, image dégradée |
| **Objectifs RSE** | Les entreprises s'engagent sur des cibles carbone | Non-respect des engagements publics |
| **Manque de visibilité** | Sans tableau de bord, personne ne sait quel bâtiment consomme quoi | Décisions d'investissement mal orientées |
| **Potentiel inexploité** | Des économies de 10 à 30 % sont possibles sans travaux lourds | Argent gaspillé |

> **RSE (Responsabilité Sociétale des Entreprises) :** engagement d'une organisation à avoir un impact positif sur la société et l'environnement, au-delà de ses obligations légales.

---
## 4. PROBLÈME MÉTIER FORMULÉ COMME DÉFI OPÉRATIONNEL

### Le problème principal

> "Nous disposons des données de consommation de nos bâtiments, mais nous ne savons pas lesquels consomment trop, pourquoi, et où agir en priorité."

### Les défis opérationnels concrets

1. **Défi de la comparaison** : Comment comparer des bâtiments de tailles différentes ? (Un entrepôt de 10 000 m² consomme naturellement plus qu'un bureau de 500 m²)

2. **Défi de la normalisation** : Comment tenir compte de la météo pour comparer des années différentes ?

3. **Défi de la détection** : Comment repérer automatiquement un bâtiment dont la consommation dérive ?

4. **Défi de l'explication** : Une fois qu'un bâtiment est identifié comme énergivore, quelles sont les causes ?

5. **Défi de la priorisation** : Avec un budget limité, quel bâtiment réhabiliter en premier pour maximiser l'impact ?

6. **Défi du suivi** : Comment mesurer l'impact des travaux réalisés ?

---
## 5. OBJECTIFS DU PROJET

### Objectif principal

Construire une analyse complète de la performance énergétique d'un parc de bâtiments permettant d'**identifier les bâtiments énergivores, d'expliquer les causes de sur-consommation et de prioriser les actions correctives**.

### Objectifs secondaires

| Objectif | Description | Livrable attendu |
|----------|-------------|-----------------|
| **Mesurer** | Calculer les consommations normalisées en kWh/m² | Tableau de performance par bâtiment |
| **Comparer** | Benchmarker les bâtiments entre eux et par rapport à des références | Classement des bâtiments |
| **Détecter** | Identifier les dérives et anomalies de consommation | Alertes automatiques |
| **Expliquer** | Comprendre les facteurs d'influence | Corrélations et régression |
| **Prioriser** | Identifier les bâtiments à traiter en urgence | Score de priorité |
| **Suivre** | Mesurer l'évolution dans le temps | Tableau de bord Power BI |
| **Communiquer** | Restituer les résultats aux décideurs | Dashboard et rapport |

---
## 6. DONNÉES UTILISÉES

### Description du jeu de données

> **Note importante :** Les données présentées ci-dessous sont **simulées à titre pédagogique** et ne proviennent d'aucune organisation réelle. Elles illustrent le type de données que l'on trouverait dans un projet réel.

### Table principale : `batiments_energie.csv`

| Variable | Type | Description | Utilité métier | Risque qualité |
|----------|------|-------------|----------------|----------------|
| `id_batiment` | Texte | Identifiant unique du bâtiment | Clé de jointure | Doublons, formats incohérents |
| `nom_batiment` | Texte | Nom ou libellé du bâtiment | Lisibilité des rapports | Orthographes multiples |
| `type_usage` | Catégorie | Bureau, entrepôt, logement, industrie | Segmentation | Catégories non standardisées |
| `surface_m2` | Numérique | Surface utile en mètres carrés | Normalisation kWh/m² | Valeurs manquantes, erreurs de saisie |
| `annee_construction` | Entier | Année de construction | Analyse vétusté | Estimations approximatives |
| `date_mesure` | Date | Mois et année de la mesure | Analyse temporelle | Formats multiples, lacunes |
| `conso_elec_kwh` | Numérique | Consommation électricité en kWh | Indicateur principal | Compteurs bloqués, relève manquante |
| `conso_gaz_kwh` | Numérique | Consommation gaz en kWh | Indicateur principal | Conversions m³/kWh à vérifier |
| `conso_chaleur_kwh` | Numérique | Énergie livrée par réseau de chaleur | Indicateur principal | Données réseau parfois indisponibles |
| `conso_totale_kwh` | Numérique | Somme de toutes les énergies | Indicateur synthétique | À recalculer pour vérification |
| `temp_ext_moy_c` | Numérique | Température extérieure moyenne | Correction climatique | Stations météo manquantes |
| `djc_mois` | Numérique | Degrés-jours climatiques du mois | Normalisation météo | Calcul à vérifier selon base |
| `taux_occupation` | Numérique | Taux moyen d'occupation (0-100%) | Correction usage | Données souvent manquantes |
| `travaux_realises` | Booléen | Indicateur de travaux de rénovation | Mesure d'impact | Déclaratif, peu fiable |
| `classe_dpe` | Catégorie | Classe énergétique DPE (A à G) | Benchmark réglementaire | DPE parfois obsolète |

> **DPE (Diagnostic de Performance Énergétique) :** diagnostic obligatoire qui classe un bâtiment de A (très performant) à G (très énergivore) selon sa consommation théorique d'énergie.

### Variables dérivées à créer

| Variable créée | Formule | Intérêt |
|----------------|---------|---------|
| `iep_kwh_m2` | `conso_totale_kwh / surface_m2` | Indicateur de Performance Énergétique normalisé par surface |
| `iep_kwh_m2_djc` | `conso_totale_kwh / (surface_m2 * djc_mois)` | Indicateur corrigé du climat |
| `ecart_reference` | `iep_kwh_m2 - mediane_type_usage` | Écart par rapport au groupe de référence |
| `mois` | Extraction depuis `date_mesure` | Analyse saisonnière |
| `annee` | Extraction depuis `date_mesure` | Analyse tendancielle |
| `age_batiment` | `2026 - annee_construction` | Lien vétusté / consommation |
| `variation_mois_precedent` | Différence sur `conso_totale_kwh` | Détection de dérives |
| `score_anomalie` | Calculé par modèle | Probabilité d'être un bâtiment atypique |

### Risques qualité détaillés

> **Valeur manquante :** une cellule vide dans un tableau de données. Par exemple, un compteur hors service pendant un mois laisse un trou dans la série.

> **Valeur aberrante (outlier) :** une valeur qui semble irréaliste, comme une consommation de -500 kWh ou de 10 000 000 kWh pour un petit bureau.

| Problème | Exemple concret | Impact | Traitement |
|----------|-----------------|--------|------------|
| Compteur bloqué | Même valeur répétée 3 mois | Sous-estimation artificielle | Détection par variation nulle |
| Relève manquante | Trou de données sur janv. 2025 | Biais dans les agrégats | Interpolation ou exclusion |
| Mauvaise unité | Gaz en m³ non converti en kWh | Erreur de calcul grave | Contrôle et conversion (1 m³ gaz ≈ 11,6 kWh) |
| Doublon de ligne | Même bâtiment, même mois, 2 lignes | Surestimation | Dédoublonnage |
| Surface incorrecte | Bâtiment de 50 m² saisi à 500 m² | IEP complètement faussé | Contrôle par rapport à la moyenne |
| DJC incohérent | DJC en été > DJC en hiver | Correction climatique erronée | Vérification par station météo |
| Changement de compteur | Rupture de série en juin 2024 | Fausse anomalie détectée | Annotation des changements |

---
## 7. PRÉPARATION DES DONNÉES

### Vue d'ensemble de la démarche

```
Données brutes → Chargement → Nettoyage → Contrôle qualité → 
Variables dérivées → Normalisation → Jeu de données analytique propre
```

### Étape 1 : Chargement des données

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Chargement du fichier principal
df = pd.read_csv("data_sample/batiments_energie.csv", 
                  sep=";", 
                  encoding="utf-8",
                  parse_dates=["date_mesure"])

# Premier aperçu
print(df.shape)        # Nombre de lignes et colonnes
print(df.dtypes)       # Types de chaque colonne
print(df.head(5))      # Premières lignes
```

### Étape 2 : Diagnostic qualité initial

```python
# Taux de valeurs manquantes par colonne
taux_manquants = df.isnull().sum() / len(df) * 100
print(taux_manquants.sort_values(ascending=False))

# Détection des doublons
nb_doublons = df.duplicated(subset=["id_batiment", "date_mesure"]).sum()
print(f"Doublons détectés : {nb_doublons}")

# Statistiques descriptives
df.describe()
```

### Étape 3 : Nettoyage

```python
# Suppression des doublons (garder la première occurrence)
df = df.drop_duplicates(subset=["id_batiment", "date_mesure"], keep="first")

# Traitement des valeurs manquantes
# Surface : valeur critique — on exclut si manquante (impossible de normaliser)
df = df.dropna(subset=["surface_m2", "conso_totale_kwh"])

# Température extérieure : interpolation linéaire si manquante
df["temp_ext_moy_c"] = df.groupby("id_batiment")["temp_ext_moy_c"].transform(
    lambda x: x.interpolate(method="linear")
)

# Conversion gaz m³ → kWh si nécessaire
# 1 m³ de gaz naturel ≈ 11.6 kWh (pouvoir calorifique inférieur)
# df["conso_gaz_kwh"] = df["conso_gaz_m3"] * 11.6

# Contrôle des valeurs aberrantes sur la surface
q01 = df["surface_m2"].quantile(0.01)
q99 = df["surface_m2"].quantile(0.99)
df = df[(df["surface_m2"] >= q01) & (df["surface_m2"] <= q99)]
```

> **IQR (Interquartile Range) :** écart entre le 25e et le 75e percentile d'une distribution. On l'utilise pour définir des bornes au-delà desquelles une valeur est considérée comme aberrante. Les bornes courantes sont : Q1 - 1,5 × IQR et Q3 + 1,5 × IQR.

### Étape 4 : Création des variables dérivées

```python
# Indicateur de Performance Énergétique (IEP) en kWh/m²
df["iep_kwh_m2"] = df["conso_totale_kwh"] / df["surface_m2"]

# IEP corrigé du climat (si DJC disponible)
df["iep_kwh_m2_djc"] = np.where(
    df["djc_mois"] > 0,
    df["conso_totale_kwh"] / (df["surface_m2"] * df["djc_mois"]),
    np.nan
)

# Extraction de la période
df["annee"] = df["date_mesure"].dt.year
df["mois"] = df["date_mesure"].dt.month

# Âge du bâtiment
df["age_batiment"] = 2026 - df["annee_construction"]

# Variation mensuelle (détection de dérives)
df = df.sort_values(["id_batiment", "date_mesure"])
df["variation_conso"] = df.groupby("id_batiment")["conso_totale_kwh"].pct_change()
```

### Étape 5 : Normalisation (StandardScaler)

> **StandardScaler :** méthode qui transforme chaque variable pour qu'elle ait une moyenne de 0 et un écart-type de 1. Cela permet de comparer des variables qui n'ont pas les mêmes unités (kWh, m², °C). Sans cela, une variable avec de grands chiffres dominerait artificiellement les calculs.

```python
from sklearn.preprocessing import StandardScaler

# Variables numériques à normaliser pour la modélisation
features = ["iep_kwh_m2", "age_batiment", "surface_m2", "temp_ext_moy_c"]

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[features].dropna())
df_scaled = pd.DataFrame(df_scaled, columns=features)
```

> **Erreur fréquente :** Appliquer le StandardScaler sur tout le jeu de données avant la séparation train/test. Le scaler doit être ajusté UNIQUEMENT sur les données d'entraînement, puis appliqué sur les données de test. Sinon, il y a une "fuite de données" (data leakage).

---
## 8. MÉTHODES, MODÈLES ET OUTILS

### A. Méthodes descriptives et comparatives

**Benchmark par type d'usage :**
- Calcul des médianes de consommation par type de bâtiment
- Identification des bâtiments au-dessus de la médiane + 1,5 × IQR

```python
# Médiane de l'IEP par type d'usage
mediane_iep = df.groupby("type_usage")["iep_kwh_m2"].median()
df["mediane_ref"] = df["type_usage"].map(mediane_iep)
df["ecart_reference"] = df["iep_kwh_m2"] - df["mediane_ref"]
df["sur_consommateur"] = df["ecart_reference"] > 0
```

### B. Méthodes statistiques — Détection par score Z

> **Score Z (Z-score) :** mesure qui indique à combien d'écarts-types une valeur se trouve de la moyenne. Un score Z > 2 ou < -2 signale généralement une valeur inhabituelle.

```python
from scipy import stats

# Score Z sur l'IEP par type d'usage
df["z_score_iep"] = df.groupby("type_usage")["iep_kwh_m2"].transform(
    lambda x: stats.zscore(x, nan_policy="omit")
)

# Flaguer les bâtiments anormaux
df["anomalie_zscore"] = df["z_score_iep"].abs() > 2
```

### C. Régression linéaire — Explication de la consommation

> **Régression linéaire :** méthode qui cherche à expliquer une variable (consommation) par d'autres variables (surface, âge, température). Elle donne des coefficients qui indiquent l'impact de chaque facteur.

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

# Préparation
df_reg = df.dropna(subset=["iep_kwh_m2", "age_batiment", "djc_mois"])

X = df_reg[["age_batiment", "djc_mois", "surface_m2", "taux_occupation"]]
y = df_reg["iep_kwh_m2"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"R² : {r2_score(y_test, y_pred):.3f}")
print(f"MAE : {mean_absolute_error(y_test, y_pred):.1f} kWh/m²")

# Importance des variables
coeff_df = pd.DataFrame({
    "variable": X.columns,
    "coefficient": model.coef_
}).sort_values("coefficient", ascending=False)
print(coeff_df)
```

> **R² (R-carré) :** mesure de la qualité d'un modèle de régression. Un R² de 0,80 signifie que le modèle explique 80 % de la variabilité de la consommation. Un R² de 1,0 serait parfait.

> **MAE (Mean Absolute Error — Erreur Absolue Moyenne) :** écart moyen entre la valeur prédite et la valeur réelle. Si la MAE est de 15 kWh/m², le modèle se trompe en moyenne de 15 kWh/m².

### D. Random Forest — Modèle plus robuste et importance des variables

> **Random Forest (Forêt Aléatoire) :** ensemble de nombreux arbres de décision entraînés sur des sous-ensembles aléatoires des données. La prédiction finale est la moyenne de tous les arbres. Ce modèle est plus robuste aux valeurs aberrantes et aux relations non-linéaires.

```python
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

y_pred_rf = rf.predict(X_test)
print(f"R² Random Forest : {r2_score(y_test, y_pred_rf):.3f}")

# Importance des variables
importances = pd.DataFrame({
    "variable": X.columns,
    "importance": rf.feature_importances_
}).sort_values("importance", ascending=False)
print(importances)
```

### E. Segmentation des bâtiments — KMeans

> **KMeans (K-moyennes) :** algorithme qui regroupe automatiquement des objets similaires en K groupes (clusters). On choisit K à l'avance. L'algorithme cherche à minimiser la distance entre les objets et le centre de leur groupe.

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

features_cluster = ["iep_kwh_m2", "age_batiment", "surface_m2"]
df_cluster = df[features_cluster].dropna()

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_cluster)

# Trouver le bon nombre de clusters avec la méthode du coude
inertias = []
for k in range(2, 10):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(df_scaled)
    inertias.append(km.inertia_)

plt.plot(range(2, 10), inertias, marker="o")
plt.xlabel("Nombre de clusters K")
plt.ylabel("Inertie")
plt.title("Méthode du coude — Choix de K")
plt.savefig("figures/coude_kmeans.png")

# Application avec K=4 (hypothèse)
km = KMeans(n_clusters=4, random_state=42, n_init=10)
df_cluster["segment"] = km.fit_predict(df_scaled)
```

> **Méthode du coude (Elbow Method) :** technique graphique pour choisir le nombre optimal de clusters. On cherche le point où la courbe d'inertie "fait un coude", c'est-à-dire où l'ajout d'un cluster supplémentaire n'améliore plus beaucoup la qualité du regroupement.

---
## 9. DÉMARCHE ÉTAPE PAR ÉTAPE

### Vue d'ensemble

```
ÉTAPE 1 : Chargement et diagnostic qualité
    ↓
ÉTAPE 2 : Nettoyage et préparation
    ↓
ÉTAPE 3 : Analyse exploratoire (EDA)
    ↓
ÉTAPE 4 : Calcul des indicateurs de performance (IEP)
    ↓
ÉTAPE 5 : Comparaison et benchmark
    ↓
ÉTAPE 6 : Détection des bâtiments énergivores
    ↓
ÉTAPE 7 : Analyse des causes (régression)
    ↓
ÉTAPE 8 : Segmentation (clustering)
    ↓
ÉTAPE 9 : Priorisation et scoring
    ↓
ÉTAPE 10 : Visualisation et dashboard
    ↓
ÉTAPE 11 : Restitution aux métiers
```

### Détail de chaque étape

**ÉTAPE 1 — Chargement et diagnostic qualité (30 min)**
- Charger les fichiers CSV/Excel
- Vérifier les dimensions du jeu de données
- Identifier les valeurs manquantes, doublons, types incohérents
- Produire un rapport qualité initial

**ÉTAPE 2 — Nettoyage et préparation (1-2 h)**
- Supprimer les doublons
- Traiter les valeurs manquantes (exclusion ou interpolation)
- Corriger les unités (m³ gaz → kWh)
- Créer les variables dérivées (IEP, âge, variation)
- Normaliser pour la modélisation

**ÉTAPE 3 — Analyse exploratoire (EDA) (2-3 h)**

> **EDA (Exploratory Data Analysis — Analyse Exploratoire des Données) :** phase d'exploration visuelle et statistique des données avant toute modélisation. L'objectif est de comprendre les données, détecter les anomalies, comprendre les distributions et les relations entre variables.

```python
# Distribution de l'IEP
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].hist(df["iep_kwh_m2"].dropna(), bins=50, edgecolor="white")
axes[0].set_title("Distribution de l'IEP (kWh/m²)")
axes[0].set_xlabel("kWh/m²")

# Boîte à moustaches par type d'usage
df.boxplot(column="iep_kwh_m2", by="type_usage", ax=axes[1])
axes[1].set_title("IEP par type d'usage")

plt.savefig("figures/eda_iep.png", dpi=150, bbox_inches="tight")
```

> **Boîte à moustaches (Boxplot) :** graphique qui résume la distribution d'une variable : la boîte centrale représente les 50 % centraux des données, les moustaches s'étendent vers les valeurs extrêmes, et les points isolés représentent des valeurs potentiellement aberrantes.

**ÉTAPE 4 — Calcul des indicateurs de performance (1 h)**
- Calculer l'IEP en kWh/m² pour chaque bâtiment et chaque mois
- Calculer l'IEP corrigé du climat (kWh/m²/DJC)
- Calculer la consommation annuelle consolidée
- Comparer aux références réglementaires (décret tertiaire)

**ÉTAPE 5 — Comparaison et benchmark (1-2 h)**
- Calculer la médiane par type d'usage
- Identifier les bâtiments au-dessus de la médiane
- Comparer aux valeurs de référence réglementaires
- Créer un classement des bâtiments du moins au plus performant

```python
# Classement des bâtiments par IEP annuel moyen
iep_annuel = df.groupby(["id_batiment", "type_usage"])["iep_kwh_m2"].mean().reset_index()
iep_annuel = iep_annuel.sort_values("iep_kwh_m2", ascending=False)
iep_annuel["rang"] = range(1, len(iep_annuel) + 1)
```

**ÉTAPE 6 — Détection des bâtiments énergivores (1 h)**
- Appliquer le score Z par type d'usage
- Identifier les bâtiments avec Z > 2
- Identifier les dérives temporelles (hausse de consommation inexpliquée)
- Créer un flag "alerte énergie"

**ÉTAPE 7 — Analyse des causes par régression (2-3 h)**
- Régression linéaire : quels facteurs expliquent la consommation ?
- Random Forest : quelles variables sont les plus importantes ?
- Résidus de régression : les bâtiments qui consomment plus que prévu par le modèle

> **Résidu de régression :** différence entre la valeur réelle et la valeur prédite par le modèle. Un résidu positif signifie que le bâtiment consomme plus que ce que le modèle attendrait étant donné ses caractéristiques. Cela indique un problème potentiel.

**ÉTAPE 8 — Segmentation KMeans (1-2 h)**
- Regrouper les bâtiments en segments homogènes
- Interpréter chaque segment (performants, moyens, énergivores, très vieux)
- Associer des recommandations par segment

**ÉTAPE 9 — Priorisation et scoring (1 h)**
```python
# Score de priorité combinant plusieurs critères
df_priorite = df.groupby("id_batiment").agg({
    "iep_kwh_m2": "mean",
    "surface_m2": "first",
    "ecart_reference": "mean",
    "age_batiment": "first"
}).reset_index()

# Normalisation des scores (0 à 1) pour chaque critère
from sklearn.preprocessing import MinMaxScaler

scaler_min = MinMaxScaler()
df_priorite["score_iep"] = scaler_min.fit_transform(df_priorite[["iep_kwh_m2"]])
df_priorite["score_surface"] = scaler_min.fit_transform(df_priorite[["surface_m2"]])
df_priorite["score_age"] = scaler_min.fit_transform(df_priorite[["age_batiment"]])

# Score global pondéré
df_priorite["score_priorite"] = (
    0.5 * df_priorite["score_iep"] +
    0.3 * df_priorite["score_surface"] +
    0.2 * df_priorite["score_age"]
)

df_priorite = df_priorite.sort_values("score_priorite", ascending=False)
```

**ÉTAPE 10 — Visualisation et dashboard (2-4 h)**
- Graphiques Python pour le notebook
- Export des données pour Power BI
- Création du dashboard interactif

**ÉTAPE 11 — Restitution aux métiers (présentation)**
- Synthèse des bâtiments prioritaires
- Plan d'action recommandé
- Indicateurs de suivi

---
## 10. MÉTRIQUES UTILISÉES

### Tableau complet des métriques

| Métrique | Formule | Définition simple | Utilité | Limite | Interprétation métier |
|---------|---------|-------------------|---------|--------|----------------------|
| **IEP (kWh/m²)** | Conso / Surface | Consommation par mètre carré | Comparaison entre bâtiments | Ne tient pas compte du climat | Un bureau à 150 kWh/m²/an est dans la moyenne |
| **IEP climatisé (kWh/m²/DJC)** | Conso / (Surface × DJC) | IEP corrigé de la météo | Comparaison inter-annuelle | Complexe à expliquer | Permet de comparer 2020 (froid) et 2022 (chaud) |
| **Score Z** | (X - µ) / σ | Distance à la moyenne en écarts-types | Détection d'anomalies statistiques | Sensible aux outliers | Z > 2 : bâtiment suspect |
| **Écart à la référence** | IEP - Médiane_groupe | Différence par rapport au groupe | Benchmarking | Dépend de la qualité du groupe | +50 kWh/m² : sur-consommation de 50 kWh/m² |
| **R²** | Variance expliquée / Variance totale | Part de la variabilité expliquée par le modèle | Qualité de la régression | Ne dit pas si les coefficients sont corrects | R² = 0,75 : le modèle explique 75 % de la conso |
| **MAE (kWh/m²)** | Moyenne( |réel - prédit| ) | Erreur moyenne du modèle | Qualité de prédiction | Comparable à l'unité de la variable cible |
| **RMSE (kWh/m²)** | √Moyenne(réel - prédit)² | Erreur quadratique moyenne | Pénalise les grandes erreurs | Sensible aux outliers | RMSE > MAE signifie de grandes erreurs ponctuelles |
| **Silhouette Score** | Cohésion / Séparation | Qualité du clustering | Choix du nombre de clusters | Entre -1 et 1, difficile à interpréter | Score > 0,5 : clusters bien séparés |
| **Taux de sur-consommateurs** | % bâtiments > médiane + IQR | Part des bâtiments énergivores | Pilotage global | Dépend du seuil choisi | 20 % de sur-consommateurs = problème systémique |

> **RMSE (Root Mean Square Error — Racine de l'Erreur Quadratique Moyenne) :** comme la MAE, mais les erreurs sont élevées au carré avant d'être moyennées, puis on prend la racine. Cela pénalise plus les grandes erreurs que les petites.

### Métriques réglementaires

| Classe DPE | Seuil indicatif (tertiaire) | Objectif décret tertiaire 2030 |
|------------|----------------------------|-------------------------------|
| A | < 50 kWh/m²/an | Référence d'excellence |
| B | 50-90 kWh/m²/an | Objectif réaliste pour neuf |
| C | 90-150 kWh/m²/an | Standard actuel pour rénové |
| D | 150-230 kWh/m²/an | Amélioration nécessaire |
| E | 230-330 kWh/m²/an | Priorité de rénovation |
| F-G | > 330 kWh/m²/an | Urgence — passoire énergétique |

> **Passoire énergétique :** terme courant pour désigner les bâtiments classés F ou G au DPE, qui consomment beaucoup d'énergie et produisent beaucoup de CO₂.

---
## 11. RÉSULTATS ATTENDUS (SIMULÉS)

> **Rappel important :** Les chiffres ci-dessous sont entièrement simulés à titre pédagogique. Ils illustrent le type de résultats attendus dans un projet réel mais ne correspondent à aucune organisation réelle.

### Résultats de l'analyse descriptive (hypothétiques)

| Indicateur | Valeur simulée | Interprétation |
|-----------|----------------|----------------|
| Nombre de bâtiments analysés | 120 | Parc de taille moyenne |
| Période couverte | 2020-2025 | 5 ans de données |
| IEP médian du parc | 185 kWh/m²/an | Classe C-D |
| Bâtiments en classe E-F-G | 22 (18 %) | Priorité immédiate |
| Bâtiments en classe A-B | 15 (12 %) | Références du parc |
| Gain estimé (10 % des actions) | 12-15 % de la facture | ≈ 280 000 €/an (hypothétique) |

### Résultats de la régression

| Variable explicative | Coefficient (kWh/m²) | Signification |
|---------------------|---------------------|---------------|
| DJC (chauffage) | +2,3 kWh/m²/DJC | Forte sensibilité au froid |
| Âge du bâtiment | +1,8 kWh/m²/an | Vétusté = sur-consommation |
| Présence isolation | -45 kWh/m² | Impact fort de l'isolation |
| Type industriel | +85 kWh/m² | Procédés industriels énergivores |

*Hypothétique — R² = 0,72 pour la régression multiple*

### Top 5 bâtiments prioritaires (hypothétiques)

| Rang | Bâtiment (anonymisé) | IEP (kWh/m²) | Écart référence | Gain potentiel |
|------|----------------------|--------------|-----------------|----------------|
| 1 | BâtA-2203 | 520 kWh/m² | +285 kWh/m² | -55 % |
| 2 | BâtB-1187 | 415 kWh/m² | +230 kWh/m² | -45 % |
| 3 | BâtC-0892 | 380 kWh/m² | +195 kWh/m² | -40 % |
| 4 | BâtD-3341 | 350 kWh/m² | +165 kWh/m² | -35 % |
| 5 | BâtE-2765 | 320 kWh/m² | +135 kWh/m² | -30 % |

---
## 12. VALEUR MÉTIER

### Ce que le projet apporte concrètement

> **Décision métier rendue possible :** Sans ce projet, le gestionnaire de parc immobilier examine chaque bâtiment manuellement une fois par an. Avec ce projet, il dispose d'une alerte automatique dès qu'un bâtiment dévie de son profil normal, et d'un tableau de bord permettant de prioriser ses actions en quelques minutes.

| Valeur apportée | Avant | Après | Impact estimé |
|-----------------|-------|-------|---------------|
| Visibilité | Aucune (Excel dispersé) | Dashboard centralisé | Gain de temps : -70 % |
| Détection dérives | Manuel, annuel | Automatique, mensuel | Détection précoce : -6 mois |
| Priorisation | Intuitive | Basée sur les données | Meilleur ROI des investissements |
| Conformité | Déclaratif | Calculé automatiquement | Conformité décret tertiaire |
| Communication | Rapports statiques | Visualisations interactives | Meilleure adhésion des équipes |

> **ROI (Return on Investment — Retour sur Investissement) :** rapport entre le bénéfice généré par une action et son coût. Un ROI de 200 % signifie que l'action a rapporté 2 € pour chaque 1 € investi.

---
## 13. LIMITES DU PROJET

> **À retenir :** Présenter honnêtement les limites d'un projet est une marque de maturité professionnelle. Un Data Scientist qui ne cite pas les limites est soit débutant, soit commercial.

| Limite | Description | Impact | Mitigation possible |
|--------|-------------|--------|---------------------|
| **Qualité des compteurs** | Données manquantes, compteurs en panne | Bâtiments exclus de l'analyse | Compléter par les factures |
| **Surface inexacte** | Surface utile ≠ surface chauffée | IEP biaisé | Vérification terrain |
| **Correction climatique** | DJC ne capturent pas toutes les variations météo | Comparaison imparfaite | Utiliser des données météo détaillées |
| **Usage non documenté** | Horaires d'occupation, types d'activité | Comparaisons injustes | Enquête terrain |
| **Données historiques courtes** | < 3 ans de données | Tendances peu fiables | Attendre plus de données |
| **Causalité vs corrélation** | L'âge du bâtiment corrèle avec la conso, mais n'est pas la seule cause | Conclusions à nuancer | Analyses complémentaires |
| **Changements non déclarés** | Travaux, changement d'usage | Ruptures inexpliquées | Journal des interventions |
| **Coût des actions** | Le modèle ne calcule pas le coût des travaux | Priorisation incomplète | Données financières à intégrer |

> **Corrélation vs causalité :** deux variables peuvent évoluer ensemble (corrélation) sans que l'une soit la cause de l'autre (causalité). Par exemple, l'âge d'un bâtiment est corrélé à sa consommation, mais la vraie cause est souvent l'état de l'isolation, pas l'âge en lui-même.

---
## 14. AMÉLIORATIONS POSSIBLES

### Améliorations techniques

| Amélioration | Description | Difficulté | Impact attendu |
|-------------|-------------|------------|----------------|
| **Séries temporelles** | Modèle ARIMA/Prophet pour détecter les dérives automatiquement | Moyenne | Alertes plus précises |
| **Données météo détaillées** | Intégration température horaire, ensoleillement, vent | Faible | Meilleure correction climatique |
| **Données d'occupation** | Capteurs de présence, badges d'accès | Moyenne | Normalisation par occupant |
| **Dashboard Power BI** | Tableau de bord interactif avec filtres | Faible | Adoption par les équipes |
| **Scoring de criticité** | Note composite pondérant IEP, surface, coût travaux, ROI | Moyenne | Priorisation optimale |
| **API FastAPI** | Endpoint pour intégrer le modèle dans un SI existant | Élevée | Industrialisation |
| **MLflow** | Suivi des expériences et versionnement des modèles | Moyenne | Reproductibilité |
| **SHAP** | Explication des prédictions pour chaque bâtiment | Moyenne | Acceptabilité métier |
| **Application Streamlit** | Interface web simple pour les non-techniciens | Moyenne | Démocratisation |
| **Déploiement Docker** | Containerisation pour déploiement serveur | Élevée | Industrialisation |
| **Alertes email** | Notification automatique quand un bâtiment dépasse un seuil | Faible | Réactivité équipes |
| **Intégration SQL** | Pipeline automatique depuis une base de données | Moyenne | Automatisation |

> **ARIMA :** modèle statistique pour analyser et prévoir des séries temporelles. Il tient compte de la tendance, de la saisonnalité et des erreurs passées.

> **Prophet :** outil de prévision de séries temporelles développé par Meta (Facebook), conçu pour être robuste aux données manquantes et aux changements de tendance.

> **FastAPI :** framework Python pour créer des APIs web rapidement. Permet d'exposer un modèle Machine Learning comme un service accessible via internet.

> **MLflow :** plateforme open-source pour gérer le cycle de vie des modèles Machine Learning : enregistrement des expériences, comparaison des modèles, déploiement.

> **SHAP (SHapley Additive exPlanations) :** méthode mathématique pour expliquer la contribution de chaque variable à une prédiction individuelle. Permet de dire "pour ce bâtiment, la consommation élevée est due à 60 % à son âge et 40 % à son exposition climatique".

> **Streamlit :** bibliothèque Python qui permet de créer rapidement des applications web interactives à partir d'un script Python, sans connaître le développement web.

> **Docker :** outil qui permet d'empaqueter une application et toutes ses dépendances dans un conteneur portable, exécutable sur n'importe quel serveur.

---
## 15. ARCHITECTURE GITHUB RECOMMANDÉE

### Nom du dépôt

```
building-energy-efficiency-analytics
```

> **Dépôt (repository) :** espace de stockage sur GitHub qui contient tous les fichiers d'un projet, son historique de modifications et sa documentation.

### Structure des dossiers

```
building-energy-efficiency-analytics/
│
├── README.md                          ← Fichier LISEZ-MOI principal
├── requirements.txt                   ← Liste des bibliothèques Python nécessaires
├── .gitignore                         ← Fichiers à ne pas envoyer sur GitHub
├── LICENSE                            ← Licence d'utilisation du code
│
├── data_sample/                       ← Données d'exemple (simulées, anonymisées)
│   ├── batiments_energie_sample.csv   ← 100-200 lignes de données fictives
│   └── README_data.md                 ← Description des variables
│
├── notebooks/                         ← Analyses Jupyter pas-à-pas
│   ├── 01_exploration_donnees.ipynb   ← Chargement, qualité, EDA
│   ├── 02_indicateurs_iep.ipynb       ← Calcul des IEP et benchmark
│   ├── 03_detection_anomalies.ipynb   ← Score Z, outliers, alertes
│   ├── 04_regression_causes.ipynb     ← Régression et importance variables
│   ├── 05_segmentation_kmeans.ipynb   ← Clustering et segments
│   └── 06_scoring_priorite.ipynb      ← Score de priorité final
│
├── src/                               ← Code Python réutilisable
│   ├── __init__.py
│   ├── data/
│   │   ├── loader.py                  ← Chargement et validation des données
│   │   └── cleaner.py                 ← Nettoyage et préparation
│   ├── features/
│   │   ├── iep.py                     ← Calcul des indicateurs énergétiques
│   │   └── anomaly_flags.py           ← Détection et flagging des anomalies
│   ├── models/
│   │   ├── regression.py              ← Modèles de régression
│   │   ├── clustering.py              ← Segmentation KMeans
│   │   └── scoring.py                 ← Score de priorité
│   └── evaluation/
│       └── metrics.py                 ← Calcul et affichage des métriques
│
├── reports/                           ← Rapports et synthèses
│   ├── rapport_executive_summary.md   ← Synthèse pour décideurs
│   └── analyse_complete.md            ← Rapport technique complet
│
├── figures/                           ← Graphiques exportés
│   ├── eda_iep_distribution.png
│   ├── boxplot_par_usage.png
│   ├── heatmap_correlation.png
│   ├── coude_kmeans.png
│   ├── regression_importance.png
│   └── top10_batiments_prioritaires.png
│
├── dashboards/                        ← Fichiers Power BI ou Streamlit
│   ├── energy_dashboard.pbix          ← Dashboard Power BI
│   └── app.py                         ← Application Streamlit (optionnel)
│
└── docs/                              ← Documentation technique
    ├── methodologie.md                ← Explication de la démarche
    ├── glossaire.md                   ← Définitions des termes
    └── dictionnaire_donnees.md        ← Description des variables
```

### Explication de chaque dossier

| Dossier | Contenu | À quoi il sert | À ne PAS mettre | Risque évité |
|---------|---------|----------------|-----------------|--------------|
| `data_sample/` | Données fictives allégées | Permettre à quiconque de reproduire l'analyse | Données réelles, confidentielles, volumineuses | Fuite de données, problème RGPD |
| `notebooks/` | Notebooks Jupyter numérotés | Montrer la démarche pas-à-pas | Notebooks non nettoyés avec erreurs | Mauvaise image professionnelle |
| `src/` | Modules Python réutilisables | Code propre, testable, importable | Tout le code en vrac dans un seul fichier | Code illisible, non maintenable |
| `reports/` | Synthèses et rapports | Communication aux non-techniciens | Données brutes | Confusion entre données et conclusions |
| `figures/` | Images exportées des graphiques | Illustrer le README et les rapports | Fichiers temporaires, images personnelles | Dépôt encombré |
| `dashboards/` | Fichiers de visualisation | Démontrer la compétence BI | Fichiers trop lourds (> 25 MB) | Limite GitHub |
| `docs/` | Documentation technique | Référence pour les utilisateurs | Code source | Mélange documentation et implémentation |

> **Commit (Validation) :** action d'enregistrer une modification dans l'historique Git. Chaque commit a un message qui décrit ce qui a changé.

> **Push (Envoi) :** action d'envoyer les commits locaux vers GitHub pour les rendre visibles en ligne.

> **Branch (Branche) :** version parallèle du code qui permet de travailler sur une fonctionnalité sans modifier le code principal.

> **Pull Request (Demande de fusion) :** demande d'intégrer les modifications d'une branche dans la branche principale, avec possibilité de révision.

---
## 22. COMPÉTENCES DÉMONTRÉES

### Vue d'ensemble

| Compétence | Preuve dans le projet | Valeur pour l'entreprise | Phrase CV possible |
|-----------|----------------------|--------------------------|-------------------|
| **Python** | Scripts de chargement, nettoyage, modélisation, visualisation | Automatisation de l'analyse, gain de temps | "Développement de pipelines d'analyse en Python (pandas, scikit-learn)" |
| **pandas** | Manipulation des données, agrégations, variables dérivées | Traitement efficace de grands volumes | "Traitement et transformation de données tabulaires complexes avec pandas" |
| **scikit-learn** | StandardScaler, LinearRegression, RandomForest, KMeans | Modèles prêts à déployer, maintenables | "Modélisation ML avec scikit-learn : régression, clustering, preprocessing" |
| **Statistiques** | Score Z, IQR, corrélation, régression | Rigueur dans les conclusions | "Analyse statistique rigoureuse : distributions, corrélations, tests" |
| **Détection d'anomalies** | Score Z, outliers IQR, résidus de régression | Surveillance automatique du parc | "Détection de bâtiments énergivores par méthodes statistiques" |
| **Analyse énergétique** | IEP, DJC, DPE, benchmark réglementaire | Conformité décret tertiaire | "Calcul et analyse d'indicateurs de performance énergétique (IEP, DJC)" |
| **Régression** | Explication des facteurs, importance variables | Aide à la décision d'investissement | "Modélisation régressive pour identifier les leviers d'action énergétique" |
| **Clustering** | KMeans, segmentation du parc | Personnalisation des recommandations | "Segmentation de parc immobilier par KMeans pour prioriser les actions" |
| **Visualisation** | Histogrammes, boxplots, heatmaps, scatter plots | Communication aux non-techniciens | "Visualisation Python (matplotlib, seaborn) pour restitution métier" |
| **Power BI** | Dashboard interactif, filtres, alertes | Adoption par les équipes terrain | "Construction de dashboards Power BI pour le pilotage opérationnel" |
| **Interprétation métier** | Score de priorité, recommandations par segment | Lien entre technique et décision | "Traduction des résultats Data en recommandations opérationnelles" |
| **GitHub** | Structure professionnelle, README, versionnement | Reproductibilité, collaboration | "Organisation et publication de projets Data sur GitHub" |
| **Qualité des données** | Nettoyage, diagnostic, contrôle unités | Fiabilité des analyses | "Audit et nettoyage de données : valeurs manquantes, doublons, outliers" |
| **Communication** | Fiche projet, post LinkedIn, version entretien | Adoption par les décideurs | "Communication des analyses à des publics techniques et non-techniques" |
| **Industrialisation** | Structure src/, modules réutilisables, requirements.txt | Passage en production | "Structuration de code Python en modules réutilisables et déployables" |
---

## Contact & Liens

**TSAGUE EMMANUEL** - Data Scientist

| | |
|---|---|
| Email | [emmatsague@yahoo.fr](mailto:emmatsague@yahoo.fr) |
| GitHub | [github.com/TSAGUE25](https://github.com/TSAGUE25) |
| Formation | Datascientest 2024 |
| Experience | EDF MAD EDVANCE |
| Domaines | Machine Learning - Data Analysis - Energie |

---

> Toutes les donnees de ce depot sont simulees et anonymisees.  
> Aucune donnee reelle ou confidentielle n'est presente.
