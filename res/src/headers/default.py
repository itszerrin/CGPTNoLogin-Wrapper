from fake_useragent import UserAgent
from secrets import randbelow

from ...typing import Dict

def get_headers() -> Dict[str, str]: 

    return {
        "Host": "chatgptnologin.com",
        "User-Agent": f"{UserAgent().random}",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://chatgptnologin.com/chatbot",
        "Content-Type": "application/json",
        "Content-Length": f"{randbelow(100)}",
        "Origin": "https://chatgptnologin.com",
        "Alt-Used": "chatgptnologin.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"
    }