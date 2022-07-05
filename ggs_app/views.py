from django.http import JsonResponse
from django.shortcuts import render
import requests
from requests_oauthlib import OAuth1
import os
from dotenv import load_dotenv
import json

load_dotenv()


def main(request):
    return render(request, 'ggs_app/main.html')


def shirts(request):
    items = {'shirts': store}
    return render(request, 'ggs_app/shirts.html', items)


def socks(request):
    items = {'socks': store}
    return render(request, 'ggs_app/socks.html', items)


def supplements(request):
    items = {'supplements': store}
    return render(request, 'ggs_app/supplements.html', items)


def cart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    print('Cart:', cart)
    items = []
    order = {'total_items': 0, 'total_cost': 0}

    for i in cart:
        if int(i) >= 7:
            total = 45 * cart[i]['quantity']
        elif int(i) <= 3:
            total = 25 * cart[i]['quantity']
        else:
            total = 12 * cart[i]['quantity']
        order['total_items'] += cart[i]['quantity']
        order['total_cost'] += total
        for j in store:
            if int(i) == j['id']:
                product = {
                    'id': store[int(i) - 1]['id'],
                    'name': store[int(i) - 1]['name'],
                    'price': store[int(i) - 1]['price'],
                    'photo': store[int(i) - 1]['photo'],
                    'quantity': cart[i]['quantity'],
                    'get_total': total
                }
                items.append(product)

    basket = {'items': items, 'order': order}
    print(basket)
    return render(request, 'ggs_app/cart.html', basket)


def search(request):
    return render(request, 'ggs_app/search.html')


def result(request):
    query = request.GET.get('query')
    auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])
    endpoint = f"http://api.thenounproject.com/icon/{query}"
    API_response = requests.get(endpoint, auth=auth)
    json_API_response = json.loads(API_response.content)
    img_url = json_API_response['icon']['preview_url']
    return JsonResponse({'url': img_url})


store = [
    {
        'id': 1,
        'type': 'shirt',
        'photo': 'https://i.etsystatic.com/12906150/r/il/637ba2/2750528600/il_1588xN.2750528600_mcw4.jpg',
        'name': 'Hard Corps',
        'price': 25,
    },
    {
        'id': 2,
        'type': 'shirt',
        'photo': 'https://res.cloudinary.com/teepublic/image/private/s--zh-aNnzR--/t_Resized%20Artwork/c_crop,x_10,y_10/c_fit,w_320/c_crop,g_north_west,h_626,w_470,x_-73,y_-36/g_north_west,u_upload:v1571669489:production:blanks:jaeeqnv4r8crsxalh03n,x_-468,y_-361/b_rgb:eeeeee/c_limit,f_auto,h_630,q_90,w_630/v1506443051/production/designs/1931511_1.jpg',
        'name': 'R4',
        'price': 25,
    },
    {
        'id': 3,
        'type': 'shirt',
        'photo': 'https://res.cloudinary.com/teepublic/image/private/s--HXYheOEK--/t_Resized%20Artwork/c_crop,x_10,y_10/c_fit,w_470/c_crop,g_north_west,h_626,w_470,x_0,y_0/g_north_west,u_upload:v1462829015:production:blanks:mtl53ofohwq5goqjo9ke,x_-395,y_-325/b_rgb:eeeeee/c_limit,f_auto,h_630,q_90,w_630/v1557944278/production/designs/4849871_0.jpg',
        'name': 'Battletoads/Double Dragon',
        'price': 25,
    },
    {
        'id': 4,
        'type': 'socks',
        'photo': 'https://images.fun.com/products/69244/1-1/-striped-knee-high-socks--cuphead--mugman.jpg',
        'name': 'Cuphead Socks',
        'price': 12

    },
    {
        'id': 5,
        'type': 'socks',
        'photo': 'https://cdn.shopify.com/s/files/1/0317/1509/products/30848MONCD-3_085aee83-ea41-4a07-8f10-a1809886a8ab.jpg',
        'name': 'Megaman Socks',
        'price': 12

    },
    {
        'id': 6,
        'type': 'socks',
        'photo': 'https://cdn.shopify.com/s/files/1/0051/3825/1869/products/MBM-999-313-5-fr-xxl_1365x.jpg?v=1634220159',
        'name': 'Punch-Out! Socks',
        'price': 12
    },
    {
        'id': 7,
        'type': 'supplements',
        'photo': 'https://i0.wp.com/fatherhoodreloaded.com/wp-content/uploads/2022/04/278268255_3298977400426010_4330680277021500046_n.jpg?resize=820%2C1024&ssl=1',
        'name': 'Ghost Turtle Ooze Pump',
        'price': 45

    },
    {
        'id': 8,
        'type': 'supplements',
        'photo': 'https://i.ebayimg.com/images/g/mKcAAOSwX9lgo~lg/s-l500.jpg',
        'name': 'Ghost Chips Ahoy Protein',
        'price': 45

    },
    {
        'id': 9,
        'type': 'supplements',
        'photo': 'https://i.ebayimg.com/images/g/7BsAAOSwdZRg~fl1/s-l500.jpg',
        'name': 'Tetris G-Fuel',
        'price': 45
    }
]
