import streamlit as st

from components.header import *
from components.footer import *
from content.utils import *

from src.config import KAGGLE_DATASETS, KAGGLE_USERNAME

header_basic()

st.set_page_config(
    page_title="Datasets",
    page_icon="📊",
)

#content = load_markdown_content("app/content/info/datasets_info.md")
st.markdown(load_markdown_content("app/content/info/datasets_info.md"))

for dataset in KAGGLE_DATASETS:
    if st.button(f"📊 {dataset.title()}", key=f"btn_{dataset}"):
        st.success(f"""
                ### {dataset}
                Este dataset contiene datos relacionados con {dataset}.
                
                Número de archivos: Esta es una prueba
                
                Puedes descargarlo desde [Kaggle](https://www.kaggle.com/datasets/{KAGGLE_USERNAME}/{dataset}).
                """)
        
footer_contact()