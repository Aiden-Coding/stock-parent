from tortoise import Model, fields


class cn_ths_stock_block(Model):
    id = fields.BigIntField(pk=True, source_field='id', generated=True, description='id')
    name = fields.CharField(100, source_field='name', description='概念名称')
    code = fields.CharField(50, unique=True, source_field='code', description='代码')
    date = fields.DateField(source_field='date', null=True, description='日期')
    counts = fields.BigIntField(source_field='ranking_times', null=True, description='成分股数量')
    url = fields.CharField(200, source_field='sum_buy', null=True, description='网址')

    def __str__(self):
        return f"I am {self.name}"

    class Meta:
        abstract = False
        table = 'cn_ths_stock_block'
        indexes = ["code"]  # 索引
        table_description = '同花顺-概念板块'
