from datetime import datetime

import pandas as pd
from sanic import Blueprint, response
from tortoise.expressions import Q
from tortoise.transactions import in_transaction

import app.utils.akshare_ext as akext
from app.constant import Result, MyEncoder
from app.constant import SUCCESS
from app.dao.cn_ths_stock_block import cn_ths_stock_block
from app.dao.group.group import group
from app.dao.stock_base_info import StockBaseInfo
from app.service import stock
from app.view.group.groupStockdto import GroupStockDto
from app.view.group.groupdto import GroupDto

stockApi = Blueprint('stockApi', url_prefix='/stock')


class TickData:
    def __init__(self, time, open, high, low, close, volume, turnover):
        self.t = time
        self.o = open
        self.h = high
        self.l = low
        self.c = close
        self.v = volume
        self.vw = turnover  # 营业额


class StockBase:
    def __init__(self, name, shortName, ticker):
        self.name = name
        self.shortName = shortName
        self.ticker = ticker


@stockApi.route("/search")
async def search_base_info(request):
    search = request.args.get("search")
    result_data = []
    if search is not None:
        stocks = await StockBaseInfo.filter(Q(Q(code__contains=search), Q(name__contains=search), join_type="OR"))
        for stock in stocks:
            stock_tmp = StockBase(stock.name, stock.name, stock.code)
            result_data.append(stock_tmp)

        stocks2 = await cn_ths_stock_block.filter(Q(Q(code__contains=search), Q(name__contains=search), join_type="OR"))
        for stock in stocks2:
            stock_tmp = StockBase(stock.name, stock.name, stock.code)
            result_data.append(stock_tmp)
    ret = Result(result_data, SUCCESS)
    return response.text(MyEncoder().encode(ret))


@stockApi.route("/ticker/<ticker>/range/<multiplier>/<timespan>/<from_time>/<to>")
async def logout(request, ticker, multiplier, timespan, from_time, to):
    stt = await cn_ths_stock_block.get_or_none(code=ticker)
    oldTO = int(to)
    resultData = []
    if stt is not None:
        # 同花顺板块数据
        from_time = datetime.fromtimestamp(int(from_time) / 1000).year
        to = datetime.fromtimestamp(int(to) / 1000).year
        if from_time != to and timespan == 'day':
            data = pd.DataFrame()
            for i in range(from_time, to + 1):
                data1 = akext.stock_board_concept_hist_ths(year=i, symbol=stt.name, symbol_code=stt.code,
                                                           timespan=timespan)
                data = pd.concat([data, data1])

        else:
            data = akext.stock_board_concept_hist_ths(year=to, symbol=stt.name, symbol_code=stt.code,
                                                      timespan=timespan)
        first_row = data.iloc[0]
        time_struct = datetime.strptime(first_row['日期'], "%Y-%m-%d")
        ttime = int(time_struct.timestamp()) * 1000
        if ttime > oldTO:
            ret = Result(resultData, SUCCESS)
            return response.text(MyEncoder().encode(ret))
        for index, row in data.iterrows():
            data = TickData(row['日期'], row['开盘价'], row['最高价'], row['最低价'], row['收盘价'], row['成交量'],
                            row['成交额'])
            time_struct = datetime.strptime(row['日期'], "%Y-%m-%d")
            data.t = int(time_struct.timestamp()) * 1000
            resultData.append(data)
    else:
        if timespan == 'day':
            # '1644289200000'
            from_time = datetime.fromtimestamp(int(from_time) / 1000).strftime('%Y%m%d')
            to = datetime.fromtimestamp(int(to) / 1000).strftime('%Y%m%d')
            timespan = 'daily'
        elif timespan == 'week':
            timespan = 'weekly'
            from_time = datetime.fromtimestamp(int(from_time) / 1000).strftime('%Y%m%d')
            to = datetime.fromtimestamp(int(to) / 1000).strftime('%Y%m%d')
        elif timespan == 'month':
            timespan = 'monthly'
            from_time = datetime.fromtimestamp(int(from_time) / 1000).strftime('%Y%m%d')
            to = datetime.fromtimestamp(int(to) / 1000).strftime('%Y%m%d')
        data = stock.stock_zh_a_hist(ticker, timespan, from_time, to)
        first_row = data.iloc[0]
        time_struct = datetime.strptime(first_row['日期'], "%Y-%m-%d")
        ttime = int(time_struct.timestamp()) * 1000
        if ttime > oldTO:
            ret = Result(resultData, SUCCESS)
            return response.text(MyEncoder().encode(ret))
        for index, row in data.iterrows():
            data = TickData(row['日期'], row['开盘'], row['最高'], row['最低'], row['收盘'], row['成交量'],
                            row['成交额'])
            time_struct = datetime.strptime(row['日期'], "%Y-%m-%d")
            data.t = int(time_struct.timestamp()) * 1000
            resultData.append(data)
    ret = Result(resultData, SUCCESS)
    return response.text(MyEncoder().encode(ret))
async def execute_raw_sql(sql, params):
    # 在事务中执行原生 SQL 查询
    async with in_transaction() as conn:
        result = await conn.execute_query(sql, params)
    # 获取查询返回的所有行
    result = result[1]
    return result


@stockApi.route("/myGroup/stocks", methods=['POST'])
async def myGroupstocks(request):
    sql = 'SELECT `group`.id,group_stock.stock_code FROM `group` inner join group_stock on `group`.id = group_stock.group_id where `group`.name= %s'
    params = (request.json.get('groupName'),)
    result = await execute_raw_sql(sql, params)

    groups = []
    for groupT in result:
        groups.append(GroupStockDto(group_id=groupT['id'], code=groupT['stock_code']))
    ret = Result(groups, SUCCESS)
    return response.text(MyEncoder().encode(ret))
