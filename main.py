import argparse
import cv2
import minerl
import numpy as np
import plotly.express as px
import random
import streamlit as st
from pathlib import Path
import sqlite3
from database import return_all_data, get_number_of_unrated_pairs, get_one_unrated_pair, rate_traj_pair, NoUnratedPair

import time


def run_app(videos_folder=None, database_name=None):
    st.set_page_config(page_title="Human preferences user interface", page_icon=None, layout='wide')
    st.title("Human preferences user interface")

    instructions = st.container()
    number_left = st.container()
    left, right= st.columns(2)
    ask_for_new = st.container()

    with instructions:
        st.write("Instructions:")
        st.write("Pick the video you prefer for now :)")



    # check folder for videos
    # videos will names as ids, same as in table
    # do pre-populated database in previous step that doesn't have the choices yet
    # load the pair vids from the database
    # https://towardsdatascience.com/python-has-a-built-in-database-heres-how-to-use-it-47826c10648a
    (left_id,right_id) = get_one_unrated_pair()

    with left:
        choose_left = st.button(
            'The left one is better', key = "left")
        if choose_left:
            rate_traj_pair(left_id, right_id, 1)
            (left_id,right_id) = get_one_unrated_pair()
    with right:
        choose_right = st.button(
            'The right one is better', key = "right")
        if choose_right:
            rate_traj_pair(left_id, right_id, 2)
            (left_id,right_id) = get_one_unrated_pair()
    with ask_for_new:
        undecided = st.button(
            'Cannot decide, give me a new one!')
        if undecided:
            rate_traj_pair(left_id, right_id, 3)
            (left_id,right_id) = get_one_unrated_pair()

    with left:
        st.write(f"Video file: {left_id}.mp4")
        left_path = Path(videos_folder, f"{left_id}.mp4")
        video_file = open(left_path, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    with right:
        st.write(f"Video file: {right_id}.mp4")
        right_path = Path(videos_folder, f"{right_id}.mp4")
        video_file = open(right_path, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    with number_left:
        conn = sqlite3.connect('trajectories.db') 
        c = conn.cursor()
        st.write(return_all_data())
        st.write(f"Trajectory pairs waiting to be rated: {get_number_of_unrated_pairs()}")



        #try:
         #   (left_id,right_id)=get_one_unrated_pair()
        #except NoUnratedPair:
         #   st.write("All pairs have been rated. Please check back later and refresh the page.")



            
    

if __name__ == '__main__':
    run_app(videos_folder="videos")