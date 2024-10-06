# Tire Quality Prediction WebApp

This project is a web application that predicts tire quality using a machine learning model. It leverages Streamlit for the web interface and TensorFlow for the model predictions.

## Features

- **User-Friendly Interface**: Allows users to upload an image of a tire to get a quality prediction.
- **Model Integration**: Downloads and loads a pre-trained TensorFlow model.
- **Real-Time Predictions**: Provides instant feedback on the quality of the uploaded tire image.

## File Structure

- `streamlit_app.py`: Main application file using Streamlit to set up the web interface.
- `download_model.py`: Script to download and extract the pre-trained model.

## Key Components

### Streamlit Application (`streamlit_app.py`)

- **Model Loading**:
  - Downloads the model if not already present.
  - Loads the model into the session state for reuse.
- **Image Preprocessing**:
  - Converts uploaded images to a format suitable for the model.
  - Resizes and normalizes the image.
- **Prediction**:
  - Uses the model to predict tire quality.
  - Displays the prediction result on the web interface.

### Model Download (`download_model.py`)

- **Download and Extraction**:
  - Downloads the model zip file from a provided URL.
  - Extracts the model files for use in the application.

## Challenges and Solutions

- **Model Integration**: Ensuring the model is properly downloaded and loaded into the application required handling file downloads and TensorFlow model loading.
- **Image Preprocessing**: Converting user-uploaded images to a format compatible with the model involved resizing and normalizing the images.
- **Real-Time Predictions**: Providing instant feedback required efficient processing and prediction mechanisms.

## Getting Started

1. Clone the repository.
2. Install the required dependencies.
3. Run the Streamlit app.

```bash
git clone https://github.com/faisal-fida/tyre-quality-prediction.git
cd tyre-quality-prediction
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Conclusion

This project demonstrates a practical application of integrating machine learning models into a web application, showcasing the use of Streamlit and TensorFlow to predict tire quality from images. The project highlights the complexities of model integration, image preprocessing, and real-time predictions.

Feel free to contribute or raise issues if you encounter any problems!
