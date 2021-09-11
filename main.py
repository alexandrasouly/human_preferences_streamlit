import argparse
import cv2
import minerl
import numpy as np
import plotly.express as px
import random
import streamlit as st
from pathlib import Path

import time



#TODO
# What is input preferences?

def run_app(preferences= None):
    st.set_page_config(page_title="Human preferences user interface", page_icon=None, layout='wide')
    st.title("Human preferences user interface")

    instructions = st.container()
    left, right= st.columns(2)
    ask_for_new = st.container()

    with instructions:
        st.write("Instructions how to pick traj")


    with left:

         # # Display GIF / video
        # st.write("## Playback")
        # st.write(str(Path(chosen_path) / "recording.mp4"))
        # st.image(str(Path(chosen_path) / "recording.mp4"))
        # Select trajectory
        st.write("here goes the video")
        choose_left = st.button(
            'Left is better', key = "left")

    with right:

         # # Display GIF / video
        # st.write("## Playback")
        # st.write(str(Path(chosen_path) / "recording.mp4"))
        # st.image(str(Path(chosen_path) / "recording.mp4"))
        # Select trajectory
        st.write("here goes the video")
        choose_right = st.button(
            'Left is better', key = "right")
    
    with ask_for_new:
        choose_left = st.button(
            'Cannot decide, give me a new one!')


if __name__ == '__main__':
    run_app()