from pickle import load
import streamlit as st

model=load(open("../models/BosqueSabio.sav", "rb"))


class_dict={
    "0": "There is a mayor probability that you dont have Diabetes",
    "1": "There is a mayor probability that you have diabetes"
}

st.tittle ("Think you have Diabetes?-Test it")

val1= st.slider("Numer of pregnancies had:", min_value = 0, max_value = 10, step=1)
val2= st.slider("Glucose in blood:", min_value = 10, max_value = 50, step=1)
val3= st.slider("Blood Pressure:", min_value = 1, max_value = 250, step=1)
val4= st.slider("Skin Thickness:", min_value = 1, max_value = 60, step=1)
val5= st.slider("Insuline Level:", min_value = 0, max_value = 250, step=1)
val6= st.slider("Body Mass Index:", min_value = 0.0, max_value = 100.0, step=0.1)
val7= st.slider("Diabetes Pedigree Function:", min_value = 0.000, max_value = 1.000, step=0.001)
val8= st.slider("Age:", min_value = 0, max_value = 100, step=1)

if st.button("Predict"):

    prediction = str(model.predict([val1,val2,val3,val4,val5,val6,val7,val8])[0])

    pred_class=class_dict[prediction]

    st.write("Prediction:", pred_class)