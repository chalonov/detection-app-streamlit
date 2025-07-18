import streamlit as st

from src.config import APP_AUTHOR_MAIL, APP_DATE, APP_VERSION, APP_AUTHOR_GITHUB

def footer_contact():
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Contacto**")
        st.markdown(f"📧 {APP_AUTHOR_MAIL}")
        st.markdown(f"🐱 [GitHub]({APP_AUTHOR_GITHUB})")
    
    with col2:
        st.markdown("**Recursos**")
        st.markdown("📊 [Documentación](https://docs.ejemplo.com)")
        st.markdown("🔧 [API](https://api.ejemplo.com)")
    
    st.markdown(
        "<div style='text-align: center; color: gray; font-size: 12px; margin-top: 20px;'>"
        f"© {APP_DATE} Todos los derechos reservados | Versión {APP_VERSION} | Streamlit"
        "</div>", 
        unsafe_allow_html=True
    )
    
def sidebar_footer():
    with st.sidebar:        
        st.markdown(
            f"""
            <div style='text-align: center; font-size: 10px; color: gray;'>
                © 2025 Tu App<br>
                Versión {APP_VERSION}<br>
                <a href="https://github.com/tu-repo" target="_blank">GitHub</a>
            </div>
            """, 
            unsafe_allow_html=True
        )