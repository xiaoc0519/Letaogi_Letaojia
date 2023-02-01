// ==UserScript==
// @name         ltj_fuck_dashboard
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  try_to_take_over_the_world!
// @author       Xiaoc
// @match        登陆后网址粘贴在这里
// @icon         https://www.google.com/s2/favicons?sz=64&domain=letaojiashop.com
// @downloadURL    https://greasyfork.org/zh-CN/scripts/455586-dashboard
// @grant        none
// ==/UserScript==

(function() {
    window.onload = function(){
        var sideAll = document.getElementsByClassName('layui-nav-child')[1]
        var btn1 = sideAll.getElementsByTagName('dd')[0]
        let nav = document.createElement('nav')
        btn1.onclick = function(){
            var new_e = $('div.layui-tab-content div.layui-tab-item:last')[0]
            var iframed = new_e.getElementsByTagName('iframe')[0]
            iframed.onload = function(){
                var ifnav = iframed.contentWindow.document.getElementsByClassName('br')[0]
                let input = document.createElement('input')
                input.setAttribute('class','layui-btn layui-btn-sm')
                input.setAttribute('type','button')
                input.setAttribute('id','nav')
                input.value = 'Click me'
                ifnav.appendChild(input)
                nav = iframed.contentWindow.document.getElementById('nav')
                nav.onclick = function(){
                    iframed.contentWindow.document.getElementById('btn').nextElementSibling.click()
                    var title = iframed.contentWindow.document.getElementsByClassName('layui-layer-title')[0]
                    title.style.textAlign = 'left'
                    title.style.width = '10vw'
                    title.style.float = 'left'
                    var result = []
                    function abtn(inp,value){
                        inp.setAttribute('class','layui-btn')
                        inp.setAttribute('type','button')
                        inp.value = value
                        inp.style.margin = '3px'
                        title.after(inp)
                    }
                    var inp = document.createElement('input')
                    abtn(inp,'<(￣︶￣)↗[GO!]')
                    inp.onclick = function(){
                        let dataa = prompt()
                        let list = dataa.split(',')
                        let iiframeddom = iframed.contentWindow.document.getElementById('layui-layer-iframe1')
                        let iiframed = iiframeddom.contentWindow.document
                        let line = iiframed.getElementsByClassName('layui-form-item')
                        line[1].firstElementChild.getElementsByClassName('layui-input-inline')[0].childNodes[2].firstElementChild.firstElementChild.click()
                        line[1].firstElementChild.getElementsByClassName('layui-input-inline')[0].childNodes[2].childNodes[1].childNodes[23].click()
                        let a = list[0]
                        let rankl = a<4?0:a<=10?1:a<=40?2:a<=90?3:a<=150?4:a<=250?5:a<=500?6:a<=1000?7:a<=2000?8:a<=5000?9:a<=10000?10:a<=20000?11:a<=50000?12:a<=100000?13:a<=200000?14:a<=500000?15:a<=1000000?16:a<=2000000?17:a<=5000000?18:a<=10000000?19:20
                        line[1].childNodes[5].childNodes[3].lastElementChild.firstElementChild.firstElementChild.click()
                        line[1].childNodes[5].childNodes[3].childNodes[2].childNodes[1].childNodes[rankl].click()
                        line[1].childNodes[7].lastElementChild.childNodes[2].firstElementChild.firstElementChild.click()
                        console.log(Number(list[1])+1)
                        line[1].childNodes[7].lastElementChild.childNodes[2].childNodes[1].childNodes[Number(list[1])+1].click()
                        line[1].childNodes[19].lastElementChild.childNodes[2].childNodes[1].childNodes[list[2]].click()
                        line[1].childNodes[23].childNodes[3].firstElementChild.value = list[3]
                        line[1].childNodes[11].firstElementChild.click()
                        line[2].lastElementChild.childNodes[11].click()
                        line[3].lastElementChild.firstElementChild.childNodes[3].firstElementChild.value = list[4]
                        line[3].lastElementChild.lastElementChild.lastElementChild.firstElementChild.value = list[5]
                        line[5].firstElementChild.childNodes[1].lastElementChild.firstElementChild.value = list[6] == -2?0:list[6]
                        line[5].firstElementChild.childNodes[1].lastElementChild.lastElementChild.lastElementChild.childNodes[list[7] == 1?1:list[7]==0?1:list[7] == 2?3:2].click()
                        line[5].firstElementChild.childNodes[3].lastElementChild.firstElementChild.value = list[8] == -2?0:list[8]
                        line[5].firstElementChild.childNodes[3].lastElementChild.lastElementChild.lastElementChild.childNodes[list[9] == 1?1:list[9]==0?1:list[9] == 2?3:2].click()
                        line[5].firstElementChild.childNodes[5].lastElementChild.firstElementChild.value = list[10] == -2?0:list[8]
                        line[5].firstElementChild.childNodes[5].lastElementChild.lastElementChild.lastElementChild.childNodes[list[11] == 1?1:list[11]==0?1:list[11] == 2?3:2].click()
                    }

                }
            }
        }
    }
})();
