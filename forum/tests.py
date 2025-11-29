from django.test import TestCase

from io import BytesIO
import requests

# 1. Token al
login_url = "http://localhost:8080/api/token/"
login_data = {
    "Username": "salata",
    "password": "domates321"
}
res = requests.post(login_url, json=login_data)
res.raise_for_status()
tokens = res.json()
access_token = tokens["access"]

# 2. Me endpointinden user bilgilerini al
api_url = "http://localhost:8080/api/forum/likes/3/remove_like/"
headers = {"Authorization": f"Bearer {access_token}"}
res = requests.delete(api_url, headers=headers)
res.raise_for_status()
print(res.json())
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
