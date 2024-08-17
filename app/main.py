import streamlit as st
import pickle as pickle

def side_bar():
    st.sidebar.header("cell Nuclei Measurement")

def main():
    st.set_page_config(
        page_title="Breast Cancer Predictor ",
        page_icon=":female-doctor:",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    with st.container():
        st.title('Breast Cancer Predictor')
        st.write('Please Connect this app to your cytology lab to help diagnose breast cancer from your tissue sample. This app predicts using a machine learning model whether a breast mass is benign or malignant based on the measurements it receives from your cytosis lab. You can also update the measurements by hand using the sliders in the slidebar.')
    col1, col2 = st.columns([4, 1])
    with col1:
        st.write('1')
    with col2:
        st.write('2')
    add_sidebar()

if __name__  == '__main__':
    main()