import streamlit as st
import pandas as pd
st.markdown(
    """
    <style>
    .stApp {
        background-color: #00fa9a;
        
    }
    </style>
    """,
    unsafe_allow_html=True
)

# CSVファイルのアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

# アップロードされたファイルをデータフレームに読み込む
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # テーブルの表示
    st.write("### 今までのがんばり")
    st.write(df)

st.title('Bar Chart')
# 棒グラフを表示
st.bar_chart(data, x='category', y='value')
