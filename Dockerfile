# Dockerfile corregido
FROM python:3.11

# Establecer directorio de trabajo
WORKDIR /webapp

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY . .

# Exponer puerto
EXPOSE 8501

# Configurar Streamlit para aceptar conexiones externas
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_HEADLESS=true

# Comando corregido para ejecutar la aplicación
CMD ["streamlit", "run", "app/home.py", "--server.address", "0.0.0.0", "--server.port", "8501"]