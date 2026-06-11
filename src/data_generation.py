import numpy as np
import pandas as pd
from pathlib import Path


def generate_building_data(n=6000, seed=42):
    rng = np.random.default_rng(seed)

    type_batiment = rng.choice(['residentiel', 'bureau', 'commercial', 'industriel'], n,
                               p=[0.45, 0.25, 0.20, 0.10])
    isolation = rng.choice(['faible', 'moyen', 'fort', 'tres_fort'], n, p=[0.20, 0.35, 0.30, 0.15])
    vitrage   = rng.choice(['simple', 'double', 'triple'], n, p=[0.25, 0.55, 0.20])
    chauffage = rng.choice(['gaz', 'elec', 'pompe_chaleur', 'fioul', 'bois'], n,
                           p=[0.40, 0.25, 0.20, 0.10, 0.05])
    orientation = rng.choice(['N', 'S', 'E', 'O', 'NE', 'NO', 'SE', 'SO'], n)

    surface_m2       = np.clip(rng.lognormal(5.5, 0.7, n), 30, 5000).round(0)
    nb_etages        = rng.integers(1, 15, n)
    annee_construction = rng.integers(1920, 2024, n)
    occupation_h_j   = rng.integers(4, 24, n)
    altitude_m       = np.clip(rng.exponential(150, n), 0, 2000).round(0)

    iso_score = np.where(isolation == 'faible', 1.0,
                np.where(isolation == 'moyen',  0.7,
                np.where(isolation == 'fort',   0.5, 0.35)))
    vit_score = np.where(vitrage == 'simple', 1.2,
                np.where(vitrage == 'double', 1.0, 0.8))
    age_score  = (2024 - annee_construction) / 100 + 0.5
    orient_bonus = np.where(np.isin(orientation, ['S', 'SE', 'SO']), -0.08, 0.05)

    conso_kwh_m2 = (
        80 * iso_score * vit_score * age_score
        + 20 * (occupation_h_j / 12)
        + 5  * (altitude_m / 1000)
        + orient_bonus * 40
        + rng.normal(0, 10, n)
    )
    conso_kwh_m2 = np.clip(conso_kwh_m2, 20, 500).round(1)
    conso_totale_kwh = (conso_kwh_m2 * surface_m2).round(0)

    # Energy label (French DPE A-G)
    cuts  = [0, 50, 90, 150, 230, 330, 450, np.inf]
    labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    label_dpe = pd.cut(conso_kwh_m2, bins=cuts, labels=labels).astype(str)

    return pd.DataFrame({
        'surface_m2': surface_m2.astype(int),
        'nb_etages': nb_etages,
        'annee_construction': annee_construction,
        'occupation_h_j': occupation_h_j,
        'altitude_m': altitude_m.astype(int),
        'type_batiment': type_batiment,
        'isolation': isolation,
        'vitrage': vitrage,
        'chauffage': chauffage,
        'orientation': orientation,
        'conso_kwh_m2': conso_kwh_m2,
        'conso_totale_kwh': conso_totale_kwh.astype(int),
        'label_dpe': label_dpe,
    })


def load_or_generate(csv_path, n=6000, seed=42):
    path = Path(csv_path)
    if path.exists():
        return pd.read_csv(path)
    df = generate_building_data(n=n, seed=seed)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return df
