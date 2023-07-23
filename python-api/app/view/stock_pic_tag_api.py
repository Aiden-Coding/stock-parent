from datetime import datetime

from sanic import Blueprint, response
from tortoise.expressions import Q

from app.constant import Result, MyEncoder
from app.constant import SUCCESS
from app.dao.cn_stock_pic_tag import cn_stock_pic_tag
from app.utils.Snowflake import Snowflake

stockPicTagApi = Blueprint('stockPicTagApi', url_prefix='/stockPicTag')

snowflake = Snowflake(worker_id=1, datacenter_id=1)


@stockPicTagApi.route("/add", methods=['POST'])
async def search_base_info(request):
    picTag = request.json
    picTagDB = cn_stock_pic_tag(id=picTag['id'], name=picTag['name'], code=picTag['code'], timespan=picTag['timespan'],
                                tagClass=picTag['tagClass'],
                                tagText=picTag['tagText'], createDate=datetime.now())
    await picTagDB.save()
    ret = Result('ok', SUCCESS)
    return response.json(MyEncoder().encode(ret))


@stockPicTagApi.route("/getId")
async def getId(request):
    id = snowflake.generate_id()
    ret = Result(id, SUCCESS)
    return response.text(MyEncoder().encode(ret))


@stockPicTagApi.route("/deleteById/<id>", methods=['DELETE'])
async def deleteById(request, id):
    count = await cn_stock_pic_tag.filter(pk=id).delete()
    ret = Result(count, SUCCESS)
    return response.text(MyEncoder().encode(ret))


@stockPicTagApi.route("/getPicTag")
async def getPicTag(request):
    code = request.args.get("code")
    timespan = request.args.get("timespan")
    result_data = []
    stocks2 = await cn_stock_pic_tag.filter(Q(Q(code=code), Q(timespan=timespan), join_type="AND"))
    for stock in stocks2:
        stock_tmp = cn_stock_pic_tag(id=stock.id, name=stock.name, code=stock.code, timespan=stock.timespan,
                                     tagClass=stock.tagClass, tagText=stock.tagText)
        result_data.append(stock_tmp)
    ret = Result(result_data, SUCCESS)
    return response.text(MyEncoder().encode(ret))
