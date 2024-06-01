import streamlit as st
# from rembg import remove
from PIL import Image
from io import BytesIO
import base64
from datetime import datetime

import socket

import google_auth_httplib2
import httplib2
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import HttpRequest


st.set_page_config(layout="wide", page_title="Hello Page")

st.title("🎸 陈楚生&花生资源库")
st.markdown(
    """
    这是一个陈楚生相关信息总结网站，将包含多个板块。
    ***音乐作品安利，奖项科普，音综战绩，破除洗脑包，...*** ，欢迎朋友们一起建设。

    👈 **请点开左侧小箭头查看更多内容。**

    👈 **要联系我，请在下方留言。**
    """
)
st.markdown("\n")
st.markdown('\n')
st.markdown('\n')


 
def sidebar_bg(side_bg):
 
   side_bg_ext = 'png'
 
   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )
 
#调用
# sidebar_bg('/Users/wcheng/Desktop/ticket/陈楚生/ccs/image/sidebar_bg.png')



st.title("🦈 陈楚生简介")
st.markdown(
    """
    写写写写写写到头大
    """
)
st.markdown("\n")
st.markdown('\n')
st.markdown('\n')



def main_bg(main_bg):
    main_bg_ext = "jpg"
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
 
#调用
main_bg('/Users/wcheng/Desktop/ticket/陈楚生/ccs/image/background.png')


st.subheader('🙌 留下评论与建议')
st.markdown(
    """
    Please leave your comments here and also take a look at what others said about this project.
    """
)
st.markdown("\n")
st.markdown('\n')
st.markdown('\n')

socket.setdefaulttimeout(15 * 60)

SCOPE = "https://www.googleapis.com/auth/spreadsheets"
SPREADSHEET_ID = "1RtSCrn232rwYZ_DZAOU1lqzEha-2zP0ZjMf7342YZBA" #"1rkMVLvh3JrBq_tbi4Ho0qjCDAP3vYdNuWOEjYpkJLNU"
SHEET_NAME = "Database"
GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"


@st.cache_resource()
def connect():
    # Create a connection object.
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=[SCOPE],
    )

    # Create a new Http() object for every request
    def build_request(http, *args, **kwargs):
        new_http = google_auth_httplib2.AuthorizedHttp(
            credentials, http=httplib2.Http()
        )
        return HttpRequest(new_http, *args, **kwargs)

    authorized_http = google_auth_httplib2.AuthorizedHttp(
        credentials, http=httplib2.Http()
    )
    service = build(
        "sheets",
        "v4",
        requestBuilder=build_request,
        http=authorized_http,
    )
    gsheet_connector = service.spreadsheets()
    return gsheet_connector


def collect(gsheet_connector) -> pd.DataFrame:
    values = (
        gsheet_connector.values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{SHEET_NAME}!A:C",
        )
        .execute()
    )

    df = pd.DataFrame(values["values"])
    df.columns = df.iloc[0]
    df = df[1:]
    return df


def insert(gsheet_connector, row) -> None:
    values = (
        gsheet_connector.values()
        .append(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{SHEET_NAME}!A:C",
            body=dict(values=row),
            valueInputOption="USER_ENTERED",
        )
        .execute()
    )

COMMENT_TEMPLATE_MD = """{} - {}
> {}"""









c1, c2 = st.columns(2)

with c1:
    st.info('**陈楚生&花生**', icon="🥜")

with c2:
    st.info('**Contact: [@Ulrica ](wen_cheng@berkeley.edu)**', icon="📩")

st.title("📕 Sources and Reference")
st.markdown(
    """
    - https://github.com/deep-floyd/IF 
    - https://stability.ai/blog/deepfloyd-if-text-to-image-model
    - https://www.nftparis.xyz/blog/introducing-deepfloyd-if-a-revolutionary-text-to-image-model-by-stability-ai
    - https://the-decoder.com/deepfloyd-if-is-a-crazy-good-text-to-image-model-and-open-source/
    - https://github.com/deep-floyd/IF
    - https://github.com/guofei9987/blind_watermark/tree/master
    - https://github.com/fire-keeper/BlindWatermark
    - https://bgremoval.streamlit.app/
    - https://onlinelibrary.wiley.com/doi/10.1002/0471745790.ch5 
    - https://link.springer.com/referenceworkentry/10.1007/0-387-30038 4_62#:~:text=Definition%3ADiscrete%20Wavelet%20Transform%20is,wavelet%2Dbased%20compression%20and%20coding. 
    - J. Liu et al., "An Optimized Image Watermarking Method Based on HD and SVD in DWT Domain," in IEEE Access, vol. 7, pp. 80849-80860, 2019, doi: 10.1109/ACCESS.2019.2915596.
    """
)

