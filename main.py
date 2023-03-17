import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration{i + 1}')
  bar.progress(i + 1)
  time.sleep(0.01)
  
st.write('Done!!')

st.title('Stramlit の基礎')
st.write('Hello World')

# データフレームの作成
df = pd.DataFrame({
  '一列目': [10, 20, 30, 40, 50],
  '二列目': [1, 2, 3, 4, 5]
})

#     '1列目' : [1, 2, 3, 4],
#     '2列目' : [10, 20, 30, 40]
# })
st.dataframe(df.style.highlight_max(axis = 0), width=100, height=150)

st.table(df)

df1 = pd.DataFrame(
  np.random.rand(10, 3),
  columns=['a', 'b', 'c']
)

st.line_chart(df1)
st.area_chart(df1)
st.bar_chart(df1)

# プロットする乱数をデータフレームで用意
df2 = pd.DataFrame(

    # 乱数 + 新宿の緯度と経度
    np.random.rand(100,2) / [50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon']
)

st.map(df2)


if st.checkbox('Show Image'):
  img = Image.open('iris.jpg')
  st.image(img, caption='Iris', use_column_width=True)
  
option = st.selectbox(
  '好きな数字を入力：', list(range(1, 11))
)

'あなたの名前は', option, 'です。'

text = st.sidebar.text_input('好きなスポーツを教えて下さい。')
st.write(f'あなたの好きなスポーツは{text}')

condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
st.write(f'コンディション：{condition}')

expander1 = st.expander('質問１')
expander1.write('質問１の回答は？？？？')

expander1 = st.expander('質問２')
expander1.write('質問２の回答は？？？？')

expander1 = st.expander('質問３')
expander1.write('質問３の回答は？？？？')

expander1 = st.expander('質問４')
expander1.write('質問４の回答は？？？？')
