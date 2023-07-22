from json import JSONEncoder

import talib as tl

import app.strategy.backtrace_ma250 as backtrace_ma250
import app.strategy.breakthrough_platform as breakthrough_platform
import app.strategy.climax_limitdown as climax_limitdown
import app.strategy.enter as enter
import app.strategy.high_tight_flag as high_tight_flag
import app.strategy.keep_increasing as keep_increasing
import app.strategy.low_atr as low_atr
import app.strategy.low_backtrace_increase as low_backtrace_increase
import app.strategy.parking_apron as parking_apron
import app.strategy.turtle_trade as turtle_trade

SUCCESS = '0000'


class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__


class Result:
    def __init__(self, data, code):
        self.data = data
        self.code = code


RATE_FIELDS_COUNT = 100  # N日收益率字段数目，即N值

TABLE_CN_ETF_SPOT = {'name': 'cn_etf_spot', 'cn': '每日ETF数据',
                     'columns': {'date': {'cn': '日期', 'size': 0},
                                 'code': {'cn': '代码', 'size': 60},
                                 'name': {'cn': '名称', 'size': 120},
                                 'new_price': {'cn': '最新价', 'size': 70},
                                 'change_rate': {'cn': '涨跌幅', 'size': 70},
                                 'ups_downs': {'cn': '涨跌额', 'size': 70},
                                 'volume': {'cn': '成交量', 'size': 90},
                                 'deal_amount': {'cn': '成交额', 'size': 100},
                                 'open_price': {'cn': '开盘价', 'size': 70},
                                 'high_price': {'cn': '最高价', 'size': 70},
                                 'low_price': {'cn': '最低价', 'size': 70},
                                 'pre_close_price': {'cn': '昨收', 'size': 70},
                                 'turnoverrate': {'cn': '换手率', 'size': 70},
                                 'total_market_cap': {'cn': '总市值', 'size': 120},
                                 'free_cap': {'cn': '流通市值', 'size': 120}}}

TABLE_CN_STOCK_SPOT = {'name': 'cn_stock_spot', 'cn': '每日股票数据',
                       'columns': {'date': {'cn': '日期', 'size': 0},
                                   'code': {'cn': '代码', 'size': 60},
                                   'name': {'cn': '名称', 'size': 70},
                                   'new_price': {'cn': '最新价', 'size': 70},
                                   'change_rate': {'cn': '涨跌幅', 'size': 70},
                                   'ups_downs': {'cn': '涨跌额', 'size': 70},
                                   'volume': {'cn': '成交量', 'size': 90},
                                   'deal_amount': {'cn': '成交额', 'size': 100},
                                   'amplitude': {'cn': '振幅', 'size': 70},
                                   'volume_ratio': {'cn': '量比', 'size': 70},
                                   'turnoverrate': {'cn': '换手率', 'size': 70},
                                   'open_price': {'cn': '今开', 'size': 70},
                                   'high_price': {'cn': '最高', 'size': 70},
                                   'low_price': {'cn': '最低', 'size': 70},
                                   'pre_close_price': {'cn': '昨收', 'size': 70},
                                   'speed_increase': {'cn': '涨速', 'size': 70},
                                   'speed_increase_5': {'cn': '5分钟涨跌', 'size': 70},
                                   'speed_increase_60': {'cn': '60日涨跌幅', 'size': 70},
                                   'speed_increase_all': {'cn': '年初至今涨跌幅', 'size': 70},
                                   'dtsyl': {'cn': '市盈率动', 'size': 70},
                                   'pe9': {'cn': '市盈率TTM', 'size': 70},
                                   'pe': {'cn': '市盈率静', 'size': 70},
                                   'pbnewmrq': {'cn': '市净率', 'size': 70},
                                   'basic_eps': {'cn': '每股收益', 'size': 70},
                                   'bvps': {'cn': '每股净资产', 'size': 70},
                                   'per_capital_reserve': {'cn': '每股公积金', 'size': 70},
                                   'per_unassign_profit': {'cn': '每股未分配利润', 'size': 70},
                                   'roe_weight': {'cn': '加权净资产收益率', 'size': 70},
                                   'sale_gpr': {'cn': '毛利率', 'size': 70},
                                   'debt_asset_ratio': {'cn': '资产负债率', 'size': 70},
                                   'total_operate_income': {'cn': '营业收入', 'size': 120},
                                   'toi_yoy_ratio': {'cn': '营业收入同比增长', 'size': 70},
                                   'parent_netprofit': {'cn': '归属净利润', 'size': 110},
                                   'netprofit_yoy_ratio': {'cn': '归属净利润同比增长', 'size': 70},
                                   'report_date': {'cn': '报告期', 'size': 80},
                                   'total_shares': {'cn': '总股本', 'size': 120},
                                   'free_shares': {'cn': '已流通股份', 'size': 120},
                                   'total_market_cap': {'cn': '总市值', 'size': 120},
                                   'free_cap': {'cn': '流通市值', 'size': 120},
                                   'industry': {'cn': '所处行业', 'size': 100},
                                   'listing_date': {'cn': '上市时间', 'size': 80}}}

