import streamlit as st # type: ignore
from random import choice
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fffacd;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("<h2 style = 'color:blue;'>これができたよ！！</h2>",
            unsafe_allow_html=True)
st.subheader('やらなくてはいけないことたくさんあるよね\n'
        'それをひとつずつやってしまうおてつだいをするよ')

#name
name = st.text_input('名前をいれてね٩꒰｡•◡•｡꒱۶')

#もし多かったらラジオボタンかこれ以上でほめる。
#ボタン
submit_btn = st.button('これでいいかな？')
cancel_btn = st.button('やっぱりやめておく')
if submit_btn:
    st.text(f'ようこそ、{name}さん！')

st.write(f"今日は{name}さんは何をしたのかな？")

#複数選択
options = st.multiselect(
    'この中からえらんでね( ˘ω˘ )',
    ['宿題', '読書', '習い事','お手伝い']
)

st.write(f"今日{options}をしたんだね！！")

st.write(f"すごいな{name}さん！！(ᗒ⩊ᗕ)⸝ި ʕᦏ")
st.write ( "そんなすごい人には、プレゼントがあるよ🎁")

if st.button("何がでるかな？？"):
    r = choice(["happy","大吉","おめでとう！"])
    st.write(r)
if st.button("おしてみてね"):
    st.balloons() 
        
    st.write ( "あしたもがんばろうね☆")
