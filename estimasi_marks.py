import pickle
import streamlit as st

model = pickle.load(open('estimasi_marks.sav', 'rb'))

st.title('Estimasi Nilai Post Test Siswa')

school_setting = st.number_input('Input Pengaturan Sekolah (Urban = 1 , Suburban = 2, Rural = 3)')
school_type = st.number_input('Input Tipe Sekolah (Non-public = 1, Public = 2)')
teaching_method = st.number_input('Input Metode Belajar (Standard = 1, Experimental = 2)')
n_student = st.number_input('Input Jumlah Siswa Dalam Kelas ()')
gender = st.number_input('Input Jenis Kelamin (Female = 0, Male = 1)')
lunch = st.number_input('Input Kualitas Makan Siang (Does not qualify = 1, Qualifies for reduced/free lunch = 2)')
pretest = st.number_input('Input Nilai Pretest')

predict = ''

if st.button('Estimasi Nilai'):
    predict = model.predict(
        [[school_setting,school_type,teaching_method,n_student,gender,lunch,pretest]]
    )
    st.write ('Estimasi Nilai yang diperoleh Siswa : ', predict)