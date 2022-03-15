# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 22:52:13 2022

@author: Administrator
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image

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
    image = Image.open('STGF_logo.png')
    st.image(image,width=320)
   #st.write("""
   #**商道融绿** | Syntao Green Finance
   #""")

st.write("")
st.markdown("***")
length=""
st.write(f"目前选择的产品/项目是 **{main_product}**")
st.markdown("***")
std=products.L3[products["name_product"]== main_product]
st.write("对应的目录条目为：")
st.write(f"绿色产业目录 **{std.to_string(index=False)}**")
st.write(f"绿色债券支持项目目录 **{std.to_string(index=False)}**")
st.markdown("***")
nrow=len(reports[reports["GL_code"]==std.to_string(index=False)])
st.write(f"该项目共有 {nrow} 条记录")
st.markdown("""对应报告如下：""")
data_selected=reports[["ID","report_name","type","GL_name"]][reports["GL_code"]==std.to_string(index=False)]
title=("债券代码","报告标题","报告类型","参考准则")

if len(data_selected)>0:
    fig = go.Figure(data=[go.Table(
        columnorder=[1,2,3,4],
        columnwidth=[150,900,200,350],
        header=dict(values=title,
                fill_color='rgba(79,162,134,0.3)',
                align='left'),
        cells=dict(values=[data_selected.ID, data_selected.report_name, data_selected.type,data_selected.GL_name],
               fill_color='rgba(217,160,72,0.6)',
               align='left'))
]   )
    fig.update_layout(
        margin=dict(l=0, r=20, t=20, b=20)
    )   
    st.write(fig)
else:
    st.info("报告库内当前无合适报告")