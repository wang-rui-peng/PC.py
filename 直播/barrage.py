import random,time
import requests
while True:
    lis = ["主播666", "主播真帅", "666"]
    word = random.choice(lis)
    url = "https://api.live.bilibili.com/msg/send"
    data = {
        "bubble": "0",
        "msg": word,
        "color": "16777215",
        "mode": "1",
        "fontsize": "25",
        "rnd": "1690366170",
        "roomid": "23170544",
        "csrf": "2f4a61c64f3965cdc8942abed979f0c9",
        "csrf_token": "2f4a61c64f3965cdc8942abed979f0c9",
    }
    headers = {
    "COOKIE": "buvid3=388DACC5-4E2D-70FA-08EE-915709BE35A921110infoc; b_nut=1667789121; CURRENT_FNVAL=4048; rpdid=|(J~J|ll||mR0J'uYYmRlJRm); _uuid=8110CEC3E-AD62-755D-C9EC-28D3B9F23AC982061infoc; buvid4=8557D499-D049-7919-0584-4474B053956183184-023020219-E0glGruAoXLPnRsA1LkgLQ%3D%3D; buvid_fp=ec13f19f7112ba768ffa74c59919a349; i-wanna-go-back=-1; header_theme_version=CLOSE; home_feed_column=5; nostalgia_conf=-1; SESSDATA=ccc384cc%2C1693724684%2Cc2ab1%2A31; bili_jct=2f4a61c64f3965cdc8942abed979f0c9; DedeUserID=369457363; DedeUserID__ckMd5=3623c1ee8388f06b; CURRENT_QUALITY=80; b_ut=5; FEED_LIVE_VERSION=V8; innersign=0; b_lsid=2C2DEDC1_18991ABC9F4; browser_resolution=2066-1012; LIVE_BUVID=AUTO5616903661143654",
    "origin": "https://www.bilibili.com",
    "referer": "https://www.bilibili.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183"
    }
    response= requests.post(url=url, data=data, headers=headers)
    print(response.text)
    print('6666666666666666666666666666666666666666666666')
    time.sleep(5)