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



# '''正式交互界面'''
st.caption('选择翻译模型:')
st.markdown("> 该平台实现了中文古文到中文现代文和英文的自动翻译。在网站首页用户可以直接进入古文翻译界面，在文本输入框中输入需要翻译的古文文本并选择需要翻译的目标语言后，在翻译结果栏便会返回相应的译文。 ")

