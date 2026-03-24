import streamlit as st # type: ignore
from random import choice
st.title('今日はこれができたよ！！')
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
    if st.button("Send balloons!"):
    st.balloons()    
    st.write ( "あしたもがんばろうね☆")
