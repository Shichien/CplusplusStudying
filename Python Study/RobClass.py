import requests

cookies = {
    'semester.id': '1185',
    'JSESSIONID': '3CCBC11EDD2376F1D11206FD161D63BD',
    'Hm_lvt_f76f8c7e3ddd48018c54d9d37f42086a': '1702541565',
    'BIGipServerpool_202.120.83.236_80': '3964893386.20480.0000',
}

headers = {
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    # 'Cookie': 'semester.id=1185; JSESSIONID=3CCBC11EDD2376F1D11206FD161D63BD; Hm_lvt_f76f8c7e3ddd48018c54d9d37f42086a=1702541565; BIGipServerpool_202.120.83.236_80=3964893386.20480.0000',
    'Referer': 'https://applicationnewjw.ecnu.edu.cn/eams/home!childmenus.action?menu.id=844',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'menu.id': '845',
    '_': '1702739247061',
}

while True:
    response = requests.get(
    'https://applicationnewjw.ecnu.edu.cn/eams/home!childmenus.action',
    params=params,
    cookies=cookies,
    headers=headers,
    )
    print(response.text)
    res = json.loads(response.text)
    flag = res['flag']
    localtime = time.asctime(time.localtime(time.time()))
    if flag == "-1":
        print(loadtime, "Code is Running Successfully.")

        time.sleep(2)