TABLE_CN_STOCK_SPOT_BUY = {'name': 'cn_stock_spot_buy', 'cn': '基本面选股',
                           'columns': TABLE_CN_STOCK_SPOT['columns'].copy()}

CN_STOCK_FUND_FLOW = ({'name': 'stock_individual_fund_flow_rank', 'cn': '今日',
                       'columns': {'code': {'cn': '代码', 'size': 60},
                                   'name': {'cn': '名称', 'size': 70},
                                   'new_price': {'cn': '最新价', 'size': 70},
                                   'change_rate': {'cn': '涨跌幅', 'size': 70},
                                   'fund_amount': {'cn': '今日主力净流入-净额', 'size': 100},
                                   'fund_rate': {'cn': '今日主力净流入-净占比', 'size': 70},
                                   'fund_amount_super': {'cn': '今日超大单净流入-净额', 'size': 100},
                                   'fund_rate_super': {'cn': '今日超大单净流入-净占比', 'size': 70},
                                   'fund_amount_large': {'cn': '今日大单净流入-净额', 'size': 100},
                                   'fund_rate_large': {'cn': '今日大单净流入-净占比', 'size': 70},
                                   'fund_amount_medium': {'cn': '今日中单净流入-净额', 'size': 100},
                                   'fund_rate_medium': {'cn': '今日中单净流入-净占比', 'size': 70},
                                   'fund_amount_small': {'cn': '今日小单净流入-净额', 'size': 100},
                                   'fund_rate_small': {'cn': '今日小单净流入-净占比', 'size': 70}}},
                      {'name': 'stock_individual_fund_flow_rank', 'cn': '3日',
                       'columns': {'code': {'cn': '代码', 'size': 60},
                                   'name': {'cn': '名称', 'size': 70},
                                   'new_price': {'cn': '最新价', 'size': 70},
                                   'change_rate_3': {'cn': '3日涨跌幅', 'size': 70},
                                   'fund_amount_3': {'cn': '3日主力净流入-净额', 'size': 100},
                                   'fund_rate_3': {'cn': '3日主力净流入-净占比', 'size': 70},
                                   'fund_amount_super_3': {'cn': '3日超大单净流入-净额', 'size': 100},
                                   'fund_rate_super_3': {'cn': '3日超大单净流入-净占比', 'size': 70},
                                   'fund_amount_large_3': {'cn': '3日大单净流入-净额', 'size': 100},
                                   'fund_rate_large_3': {'cn': '3日大单净流入-净占比', 'size': 70},
                                   'fund_amount_medium_3': {'cn': '3日中单净流入-净额', 'size': 100},
                                   'fund_rate_medium_3': {'cn': '3日中单净流入-净占比', 'size': 70},
                                   'fund_amount_small_3': {'cn': '3日小单净流入-净额', 'size': 100},
                                   'fund_rate_small_3': {'cn': '3日小单净流入-净占比', 'size': 70}}},
                      {'name': 'stock_individual_fund_flow_rank', 'cn': '5日',
                       'columns': {'code': {'cn': '代码', 'size': 60},
                                   'name': {'cn': '名称', 'size': 70},
                                   'new_price': {'cn': '最新价', 'size': 70},
                                   'change_rate_5': {'cn': '5日涨跌幅', 'size': 70},
                                   'fund_amount_5': {'cn': '5日主力净流入-净额', 'size': 100},
                                   'fund_rate_5': {'cn': '5日主力净流入-净占比', 'size': 70},
                                   'fund_amount_super_5': {'cn': '5日超大单净流入-净额', 'size': 100},
                                   'fund_rate_super_5': {'cn': '5日超大单净流入-净占比', 'size': 70},
                                   'fund_amount_large_5': {'cn': '5日大单净流入-净额', 'size': 100},
                                   'fund_rate_large_5': {'cn': '5日大单净流入-净占比', 'size': 70},
                                   'fund_amount_medium_5': {'cn': '5日中单净流入-净额', 'size': 100},
                                   'fund_rate_medium_5': {'cn': '5日中单净流入-净占比', 'size': 70},
                                   'fund_amount_small_5': {'cn': '5日小单净流入-净额', 'size': 100},
                                   'fund_rate_small_5': {'cn': '5日小单净流入-净占比', 'size': 70}}},
                      {'name': 'stock_individual_fund_flow_rank', 'cn': '10日',
                       'columns': {'code': {'cn': '代码', 'size': 60},
                                   'name': {'cn': '名称', 'size': 70},
                                   'new_price': {'cn': '最新价', 'size': 70},
                                   'change_rate_10': {'cn': '10日涨跌幅', 'size': 70},
                                   'fund_amount_10': {'cn': '10日主力净流入-净额', 'size': 100},
                                   'fund_rate_10': {'cn': '10日主力净流入-净占比', 'size': 70},
                                   'fund_amount_super_10': {'cn': '10日超大单净流入-净额', 'size': 100},
                                   'fund_rate_super_10': {'cn': '10日超大单净流入-净占比', 'size': 70},
                                   'fund_amount_large_10': {'cn': '10日大单净流入-净额', 'size': 100},
                                   'fund_rate_large_10': {'cn': '10日大单净流入-净占比', 'size': 70},
                                   'fund_amount_medium_10': {'cn': '10日中单净流入-净额', 'size': 100},
                                   'fund_rate_medium_10': {'cn': '10日中单净流入-净占比', 'size': 70},
                                   'fund_amount_small_10': {'cn': '10日小单净流入-净额', 'size': 100},
                                   'fund_rate_small_10': {'cn': '10日小单净流入-净占比', 'size': 70}}})

