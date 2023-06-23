import streamlit as st
from lightgbm import LGBMClassifier
from joblib import load
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import random

model = load('lgbm.pkl')
sc=load('std_scaler.bin')

st.title("Exoplanet Simulator")
st.text("Move the sliders around to experiment and see what type of planet is formed. Click on the button")

x = st.slider("Planet Mass (w.t.r Earth)",min_value=1, max_value=100)
y = st.slider("Planet Radius (w.t.r Earth)",min_value=1, max_value=100)
bt = st.button('SHOW ME THE PLANET')

gas = ['Gas Giant.png', 'Gas Giant2.png']
ice = ['Neptune-like.png', 'Neptune-like2.png']
superEarth = ['Super Earth.png']
terrestrial = ['Terrestrial.png', 'Terrestrial2.png', 'Terrestrial3.png']

if bt:
    q = model.predict(sc.transform([[x,y]]))
    if (q == ['Super Earth']):
        st.image(superEarth[0])
        st.header("Planet created: Super Earth (Reference Image Above)")
        st.subheader("Description:")
        st.write("Super Earths are a class of exoplanets that are larger and more massive than Earth but smaller than gas giants. These rocky worlds, often referred to as super-sized versions of our planet, can vary in size and composition. They have solid surfaces and may possess atmospheres and water in different states. Super Earths offer intriguing possibilities for habitability and provide valuable insights into the diversity of planetary systems beyond our solar system.")
    if (q == ['Terrestrial']):
        st.image(terrestrial[random.randint(0,2)])
        st.header("Planet created: Terrestrial Planet (Reference Image Above)")
        st.subheader("Description:")
        st.write("Terrestrial planets, also known as rocky planets, are a class of planets that share similar characteristics to Earth. They are primarily composed of silicate rocks and metals, with a solid surface. Terrestrial planets are relatively smaller in size compared to gas giants and are typically found closer to their host star in planetary systems. They often possess thin atmospheres, if any, and may have features such as mountains, valleys, and even bodies of water. These planets are of particular interest in the search for extraterrestrial life, as they offer the potential for habitability and the presence of complex organic molecules.")
    if (q == ['Neptune-like']):
        st.image(ice[random.randint(0,1)])
        st.header("Planet created: Ice Giant (Reference Image Above)")
        st.subheader("Description:")
        st.write("Ice giants are planets larger than Earth but smaller than gas giants, composed of rock, metal, and a thick layer of icy materials. Their atmospheres contain hydrogen, helium, and ice, giving them a bluish hue. Ice giants, like Uranus and Neptune, display complex weather patterns and have moons with potential geologic activity. Studying ice giants enhances our understanding of planetary systems and the diverse compositions and atmospheres found in the universe.")
    if (q == ['Gas Giant']):
        st.image(gas[random.randint(0,1)])
        st.header("Planet created: Gas Giant (Reference Image Above)")
        st.subheader("Description:")
        st.write("Gas giants are enormous planets with extensive atmospheres primarily composed of hydrogen and helium. They lack a solid surface and have massive gravitational pulls. These giant planets exhibit dynamic weather patterns, including powerful storms. Gas giants often have rings and are accompanied by a system of moons. They play a crucial role in shaping planetary systems and provide insights into planetary formation and evolution.")



