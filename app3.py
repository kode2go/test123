import streamlit as st

st.title("🛍️ My Fun Retail App")

st.write("Welcome to my first interactive website!")

st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png")

name = st.text_input("What is your name?")

if st.button("Say Hello 👋"):
    st.success(f"Hello {name}! 🎉")
    st.balloons()

st.divider()

st.subheader("🎮 Try these!")

if st.button("Make it snow ❄️"):
    st.snow()

if st.button("Celebrate 🎈"):
    st.balloons()

rating = st.slider("Rate our store ⭐", 1, 10)

st.write("Your rating:", rating)

st.feedback("faces")

st.divider()

st.metric("💰 Total Revenue", "R125,000", "+12%")

st.metric("🛒 Orders", "350", "+8%")

st.progress(80)

st.success("Great work! 🎉")
