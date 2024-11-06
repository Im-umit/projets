import requests

# Giriş yapılacak web sitesinin URL'si
url = 'https://www.instagram.com/accounts/login/'

# Giriş bilgileri
login_data = {
    'username': 'pyden_eme',
    'password': 'py1234'
}

# Giriş isteğini POST olarak gönder
with requests.Session() as session:
    response = session.post(url, data=login_data)
    
    # Başarılı giriş kontrolü
    if response.ok:
        print("Giriş başarılı!")
    else:
        print("Giriş başarısız.")

    # Giriş sonrası, giriş yapılmış sayfayı kontrol edelim
    dashboard_url = 'https://www.instagram.com/accounts/login/'
    dashboard_response = session.get(dashboard_url)
    print(dashboard_response.text)  # Giriş sonrası sayfa içeriği