# v 1.1
from wsgiref import headers
import requests
import json
import random
import datetime

type = ['网店估价', '快捷出售']
requests.DEFAULT_RETRIES = 5

cookie = ''
name = ''
webhook = ''

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'

def order(ck, url, t, body):
    headers = {
        'Cookie': ck,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.23',
        'Content-Type': 'application/json'
    }
    req = requests.post(url=url, headers=headers, data=json.dumps(body))
    reqq = json.loads(req.text)
    if reqq['code'] == 1:
        bo = {
            'msgtype': 'markdown',
            'markdown': {
                "content": f'{type[t]}  Ordered , Check & Contact <@{name}>'
            }
        }
        requests.post(webhook,
                      headers={'Content-Type': 'application/json'}, data=json.dumps(bo))
        return reqq['code']
    else:
        return 0


def isorder(t, pid):
    ourl = 'https://letaojiabackstage.letaojiashop.com/Common/ValuationEdit' if t == 0 else 'https://letaojiabackstage.letaojiashop.com/Common/SellMallEdit'
    id = 'itemid' if t == 0 else 'id'
    body = {id: pid}
    order(cookie, ourl, t, body)


def check(h, t=0):
    url = 'https://letaojiabackstage.letaojiashop.com/Common/GetValuation?random={}'.format(random.randint(00000000, 99999999)) if t == 0 else 'https://letaojiabackstage.letaojiashop.com/Common/GetSellMall?random={}'.format(
        random.randint(0000000, 9999999))
    try:
        req = requests.get(url=url, headers=h)
    except:
        req = requests.get(url=url, headers=h)
    mem = json.loads(req.text).get('data')
    for i in mem:
        if i['truename'] == '':
            isorder(t, int(i['id']) if t == 1 else int(i['itemid']))


headers = {'User-Agent': ua,
           'Cookie': cookie,
           'Connection': 'close'}

check(headers)
check(headers, 1)
print(str(datetime.datetime.now())+' check finish')
