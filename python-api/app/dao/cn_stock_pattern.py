from tortoise import Model, fields


class cn_stock_pattern(Model):
    id = fields.BigIntField(pk=True, source_field='id', generated=True, description='id')
    name = fields.CharField(100, source_field='name', description='名称')
    code = fields.CharField(50, unique=True, source_field='code', description='代码')
    date = fields.DateField(source_field='date', null=True, description='日期')
    tow_crows = fields.SmallIntField(source_field='tow_crows', null=True, description='两只乌鸦')
    upside_gap_two_crows = fields.SmallIntField(source_field='upside_gap_two_crows', null=True,
                                                description='向上跳空的两只乌鸦')
    three_black_crows = fields.SmallIntField(source_field='three_black_crows', null=True, description='三只乌鸦')
    identical_three_crows = fields.SmallIntField(source_field='identical_three_crows', null=True,
                                                 description='三胞胎乌鸦')
    three_line_strike = fields.SmallIntField(source_field='three_line_strike', null=True, description='三线打击')
    dark_cloud_cover = fields.SmallIntField(source_field='dark_cloud_cover', null=True, description='乌云压顶')
    evening_doji_star = fields.SmallIntField(source_field='evening_doji_star', null=True, description='十字暮星')
    doji_Star = fields.SmallIntField(source_field='doji_Star', null=True, description='十字星')
    hanging_man = fields.SmallIntField(source_field='hanging_man', null=True, description='上吊线')
    hikkake_pattern = fields.SmallIntField(source_field='hikkake_pattern', null=True, description='陷阱')
    modified_hikkake_pattern = fields.SmallIntField(source_field='modified_hikkake_pattern', null=True,
                                                    description='修正陷阱')
    in_neck_pattern = fields.SmallIntField(source_field='in_neck_pattern', null=True, description='颈内线')
    on_neck_pattern = fields.SmallIntField(source_field='on_neck_pattern', null=True, description='颈上线')
    thrusting_pattern = fields.SmallIntField(source_field='thrusting_pattern', null=True, description='插入')
    shooting_star = fields.SmallIntField(source_field='shooting_star', null=True, description='射击之星')
    stalled_pattern = fields.SmallIntField(source_field='stalled_pattern', null=True, description='停顿形态')
    advance_block = fields.SmallIntField(source_field='advance_block', null=True, description='大敌当前')
    high_wave_candle = fields.SmallIntField(source_field='high_wave_candle', null=True, description='风高浪大线')
    engulfing_pattern = fields.SmallIntField(source_field='engulfing_pattern', null=True, description='吞噬模式')
    abandoned_baby = fields.SmallIntField(source_field='abandoned_baby', null=True, description='弃婴')
    closing_marubozu = fields.SmallIntField(source_field='closing_marubozu', null=True, description='收盘缺影线')
    doji = fields.SmallIntField(source_field='doji', null=True, description='十字')
    up_down_gap = fields.SmallIntField(source_field='up_down_gap', null=True, description='向上/下跳空并列阳线')
    long_legged_doji = fields.SmallIntField(source_field='long_legged_doji', null=True, description='长脚十字')
    rickshaw_man = fields.SmallIntField(source_field='rickshaw_man', null=True, description='黄包车夫')
    marubozu = fields.SmallIntField(source_field='marubozu', null=True, description='光头光脚/缺影线')
    three_inside_up_down = fields.SmallIntField(source_field='three_inside_up_down', null=True,
                                                description='三内部上涨和下跌')
    three_outside_up_down = fields.SmallIntField(source_field='three_outside_up_down', null=True,
                                                 description='三外部上涨和下跌')
    three_stars_in_the_south = fields.SmallIntField(source_field='three_stars_in_the_south', null=True,
                                                    description='南方三星')
    three_white_soldiers = fields.SmallIntField(source_field='three_white_soldiers', null=True, description='三个白兵')
    belt_hold = fields.SmallIntField(source_field='belt_hold', null=True, description='捉腰带线')
    breakaway = fields.SmallIntField(source_field='breakaway', null=True, description='脱离')
    concealing_baby_swallow = fields.SmallIntField(source_field='concealing_baby_swallow', null=True,
                                                   description='藏婴吞没')
    counterattack = fields.SmallIntField(source_field='counterattack', null=True, description='反击线')
    dragonfly_doji = fields.SmallIntField(source_field='dragonfly_doji', null=True, description='蜻蜓十字/T形十字')
    evening_star = fields.SmallIntField(source_field='evening_star', null=True, description='暮星')
    gravestone_doji = fields.SmallIntField(source_field='gravestone_doji', null=True, description='墓碑十字/倒T十字')
    hammer = fields.SmallIntField(source_field='hammer', null=True, description='锤头')
    harami_pattern = fields.SmallIntField(source_field='harami_pattern', null=True, description='母子线')
    harami_cross_pattern = fields.SmallIntField(source_field='harami_cross_pattern', null=True, description='十字孕线')
    homing_pigeon = fields.SmallIntField(source_field='homing_pigeon', null=True, description='家鸽')
    inverted_hammer = fields.SmallIntField(source_field='inverted_hammer', null=True, description='倒锤头')
    kicking = fields.SmallIntField(source_field='kicking', null=True, description='反冲形态')
    kicking_bull_bear = fields.SmallIntField(source_field='kicking_bull_bear', null=True,
                                             description='由较长缺影线决定的反冲形态')
    ladder_bottom = fields.SmallIntField(source_field='ladder_bottom', null=True, description='梯底')
    long_line_candle = fields.SmallIntField(source_field='long_line_candle', null=True, description='长蜡烛')
    matching_low = fields.SmallIntField(source_field='matching_low', null=True, description='相同低价')
    mat_hold = fields.SmallIntField(source_field='mat_hold', null=True, description='铺垫')
    morning_doji_star = fields.SmallIntField(source_field='morning_doji_star', null=True, description='十字晨星')
    morning_star = fields.SmallIntField(source_field='morning_star', null=True, description='晨星')
    piercing_pattern = fields.SmallIntField(source_field='piercing_pattern', null=True, description='刺透形态')
    rising_falling_three = fields.SmallIntField(source_field='rising_falling_three', null=True,
                                                description='上升/下降三法')
    separating_lines = fields.SmallIntField(source_field='separating_lines', null=True, description='分离线')
    short_line_candle = fields.SmallIntField(source_field='short_line_candle', null=True, description='短蜡烛')
    spinning_top = fields.SmallIntField(source_field='spinning_top', null=True, description='纺锤')
    stick_sandwich = fields.SmallIntField(source_field='stick_sandwich', null=True, description='条形三明治')
    takuri = fields.SmallIntField(source_field='takuri', null=True, description='探水竿')
    tasuki_gap = fields.SmallIntField(source_field='tasuki_gap', null=True, description='跳空并列阴阳线')
    tristar_pattern = fields.SmallIntField(source_field='tristar_pattern', null=True, description='三星')
    unique_3_river = fields.SmallIntField(source_field='unique_3_river', null=True, description='奇特三河床')
    upside_downside_gap = fields.SmallIntField(source_field='upside_downside_gap', null=True,
                                               description='上升/下降跳空三法')

    def __str__(self):
        return f"I am {self.name}"

    class Meta:
        abstract = False
        table = 'cn_stock_pattern'
        indexes = ["code"]  # 索引
        table_description = '股票K线形态'
