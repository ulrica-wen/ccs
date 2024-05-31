import streamlit as st
from PIL import Image
import os
dir_path = os.path.split(os.path.realpath(__file__))[0]
import sys
sys.path.append(dir_path)

st.set_page_config(
    page_title="音综战绩",
    page_icon=":Scroll:",
    layout='wide'
)

st.title('🎉 音综战绩')

st.subheader('Introduction')
st.markdown(
    """
    DeepFloyd IF is a state-of-the-art text-to-image model released by StabilityAI in late April, 2023 that achieves a high degree of photorealism and language understanding. DeepFloyd is built with multiple neural modules (independent neural networks that tackle specific tasks), and generates high-resolution images in a cascading approach. The model is composed of a frozen text encoder and three cascaded pixel diffusion modules: a base model that generates 64x64 pixel image based on the input text prompt and two super-resolution models that generates images with resolution 256x256 pixel and 1024x1024 pixel. All stages of the model utilize a frozen text encoder based on the T5-XXL to extract text embeddings, which are then fed into a UNet architecture enhanced with cross-attention and attention pooling. 
    \n
    As a result, DeepFloyd achieves a zero-shot Frechet Inception Distance (FID) score of 6.66 on the COCO dataset, which outperforms other novel text-to-image models including DALL-E 2 (10.39), Imagen (7.27), and eDiff-I (6.95).

    **The following generation flowchart demonstrates the three-stage process**:
    \n

    - A **text prompt** is passed through the frozen T5-XXL language model to convert into a qualitative text representation
    \n
    - **Stage 1**: A base diffusion model transforms the qualitative text into a 64x64 image. There are three versions of the base model each with different number of parameters: 400M, 900M, and 4.3B. 
    \n
    - **Stage 2**: To upscale the image, two text-conditional super-resolution models are applied to the output of the base model. The first super-resolution model upscales the 64x64 image to 256x256. 
    \n
    - **Stage 3**: The second super-resolution diffusion model is applied and produces a 1024x1024 image.
    """
)

tab1, tab2, tab3, tab4 = st.tabs(["披荆斩棘3", "声生不息家年华", "天赐的声音5","一起来看我们的演唱会"])



with tab1:
   st.header("披荆斩棘成团哥哥平台数据汇总")
   st.image('/Users/wcheng/Desktop/ticket/陈楚生/ccs/image/批哥汇总.jpg', width=1000)
   with st.expander("查看具体数据"):
        st.image('/Users/wcheng/Desktop/ticket/陈楚生/ccs/image/批哥_战绩1.jpg', width=800)
        st.image('/Users/wcheng/Desktop/ticket/陈楚生/ccs/image/批哥_战绩2.jpg', width=800)
        st.image('/Users/wcheng/Desktop/ticket/陈楚生/ccs/image/批哥_战绩3.jpg', width=800)
        st.image('/Users/wcheng/Desktop/ticket/陈楚生/ccs/image/批哥_战绩4.jpg', width=800)
        st.write("""
            上面的图表展示了我为您选择的一些数字。
            这些数字是通过真实的骰子摇出来的，所以它们*保证*是随机的。
        """)

with tab2:
   st.header("A dog")
   st.image("/Users/wcheng/Desktop/ticket/陈楚生/ccs/image/批哥_战绩1.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("/Users/wcheng/Desktop/ticket/陈楚生/ccs/image/批哥_战绩1.jpg", width=200)
