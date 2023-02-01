// ==UserScript==
// @name         ltj_taobao_data_show
// @namespace    http://tampermonkey.net/
// @version      1.5
// @description  try to take over the world!
// @author       Xiaoc
// @match        https://rate.taobao.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=taobao.com
// @grant        none
// @require      https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js
// ==/UserScript==

(function () {
    'use strict';

    window.onload = function () {

            if(document.getElementById('ks-component227')){
                1
            }else{
                var elm = function (e, text, top, color) {
                    e.innerHTML = text
                    e.style.position = 'fixed'
                    e.style.fontWeight = 'bold'
                    e.style.right = '5%'
                    e.style.top = top
                    e.style.color = color
                    e.style.zIndex = '100'
                    e.style.cursor = 'pointer'
                    document.getElementsByTagName('body')[0].appendChild(e)
                }
                //  查不到开店时间 用 https://main.m.taobao.com/search/index.html?spm=a215s.7406091.topbar.1.560c67702I7NFb&pageType=4&q=店铺名
                //  手套开店时间 里项目


                let cc = document.createElement('cc')
                elm(cc, '关闭', '55%', 'red')
                let fans = document.createElement('fans')
                elm(fans, '粉丝', '25%', 'deeppink')
                let homep = document.createElement('homep')
                elm(homep, '主页', '20%', 'purple')
                let ssidebar = document.createElement('sidebar')
                elm(ssidebar, '一次性打码', '50%', 'blue')
                let copy = document.createElement('copy')
                elm(copy, '复制店铺数据', '45%', 'orange')
                let st = document.createElement('copy')
                elm(st, '手淘', '15%', 'orange')
                var check = document.createElement('sidebar')
                check.style.padding = '5px 10px'
                elm(check, '显', '30%', 'black')
                st.onclick = function () {
                    document.getElementsByClassName('col-sub')[0].firstElementChild.getElementsByTagName('a')[0].click()
                }
                check.onclick = function () {
                    document.getElementsByClassName('col-sub')[0].firstElementChild.getElementsByTagName('a')[0].click()
                }
                cc.onclick = function () {
                    window.close()
                }
                copy.onclick = function () {
                    var outt = []
                    // 判断是否是企业店铺
                    var isP = 1
                    if($('div.tmall-pro').length == 1){isP = 2}
                    // 企业logo代码 $('div.tmall-pro')

                    // 好评率
                    let tableZone = document.getElementsByClassName('ks-switchable-panel-internal12')[1]
                    let tbzp = tableZone.parentElement.parentElement.parentElement.parentElement.parentElement
                    let emdom = tbzp.getElementsByClassName('hd')[0]
                    var rnum = emdom.innerText.match(/(\d+.\d+)/)[0]
                    //主页
                    let ul = window.location.href
                    let ull = ul.match(/\?(.*)/)[0]
                    let va = document.getElementById('J_ShopIdHidden').value
                    let uvalue = `https://shop${va}.taobao.com/${ull}`
                    //信誉等级 需要提取数字处理

                    //判断是否半年内有服务分
                    var ti = $('div.bd .info-block .title')[0].innerText
                    if($('.item-scrib em.count').length ==0 ){
                        let mlist = '珠宝首饰,书籍音像,车品配件,其他行业,游戏话费,玩乐收藏,食品保健,运动户外,3C数码,母婴用品,美容护理,家装家饰,家居用品,服饰鞋包,淘宝农资,生活服务'.split(',')
                        outt.push(mjxyn,mlist.indexOf(Ptext[pie].replace('/','')=='母婴'?'母婴用品':Ptext[pie].replace('/','')),isP,rnum,uvalue,ti,-2,-2,-2,-2,-2,-2)
                    }else{
                        function count(n){return $('.item-scrib em.count')[n].innerText}
                        function check(n){return $('.item-scrib em strong')[n].getAttribute('class')== 'percent over'? '1':($('.item-scrib em strong')[n].getAttribute('class')== 'percent lower'?'-1':'0')}
                        //['珠宝首饰', '书籍音像', '车品配件', '其他行业', '游戏话费', '玩乐收藏', '食品保健', '运动户外', '3C数码', '母婴用品', '美容护理', '家装家饰', '家居用品', '服饰鞋包', '淘宝农资', '生活服务']
                        let mlist = '珠宝首饰,书籍音像,车品配件,其他行业,游戏话费,玩乐收藏,食品保健,运动户外,3C数码,母婴用品,美容护理,家装家饰,家居用品,服饰鞋包,淘宝农资,生活服务'.split(',')
                        outt.push(mjxyn,mlist.indexOf(Ptext[pie].replace('/','')=='母婴'?'母婴用品':Ptext[pie].replace('/','')),isP,rnum,uvalue,ti,count(0),check(0),count(1),check(1),count(2),check(2))
                    }
                    navigator.clipboard.writeText(outt)
                    alert('Copy successful')
                }
                homep.onclick = function () {
                    let ul = window.location.href
                    let ull = ul.match(/\?(.*)/)[0]
                    let va = document.getElementById('J_ShopIdHidden').value
                    let uvalue = `https://shop${va}.taobao.com/${ull}`
                    window.open(uvalue)
                }

                fans.onclick = function () {
                    let ul2 = window.location.href
                    let ull2 = ul2.match(/\?(.*)/)[0]
                    let va2 = document.getElementById('J_ShopIdHidden').value
                    let uvalue2 = `https://shop${va2}.m.taobao.com/${ull2}`
                    window.open(uvalue2)
                }

                ssidebar.onclick = function () {
                    hs()
                    as()
                    service()
                    dongtai()
                }

                var a = document.getElementById('relalist')
                var b = a.getElementsByClassName('rate-item').length

                var tableZone = document.getElementsByClassName('ks-switchable-panel-internal12')[1]
                var block =tableZone.getElementsByTagName('td')
                var c = block[5].innerText

                var montz = document.getElementsByClassName('ks-switchable-panel-internal12')[2]
                var bmon =montz.getElementsByTagName('td')
                var mon = bmon[5].innerText

                var Pdata= document.getElementById('rate-chart')
                var Ptext =Pdata.getAttribute('data-names').split(',')
                var Pnums = Pdata.getAttribute('data-datas').split(',')
                let maxnum = Math.max(...Pnums)
                var pie = Pnums.indexOf(maxnum.toString())

                try{var wtime= document.getElementsByClassName('tb-r-date')[0].innerText}catch(e){wtime = 'No DATE'}
                let mjxy = document.getElementsByClassName('sep')[0]
                let ret = mjxy.innerText
                let mjxyn = ret.match(/(\d+)/)[0]
                let price
                if(mjxyn<=20000){
                    price = 1.0
                }
                if(mjxyn<=50000 && mjxyn >20000){
                    price = 1.3
                }
                if(mjxyn<=100000 && mjxyn >50000){
                    price = 1.7
                }
                if(mjxyn<=200000 && mjxyn >100000){
                    price = 2.7
                }
                if(mjxyn<=500000&& mjxyn >200000){
                    price = 3.7
                }

                //check.innerHTML = ` Recently praised (Mon/Half Year):  ${c} / ${mon} <br> Number of comments:  ${b}+ <br> Estimated price:  ${price} (Reference Only)<br> Main industry: ${Ptext[pie].replace('/','')} ${maxnum}<br>Recently placed order:  <br> ${wtime}`
                check.innerHTML = `最近评价(月/半年):  ${c} / ${mon} <br> 评论数:  ${b}+ <br> 价格:  ${price} (预计)<br> 主营类目: ${Ptext[pie].replace('/','')} ${maxnum}<br>最近下单时间:  <br> ${wtime}`
                if(c<=30){
                    check.style.backgroundColor = 'green'
                    check.style.color = 'white'
                    //document.getElementsByClassName('col-sub')[0].firstElementChild.getElementsByTagName('a')[0].click()
                }
                if(c>30){
                    check.style.backgroundColor = 'red'
                }


                var hs = function () {
                    document.getElementById('chart-num').innerText = ''
                    let frameDom = document.getElementsByClassName('frame')[0]
                    let l = frameDom.getElementsByClassName('list')
                    l[0].innerHTML = l[0].innerHTML.replace(/\d+/, '')
                    l[1].innerHTML = l[1].innerHTML.replace(/\d+/, '')
                    l[2].innerHTML = l[2].innerHTML.replace(/\d+.\d+/, '')
                }

                var as = function () {
                    let tableZone = document.getElementsByClassName('ks-switchable-panel-internal12')[1]
                    let block = tableZone.getElementsByTagName('td')
                    let w = [5, 6, 7, 9, 10, 11, 13, 14, 15]
                    for (var i in w) {
                        block[w[i]].innerText = block[w[i]].innerText.replace(/\d+/, 'N')
                    }
                    let tbzp = tableZone.parentElement.parentElement.parentElement.parentElement.parentElement
                    let emdom = tbzp.getElementsByClassName('hd')[0]
                    var rnum = emdom.innerText.match(/(\d+.\d+)/)[0]
                    let b = Math.floor(rnum)
                    emdom.innerHTML = emdom.innerHTML.replace(/\d+.\d+/, b)
                }

                var service = function () {
                    let a = document.getElementsByClassName('main-wrap')[0]
                    let service = a.getElementsByClassName('bd')[1]

                    let left = service.getElementsByClassName('summary')[0]
                    let num = left.getElementsByClassName('my-val')
                    num[1].innerHTML = num[1].innerHTML.replace(/\d+.\d+/, '')
                    num[2].innerHTML = num[2].innerHTML.replace(/\d+.\d+/, '')
                    let n = left.getElementsByClassName('ind-val')
                    n[1].innerHTML = n[1].innerHTML.replace(/\d+.\d+/, '')
                    n[2].innerHTML = n[2].innerHTML.replace(/\d+.\d+/, '')

                    let right = service.getElementsByClassName('detail')[0]
                    let m = right.getElementsByClassName('title')[0]
                    let emd = m.getElementsByTagName('em')[0]
                    emd.innerHTML = emd.innerHTML.replace(/\d+.\d+/, '')
                }

                var dongtai = function () {
                    let a = document.getElementById('dsr')
                    a.getElementsByClassName('count')[0].innerHTML = 'N'
                    a.getElementsByClassName('count')[6].innerHTML = 'N'
                    a.getElementsByClassName('count')[12].innerHTML = 'N'
                    a.getElementsByClassName('percent over')[2].innerHTML = 'N'
                    a.getElementsByClassName('percent over')[0].innerHTML = 'N'
                    a.getElementsByClassName('percent over')[1].innerHTML = 'N'

                    let e = a.getElementsByClassName('box-wrap')
                    e[0].getElementsByTagName('span')[1].innerHTML = 'N'
                    e[1].getElementsByTagName('span')[1].innerHTML = 'N'
                    e[2].getElementsByTagName('span')[1].innerHTML = 'N'

                    let g = a.getElementsByClassName('h')
                    for (var i = 0; i < g.length; i++) { g[i].innerHTML = g[i].innerHTML.replace(/\d+.\d+/, '') }
                
                }}}
})();
