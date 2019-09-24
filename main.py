import requests


def main():
    # 入力
    zipcode = input('郵便番号を入力してください:')
    if len(zipcode) != 7:


    url = f'http://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}'

    # 計算
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
