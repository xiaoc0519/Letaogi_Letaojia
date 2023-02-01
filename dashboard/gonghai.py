import requests
import json,random,re,datetime

common_sea = 'https://letaojiabackstage.letaojiashop.com/Mall/GetCommonSea?page=1&limit=20&creditid=9&random={}'.format(random.randint(11111111,99999999))

headers = {
        'Content-Type': 'application/json',
        'cookie' : '',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.23'
    }

def postmsg(msg):
    webhook = ''
    header = {
        'Content-Type': 'application/json'
    }
    body = {
        'msgtype': 'markdown',
        'markdown': {
            "content": msg
        }
    }
    requests.post(webhook, headers=header, data=json.dumps(body))


req = requests.get(url = common_sea,headers=headers,verify=False)
csjc = json.loads(req.text)
if csjc['count'] == 0:
    print(req.text+' '+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
if csjc['count'] > 0:
    print('{"code":0,"msg":null,"count":'+str(csjc['count'])+',"data":[]} '+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    csjcd = json.loads(req.text).get('data')
#    postmsg('{} 新增 {} 个'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),csjc['count']))
    if len(csjcd)>30:
        csjcd = csjcd[:30]
    for i in csjcd:
        codeid = i['codeid']
        price = i['price']
        types = i['types']

        dl = 'https://letaojiabackstage.letaojiashop.com/Mall/SalvageMall'
        dalao = requests.post(url = dl,headers=headers,data=json.dumps({'codeid':codeid}))
        did = json.loads(dalao.text)
        if did['code'] == 0:
            break
        pt = did['msg'].replace("<span style='color:red'>",'')
        pt = pt.replace("<span style='color:blue'>",'')
        pt = pt.replace('</span>','')

        get_url = 'https://letaojiabackstage.letaojiashop.com/Mall/MallEdit?id={}'.format(codeid)
        t2 = requests.get(get_url, headers=headers)
        html = t2.text

        level = re.findall('<select name="credit" lay-verify="required">.*?selected>(.*?)</option>', html, re.S)
        shoptime = re.findall('id="yearOnly" class="layui-input" value="(.*)"', html)

        infou = 'https://letaojiabackstage.letaojiashop.com/Mall/GetMallInfo'
        a = requests.post(infou, headers=headers, data=json.dumps({'codeid':codeid}))
        info = json.loads(a.text)
        # print(info+' '+str(dtime.now()))
        shopurl = re.findall('(\w+.taobao.com)',info['shopurl'])
        shopurl = shopurl[0]
        if shopurl == '':
            shopurl = codeid
        try:
            f = '{} {} {} {} \n**{}**  {} \n{} \n'.format(\
                    types,level[0],price,shoptime[0],info['mobile'],info['shopkeeper'],shopurl)
            f = f+'\n'+pt+'\n'+str(datetime.datetime.now())
        except:
            f = info
        print(codeid)
        postmsg(f)
#        postmsg(pt)
