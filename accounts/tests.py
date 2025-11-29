from django.test import TestCase

from io import BytesIO
import requests

# 1. Token al
login_url = "https://muratyl2k4.pythonanywhere.com/api/token/"
login_data = {
    "Username": "salata",
    "password": "domates321"
}
res = requests.post(login_url, json=login_data)
res.raise_for_status()
tokens = res.json()
access_token = tokens["access"]

# 2. Me endpointinden user bilgilerini al
api_url = "https://muratyl2k4.pythonanywhere.com/api/accounts/"
headers = {"Authorization": f"Bearer {access_token}"}
res = requests.get(api_url, headers=headers)
print(res.json())
# res.raise_for_status()
# user_data = res.json()

# # 3. Profile_Picture URL’ini al
# image_url = user_data.get("Profile_Picture")
# if not image_url:
#     print("User has no profile picture.")
# else:
#     # 4. Image’i indir
#     img_res = requests.get(image_url)
#     img_res.raise_for_status()
#     img_file = BytesIO(img_res.content)
    
#     # İsteğe bağlı: kaydetmek
#     with open("downloaded_profile_picture.jpg", "wb") as f:
#         f.write(img_file.getbuffer())
#     print("Profile picture downloaded successfully.")
