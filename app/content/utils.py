import streamlit as st

def load_markdown_content(file_path):
    """Carga contenido desde archivo markdown"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        st.error(f"❌ Archivo no encontrado: {file_path}")
        return "Contenido no disponible"
    except Exception as e:
        st.error(f"❌ Error al cargar contenido: {e}")
        return "Error al cargar contenido"