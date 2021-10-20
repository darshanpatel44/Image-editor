import streamlit as st
import cv2
from PIL import Image,ImageEnhance
import numpy as np
import os

st.set_page_config(
     page_title="Image Enhancement",
     page_icon="edit.png",
 )
@st.cache
def load_image(img):
    im = Image.open(img)
    return im

def app():
    st.title('Image Enhancement Editor')
    activities = ['Enhancements']
    choice = st.sidebar.selectbox('Select activities',activities)

    if choice == 'Enhancements':
        st.subheader('Image Editor')
        image_file = st.file_uploader("Upload Image",type = ['jpg','png','jpeg'])

        if image_file is None:
            st.error('please upload image!!')
        else:
            if image_file is not None:
                col1, col2 = st.columns(2)
                our_image = Image.open(image_file)
                col1.header('Original Image')
                col1.image(our_image,use_column_width=True)

            enhance_type = st.sidebar.radio('Enhancement Types',['Original','Gray scale','Contrast','Brightness','Bluring'])
            if enhance_type == 'Gray scale':
                new_img = np.array(our_image.convert('RGB'))
                img = cv2.cvtColor(new_img,1)
                img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                col2.header('Edited Image')
                col2.image(img,use_column_width=True)

            elif enhance_type == 'Contrast':
                c_rate = st.sidebar.slider('Constrast',0.5,4.5)
                enhancer = ImageEnhance.Contrast(our_image)
                img_output = enhancer.enhance(c_rate)
                col2.header('Edited Image')
                col2.image(img_output,use_column_width=True)

            elif enhance_type == 'Brightness':
                br_rate = st.sidebar.slider('Brightness',0.5,4.5)
                enhancer = ImageEnhance.Brightness(our_image)
                img_out = enhancer.enhance(br_rate)
                col2.header('Edited Image')
                col2.image(img_out,use_column_width=True)

            elif enhance_type == 'Bluring':
                new_img = np.array(our_image.convert('RGB'))
                b_rate = st.sidebar.slider('Bluring',0.5,4.5)
                img = cv2.cvtColor(new_img,1)
                blur_img = cv2.GaussianBlur(img,(11,11),b_rate)
                col2.header('Edited Image')
                col2.image(blur_img,use_column_width=True)

if __name__ == "__main__":
    app()