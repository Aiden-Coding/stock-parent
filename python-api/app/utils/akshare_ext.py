"""
Date: 2022/5/30 19:10
Desc: 同花顺-板块-概念板块
http://q.10jqka.com.cn/gn/detail/code/301558/
"""

import pandas as pd
import requests
from akshare.utils import demjson
from bs4 import BeautifulSoup

timespan_code = {'day': '01', 'week': '11', 'month': '21'}


def stock_board_concept_hist_ths(
        year: str = "2000", symbol: str = "安防", symbol_code: str = '', timespan: str = ''
) -> pd.DataFrame:
    symbol_url = f"http://q.10jqka.com.cn/gn/detail/code/{symbol_code}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    }
    r = requests.get(symbol_url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    symbol_code = (
        soup.find("div", attrs={"class": "board-hq"}).find("span").text
    )
    big_df = pd.DataFrame()
    if timespan != 'day':
        year = 'last'
    url = f"http://d.10jqka.com.cn/v4/line/bk_{symbol_code}/{timespan_code[timespan]}/{year}.js"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "Referer": "http://q.10jqka.com.cn",
        "Host": "d.10jqka.com.cn",
    }
    r = requests.get(url, headers=headers)
    data_text = r.text
    try:
        demjson.decode(data_text[data_text.find("{"): -1])
    except:
        return big_df
    temp_df = demjson.decode(data_text[data_text.find("{"): -1])
    temp_df = pd.DataFrame(temp_df["data"].split(";"))
    temp_df = temp_df.iloc[:, 0].str.split(",", expand=True)
    big_df = pd.concat([big_df, temp_df], ignore_index=True)
    if big_df.columns.shape[0] == 12:
        big_df.columns = [
            "日期",
            "开盘价",
            "最高价",
            "最低价",
            "收盘价",
            "成交量",
            "成交额",
            "_",
            "_",
            "_",
            "_",
            "_",
        ]
    else:
        big_df.columns = [
            "日期",
            "开盘价",
            "最高价",
            "最低价",
            "收盘价",
            "成交量",
            "成交额",
            "_",
            "_",
            "_",
            "_",
        ]
    big_df = big_df[
        [
            "日期",
            "开盘价",
            "最高价",
            "最低价",
            "收盘价",
            "成交量",
            "成交额",
        ]
    ]
    big_df["日期"] = pd.to_datetime(big_df["日期"]).dt.strftime('%Y-%m-%d')
    big_df["开盘价"] = pd.to_numeric(big_df["开盘价"])
    big_df["最高价"] = pd.to_numeric(big_df["最高价"])
    big_df["最低价"] = pd.to_numeric(big_df["最低价"])
    big_df["收盘价"] = pd.to_numeric(big_df["收盘价"])
    big_df["成交量"] = pd.to_numeric(big_df["成交量"])
    big_df["成交额"] = pd.to_numeric(big_df["成交额"])
    return big_df
