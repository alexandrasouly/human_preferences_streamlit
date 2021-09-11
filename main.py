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

def run_app(videos_folder= None):
    st.set_page_config(page_title="Human preferences user interface", page_icon=None, layout='wide')
    st.title("Human preferences user interface")

    instructions = st.container()
    left, right= st.columns(2)
    ask_for_new = st.container()

    with instructions:
        st.write("Instructions how to pick traj")

    # check folder for videos
    # videos will names as ids, same as in table
    # do pre-populated database in previous step that doesn't have the choices yet
    # load the pair vids from the database
    # https://towardsdatascience.com/python-has-a-built-in-database-heres-how-to-use-it-47826c10648a

    with left:

         # # Display GIF / video
        # st.write("## Playback")
        # st.write(str(Path(chosen_path) / "recording.mp4"))
        # st.image(str(Path(chosen_path) / "recording.mp4"))
        # https://docs.streamlit.io/en/0.66.0/api.html#streamlit.video
        # do't try with minerl videos

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

    # add choice to sql database that stores ids

if __name__ == '__main__':
    run_app()