TABLE_CN_STOCK_FUND_FLOW = {'name': 'cn_stock_fund_flow', 'cn': '股票资金流向',
                            'columns': {'date': {'cn': '日期', 'size': 0}}}
for cf in CN_STOCK_FUND_FLOW:
    TABLE_CN_STOCK_FUND_FLOW['columns'].update(cf['columns'].copy())

TABLE_CN_STOCK_TOP = {'name': 'cn_stock_top', 'cn': '股票龙虎榜',
                      'columns': {'date': {'cn': '日期', 'size': 0},
                                  'code': {'cn': '代码', 'size': 60},
                                  'name': {'cn': '名称', 'size': 70},
                                  'ranking_times': {'cn': '上榜次数', 'size': 70},
                                  'sum_buy': {'cn': '累积购买额', 'size': 100},
                                  'sum_sell': {'cn': '累积卖出额', 'size': 100},
                                  'net_amount': {'cn': '净额', 'size': 100},
                                  'buy_seat': {'cn': '买入席位数', 'size': 100},
                                  'sell_seat': {'cn': '卖出席位数', 'size': 100}}}

TABLE_CN_STOCK_BLOCKTRADE = {'name': 'cn_stock_blocktrade', 'cn': '股票大宗交易',
                             'columns': {'date': {'cn': '日期', 'size': 0},
                                         'code': {'cn': '代码', 'size': 60},
                                         'name': {'cn': '名称', 'size': 70},
                                         'new_price': {'cn': '收盘价', 'size': 70},
                                         'change_rate': {'cn': '涨跌幅', 'size': 70},
                                         'average_price': {'cn': '成交均价', 'size': 70},
                                         'overflow_rate': {'cn': '折溢率', 'size': 120},
                                         'trade_number': {'cn': '成交笔数', 'size': 70},
                                         'sum_volume': {'cn': '成交总量', 'size': 100},
                                         'sum_turnover': {'cn': '成交总额', 'size': 100},
                                         'turnover_market_rate': {'cn': '成交占比流通市值', 'size': 120}}}

