import datetime
import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Belajar Analisis Data');
st.header('Pengembangan Dashboard');
st.subheader('Pengembangan Dashboard');
st.caption('Copyright (c) 2023');

code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

st.write(
    """
    # My first app
    Hello juan ganteng, para calon praktisi data masa depan!
    """
)
st.write(pd.DataFrame({
    'First Column':[1,2,3,4,5],
    'Second Column':[6,7,8,9,10]
}))


st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
 
st.dataframe(data=df, width=500, height=150)
st.table(data=df)
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)

text = st.text_area('Feedback')
st.write('Feedback: ', text)
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)

uploaded_file = st.file_uploader('Choose a CSV file')
 
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)
    
if st.button('Say hello'):
    st.write('Hello there')

agree = st.checkbox('I agree')
 
if agree:
    st.write('Welcome to MyApp')
    
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)
if genre:
    st.write('wlcop')

ka = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

with st.sidebar:
    
    st.text('Ini merupakan sidebar')
    st.image("https://static.streamlit.io/examples/cat.jpg")
    
    values = st.slider(
        label='Select a range of values',
        min_value=0, max_value=100, value=(0, 100)
    )
    st.write('Values:', values)
    
st.title('Belajar Analisis Data')

tab1, tab2, tab3,tab4, tab5, tab6 = st.tabs(["Tab 1", "Tab 2", "Tab 3", "Tab 4", "Tab 5", "Tab 6"])
 
with tab1:
    st.header("Tab 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with tab2:
    st.header("Tab 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with tab3:
    st.header("Tab 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")
    
with tab4:
    st.header("Tab 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with tab5:
    st.header("Tab 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with tab6:
    st.header("Tab 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")

with st.container():
    tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
    with tab1:
        st.header("Tab 1")
        st.image("https://static.streamlit.io/examples/cat.jpg")
 
    with tab2:
        st.header("Tab 2")
        st.image("https://static.streamlit.io/examples/dog.jpg")
 
    with tab3:
        st.header("Tab 3")
        st.image("https://static.streamlit.io/examples/owl.jpg")
        st.write("Inside the container")
    
    x = np.random.normal(15, 5, 250)
 
    fig, ax = plt.subplots()
    ax.hist(x=x, bins=15)
    st.pyplot(fig) 
    st.title('Belajar Analisis Data')
    st.write("Outside the container")
 
 
with st.container():    
    st.title('Belajar menggunakan container')
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.header("Kolom 1")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    
    with col2:
        st.header("Kolom 2")
        st.image("https://static.streamlit.io/examples/dog.jpg")
    
    with col3:
        st.header("Kolom 3")
        st.image("https://static.streamlit.io/examples/owl.jpg")
        
x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig) 
 
with st.expander("See explanation"):
    st.write(
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
        sunt in culpa qui officia deserunt mollit anim id est laborum.
        """
    )