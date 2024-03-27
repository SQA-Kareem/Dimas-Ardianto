import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SystemTest(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Tambahkan penundaan waktu sebelum menutup WebDriver
        time.sleep(5)

        # Menutup WebDriver
        self.driver.quit()

    def login(self, username, password):
        # Temukan tombol login di dalam menu
        time.sleep(2)

        # Mencari elemen input username dan password menggunakan ID
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "hs-toggle-password")

        # Memasukkan nama pengguna dan kata sandi
        email_input.send_keys(username)
        password_input.send_keys(password)

        time.sleep(2)

        # Klik tombol Login
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        time.sleep(3)

        # Cari dan klik tombol OK pada popup
        swal = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
        swal.click()
    
        
    def menu_cari(self):
        time.sleep(2)

        # Mencari menu search dan klik
        search_button = self.driver.find_element(By.XPATH, "//a[@href='cariInternship.html']")
        search_button.click()

        time.sleep(2)

    def keywoard_search(self):
        time.sleep(2)
        # Mencari elemen input pencarian menggunakan ID
        posisi_input = self.driver.find_element(By.ID, "posisi")
        perusahaan_input = self.driver.find_element(By.ID, "nama")
        lokasi_input = self.driver.find_element(By.ID, "lokasi")

        # Memasukkan kata kunci pencarian
        posisi_input.send_keys("Front End Developer")
        perusahaan_input.send_keys("ARDIANT COMPANY")
        lokasi_input.send_keys("Jakarta Selatan")

        time.sleep(2)

        # Klik tombol cari
        button = self.driver.find_element(By.ID, "searchButton")
        button.click()

        time.sleep(1)

        # Scroll ke bawah
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Scroll ke atas
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

        # Button Clear
        button_clear = self.driver.find_element(By.ID, "clearButton")
        button_clear.click()

        time.sleep(2)

    def test_search_internship(self):
        # Membuka halaman web
        self.driver.get("https://intermoni.my.id/")

        time.sleep(2)

        button = self.driver.find_element(By.XPATH, "//a[@href='pages/signIn.html']")
        button.click()

        time.sleep(2)

        # Login dengan username dan password tertentu
        self.login("dimasmhs@gmail.com", "fghjkliow")
        self.menu_cari()
        self.keywoard_search()

if __name__ == "__main__":
    unittest.main()