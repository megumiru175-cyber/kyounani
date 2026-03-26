import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("### 今までのがんばり")
    st.write(df)

    st.write("#### 列名:", list(df.columns))

    st.title('Bar Chart')

    # ✨ 列名が存在するかチェック
    if 'category' in df.columns and 'value' in df.columns:
        st.bar_chart(df, x='category', y='value')
    else:
        st.error("📛 CSV に 'category' または 'value' 列がありません。上の列名を確認して指定してください。")
else:
    st.info("CSVファイルをアップロードすると棒グラフが表示されます。")
