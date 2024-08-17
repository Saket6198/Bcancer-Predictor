import streamlit as st
import pandas as pd
import pickle as pickle


def clean_data():
    bcancer = pd.read_csv('C:/Users/Saket Singh/Desktop/StreamLit_ML_cancer/data/data.csv')
    bcancer = bcancer.drop(['Unnamed: 32', 'id'], axis=1)  # deleting unnamed col and id because it's not req
    bcancer['diagnosis'] = bcancer['diagnosis'].map({'M': 1, 'B': 0})  # mapping diagnosis values to 1 and 0
    print(bcancer.head())
    return bcancer


def add_sidebar():
    st.sidebar.header("Cell Nuclei Measurement")
    data = clean_data()
    input_dict = {}

    slider_labels = [
        ("Radius (mean)", "radius_mean"),  # label, key values are used here
        ("Texture (mean)", "texture_mean"),
        ("Perimeter (mean)", "perimeter_mean"),
        ("Area (mean)", "area_mean"),
        ("Smoothness (mean)", "smoothness_mean"),
        ("Compactness (mean)", "compactness_mean"),
        ("Concavity (mean)", "concavity_mean"),
        ("Concave points (mean)", "concave points_mean"),
        ("Symmetry (mean)", "symmetry_mean"),
        ("Fractal dimension (mean)", "fractal_dimension_mean"),
        ("Radius (se)", "radius_se"),
        ("Texture (se)", "texture_se"),
        ("Perimeter (se)", "perimeter_se"),
        ("Area (se)", "area_se"),
        ("Smoothness (se)", "smoothness_se"),
        ("Compactness (se)", "compactness_se"),
        ("Concavity (se)", "concavity_se"),
        ("Concave points (se)", "concave points_se"),
        ("Symmetry (se)", "symmetry_se"),
        ("Fractal dimension (se)", "fractal_dimension_se"),
        ("Radius (worst)", "radius_worst"),
        ("Texture (worst)", "texture_worst"),
        ("Perimeter (worst)", "perimeter_worst"),
        ("Area (worst)", "area_worst"),
        ("Smoothness (worst)", "smoothness_worst"),
        ("Compactness (worst)", "compactness_worst"),
        ("Concavity (worst)", "concavity_worst"),
        ("Concave points (worst)", "concave points_worst"),
        ("Symmetry (worst)", "symmetry_worst"),
        ("Fractal dimension (worst)", "fractal_dimension_worst"),
    ]
    for label, key in slider_labels:
        input_dict[key] = st.sidebar.slider(
            label,
            min_value=float(data[key].min()),
            max_value=float(data[key].max()),
            value=float(data[key].mean())
        )


def main():
    st.set_page_config(
        page_title="Breast Cancer Predictor ",
        page_icon=":female-doctor:",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    with st.container():
        st.title('Breast Cancer Predictor')
        st.write('Please Connect this app to your cytology lab to help diagnose breast cancer from your tissue '
                 'sample. This app predicts using a machine learning model whether a breast mass is benign or '
                 'malignant based on the measurements it receives from your cytosis lab. You can also update the '
                 'measurements by hand using the sliders in the slidebar.')
    col1, col2 = st.columns([4, 1])
    with col1:
        st.write('1')
    with col2:
        st.write('2')
    add_sidebar()


if __name__ == '__main__':
    main()
