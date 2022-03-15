# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 22:52:13 2022

@author: Administrator
"""
   

import streamlit as st
import numpy as np
import pandas as pd
from datetime import date
import os


today = date.today()

st.set_page_config(
    page_title="商道绿色债券查询",
    layout='wide',
    initial_sidebar_state='auto',
)


#def get_data(url):
    #products_gl = 'https://github.com/IronK77/green-identifier/blob/f227f60d7fcb21a5a7b0e2992daa61ecd89ec6fa/product-guideline.csv'
    #reports_gl = 'https://github.com/IronK77/green-identifier/blob/f227f60d7fcb21a5a7b0e2992daa61ecd89ec6fa/report-guideline.csv'
#    reports = pd.read_csv(url)
#    return reports

########################################################
products = pd.read_csv("product-guideline.csv",encoding='gbk')
p_name=products.name_product.unique().tolist()
    
main_product=st.sidebar.selectbox('查询项目',p_name)
st.sidebar.markdown("***")
st.sidebar.markdown("### 遵循准则 ")
sidebar_selection_1 = st.sidebar. checkbox(
    '绿色产业目录',)
sidebar_selection_2 = st.sidebar.checkbox(
    '绿色债券支持项目目录',)
sidebar_selection_3 = st.sidebar.checkbox(
    '节能环保清洁产业统计分类',)
sidebar_selection_4 = st.sidebar.checkbox(
    '国民经济行业',)
st.sidebar.markdown("***")
sidebar_slider = st.sidebar.slider("报告显示数量",
    1, 10, (5)
)

st.sidebar.markdown("***")
st.sidebar.button('查询')
#######################################################
reports = pd.read_csv("report-guideline.csv",encoding='gbk')

t1, t2 = st.columns(2)
with t1:
    st.header('绿色债券识别')
    st.markdown("""
        通过输入产品、债券名称，得到相关准则信息
    """)
with t2:
    st.write("")
    st.write("")
    st.write("""
    **商道融绿** | Syntao Green Finance
    """)

st.write("")
st.markdown("***")
length=""
st.write(f"目前选择的产品/项目是 **{main_product}**")

st.write('该项目共有',length,'条记录')
st.markdown("***")
st.markdown("""对应报告如下：""")


