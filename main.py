import streamlit as st
from PIL import Image

# タイトル
st.title("1秒おきに10秒間、10枚の画像を取得")

# 画像を保存するリスト
if 'images' not in st.session_state:
    st.session_state.images = []

# カメラ入力
img_data = st.camera_input("Take a picture")

# 画像がキャプチャされた場合
if img_data:
    # 画像を読み込み
    img = Image.open(img_data)
    st.session_state.images.append(img)
    st.image(img, caption=f"Captured image {len(st.session_state.images)}")

# 取得した画像を表示
if st.session_state.images:
    st.write("取得した画像:")
    for idx, img in enumerate(st.session_state.images):
        st.image(img, caption=f"Captured image {idx+1}")

# 画像をリセットするボタン
if st.sidebar.button('Reset'):
    st.session_state.images = []
    st.write("画像がリセットされました。")
