# -*- coding: utf-8 -*-

import logging
import math
import os.path
import sys

cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current, os.pardir))
sys.path.append(cpath)
import app.utils.run_template as runt
import app.constant as tbs
# import instock.lib.database as mdb
import app.crawling.stockfetch as stf
from app.crawling.singleton_stock import stock_data
from app.dao.cn_etf_spot import CnEtfSpot


# 股票实时行情数据。
def save_nph_stock_spot_data(date, before=True):
    if before:
        return
    # 股票列表
    try:
        data = stock_data(date).get_data()
        if data is None or len(data.index) == 0:
            return

        table_name = tbs.TABLE_CN_STOCK_SPOT['name']
        # 删除老数据。
        # if mdb.checkTableIsExist(table_name):
        #     del_sql = f"DELETE FROM `{table_name}` where `date` = '{date}'"
        #     mdb.executeSql(del_sql)
        #     cols_type = None
        # else:
        #     cols_type = tbs.get_field_types(tbs.TABLE_CN_STOCK_SPOT['columns'])
        #
        # mdb.insert_db_from_df(data, table_name, cols_type, False, "`date`,`code`")
    except Exception as e:
        logging.error(f"basic_data_daily_job.save_stock_spot_data处理异常：{e}")


# 基金实时行情数据。
def save_nph_etf_spot_data(date, before=True):
    if before:
        return
    # 股票列表
    try:
        data = stf.fetch_etfs(date)
        if data is None or len(data.index) == 0:
            return
        # todo
        sto = []
        for index, row in data.iterrows():
            st = CnEtfSpot(code=row['代码'], name=row['名称'])
            if not math.isnan(row['最新价']):
                st.latestPrice = row['最新价']
            sto.append(st)
        for st in sto:
            stt = await CnEtfSpot.get_or_none(pk=st.id)
            if stt is None:
                await st.save()
        # 删除老数据。
        # if mdb.checkTableIsExist(table_name):
        #     del_sql = f"DELETE FROM `{table_name}` where `date` = '{date}'"
        #     mdb.executeSql(del_sql)
        #     cols_type = None
        # else:
        #     cols_type = tbs.get_field_types(tbs.TABLE_CN_ETF_SPOT['columns'])
        #
        # mdb.insert_db_from_df(data, table_name, cols_type, False, "`date`,`code`")
    except Exception as e:
        logging.error(f"basic_data_daily_job.save_nph_etf_spot_data处理异常：{e}")


def main():
    runt.run_with_args(save_nph_stock_spot_data)
    runt.run_with_args(save_nph_etf_spot_data)


# main函数入口
if __name__ == '__main__':
    main()
