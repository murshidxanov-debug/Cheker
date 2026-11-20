import os, time, requests

TOKEN = os.environ["TG_TOKEN"]
CHAT_ID = os.environ["TG_CHAT"]
URL = "https://uzembassyryouji.rsvsys.jp/"
MARKER = "一時停止"

for i in range(5):
    try:
        html = requests.get(URL, timeout=20).text
        if MARKER not in html:
            requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                data={"chat_id": CHAT_ID,
                      "text": "Сайт очилди! Кириб бронлаб олинг: " + URL})
    except Exception as e:
        print(e)
    if i < 4:
        time.sleep(60)

