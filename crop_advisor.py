import streamlit as st
import pandas as pd

st.set_page_config(page_title="🌾 Crop Advisor UI", layout="centered")

st.title("🌱 Data-Driven Crop Advisory System")

st.markdown("### 🎚️ Adjust Parameters Using Sliders")

# 🎚️ Unique way to take input: sliders (moving bars)
n = st.slider("Nitrogen (N)", 0, 140, 70, step=5)
p = st.slider("Phosphorus (P)", 0, 140, 60, step=5)
k = st.slider("Potassium (K)", 0, 140, 50, step=5)
ph = st.slider("pH Level", 0.0, 14.0, 6.5, step=0.1)
temp = st.slider("Temperature (°C)", 0, 50, 28)
humidity = st.slider("Humidity (%)", 0, 100, 65)
rainfall = st.slider("Rainfall (mm)", 0, 300, 100)

if st.button("🌾 Recommend Crop"):
    # Basic rule-based logic (you can add ML model here)
    if ph < 6.0:
        crop = "Rice"
    elif temp > 30:
        crop = "Sugarcane"
    elif humidity > 70:
        crop = "Banana"
    else:
        crop = "Wheat"

    st.success(f"✅ Recommended Crop: **{crop}**")

    # 🎨 Show input visually in a graph
    df = pd.DataFrame({
        'Parameter': ['Nitrogen', 'Phosphorus', 'Potassium', 'pH', 'Temp', 'Humidity', 'Rainfall'],
        'Value': [n, p, k, ph, temp, humidity, rainfall]
    })

    st.markdown("### 📊 Your Input Overview")
    st.bar_chart(df.set_index("Parameter"))

