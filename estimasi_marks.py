import pickle
import streamlit as st

model = pickle.load(open('estimasi_marks.sav', 'rb'))

st.title('Estimasi Nilai Siswa')

number_courses = st.number_input('Input Jumlah Mata Pelajaran')
time_study = st.number_input('Input Jumlah Jam Belajar')

predict = ''

if st.button('Estimasi Nilai'):
    predict = model.predict(
        [[number_courses,time_study]]
    )
    st.write ('Estimasi Nilai yang diperoleh Siswa : ', predict)