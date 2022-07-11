from urllib import response
from fake_useragent import UserAgent
import requests
import json


ua = UserAgent()
# print(ua.random)

def collect_data(type_card=2):
    # response = requests.get(
    #     url='https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=30&isStore=true&limit=60&maxPrice=10000&minPrice=1&offset=0&sort=botFirst&type=2&withStack=true',
    #     headers = {'user-agent':f'{ua.random}'}
    # )
    # with open('result.json', 'w',encoding="utf-8") as file:
    #     json.dump(response.json(),file,indent=4,ensure_ascii=False)
    offset = 0
    batch_size = 60
    result = []
    count = 0
    while True:
        for item in range(offset, offset + batch_size, 60):
            # url=item
            # print(url)
            url=f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=30&isStore=true&limit=60&maxPrice=5000&minPrice=2000&offset={item}&sort=botFirst&type={type_card}&withStack=true'
            response = requests.get(
                url=url,
                headers = {'user-agent':f'{ua.random}'}
            )

            offset +=batch_size
            data = response.json()

            items = data.get('items')

            for i in items:
                if i.get('overprice') is not None and i.get('overprice') < -20:
                

                    item_full_name = i.get('fullName')
                    item_3d = i.get('3d')
                    item_price = i.get('price')
                    item_overprice = i.get('overprice')

                    result.append(
                        {
                        'full_name':item_full_name,
                        '3d':item_3d,
                        'overprice':item_overprice,
                        'item_price':item_price
                    }
                    )
        count+=1
        print(f'page #{count}')
        print(url)

        if len(items)< 60:
            break

    with open('result.json','w',encoding="utf-8") as file:
        json.dump(result,file,indent=4,ensure_ascii=False)
        
def return_back():
    return


def main():
    collect_data()
    return_back()


if __name__ == '__main__':
    main()