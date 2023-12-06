import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("tire_quality_model")


def preprocess_image(image):
    img_array = np.array(image)
    img_array = tf.cast(img_array / 255.0, tf.float32)
    img_array = tf.image.resize(img_array, [256, 256])
    img_array = tf.expand_dims(img_array, axis=0)
    return img_array


st.title("Tire Quality Classifier")
st.subheader("Is the tire good or bad?")
st.write("")
st.text("Upload a picture of a tire and the model will predict the quality")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image.resize((200, 200)), caption="Uploaded Image.")
    preprocessed_image = preprocess_image(image)
    predictions = model.predict(preprocessed_image)
    predicted_class = np.argmax(predictions[0])
    st.write("The tire is good") if predicted_class == 1 else st.write(
        "The tire is bad"
    )
