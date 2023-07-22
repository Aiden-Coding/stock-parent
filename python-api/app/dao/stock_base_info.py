from tortoise import Model, fields


class StockBaseInfo(Model):
    id = fields.BigIntField(pk=True, source_field='id', generated=True, description='id')
    name = fields.CharField(100, source_field='name', description='名称')
    code = fields.CharField(50, unique=True, source_field='code', description='代码')
    latestPrice = fields.FloatField(source_field='latest_price', null=True, description='最新价格')

    def __str__(self):
        return f"I am {self.name}"

    class Meta:
        abstract = False
        table = 'stock_base_info'
        indexes = ["code"]  # 索引
        table_description = '股票信息'

    async def insert_stockBaseInfos(stockBaseInfos):
        await StockBaseInfo.bulk_create(stockBaseInfos)
