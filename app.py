# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 22:52:13 2022

@author: Administrator
"""
   
import streamlit as st
import numpy as np
import pandas as pd
from datetime import date


today = date.today()

st.set_page_config(
    page_title="商道绿色债券查询",
    layout='wide',
    initial_sidebar_state='auto',
)

########################################################
main_selectbox = st.sidebar.selectbox('查询项目',
    ('Apple', 'Orange', 'Banana')
)

st.sidebar.markdown("***")
st.sidebar.markdown("### 遵循准则 ")
sidebar_selection_1 = st.sidebar.checkbox(
    '绿色产业目录',
)
sidebar_selection_2 = st.sidebar.checkbox(
    '绿色债券支持项目目录',
)
sidebar_selection_3 = st.sidebar.checkbox(
    '节能环保清洁产业统计分类',
)
sidebar_selection_4 = st.sidebar.checkbox(
    '国民经济行业',
)
st.sidebar.markdown("***")
sidebar_slider = st.sidebar.slider("报告显示数量",
    1, 10, (5)
)

st.sidebar.markdown("***")
st.sidebar.button('查询')
#######################################################

t1, t2 = st.columns(2)
with t1:
    st.header('绿色债券识别')

with t2:
    st.write("")
    st.write("")
    st.write("""
    **商道融绿** | Syntao Green Finance
    """)

st.write("")
st.markdown("""
通过输入产品、债券名称，得到相关准则信息
""")
st.markdown("***")
length=""
st.write('该项目共有',length,'条记录')
st.markdown("***")
st.markdown("""对应报告如下：""")


