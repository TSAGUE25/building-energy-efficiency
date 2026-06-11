import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

try:
    from xgboost import XGBRegressor
    XGB_AVAILABLE = True
except ImportError:
    XGB_AVAILABLE = False

NUM_FEATURES = ['surface_m2', 'nb_etages', 'annee_construction',
                'occupation_h_j', 'altitude_m']
OHE_FEATURES = ['type_batiment', 'chauffage', 'orientation']
ORD_FEATURES = ['isolation', 'vitrage']
ISO_CATS     = [['faible', 'moyen', 'fort', 'tres_fort']]
VIT_CATS     = [['simple', 'double', 'triple']]

TARGET = 'conso_kwh_m2'


def build_preprocessor():
    return ColumnTransformer([
        ('num', StandardScaler(), NUM_FEATURES),
        ('ohe', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'),
         OHE_FEATURES),
        ('ord', OrdinalEncoder(categories=ISO_CATS + VIT_CATS), ORD_FEATURES),
    ])


def build_pipeline(model_name='xgb'):
    pre = build_preprocessor()
    if model_name == 'xgb' and XGB_AVAILABLE:
        model = XGBRegressor(n_estimators=200, max_depth=5, learning_rate=0.1,
                             random_state=42, verbosity=0)
    elif model_name == 'rf':
        model = RandomForestRegressor(n_estimators=200, max_depth=10,
                                      random_state=42, n_jobs=-1)
    elif model_name == 'gbm':
        model = GradientBoostingRegressor(n_estimators=200, max_depth=4,
                                          learning_rate=0.1, random_state=42)
    else:
        model = Ridge(alpha=10.0)
    return Pipeline([('preprocessor', pre), ('model', model)])


def compare_models(X_train, y_train, cv=5):
    kf = KFold(n_splits=cv, shuffle=True, random_state=42)
    results = {}
    for name in ['ridge', 'rf', 'gbm']:
        scores = cross_val_score(build_pipeline(name), X_train, y_train,
                                 cv=kf, scoring='r2')
        results[name] = {'R2_mean': scores.mean(), 'R2_std': scores.std()}
    if XGB_AVAILABLE:
        scores = cross_val_score(build_pipeline('xgb'), X_train, y_train,
                                 cv=kf, scoring='r2')
        results['xgb'] = {'R2_mean': scores.mean(), 'R2_std': scores.std()}
    df = pd.DataFrame(results).T.sort_values('R2_mean', ascending=False)
    print(df.round(4))
    return df


def evaluate_model(pipeline, X_test, y_test):
    y_pred = pipeline.predict(X_test)
    mae  = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2   = r2_score(y_test, y_pred)
    print(f'MAE  = {mae:.2f} kWh/m²\nRMSE = {rmse:.2f} kWh/m²\nR²   = {r2:.4f}')
    return dict(mae=mae, rmse=rmse, r2=r2, y_pred=y_pred)


def plot_dpe_distribution(df):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    colors = {'A': '#00b050', 'B': '#92d050', 'C': '#ffff00',
              'D': '#ffc000', 'E': '#ff6600', 'F': '#ff0000', 'G': '#c00000'}
    counts = df['label_dpe'].value_counts().sort_index()
    bar_colors = [colors.get(l, 'grey') for l in counts.index]
    ax1.bar(counts.index, counts.values, color=bar_colors, edgecolor='white')
    ax1.set_title('Distribution des labels DPE'); ax1.set_xlabel('Classe')

    df['conso_kwh_m2'].hist(ax=ax2, bins=50, color='#2196F3', edgecolor='white')
    ax2.set_xlabel('Consommation (kWh/m²/an)'); ax2.set_title('Distribution consommation')

    plt.suptitle('Efficacité énergétique — Vue d\'ensemble', fontweight='bold')
    plt.tight_layout(); plt.show()


def plot_feature_importance(pipeline, top_n=12):
    model = pipeline.named_steps['model']
    pre   = pipeline.named_steps['preprocessor']
    ohe_names = list(pre.named_transformers_['ohe'].get_feature_names_out(OHE_FEATURES))
    all_names = NUM_FEATURES + ohe_names + ORD_FEATURES

    if hasattr(model, 'feature_importances_'):
        imp = model.feature_importances_
    elif hasattr(model, 'coef_'):
        imp = np.abs(model.coef_)
    else:
        return

    idx = np.argsort(imp)[-top_n:]
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.barh([all_names[i] for i in idx], imp[idx], color='#FF9800')
    ax.set_title('Importance des variables — Consommation énergétique', fontweight='bold')
    plt.tight_layout(); plt.show()
