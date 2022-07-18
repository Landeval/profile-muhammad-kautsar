from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="About Me", page_icon=":dizzy:", layout="wide")

def load_lottieurl(url):
	r = requests.get(url)
	if r.status_code != 200:
		return None
	return r.json()
	
# Use Local CSS
def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
		
local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_yqnh895a.json")
img_python = Image.open("images/python.png")
img_cyber = Image.open("images/cyber.jpg")

# ---- HEADER SECTION ----
with st.container():
	st.subheader("Hallo Pak Yopi! :wave:")
	st.title("Perkenalkan, saya Muhammad Kautsar Ramli Putra :smile:")
	st.write(
	"""
	Saya senang belajar apapun yang dapat mengembangkan diri saya, dan 
	saya sangat menyukai topik: 
	- Self-development 
	- Filsafat
	- Teknologi
	- Cybersecurity
	- Psikologi 
	- Intelijen
	- Detektif
	"""
	)
	
# ---- WHAT I DO ----
with st.container():
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("Saya ini bagaimana sih orangnya? :star:")
		st.write("##")
		st.write(
		"""
		Ini adalah beberapa deskripsi tentang diri saya:
		- Saya orang yang banyak sekali memiliki ide-ide "gila" dan menurut saya keren. 
		- Saya dikenal oleh teman-teman bisa membimbing dan memimpin dengan baik. 

		- Saya cenderung pendiam dan tidak suka keramaian atau hal-hal bising. Saya suka ketenangan, karena otak saya merasa damai. 

		- Meskipun saya pendiam, tapi teman-teman saya melihat saya sebagai orang yang mudah bergaul, enak diajak ngobrol, dan bertukar pikiran. 

		
		Bapak bisa mengenal lebih jauh tentang saya lewat Instagram saya pada tautan di bawah ini!
		"""
		)
		st.write("[Instagram Account >](https://www.instagram.com/kautsarpt/)")
	with right_column:
		st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
	st.write("---")
	st.header("Minat dan Ketertarikan :yellow_heart:")
	st.write("##")
	image_column, text_column = st.columns((1, 2))
	with image_column:
		st.image(img_cyber)
	with text_column:
		st.subheader("Cybersecurity")
		st.write(
		"""
		Saya sangat tertarik pada bidang Cybersecurity, karena keren aja bisa jadi hacker. Saya pernah ikut pelatihan Cybersecurity dari Infradigital Foundation. Belajarnya tentang Network+, Linux+, Security+. Dari pelatihan itu saya banyak mendapat pengetahuan baru soal Cybersecurity. Yang tadinya saya pikir ngehack itu gampang, ternyata prosesnya sangat panjang. Tapi yang seru adalah proses yang panjang itu pastinya.
		"""
		)
		st.markdown("[Highlight Cybersecurity ...](https://www.instagram.com/stories/highlights/17963148973545626/)")
with st.container():
	image_column, text_column = st.columns((1, 2))
	with image_column:
		st.image(img_python)
	with text_column:
		st.subheader("Python")
		st.write(
		"""
		Baru-baru ini saya juga belajar tentang bahasa pemrograman Python. Baru kemarin saya buat website profile diri saya, tapi yang sederhana.
		"""
		)
		st.markdown("[Highlight Python ...](https://www.instagram.com/stories/highlights/17931857603356966/)")

# ---- STORY ----
with st.container():
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("Sedikit Cerita :scroll:")
		st.write("##")
		st.write(
		"""
		Waktu kelas 10 pertama kali saya masuk SMKN 26, saya bisa langsung dipercaya untuk menjadi Ketua Kelas. Tapi kelas 11, saya tidak jadi Ketua Kelas lagi karena banyak hal yang mau saya lakukan. Tapi di kelas 12 ini, saya ada niatan lagi untuk menjadi Ketua Kelas.
	
		Saya juga ikut organisasi MPK. Di MPK, saya menjadi Kepala Divisi HuMas. Waktu itu ada masalah di SIJA sebelum Bapak dipindahtugaskan. Jadi saya sebagai tim MPK SIJA, mengajukan aspirasi SIJA kepada Pak Nur, yang alhamdulillah mendapatkan kabar baik, sehingga SIJA akan stabil lagi.
		"""
		)
		thanks = st.button("Klik ini, Pak!")
		if thanks:
			st.success(f"Terima kasih sudah membaca ya, Pak :blush:")
			st.balloons()
		
