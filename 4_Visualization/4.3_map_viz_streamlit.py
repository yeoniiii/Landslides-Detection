# ---- Libraries ----
import streamlit as st
import numpy as np
import pandas as pd


# ---- Title ----
st.title('⛰️ 산사태 감지 지도')
st.markdown('##### AI 학습기반 산사태 예측 및 실시간 대응 시스템 아이디어')
st.caption('2023 KETI 고려대 AI 융합∙응용기술 아이디어 경진대회')


# ---- Map ----
map_data = pd.read_csv('./longlat_coordinates.csv')

st.subheader('제천시 산사태 감지 지도') # 지도 제목
st.map(map_data, size=400) # 지도 생성
