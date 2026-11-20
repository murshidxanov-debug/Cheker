import os, requests

TOKEN = os.environ["TG_TOKEN"]
CHAT_ID = os.environ["TG_CHAT"]
URL = "https://uzembassyryouji.rsvsys.jp/"
MARKER = "XXXX"

html = requests.get(URL, timeout=20).text
if MARKER not in html:
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                  data={"chat_id": CHAT_ID,
                        "text": "Сайт очилди! Кириб бронлаб олинг: " + URL})
