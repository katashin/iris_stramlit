# 基本ライブラリ
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

iris = load_iris()
x = iris.data
t = iris.target
columns = iris.feature_names

df = pd.DataFrame(data=x, columns=columns)

# 目標値
df['target'] = iris.target

# 目標値を数字から花の名前に変更
iris_map = {
  0: 'setosa',
  1: 'versicolor',
  2: 'virginica'
}

df['target'] = df['target'].map(iris_map)
st.dataframe(df)

# 学習モデルを作成
x = iris.data[:, [0, 2]]
t = iris.target

model = LogisticRegression()
model.fit(x, t)

st.sidebar.header('Input Features')
sepalValue = st.sidebar.slider('sepal length(cm)', min_value=0.0, max_value=10.0, step=0.1)
petalValue = st.sidebar.slider('petal length(cm)', min_value=0.0, max_value=10.0, step=0.1)

st.title('Iris Classifier')
st.write('## Input Valuse')

# インプットデータ
value_df = pd.DataFrame([],columns=['data','sepal length (cm)','petal length (cm)'])
record = pd.Series(['data', sepalValue, petalValue], index=value_df.columns)
value_df = value_df.append(record, ignore_index=True)
value_df.set_index('data', inplace=True)
st.table(value_df)

y_pred = model.predict_proba(value_df)
pred_df = pd.DataFrame(data=y_pred, columns=['setosa','versicolor','virginica'],
                       index=['prob ablitity']
                       )

st.write('## Prediction')
st.table(pred_df)

# 予測結果の出力
name = pred_df.idxmax(axis=1).tolist()
st.write('## Result')
st.write(f'このアイリスはきっと、{name[0]}')