CN_STOCK_HIST_DATA = {'name': 'fund_etf_hist_em', 'cn': '基金某时间段的日行情数据库',
                      'columns': {'date': {'cn': '日期'},
                                  'open': {'cn': '开盘'},
                                  'close': {'cn': '收盘'},
                                  'high': {'cn': '最高'},
                                  'low': {'cn': '最低'},
                                  'volume': {'cn': '成交量'},
                                  'amount': {'cn': '成交额'},
                                  'amplitude': {'cn': '振幅'},
                                  'quote_change': {'cn': '涨跌幅'},
                                  'ups_downs': {'cn': '涨跌额'},
                                  'turnover': {'cn': '换手率'}}}

TABLE_CN_STOCK_FOREIGN_KEY = {'name': 'cn_stock_foreign_key', 'cn': '股票外键',
                              'columns': {'date': {'cn': '日期', 'size': 0},
                                          'code': {'cn': '代码', 'size': 60},
                                          'name': {'cn': '名称', 'size': 70}}}

TABLE_CN_STOCK_BACKTEST_DATA = {'name': 'cn_stock_backtest_data', 'cn': '股票回归测试数据',
                                'columns': {'rate_%s' % i: {'cn': '%s日收益率' % i, 'size': 100} for i in
                                            range(1, RATE_FIELDS_COUNT + 1, 1)}}

STOCK_STATS_DATA = {'name': 'calculate_indicator', 'cn': '股票统计/指标计算助手库',
                    'columns': {'close': {'cn': '价格', 'size': 0},
                                'macd': {'cn': 'dif', 'size': 70}, 'macds': {'cn': 'macd', 'size': 70},
                                'macdh': {'cn': 'histogram', 'size': 70},
                                'kdjk': {'cn': 'kdjk', 'size': 70}, 'kdjd': {'cn': 'kdjd', 'size': 70},
                                'kdjj': {'cn': 'kdjj', 'size': 70},
                                'boll_ub': {'cn': 'boll上轨', 'size': 70},
                                'boll': {'cn': 'boll', 'size': 70},
                                'boll_lb': {'cn': 'boll下轨', 'size': 70},
                                'trix': {'cn': 'trix', 'size': 70}, 'trix_20_sma': {'cn': 'trma', 'size': 70},
                                'tema': {'cn': 'tema', 'size': 70},
                                'cr': {'cn': 'cr', 'size': 70}, 'cr-ma1': {'cn': 'cr-ma1', 'size': 70},
                                'cr-ma2': {'cn': 'cr-ma2', 'size': 70}, 'cr-ma3': {'cn': 'cr-ma3', 'size': 70},
                                'rsi_6': {'cn': 'rsi_6', 'size': 70}, 'rsi_12': {'cn': 'rsi_12', 'size': 70},
                                'rsi': {'cn': 'rsi', 'size': 70}, 'rsi_24': {'cn': 'rsi_24', 'size': 70},
                                'vr': {'cn': 'vr', 'size': 70}, 'vr_6_sma': {'cn': 'mavr', 'size': 70},
                                'roc': {'cn': 'roc', 'size': 70}, 'rocma': {'cn': 'rocma', 'size': 70},
                                'rocema': {'cn': 'rocema', 'size': 70},
                                'pdi': {'cn': 'pdi', 'size': 70}, 'mdi': {'cn': 'mdi', 'size': 70},
                                'dx': {'cn': 'dx', 'size': 70},
                                'adx': {'cn': 'adx', 'size': 70}, 'adxr': {'cn': 'adxr', 'size': 70},
                                'wr_6': {'cn': 'wr_6', 'size': 70}, 'wr_10': {'cn': 'wr_10', 'size': 70},
                                'wr_14': {'cn': 'wr_14', 'size': 70},
                                'cci': {'cn': 'cci', 'size': 70}, 'cci_84': {'cn': 'cci_84', 'size': 70},
                                'tr': {'cn': 'tr', 'size': 70}, 'atr': {'cn': 'atr', 'size': 70},
                                'dma': {'cn': 'dma', 'size': 70}, 'dma_10_sma': {'cn': 'ama', 'size': 70},
                                'obv': {'cn': 'obv', 'size': 70}, 'sar': {'cn': 'sar', 'size': 70},
                                'psy': {'cn': 'psy', 'size': 70}, 'psyma': {'cn': 'psyma', 'size': 70},
                                'br': {'cn': 'br', 'size': 70}, 'ar': {'cn': 'ar', 'size': 70},
                                'emv': {'cn': 'emv', 'size': 70}, 'emva': {'cn': 'emva', 'size': 70},
                                'bias': {'cn': 'bias', 'size': 70},
                                'mfi': {'cn': 'mfi', 'size': 70}, 'mfisma': {'cn': 'mfisma', 'size': 70},
                                'vwma': {'cn': 'vwma', 'size': 70}, 'mvwma': {'cn': 'mvwma', 'size': 70},
                                'ppo': {'cn': 'ppo', 'size': 70}, 'ppos': {'cn': 'ppos', 'size': 70},
                                'ppoh': {'cn': 'ppoh', 'size': 70},
                                'wt1': {'cn': 'wt1', 'size': 70}, 'wt2': {'cn': 'wt2', 'size': 70},
                                'supertrend_ub': {'cn': 'supertrend_ub', 'size': 70},
                                'supertrend': {'cn': 'supertrend', 'size': 70},
                                'supertrend_lb': {'cn': 'supertrend_lb', 'size': 70},
                                'dpo': {'cn': 'dpo', 'size': 70}, 'madpo': {'cn': 'madpo', 'size': 70},
                                'vhf': {'cn': 'vhf', 'size': 70},
                                'rvi': {'cn': 'rvi', 'size': 70}, 'rvis': {'cn': 'rvis', 'size': 70},
                                'fi': {'cn': 'fi', 'size': 70}, 'force_2': {'cn': 'force_2', 'size': 70},
                                'force_13': {'cn': 'force_13', 'size': 70},
                                'ene_ue': {'cn': 'ene上轨', 'size': 70}, 'ene': {'cn': 'ene', 'size': 70},
                                'ene_le': {'cn': 'ene下轨', 'size': 70},
                                'stochrsi_k': {'cn': 'stochrsi_k', 'size': 70},
                                'stochrsi_d': {'cn': 'stochrsi_d', 'size': 70}}}

