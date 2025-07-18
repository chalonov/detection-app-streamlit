import streamlit as st
from datetime import datetime

from src.config import APP_NAME, APP_VERSION

def header_basic():
    st.markdown(
        f"""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
            <h1 style='color: white; text-align: center; margin: 0;'>
                {APP_NAME}
            </h1>
        </div>
        """, 
        unsafe_allow_html=True
    )

def header_with_nav():
    # Banner principal
    st.markdown(
        f"""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div>
                    <h2 style='color: white; margin: 0;'>🕵🏻 {APP_NAME}</h2>
                    <p style='color: #e6f3ff; margin: 5px 0 0 0; font-size: 14px;'>
                        v{APP_VERSION} | Última actualización: 07/07/2025
                    </p>
                </div>
                <div style='color: white; text-align: right;'>
                    <p style='margin: 0; font-size: 12px;'>👤 Usuario Admin</p>
                    <p style='margin: 0; font-size: 12px;'>🕐 {datetime.now().strftime("%H:%M")}</p>
                </div>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Barra de navegación
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        if st.button("🏠 Inicio", use_container_width=True):
            st.switch_page("home.py")
    with col2:
        if st.button("📊 Datasets", use_container_width=True):
            st.switch_page("pages/1_datasets.py")
    with col3:
        if st.button("📈 Pre-procesamiento", use_container_width=True):
            st.switch_page("pages/2_preprocesamiento.py")
    with col4:
        if st.button("⚙️ Entrenamiento", use_container_width=True):
            st.switch_page("pages/3_entrenamiento.py")
    with col5:
        if st.button("📋 Resultados", use_container_width=True):
            st.switch_page("pages/4_resultados.py")
            
def header_with_metrics():
    # Header principal
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Aquí puedes agregar tu logo
        st.image("images/cctv-camera.png", width=100)
    
    with col2:
        st.markdown(f"""
            <div style='padding-top: 10px;'>
                <h1 style='margin: 0; color: #1f4e79;'>🕵🏻 {APP_NAME}</h1>
                <p style='margin: 5px 0; color: #666; font-size: 16px;'>
                    Descripcion chevere
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    # Métricas en el header
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📊 Datasets Activos", "25", "↗️ +3")
    with col2:
        st.metric("👥 Usuarios Conectados", "142", "↗️ +12")
    with col3:
        st.metric("⚡ Consultas/min", "1,234", "↘️ -5%")
    with col4:
        st.metric("💾 Almacenamiento", "78%", "↗️ +2%")
    
    st.markdown("---")
    
def header_minimal():
    st.markdown(
        """
        <style>
        .header-container {
            background: white;
            padding: 25px 0;
            border-bottom: 3px solid #f0f2f6;
            margin-bottom: 30px;
        }
        .header-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #262730;
            text-align: center;
            margin: 0;
        }
        .header-subtitle {
            font-size: 1.1rem;
            color: #808495;
            text-align: center;
            margin: 10px 0 0 0;
        }
        </style>
        
        <div class="header-container">
            <h1 class="header-title">📊 Bio-lenceWatch</h1>
            <p class="header-subtitle">Monitoreo seguro y ético</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
def header_with_breadcrumbs(current_page):
    # Header principal
    st.markdown(f"""
        <div style='background: #f8f9fa; padding: 15px; border-radius: 8px; 
                    border-left: 4px solid #007bff; margin-bottom: 20px;'>
            <h1 style='color: #212529; margin: 0;'>🕵🏻 {APP_NAME}</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # Breadcrumbs
    breadcrumbs = {
        "Home": "🏠",
        "Datasets": "📊", 
        "Analysis": "📈",
        "Reports": "📋"
    }
    
    breadcrumb_html = " > ".join([
        f"<span style='color: {'#007bff' if page == current_page else '#6c757d'};'>"
        f"{icon} {page}</span>"
        for page, icon in breadcrumbs.items()
    ])
    
    st.markdown(f"""
        <div style='background: white; padding: 10px 15px; border-radius: 5px; 
                    margin-bottom: 20px; font-size: 14px;'>
            Estás en: {breadcrumb_html}
        </div>
    """, unsafe_allow_html=True)
    
def header_dynamic(page_title, page_description, page_icon="📊"):
    st.markdown(
        f"""
        <div style='background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); 
                    padding: 25px; border-radius: 12px; margin-bottom: 25px;'>
            <div style='text-align: center;'>
                <div style='font-size: 3rem; margin-bottom: 10px;'>{page_icon}</div>
                <h1 style='color: white; margin: 0; font-size: 2.2rem;'>{page_title}</h1>
                <p style='color: #b8d4ff; margin: 10px 0 0 0; font-size: 1.1rem;'>
                    {page_description}
                </p>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )