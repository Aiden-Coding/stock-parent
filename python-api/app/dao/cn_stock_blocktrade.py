from tortoise import Model, fields


class CnStockBlockTrade(Model):
    id = fields.BigIntField(pk=True, source_field='id', generated=True, description='id')
    name = fields.CharField(100, source_field='name', description='名称')
    code = fields.CharField(50, unique=True, source_field='code', description='代码')
    date = fields.DateField(source_field='date', null=True, description='日期')
    new_price = fields.FloatField(source_field='new_price', null=True, description='收盘价')
    change_rate = fields.FloatField(source_field='change_rate', null=True, description='涨跌幅')
    average_price = fields.FloatField(source_field='average_price', null=True, description='成交均价')
    overflow_rate = fields.FloatField(source_field='overflow_rate', null=True, description='折溢率')
    trade_number = fields.FloatField(source_field='trade_number', null=True, description='成交笔数')
    sum_volume = fields.FloatField(source_field='sum_volume', null=True, description='成交总量')
    sum_turnover = fields.FloatField(source_field='sum_turnover', null=True, description='成交总额')
    turnover_market_rate = fields.FloatField(source_field='turnover_market_rate', null=True,
                                             description='成交占比流通市值')

    def __str__(self):
        return f"I am {self.name}"

    class Meta:
        abstract = False
        table = 'cn_stock_blocktrade'
        indexes = ["code"]  # 索引
        table_description = '股票大宗交易'
