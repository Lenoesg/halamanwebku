from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis her: https://webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Dashboard", page_icon=":cyclone:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_9wpyhdzo.json")
img_contact_form = Image.open("images/2.jpg")
img_lottie_animation = Image.open("images/1.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Halo, Ya'ahowu... Saya Linus Gulo :wave:")
    st.title("Seorang Data Analytics Pemula dari Kepulauan Nias")
    st.write("Saya senang mencari tahu bagaimana cara membuat dan menganalisa data dengan SQL, Python dan menampilkannya di aplikasi seperti Excel. Saat ini saya sedang menggunakan Python-Streamlit dalam menampilkan Dashboard yang sederhana ini")
    st.write("saya juga memiliki blog [klik disini](https://kalinz.blogspot.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Kegiatan saya")
        st.write("##")
        st.write(
            """
            Saat ini saya sedang bekerja di salah satu institusi perbankan swasta, kegiatan saya yaitu:
            - Membuat query analisa data untuk menemukan anomali transaksi.
            - Membuat Web App Data Analytics yang bertujuan untuk efisiensi pekerjaan tim.
            - Melakukan audit Onsite maupun offsite pada internal perusahaan.
            - Membuat Laporan.

            Jika kamu ingin melihat profil saya di LinkedIn, silahkan ikuti saya melalui link berikut ini
            """
        )
        st.write("[LinkedIn >](https://www.linkedin.com/in/melinus-g-7bb866b3)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROYEK ----
with st.container():
    st.write("---")
    st.header("Proyek Saya")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Apa itu Streamlit")
        st.write(
            """
            Streamlit adalah sebuah framework berbasis Python dan bersifat open-source yang dibuat untuk memudahkan dalam membangun apikasi web di bidang sains data dan machine learning yang interaktif.
            Pada tutorial ini saya akan menjelaskan lebih detail tentang cara kerja Streamlit
            """
        )
        st.markdown("[Tonton videonya...](https://www.youtube.com/c/NiasNet)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Bagaimana cara Membuat Form Kontak di Website kita menggunakan Streamlit")
        st.write(
            """
            Disini saya akan mengajarkan bagaimana cara membuat form kontak sederhana pada aplikasi web menggunakan Streamlit.
            """
        )
        st.markdown("[Tonton videonya...](https://www.youtube.com/c/NiasNet)")



# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Hubungi Saya")
    st.write("##")

    # Documentation: https://formsubit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/melinusg0594@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Nama Anda" required>
        <input type="email" name="email" placeholder="Email Anda" required>
        <textarea name="message" placeholder="Tulis Pesan Anda disini..." required></textarea>
        <button type="submit">Kirim</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()