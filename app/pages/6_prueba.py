import streamlit as st

from components.header import *
from components.footer import *
from components.webcam import custom_camera_component

header_basic()

custom_camera_component()

footer_contact()