from tortoise import Model, fields


class group(Model):
    id = fields.BigIntField(pk=True, source_field='id', generated=True, description='id')
    name = fields.CharField(100, source_field='name', description='名称')

    def __str__(self):
        return f"I am {self.name}"

    class Meta:
        abstract = False
        table = 'group'
        indexes = ['name']  # 索引
        table_description = '组'
