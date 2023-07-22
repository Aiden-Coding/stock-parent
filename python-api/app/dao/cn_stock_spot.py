from tortoise import Model, fields


class CnStockSpot(Model):
    id = fields.BigIntField(pk=True, source_field='id', generated=True, description='id')
    name = fields.CharField(100, source_field='name', description='名称')
    code = fields.CharField(50, unique=True, source_field='code', description='代码')
    date = fields.DateField(source_field='date', null=True, description='日期')
    new_price = fields.FloatField(source_field='new_price', null=True, description='最新价')
    change_rate = fields.FloatField(source_field='change_rate', null=True, description='涨跌幅')
    ups_downs = fields.FloatField(source_field='ups_downs', null=True, description='涨跌额')
    volume = fields.BigIntField(source_field='volume', null=True, description='成交量')
    deal_amount = fields.BigIntField(source_field='deal_amount', null=True, description='成交额')
    amplitude = fields.FloatField(source_field='amplitude', null=True, description='振幅')
    volume_ratio = fields.FloatField(source_field='volume_ratio', null=True, description='量比')
    turnoverrate = fields.FloatField(source_field='turnoverrate', null=True, description='换手率')
    open_price = fields.FloatField(source_field='open_price', null=True, description='今开')
    high_price = fields.FloatField(source_field='high_price', null=True, description='最高')
    low_price = fields.FloatField(source_field='low_price', null=True, description='最低')
    pre_close_price = fields.FloatField(source_field='pre_close_price', null=True, description='昨收')
    speed_increase = fields.FloatField(source_field='speed_increase', null=True, description='涨速')
    speed_increase_5 = fields.FloatField(source_field='speed_increase_5', null=True, description='5分钟涨跌')
    speed_increase_60 = fields.FloatField(source_field='speed_increase_60', null=True, description='60日涨跌幅')
    speed_increase_all = fields.FloatField(source_field='speed_increase_all', null=True, description='年初至今涨跌幅')
    dtsyl = fields.FloatField(source_field='dtsyl', null=True, description='市盈率动')
    pe9 = fields.FloatField(source_field='pe9', null=True, description='市盈率TTM')
    pe = fields.FloatField(source_field='pe', null=True, description='市盈率静')
    pbnewmrq = fields.FloatField(source_field='pbnewmrq', null=True, description='市净率')
    basic_eps = fields.FloatField(source_field='basic_eps', null=True, description='每股收益')
    bvps = fields.FloatField(source_field='bvps', null=True, description='每股净资产')
    per_capital_reserve = fields.FloatField(source_field='per_capital_reserve', null=True, description='每股公积金')
    per_unassign_profit = fields.FloatField(source_field='per_unassign_profit', null=True, description='每股未分配利润')
    roe_weight = fields.FloatField(source_field='roe_weight', null=True, description='加权净资产收益率')
    sale_gpr = fields.FloatField(source_field='sale_gpr', null=True, description='毛利率')
    debt_asset_ratio = fields.FloatField(source_field='debt_asset_ratio', null=True, description='资产负债率')
    total_operate_income = fields.BigIntField(source_field='total_operate_income', null=True, description='营业收入')
    toi_yoy_ratio = fields.FloatField(source_field='toi_yoy_ratio', null=True, description='营业收入同比增长')
    parent_netprofit = fields.BigIntField(source_field='parent_netprofit', null=True, description='归属净利润')
    netprofit_yoy_ratio = fields.FloatField(source_field='netprofit_yoy_ratio', null=True,
                                            description='归属净利润同比增长')
    report_date = fields.DateField(source_field='report_date', null=True, description='报告期')
    total_shares = fields.BigIntField(source_field='total_shares', null=True, description='总股本')
    free_shares = fields.BigIntField(source_field='free_shares', null=True, description='已流通股份')
    total_market_cap = fields.BigIntField(source_field='total_market_cap', null=True, description='总市值')
    free_cap = fields.BigIntField(source_field='free_cap', null=True, description='流通市值')
    industry = fields.CharField(20, source_field='industry', null=True, description='所处行业')
    listing_date = fields.DateField(source_field='listing_date', null=True, description='上市时间')

    def __str__(self):
        return f"I am {self.name}"

    class Meta:
        abstract = False
        table = 'cn_stock_spot'
        indexes = ['code', 'date']  # 索引
        table_description = '每日股票数据'
