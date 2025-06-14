import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Mini Health Quiz", page_icon="💊")

st.title("💊 Mini Health Quiz")
st.write("Jawab pertanyaan berikut untuk mengetahui seberapa sehat gaya hidupmu!")

# Fungsi skor
def get_score(option, mapping):
    return mapping.get(option, 0)

# Form kuis
with st.form("quiz_form"):
    st.subheader("1. Berapa jam tidur kamu per hari?")
    tidur = st.radio("Pilih satu:", ["Kurang dari 5 jam", "5-7 jam", "8 jam atau lebih"], key="q1")

    st.subheader("2. Seberapa sering kamu berolahraga dalam seminggu?")
    olahraga = st.radio("Pilih satu:", ["Tidak Pernah", "1-2 kali", "3 kali atau lebih"], key="q2")

    st.subheader("3. Berapa kali kamu melakukan medical check-up dalam setahun?")
    cekup = st.radio("Pilih satu:", ["Tidak Pernah", "1 kali", "2 kali atau lebih"], key="q3")

    st.subheader("4. Seberapa sering kamu makan sayur dan buah setiap hari?")
    sayur = st.radio("Pilih satu:", ["Jarang", "Sekali sehari", "Setiap kali makan"], key="q4")

    st.subheader("5. Berapa lama kamu duduk di depan layar setiap hari?")
    layar = st.radio("Pilih satu:", ["> 6 jam", "4-6 jam", "< 4 jam"], key="q5")

    st.subheader("6. Seberapa sering kamu merokok atau terpapar asap rokok?")
    rokok = st.radio("Pilih satu:", ["Sering", "Kadang-kadang", "Tidak pernah"], key="q6")

    submit = st.form_submit_button("Lihat Hasil")

if submit:
    skor = 0
    skor += get_score(tidur, {"Kurang dari 5 jam": 1, "5-7 jam": 3, "8 jam atau lebih": 5})
    skor += get_score(olahraga, {"Tidak Pernah": 1, "1-2 kali": 3, "3 kali atau lebih": 5})
    skor += get_score(cekup, {"Tidak Pernah": 1, "1 kali": 3, "2 kali atau lebih": 5})
    skor += get_score(sayur, {"Jarang": 1, "Sekali sehari": 3, "Setiap kali makan": 5})
    skor += get_score(layar, {"> 6 jam": 1, "4-6 jam": 3, "< 4 jam": 5})
    skor += get_score(rokok, {"Sering": 1, "Kadang-kadang": 3, "Tidak pernah": 5})

    # URL GIF berdasarkan skor
    if skor >= 24:
        hasil = "🎉 Gaya hidup kamu sehat!"
        gif_url = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
    elif 15 <= skor < 24:
        hasil = "🙂 Gaya hidup kamu cukup sehat, masih bisa ditingkatkan!"
        gif_url = "https://media.giphy.com/media/l0Exk8EUzSLsrErEQ/giphy.gif"
    else:
        hasil = "⚠️ Gaya hidup kamu perlu perhatian lebih!"
        gif_url = "https://media.giphy.com/media/3oz8xLd9DJq2l2VFtu/giphy.gif"

    # Tampilkan hasil
    st.subheader("Hasil Kuis:")
    st.success(hasil)
    st.image(gif_url, use_column_width=True)