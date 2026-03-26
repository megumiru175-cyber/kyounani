import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("### 今までのがんばり（元データ）")
    st.write(df)

    # ---------------------------------------
    # すべての列を縦にしてタスク一覧にする
    # ---------------------------------------
    value_columns = df.columns[1:]

    melted = df.melt(id_vars='日にち', value_vars=value_columns, value_name='task')
    melted = melted.dropna(subset=['task'])
    melted['task'] = melted['task'].str.strip()

    # タスクごとの集計
    count_data = melted['task'].value_counts().reset_index()
    count_data.columns = ['category', 'value']

    st.write("### 種類ごとの回数")
    st.write(count_data)

    # ---------------------------------------
    # 棒グラフ
    # ---------------------------------------
    st.title("棒グラフ（がんばりの回数）")
    st.bar_chart(count_data, x='category', y='value')

    # ---------------------------------------
    # 円グラフ
    # ---------------------------------------
    st.title("円グラフ（がんばりの割合）")

    fig, ax = plt.subplots()
    ax.pie(
        count_data['value'],
        labels=count_data['category'],
        autopct='%1.1f%%',
        startangle=90
    )
    ax.axis('equal')  # 円を丸く表示

    st.pyplot(fig)

else:
    st.info("CSVファイルをアップロードすると分析グラフが表示されます。")
    
