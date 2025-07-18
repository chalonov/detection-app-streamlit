import os
from pathlib import Path

# ===== CONFIGURACIÓN BASE =====
BASE_DIR = str(Path(__file__).parent.parent.parent)  # Dos niveles antes del archivo actual

# ===== CONFIGURACIÓN DE APLICACIÓN =====
APP_NAME = "Bio-lense"
APP_REPO_NAME = "violence-detection-app"
APP_VERSION = "1.0.0"
APP_REPO = "https://github.com/chalonov/violence-detection-app"
APP_DESCRIPTION = "App para la detección de violencia en videos utilizando modelos de aprendizaje profundo y algoritmos bioinspirados."
APP_AUTHOR = "Gonzalo Novoa"
APP_AUTHOR_MAIL = "chalonovcoder@gmail.com"
APP_AUTHOR_GITHUB = "https://github.com/chalonov"
APP_DATE = "2025"

# ===== DATASETS A DESCARGAR =====
KAGGLE_USERNAME = "chalonovcoder"
KAGGLE_DATASETS = [
    'hockey',
    'movies',
]

# ===== RUTAS Y DIRECTORIOS =====
PROJECT_NAME = "project"
PROJECT_DIR = os.path.join(BASE_DIR, PROJECT_NAME)
DATA_DIR = os.path.join(PROJECT_DIR, 'datasets')
MODELS_DIR = os.path.join(PROJECT_DIR, 'models')
RESULTS_DIR = os.path.join(PROJECT_DIR, 'results')