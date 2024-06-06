import streamlit as st
import time
from PIL import Image

# タイトル
st.title("1秒おきに10秒間、10枚の画像を取得")

# 画像を保存するリスト
images = []

# サイドバーに撮影開始ボタンを配置
if st.sidebar.button('撮影開始'):
    st.write("画像をキャプチャ中...")

    for i in range(10):
        st.write(f"画像 {i+1} を撮影中...")
        # カメラ入力
        img_data = st.camera_input(f"Take a picture {i+1}", key=f"camera_{i}")

        # 画像がキャプチャされた場合
        if img_data:
            # 画像を読み込み
            img = Image.open(img_data)
            images.append(img)
            st.image(img, caption=f"Captured image {i+1}")

        # 1秒待つ
        time.sleep(1)

    st.write("画像のキャプチャが完了しました。")

# 取得した画像を表示
if images:
    st.write("取得した画像:")
    for idx, img in enumerate(images):
        st.image(img, caption=f"Captured image {idx+1}")
