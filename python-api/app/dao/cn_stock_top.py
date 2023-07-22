from tortoise import Model, fields


class CnStockTop(Model):
    id = fields.BigIntField(pk=True, source_field='id', generated=True, description='id')
    name = fields.CharField(100, source_field='name', description='名称')
    code = fields.CharField(50, unique=True, source_field='code', description='代码')
    date = fields.DateField(source_field='date', null=True, description='日期')
    ranking_times = fields.FloatField(source_field='ranking_times', null=True, description='上榜次数')
    sum_buy = fields.FloatField(source_field='sum_buy', null=True, description='累积购买额')
    sum_sell = fields.FloatField(source_field='sum_sell', null=True, description='累积卖出额')
    net_amount = fields.FloatField(source_field='net_amount', null=True, description='净额')
    buy_seat = fields.FloatField(source_field='buy_seat', null=True, description='买入席位数')
    sell_seat = fields.FloatField(source_field='sell_seat', null=True, description='卖出席位数')

    def __str__(self):
        return f"I am {self.name}"

    class Meta:
        abstract = False
        table = 'cn_stock_top'
        indexes = ["code"]  # 索引
        table_description = '股票龙虎榜'

    async def insert_stockBaseInfos(stockBaseInfos):
        await StockBaseInfo.bulk_create(stockBaseInfos)
