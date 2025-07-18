import streamlit as st
from PIL import Image
import os
from datetime import datetime

def custom_camera_component():
    st.markdown("### 🎥 Cámara Web")
    
    # HTML y JavaScript personalizado
    camera_html = """
    <div style="text-align: center; padding: 20px;">
        <video id="video" width="400" height="300" autoplay style="border: 2px solid #ddd; border-radius: 10px;"></video>
        <br><br>
        <button onclick="startCamera()" style="padding: 10px 20px; margin: 5px; background: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">
            📹 Encender Cámara
        </button>
        <button onclick="capturePhoto()" style="padding: 10px 20px; margin: 5px; background: #2196F3; color: white; border: none; border-radius: 5px; cursor: pointer;">
            📸 Capturar
        </button>
        <button onclick="stopCamera()" style="padding: 10px 20px; margin: 5px; background: #f44336; color: white; border: none; border-radius: 5px; cursor: pointer;">
            ⏹️ Apagar
        </button>
        <br><br>
        <canvas id="canvas" width="400" height="300" style="display: none;"></canvas>
        <img id="capturedImage" style="max-width: 400px; border: 2px solid #ddd; border-radius: 10px; display: none;">
    </div>
    
    <script>
    let stream = null;
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const capturedImage = document.getElementById('capturedImage');
    
    async function startCamera() {
        try {
            stream = await navigator.mediaDevices.getUserMedia({ 
                video: { width: 400, height: 300 } 
            });
            video.srcObject = stream;
            video.style.display = 'block';
        } catch (err) {
            alert('Error al acceder a la cámara: ' + err.message);
        }
    }
    
    function capturePhoto() {
        if (stream) {
            const context = canvas.getContext('2d');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            context.drawImage(video, 0, 0);
            
            const imageData = canvas.toDataURL('image/png');
            capturedImage.src = imageData;
            capturedImage.style.display = 'block';
            
            // Enviar imagen a Streamlit (esto requiere más configuración)
            console.log('Imagen capturada:', imageData);
        }
    }
    
    function stopCamera() {
        if (stream) {
            stream.getTracks().forEach(track => track.stop());
            video.style.display = 'none';
            video.srcObject = null;
            stream = null;
        }
    }
    </script>
    """
    # Mostrar el componente
    st.components.v1.html(camera_html, height=600)
    
    # Nota importante
    st.info("💡 **Nota:** Este componente requiere permisos de cámara del navegador.")
