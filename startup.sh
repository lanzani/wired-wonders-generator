#!/bin/bash

apt-get install xvfb

pip install --upgrade pip
pip install -r requirements.txt


xvfb-run streamlit run app/Home.py
