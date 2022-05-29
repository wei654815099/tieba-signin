from time import sleep
from requests_html import HTMLSession
import logging
import requests
import os
import schedule
import time

class TieBa:

    cookies = ""
    myLikeUri = "https://tieba.baidu.com/f/like/mylike"
    signInUri = "https://tieba.baidu.com/sign/add"

    def __init__(self, cookies):
        self.cookies = cookies
        pass

    def __getLikeList(self) -> list:
        session = HTMLSession()
        rep = session.get(url=self.myLikeUri,headers={"Cookie": self.cookies})
        res = []
        r = rep.html.find("table>tr>td:first-child>a")
        for target in r:
            res.append({"ie":"utf-8","kw":target.text})
        return res

    def signIn(self):
        likeList = self.__getLikeList()
        for site in likeList:
            # 请求签到
            rep = requests.post(self.signInUri, headers={"Cookie": self.cookies},data={
                "ie":site["ie"],
                "kw":site["kw"]
            })
            # 解析返回结果
            try:
                repJson = rep.json()
            except requests.JSONDecodeError:
                logging.error("签到失败，解析返回数据失败")
                continue

            if repJson["no"] != 0:
                if repJson["no"] == 1101:
                    # 已经签到过
                    logging.info(site["kw"]+"==>"+repJson["error"])
                else:
                    logging.warning(site["kw"]+"==>"+repJson["error"])
            else:
                logging.info(site["kw"]+"==>"+"签到成功")

            # sleep 1秒 模拟真实情况
            time.sleep(1)
        pass

def main():
    env = os.environ
    cookies = env.get("tiebaCookies")
    if cookies == None:
        logging.error("缺少环境变量tiebaCookies")
        return

    # 设置日志等级
    logLevel = env.get("tiebaLogLevel")
    if logLevel == None:
        logLevel = logging.WARNING
    logging.basicConfig(level=int(logLevel))

    # 初始化对象
    tieba = TieBa(cookies)
    tieba.signIn()

if __name__ == "__main__":
    # 定时每天7点半签到
    schedule.every().day.at("07:30").do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)