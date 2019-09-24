import requests


def main():
    # 1600023->'東京都新宿区西新宿'
    # 入力
    zipcode = '1600023'
    url = f'http://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}'

    # 計算
    # リクエスト送る->受け取ってParse(->フォーマット)
    response = requests.get(url)

    # 出力

    json = response.json()
    address = json['results'][0]
    # for n in range(1, 4):
    #     print(json['results'][0][f'address{n}'])  <-何の情報を print してるのか初見ではわかりにくい！！！！

    prefecture = address['address1']
    city = address['address2']
    town = address['address3']

    print(f'{prefecture}{city}{town}')


if __name__ == '__main__':
    main()
