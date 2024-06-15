import streamlit as st
import matplotlib as plt
import base64
import joblib
import pandas as pd

model = joblib.load('model/linear_regression_model.pkl')
@st.cache_resource

#Define the prediction function 
def predict(carat, cut, color, clarity, depth, table, x, y, z):
    # Mapping for cut
    cut_mapping = {'Fair': 0, 'Good': 1, 'Very Good': 2, 'Premium': 3, 'Ideal': 4}
    # Mapping for color
    color_mapping = {'J': 0, 'I': 1, 'H': 2, 'G': 3, 'F': 4, 'E': 5, 'D': 6}
    # Mapping for clarity
    clarity_mapping = {'I1': 0, 'SI2': 1, 'SI1': 2, 'VS2': 3, 'VS1': 4, 'VVS2': 5, 'VVS1': 6, 'IF': 7}
    
    # Transform the categorical variables to numerical values
    cut = cut_mapping.get(cut, 0)
    color = color_mapping.get(color, 0)
    clarity = clarity_mapping.get(clarity, 0)
    
    # Make the prediction using the transformed variables
    prediction = model.predict(pd.DataFrame([[carat, cut, color, clarity, depth, table, x, y, z]],
                                            columns=['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']))
    return prediction

#I love Ylang Ylang FkJ
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

autoplay_audio("app/FKJ-Ylang Ylang.mp3")
#Snow is wonderfull
st.snow()

#Add title for my app
st.title('💎THẦN TÀI AI-MUA KIM CƯƠNG THÔNG MINH 💎')
st.image('app/Thantai.jpeg', width =100)
st.header('Vui lòng nhập các đặc trưng của viên kim cương bạn muốn mua:')
carat = st.number_input('Carat Weight:', min_value=0.1, max_value=10.0, value=1.0)
cut = st.selectbox('Cut Rating:', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
color = st.selectbox('Color Rating:', ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
clarity = st.selectbox('Clarity Rating:', ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
depth = st.number_input('Diamond Depth Percentage:', min_value=0.1, max_value=100.0, value=1.0)
table = st.number_input('Diamond Table Percentage:', min_value=0.1, max_value=100.0, value=1.0)
x = st.number_input('Diamond Length (X) in mm:', min_value=0.1, max_value=100.0, value=1.0)
y = st.number_input('Diamond Width (Y) in mm:', min_value=0.1, max_value=100.0, value=1.0)
z = st.number_input('Diamond Height (Z) in mm:', min_value=0.1, max_value=100.0, value=1.0)
if st.button('Predict Price'):
    price = predict(carat, cut, color, clarity, depth, table, x, y, z)
    st.success(f'Giá dự đoán của viên kim cương là: ${price[0]:.2f} USD')