TABLE_CN_STOCK_INDICATORS = {'name': 'cn_stock_indicators', 'cn': '股票指标数据',
                             'columns': TABLE_CN_STOCK_FOREIGN_KEY['columns'].copy()}
TABLE_CN_STOCK_INDICATORS['columns'].update(STOCK_STATS_DATA['columns'])

_tmp_columns = TABLE_CN_STOCK_FOREIGN_KEY['columns'].copy()
_tmp_columns.update(TABLE_CN_STOCK_BACKTEST_DATA['columns'])

TABLE_CN_STOCK_INDICATORS_BUY = {'name': 'cn_stock_indicators_buy', 'cn': '股票指标买入',
                                 'columns': _tmp_columns}

TABLE_CN_STOCK_INDICATORS_SELL = {'name': 'cn_stock_indicators_sell', 'cn': '股票指标卖出',
                                  'columns': _tmp_columns}

TABLE_CN_STOCK_STRATEGIES = [
    {'name': 'cn_stock_strategy_enter', 'cn': '放量上涨', 'size': 70, 'func': enter.check_volume,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_keep_increasing', 'cn': '均线多头', 'size': 70, 'func': keep_increasing.check,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_parking_apron', 'cn': '停机坪', 'size': 70, 'func': parking_apron.check,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_backtrace_ma250', 'cn': '回踩年线', 'size': 70, 'func': backtrace_ma250.check,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_breakthrough_platform', 'cn': '突破平台', 'size': 70,
     'func': breakthrough_platform.check,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_low_backtrace_increase', 'cn': '无大幅回撤', 'size': 70,
     'func': low_backtrace_increase.check,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_turtle_trade', 'cn': '海龟交易法则', 'size': 70, 'func': turtle_trade.check_enter,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_high_tight_flag', 'cn': '高而窄的旗形', 'size': 70,
     'func': high_tight_flag.check_high_tight,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_climax_limitdown', 'cn': '放量跌停', 'size': 70, 'func': climax_limitdown.check,
     'columns': _tmp_columns},
    {'name': 'cn_stock_strategy_low_atr', 'cn': '低ATR成长', 'size': 70, 'func': low_atr.check_low_increase,
     'columns': _tmp_columns}
]

