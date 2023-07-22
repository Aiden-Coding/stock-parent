from tortoise import Model, fields


class CnEtfSpot(Model):
    id = fields.BigIntField(pk=True, source_field='id', generated=True, description='id')
    name = fields.CharField(100, source_field='name', description='名称')
    code = fields.CharField(50, unique=True, source_field='code', description='代码')
    date = fields.DateField(source_field='date', null=True, description='日期')
    new_price = fields.FloatField(source_field='new_price', null=True, description='最新价')
    change_rate = fields.FloatField(source_field='change_rate', null=True, description='涨跌幅')
    ups_downs = fields.FloatField(source_field='ups_downs', null=True, description='涨跌额')
    volume = fields.BigIntField(source_field='volume', null=True, description='成交量')
    deal_amount = fields.BigIntField(source_field='deal_amount', null=True, description='成交额')
    open_price = fields.FloatField(source_field='open_price', null=True, description='开盘价')
    high_price = fields.FloatField(source_field='high_price', null=True, description='最高价')
    low_price = fields.FloatField(source_field='low_price', null=True, description='最低价')
    pre_close_price = fields.FloatField(source_field='pre_close_price', null=True, description='昨收')
    turnoverrate = fields.FloatField(source_field='turnoverrate', null=True, description='换手率')
    total_market_cap = fields.BigIntField(source_field='total_market_cap', null=True, description='总市值')
    free_cap = fields.BigIntField(source_field='free_cap', null=True, description='流通市值')

    def __str__(self):
        return f"I am {self.name}"

    class Meta:
        abstract = False
        table = 'cn_etf_spot'
        indexes = ['code', 'date']  # 索引
        table_description = '每日ETF数据'
