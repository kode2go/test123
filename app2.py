import streamlit as st

st.title("🛍️ Retail Dashboard")
st.header("📊 Sales Analytics")
st.write("🎉 Welcome to Python!")
st.success("✅ Sales target reached!")

if st.button("🎈 Celebrate!"):
    st.balloons()

if st.button("❄️ Make it snow!"):
    st.snow()

if st.button("🎁 Surprise!"):
    st.success("You won a prize! 🏆")

st.progress(75)

st.spinner("Loading sales data...")

st.slider("Customer satisfaction", 0, 100)

st.color_picker("Choose a colour")

st.toggle("Enable dark mode")

st.feedback("stars")

st.selectbox("Favourite product", ["Shoes", "Jeans", "Shirts"])

st.success("🎉 Sales increased!")
st.warning("⚠️ Low stock!")
st.error("❌ Payment failed!")
st.info("💡 New promotion available!")
