import requests

end_point_url = "https://zipcloud.ibsnet.co.jp/api/search"

post_code = int(input("郵便番号を入力してください: "))

params = {
    "zipcode": post_code
}

response = requests.get(end_point_url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data["results"][0]["address1"] + data["results"][0]["address2"] + data["results"][0]["address3"])
else:
    print(f"エラーが発生しました。ステータスコード:{response.status_code}")
