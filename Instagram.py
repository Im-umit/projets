import instaloader

# Instagram giriş bilgileri
username = 'pyden_eme'  # Instagram kullanıcı adınız
password = 'deneme0021'  # Instagram şifreniz

L = instaloader.Instaloader()

try:
    # Giriş yapma
    L.login(username, password)
    
except instaloader.exceptions.TwoFactorAuthRequiredException:
    print("İki faktörlü kimlik doğrulama gerekli.")
    verification_code = input("Doğrulama kodunu girin: ")

    # 2FA kodunu girerek doğrulama yapma
    L.context.do_two_factor_auth(verification_code)
    
    # Takip ettiğiniz kişileri alma
    profile = instaloader.Profile.from_username(L.context, username)
    following_list = [followee.username for followee in profile.get_followees()]

    print("Takip ettiğiniz kişiler:")
    for user in following_list:
        print(user)

except Exception as e:
    print(f"Giriş yapılamadı: {e}")