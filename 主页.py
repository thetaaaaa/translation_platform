# -*- encoding: utf-8 -*-
'''
Date:2023/03/06 21:47:10
Author:LinLitao
Description:基于streamlit的Web翻译平台
'''

import streamlit as st
import time

# 后端
def interface(lan):
    if lan=='cn':
        translated_result = '我是现代汉语翻译结果'
    if lan=='en':
        translated_result = '我是英语翻译结果'
    return translated_result


# '''前端'''
st.set_page_config(page_title='古汉语智能翻译平台', page_icon='🧊', layout='wide', initial_sidebar_state='auto', menu_items=None)
st.title('古汉语智能翻译平台')
st.caption(':blue[本翻译模型基于《四库全书》全文语料结合GPT模型训练而来]:sunglasses:')

# with st.echo():
    # st.write('This code will be printed')

# '''用户超参数'''
with st.sidebar.subheader("配置参数"):
    batch_size = st.sidebar.slider("batch_size", min_value=0, max_value=10, value=3)
    generate_max_len = st.sidebar.number_input("generate_max_len", min_value=0, max_value=64, value=32, step=1)
    repetition_penalty = st.sidebar.number_input("repetition_penalty", min_value=0.0, max_value=10.0, value=1.2,step=0.1)
    top_k = st.sidebar.slider("top_k", min_value=0, max_value=10, value=3, step=1)
    top_p = st.sidebar.number_input("top_p", min_value=0.0, max_value=1.0, value=0.95, step=0.01)


# '''正式交互界面'''
st.caption('选择翻译模型:')
tab1, tab2, tab3 = st.tabs(["AncientGPT", "SikuGPT", "SikuBERT-Unilm"])

with tab1:
    content = st.text_area("输入古汉语", max_chars=512, placeholder='请输入古汉语',key='c1', label_visibility='collapsed')

    begin_trans = st.button("开始翻译", key='begin_tran1')
    if begin_trans:
        # st.header("AncientGPT")
        display_cn = st.text_area('现代汉语翻译结果：',interface('cn'), placeholder='翻译',key='cn1')
        display_en = st.text_area('英语翻译结果：',interface('en'), placeholder='翻译',key='en1')

with tab2:
   content = st.text_area("输入古汉语", max_chars=512, placeholder='请输入古汉语',key='c2', label_visibility='collapsed')
#    st.subheader("SikuGPT")
   begin_trans = st.button("开始翻译", key='begin_tran2')
   if begin_trans:
    # st.header("AncientGPT")
        display_cn = st.text_area('现代汉语翻译结果：',interface('cn'), placeholder='翻译',key='cn2')
        display_en = st.text_area('英语翻译结果：',interface('en'), placeholder='翻译',key='en2')

with tab3:
   content = st.text_area("输入古汉语", max_chars=512, placeholder='请输入古汉语',key='c3', label_visibility='collapsed')
   begin_trans = st.button("开始翻译", key='begin_tran3')
   if begin_trans:
    # st.header("AncientGPT")
        display_cn = st.text_area('现代汉语翻译结果：',interface('cn'), placeholder='翻译',key='cn3')
        display_en = st.text_area('英语翻译结果：',interface('en'), placeholder='翻译',key='en3')

# if begin_trans:
#     start_message = st.empty()
#     start_message.write("翻译中...")
#     start_time = time.time()

#     start_message.write("翻译完成")
#     # st.subheader('My sub')
#     display_en = interface('en')
    # st.text_input('现代汉语翻译结果')
    # st.text_input('英语翻译结果')

