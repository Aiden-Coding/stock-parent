from tortoise import Model, fields


class cn_stock_pic_tag(Model):
    id = fields.BigIntField(pk=True, source_field='id', generated=True, description='id')
    name = fields.CharField(100, source_field='name', description='名称')
    code = fields.CharField(50, unique=False, source_field='code', description='代码')
    timespan = fields.CharField(50, unique=False, null=True, source_field='timespan', description='周期')
    tagClass = fields.CharField(50, unique=False, null=True, source_field='tag_class', description='标记类型')
    tagText = fields.TextField(unique=False, null=True, source_field='tag_text', description='标记文本')
    createDate = fields.DatetimeField(source_field='create_date', null=True, description='创建时间')

    def __str__(self):
        return f"I am {self.name}"

    class Meta:
        abstract = False
        table = 'cn_stock_pic_tag'
        indexes = ["code", 'timespan']  # 索引
        table_description = '股票标记'