STOCK_KLINE_PATTERN_DATA = {'name': 'cn_stock_pattern_recognitions', 'cn': 'K线形态',
                            'columns': {
                                'tow_crows': {'cn': '两只乌鸦', 'size': 70, 'func': tl.CDL2CROWS},
                                'upside_gap_two_crows': {'cn': '向上跳空的两只乌鸦', 'size': 70,
                                                         'func': tl.CDLUPSIDEGAP2CROWS},
                                'three_black_crows': {'cn': '三只乌鸦', 'size': 70,
                                                      'func': tl.CDL3BLACKCROWS},
                                'identical_three_crows': {'cn': '三胞胎乌鸦', 'size': 70,
                                                          'func': tl.CDLIDENTICAL3CROWS},
                                'three_line_strike': {'cn': '三线打击', 'size': 70,
                                                      'func': tl.CDL3LINESTRIKE},
                                'dark_cloud_cover': {'cn': '乌云压顶', 'size': 70,
                                                     'func': tl.CDLDARKCLOUDCOVER},
                                'evening_doji_star': {'cn': '十字暮星', 'size': 70,
                                                      'func': tl.CDLEVENINGDOJISTAR},
                                'doji_Star': {'cn': '十字星', 'size': 70, 'func': tl.CDLDOJISTAR},
                                'hanging_man': {'cn': '上吊线', 'size': 70, 'func': tl.CDLHANGINGMAN},
                                'hikkake_pattern': {'cn': '陷阱', 'size': 70, 'func': tl.CDLHIKKAKE},
                                'modified_hikkake_pattern': {'cn': '修正陷阱', 'size': 70,
                                                             'func': tl.CDLHIKKAKEMOD},
                                'in_neck_pattern': {'cn': '颈内线', 'size': 70, 'func': tl.CDLINNECK},
                                'on_neck_pattern': {'cn': '颈上线', 'size': 70, 'func': tl.CDLONNECK},
                                'thrusting_pattern': {'cn': '插入', 'size': 70, 'func': tl.CDLTHRUSTING},
                                'shooting_star': {'cn': '射击之星', 'size': 70,
                                                  'func': tl.CDLSHOOTINGSTAR},
                                'stalled_pattern': {'cn': '停顿形态', 'size': 70,
                                                    'func': tl.CDLSTALLEDPATTERN},
                                'advance_block': {'cn': '大敌当前', 'size': 70,
                                                  'func': tl.CDLADVANCEBLOCK},
                                'high_wave_candle': {'cn': '风高浪大线', 'size': 70,
                                                     'func': tl.CDLHIGHWAVE},
                                'engulfing_pattern': {'cn': '吞噬模式', 'size': 70,
                                                      'func': tl.CDLENGULFING},
                                'abandoned_baby': {'cn': '弃婴', 'size': 70,
                                                   'func': tl.CDLABANDONEDBABY},
                                'closing_marubozu': {'cn': '收盘缺影线', 'size': 70,
                                                     'func': tl.CDLCLOSINGMARUBOZU},
                                'doji': {'cn': '十字', 'size': 70, 'func': tl.CDLDOJI},
                                'up_down_gap': {'cn': '向上/下跳空并列阳线', 'size': 70,
                                                'func': tl.CDLGAPSIDESIDEWHITE},
                                'long_legged_doji': {'cn': '长脚十字', 'size': 70,
                                                     'func': tl.CDLLONGLEGGEDDOJI},
                                'rickshaw_man': {'cn': '黄包车夫', 'size': 70,
                                                 'func': tl.CDLRICKSHAWMAN},
                                'marubozu': {'cn': '光头光脚/缺影线', 'size': 70,
                                             'func': tl.CDLMARUBOZU},
                                'three_inside_up_down': {'cn': '三内部上涨和下跌', 'size': 70,
                                                         'func': tl.CDL3INSIDE},
                                'three_outside_up_down': {'cn': '三外部上涨和下跌', 'size': 70,
                                                          'func': tl.CDL3OUTSIDE},
                                'three_stars_in_the_south': {'cn': '南方三星', 'size': 70,
                                                             'func': tl.CDL3STARSINSOUTH},
                                'three_white_soldiers': {'cn': '三个白兵', 'size': 70,
                                                         'func': tl.CDL3WHITESOLDIERS},
                                'belt_hold': {'cn': '捉腰带线', 'size': 70, 'func': tl.CDLBELTHOLD},
                                'breakaway': {'cn': '脱离', 'size': 70, 'func': tl.CDLBREAKAWAY},
                                'concealing_baby_swallow': {'cn': '藏婴吞没', 'size': 70,
                                                            'func': tl.CDLCONCEALBABYSWALL},
                                'counterattack': {'cn': '反击线', 'size': 70,
                                                  'func': tl.CDLCOUNTERATTACK},
                                'dragonfly_doji': {'cn': '蜻蜓十字/T形十字', 'size': 70,
                                                   'func': tl.CDLDRAGONFLYDOJI},
                                'evening_star': {'cn': '暮星', 'size': 70, 'func': tl.CDLEVENINGSTAR},
                                'gravestone_doji': {'cn': '墓碑十字/倒T十字', 'size': 70,
                                                    'func': tl.CDLGRAVESTONEDOJI},
                                'hammer': {'cn': '锤头', 'size': 70, 'func': tl.CDLHAMMER},
                                'harami_pattern': {'cn': '母子线', 'size': 70, 'func': tl.CDLHARAMI},
                                'harami_cross_pattern': {'cn': '十字孕线', 'size': 70,
                                                         'func': tl.CDLHARAMICROSS},
                                'homing_pigeon': {'cn': '家鸽', 'size': 70, 'func': tl.CDLHOMINGPIGEON},
                                'inverted_hammer': {'cn': '倒锤头', 'size': 70,
                                                    'func': tl.CDLINVERTEDHAMMER},
                                'kicking': {'cn': '反冲形态', 'size': 70, 'func': tl.CDLKICKING},
                                'kicking_bull_bear': {'cn': '由较长缺影线决定的反冲形态', 'size': 70,
                                                      'func': tl.CDLKICKINGBYLENGTH},
                                'ladder_bottom': {'cn': '梯底', 'size': 70, 'func': tl.CDLLADDERBOTTOM},
                                'long_line_candle': {'cn': '长蜡烛', 'size': 70, 'func': tl.CDLLONGLINE},
                                'matching_low': {'cn': '相同低价', 'size': 70,
                                                 'func': tl.CDLMATCHINGLOW},
                                'mat_hold': {'cn': '铺垫', 'size': 70, 'func': tl.CDLMATHOLD},
                                'morning_doji_star': {'cn': '十字晨星', 'size': 70,
                                                      'func': tl.CDLMORNINGDOJISTAR},
                                'morning_star': {'cn': '晨星', 'size': 70, 'func': tl.CDLMORNINGSTAR},
                                'piercing_pattern': {'cn': '刺透形态', 'size': 70,
                                                     'func': tl.CDLPIERCING},
                                'rising_falling_three': {'cn': '上升/下降三法', 'size': 70,
                                                         'func': tl.CDLRISEFALL3METHODS},
                                'separating_lines': {'cn': '分离线', 'size': 70,
                                                     'func': tl.CDLSEPARATINGLINES},
                                'short_line_candle': {'cn': '短蜡烛', 'size': 70,
                                                      'func': tl.CDLSHORTLINE},
                                'spinning_top': {'cn': '纺锤', 'size': 70, 'func': tl.CDLSPINNINGTOP},
                                'stick_sandwich': {'cn': '条形三明治', 'size': 70,
                                                   'func': tl.CDLSTICKSANDWICH},
                                'takuri': {'cn': '探水竿', 'size': 70, 'func': tl.CDLTAKURI},
                                'tasuki_gap': {'cn': '跳空并列阴阳线', 'size': 70,
                                               'func': tl.CDLTASUKIGAP},
                                'tristar_pattern': {'cn': '三星', 'size': 70, 'func': tl.CDLTRISTAR},
                                'unique_3_river': {'cn': '奇特三河床', 'size': 70,
                                                   'func': tl.CDLUNIQUE3RIVER},
                                'upside_downside_gap': {'cn': '上升/下降跳空三法', 'size': 70,
                                                        'func': tl.CDLXSIDEGAP3METHODS}}}

TABLE_CN_STOCK_KLINE_PATTERN = {'name': 'cn_stock_pattern', 'cn': '股票K线形态',
                                'columns': TABLE_CN_STOCK_FOREIGN_KEY['columns'].copy()}
TABLE_CN_STOCK_KLINE_PATTERN['columns'].update(STOCK_KLINE_PATTERN_DATA['columns'])


def get_field_cn(key, table):
    f = table.get('columns').get(key)
    if f is None:
        return key
    return f.get('cn')


def get_field_cns(cols):
    data = []
    for k in cols:
        data.append(cols[k]['cn'])
    return data


def get_field_types(cols):
    data = {}
    for k in cols:
        data[k] = cols[k]['type']
    return data
