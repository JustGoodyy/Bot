import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

last_pengumuman = None

def cek_pengumuman_baru():
    global last_pengumuman

    session = requests.Session()
    login_url = 'https://learning-if.polibatam.ac.id/login/index.php'
    login_page = session.get(login_url)
    soup_login = BeautifulSoup(login_page.text, 'html.parser')
    token_input = soup_login.find('input', attrs={'name': 'logintoken'})
    logintoken = token_input['value'] if token_input else ''

    payload = {
        'username': USERNAME,
        'password': PASSWORD,
        'logintoken': logintoken
    }
    session.post(login_url, data=payload)

    notif_url = 'https://learning-if.polibatam.ac.id/my/'
    response = session.get(notif_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    pengumuman_div = soup.find('div', class_='pengumuman')
    if pengumuman_div:
        pengumuman = pengumuman_div.text.strip()
        if pengumuman != last_pengumuman:
            last_pengumuman = pengumuman
            return pengumuman
    return None
























# Step 1: Login
#login_url = 'https://learning-if.polibatam.ac.id/login/index.php'
#payload = {
    #'username': '4312501040',
    #'password': '4312501040'
#}
#session.post(login_url, data=payload)

# Step 2: Akses halaman notifikasi
#notif_url = 'https://learning-if.polibatam.ac.id/my/'
#response = session.get(notif_url)
#soup = BeautifulSoup(response.text, 'html.parser')

#Step 3: Ambil data penting
#notifikasi = soup.find_all('div', class_='pengumuman')