from tortoise import Model, fields


class CnStockFundFlow(Model):
    id = fields.BigIntField(pk=True, source_field='id', generated=True, description='id')
    name = fields.CharField(100, source_field='name', description='名称')
    code = fields.CharField(50, unique=True, source_field='code', description='代码')
    date = fields.DateField(source_field='date', null=True, description='日期')
    new_price = fields.FloatField(source_field='new_price', null=True, description='最新价')
    change_rate = fields.FloatField(source_field='change_rate', null=True, description='涨跌幅')
    fund_amount = fields.BigIntField(source_field='fund_amount', null=True, description='今日主力净流入-净额')
    fund_rate = fields.FloatField(source_field='fund_rate', null=True, description='今日主力净流入-净占比')
    fund_amount_super = fields.BigIntField(source_field='fund_amount_super', null=True,
                                           description='今日超大单净流入-净额')
    fund_rate_super = fields.FloatField(source_field='fund_rate_super', null=True,
                                        description='今日超大单净流入-净占比')
    fund_amount_large = fields.BigIntField(source_field='fund_amount_large', null=True,
                                           description='今日大单净流入-净额')
    fund_rate_large = fields.FloatField(source_field='fund_rate_large', null=True, description='今日大单净流入-净占比')
    fund_amount_medium = fields.BigIntField(source_field='fund_amount_medium', null=True,
                                            description='今日中单净流入-净额')
    fund_rate_medium = fields.FloatField(source_field='fund_rate_medium', null=True,
                                         description='今日中单净流入-净占比')
    fund_amount_small = fields.BigIntField(source_field='fund_amount_small', null=True,
                                           description='今日小单净流入-净额')
    fund_rate_small = fields.FloatField(source_field='fund_rate_small', null=True, description='今日小单净流入-净占比')
    change_rate_3 = fields.FloatField(source_field='change_rate_3', null=True, description='3日涨跌幅')
    fund_amount_3 = fields.BigIntField(source_field='fund_amount_3', null=True, description='3日主力净流入-净额')
    fund_rate_3 = fields.FloatField(source_field='fund_rate_3', null=True, description='3日主力净流入-净占比')
    fund_amount_super_3 = fields.BigIntField(source_field='fund_amount_super_3', null=True,
                                             description='3日超大单净流入-净额')
    fund_rate_super_3 = fields.FloatField(source_field='fund_rate_super_3', null=True,
                                          description='3日超大单净流入-净占比')
    fund_amount_large_3 = fields.BigIntField(source_field='fund_amount_large_3', null=True,
                                             description='3日大单净流入-净额')
    fund_rate_large_3 = fields.FloatField(source_field='fund_rate_large_3', null=True,
                                          description='3日大单净流入-净占比')
    fund_amount_medium_3 = fields.BigIntField(source_field='fund_amount_medium_3', null=True,
                                              description='3日中单净流入-净额')
    fund_rate_medium_3 = fields.FloatField(source_field='fund_rate_medium_3', null=True,
                                           description='3日中单净流入-净占比')
    fund_amount_small_3 = fields.BigIntField(source_field='fund_amount_small_3', null=True,
                                             description='3日小单净流入-净额')
    fund_rate_small_3 = fields.FloatField(source_field='fund_rate_small_3', null=True,
                                          description='3日小单净流入-净占比')
    change_rate_5 = fields.FloatField(source_field='change_rate_5', null=True, description='5日涨跌幅')
    fund_amount_5 = fields.BigIntField(source_field='fund_amount_5', null=True, description='5日主力净流入-净额')
    fund_rate_5 = fields.FloatField(source_field='fund_rate_5', null=True, description='5日主力净流入-净占比')
    fund_amount_super_5 = fields.BigIntField(source_field='fund_amount_super_5', null=True,
                                             description='5日超大单净流入-净额')
    fund_rate_super_5 = fields.FloatField(source_field='fund_rate_super_5', null=True,
                                          description='5日超大单净流入-净占比')
    fund_amount_large_5 = fields.BigIntField(source_field='fund_amount_large_5', null=True,
                                             description='5日大单净流入-净额')
    fund_rate_large_5 = fields.FloatField(source_field='fund_rate_large_5', null=True,
                                          description='5日大单净流入-净占比')
    fund_amount_medium_5 = fields.BigIntField(source_field='fund_amount_medium_5', null=True,
                                              description='5日中单净流入-净额')
    fund_rate_medium_5 = fields.FloatField(source_field='fund_rate_medium_5', null=True,
                                           description='5日中单净流入-净占比')
    fund_amount_small_5 = fields.BigIntField(source_field='fund_amount_small_5', null=True,
                                             description='5日小单净流入-净额')
    fund_rate_small_5 = fields.FloatField(source_field='fund_rate_small_5', null=True,
                                          description='5日小单净流入-净占比')
    change_rate_10 = fields.FloatField(source_field='change_rate_10', null=True, description='10日涨跌幅')
    fund_amount_10 = fields.BigIntField(source_field='fund_amount_10', null=True, description='10日主力净流入-净额')
    fund_rate_10 = fields.FloatField(source_field='fund_rate_10', null=True, description='10日主力净流入-净占比')
    fund_amount_super_10 = fields.BigIntField(source_field='fund_amount_super_10', null=True,
                                              description='10日超大单净流入-净额')
    fund_rate_super_10 = fields.FloatField(source_field='fund_rate_super_10', null=True,
                                           description='10日超大单净流入-净占比')
    fund_amount_large_10 = fields.BigIntField(source_field='fund_amount_large_10', null=True,
                                              description='10日大单净流入-净额')
    fund_rate_large_10 = fields.FloatField(source_field='fund_rate_large_10', null=True,
                                           description='10日大单净流入-净占比')
    fund_amount_medium_10 = fields.BigIntField(source_field='fund_amount_medium_10', null=True,
                                               description='10日中单净流入-净额')
    fund_rate_medium_10 = fields.FloatField(source_field='fund_rate_medium_10', null=True,
                                            description='10日中单净流入-净占比')
    fund_amount_small_10 = fields.BigIntField(source_field='fund_amount_small_10', null=True,
                                              description='10日小单净流入-净额')
    fund_rate_small_10 = fields.FloatField(source_field='fund_rate_small_10', null=True,
                                           description='10日小单净流入-净占比')

    def __str__(self):
        return f"I am {self.name}"

    class Meta:
        abstract = False
        table = 'cn_stock_fund_flow'
        indexes = ['code', 'date']  # 索引
        table_description = '股票资金流向'
