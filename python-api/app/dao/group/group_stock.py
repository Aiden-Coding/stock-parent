from tortoise import Model, fields


class group_stock(Model):
    id = fields.BigIntField(pk=True, source_field='id', generated=True, description='id')
    group_id = fields.BigIntField(source_field='group_id', description='组名称')
    stock_code = fields.CharField(50, source_field='stock_code', description='股票code')

    def __str__(self):
        return f"I am {self.name}"

    class Meta:
        abstract = False
        table = 'group_stock'
        table_description = '组和股票关系'
