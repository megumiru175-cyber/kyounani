import streamlit as st
import pandas as pd

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
    st.bar_chart(df, x='category', y='value')

else:
    st.info("CSVファイルをアップロードすると棒グラフが表示されます。")
