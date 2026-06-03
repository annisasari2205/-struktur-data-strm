import streamlit as st
from collections import deque

# =====================================
# KELAS PRIORITY QUEUE
# =====================================
class PuskesmasQueue:
    def __init__(self):
        self.darurat = deque()
        self.lansia = deque()
        self.ibu_hamil = deque()
        self.umum = deque()
        self.nomor = 0

    def tambah_pasien(self, nama, kategori):
        self.nomor += 1

        pasien = {
            "nomor": self.nomor,
            "nama": nama,
            "kategori": kategori
        }

        if kategori == "Darurat":
            self.darurat.append(pasien)

        elif kategori == "Lansia":
            self.lansia.append(pasien)

        elif kategori == "Ibu Hamil":
            self.ibu_hamil.append(pasien)

        else:
            self.umum.append(pasien)

        return self.nomor

    def panggil_pasien(self):

        if self.darurat:
            return self.darurat.popleft()

        elif self.lansia:
            return self.lansia.popleft()

        elif self.ibu_hamil:
            return self.ibu_hamil.popleft()

        elif self.umum:
            return self.umum.popleft()

        return None

    def tampilkan(self):
        return (
            list(self.darurat),
            list(self.lansia),
            list(self.ibu_hamil),
            list(self.umum)
        )


# =====================================
# SESSION STATE
# =====================================
if "antrian" not in st.session_state:
    st.session_state.antrian = PuskesmasQueue()

# =====================================
# HALAMAN
# =====================================
st.set_page_config(
    page_title="Sistem Antrean Puskesmas",
    layout="wide"
)

st.title("🏥 SISTEM ANTREAN PUSKESMAS")
st.markdown("---")

# =====================================
# MENU UTAMA
# =====================================
menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "Beranda",
        "Daftar Pasien",
        "Lihat Antrean",
        "Panggil Pasien"
    ]
)

# =====================================
# BERANDA
# =====================================
if menu == "Beranda":

    st.header("Selamat Datang")

    st.write("""
    Sistem Antrean Puskesmas menggunakan
    Priority Queue.

    Prioritas:
    1. Darurat
    2. Lansia
    3. Ibu Hamil
    4. Umum
    """)

# =====================================
# DAFTAR PASIEN
# =====================================
elif menu == "Daftar Pasien":

    st.header("📝 Pendaftaran Pasien")

    kategori = st.selectbox(
        "Kategori Pasien",
        [
            "Umum",
            "Ibu Hamil",
            "Lansia",
            "Darurat"
        ]
    )

    nama = st.text_input(
        "Masukkan Nama Pasien"
    )

    if st.button("Ambil Nomor Antrean"):

        if nama:

            nomor = (
                st.session_state.antrian
                .tambah_pasien(
                    nama,
                    kategori
                )
            )

            st.success(
                f"Nomor Antrean Anda : {nomor}"
            )

        else:
            st.warning(
                "Nama pasien harus diisi!"
            )

# =====================================
# LIHAT ANTREAN
# =====================================
elif menu == "Lihat Antrean":

    st.header("📋 Daftar Antrean")

    darurat, lansia, ibu_hamil, umum = (
        st.session_state.antrian.tampilkan()
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🚑 Darurat")

        for p in darurat:
            st.write(
                f"No {p['nomor']} - {p['nama']}"
            )

        st.subheader("👴 Lansia")

        for p in lansia:
            st.write(
                f"No {p['nomor']} - {p['nama']}"
            )

    with col2:

        st.subheader("🤰 Ibu Hamil")

        for p in ibu_hamil:
            st.write(
                f"No {p['nomor']} - {p['nama']}"
            )

        st.subheader("👤 Umum")

        for p in umum:
            st.write(
                f"No {p['nomor']} - {p['nama']}"
            )

# =====================================
# PANGGIL PASIEN
# =====================================
elif menu == "Panggil Pasien":

    st.header("📢 Panggil Pasien")

    if st.button("Panggil Berikutnya"):

        pasien = (
            st.session_state.antrian
            .panggil_pasien()
        )

        if pasien:

            st.success(
                f"Nomor {pasien['nomor']} - "
                f"{pasien['nama']} "
                f"({pasien['kategori']}) "
                f"silakan menuju ruang pemeriksaan"
            )

        else:
            st.warning(
                "Tidak ada pasien dalam antrean"
            )
