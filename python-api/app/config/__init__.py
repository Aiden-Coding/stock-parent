from sanic import Sanic, response
from sanic.exceptions import NotFound
from sanic.log import logger
from sanic.request import Request as _Request
# from sanic_jwt import initialize
from tortoise.contrib.sanic import register_tortoise

from app.config.config import Config
# from app.service.jwt import authenticate, MyJWTAuthentication, MyJWTConfig, MyJWTResponse
from app.view import akshareApi, userApi, stockApi, stockPicTagApi


class Request(_Request):
    user = None


app = Sanic("sanic-app", request_class=Request)
register_tortoise(
    app, db_url="mysql://root:@Cl9rLemOtSn$5iq@150.158.2.196:3306/stock",
    modules={"models": ["app.dao.user", "app.dao.cn_etf_spot", "app.dao.cn_stock_backtest_data",
                        "app.dao.cn_stock_blocktrade", "app.dao.cn_stock_fund_flow", "app.dao.cn_stock_indicators_buy",
                        "app.dao.cn_stock_indicators_sell", "app.dao.cn_stock_indicators", "app.dao.cn_stock_pattern",
                        "app.dao.cn_stock_spot_by", "app.dao.cn_stock_spot",
                        "app.dao.cn_stock_strategy_backtrace_ma250", "app.dao.cn_stock_strategy_breakthrough_platform",
                        "app.dao.cn_stock_strategy_climax_limitdown", "app.dao.cn_stock_strategy_enter",
                        "app.dao.cn_stock_strategy_high_tight_flag", "app.dao.cn_stock_strategy_keep_increasing",
                        "app.dao.cn_stock_strategy_low_atr", "app.dao.cn_stock_strategy_low_backtrace_increase",
                        "app.dao.cn_stock_strategy_parking_apron", "app.dao.cn_stock_strategy_turtle_trade",
                        "app.dao.cn_stock_top", "app.dao.stock_base_info", "app.dao.stock_base_info",
                        'app.dao.cn_stock_pic_tag', "app.dao.cn_ths_stock_block",
                        "app.dao.group.group","app.dao.group.group_stock"]},
    generate_schemas=True
)
app.config.update_config(config)
app.config.RESPONSE_TIMEOUT = 6000
logger.info(f'>>> Current env:{Config.SANIC_ENV} DEBUG:{Config.DEBUG}')
app.static('/static', 'dist-pro/static', name="static")
app.static('/assets', 'dist-pro/assets', name="assets")
app.static('/favicon.ico', 'dist-pro/favicon.ico', name="favicon")
app.static('/logo.png', 'dist-pro/logo.png', name="logo")
app.blueprint(akshareApi)
app.blueprint(userApi)
app.blueprint(stockApi)
app.blueprint(stockPicTagApi)

# initialize(app, authenticate=authenticate,
#            authentication_class=MyJWTAuthentication, configuration_class=MyJWTConfig, responses_class=MyJWTResponse)


@app.exception(NotFound)
async def ignore_404s(request, exception):
    return response.text("404. Oops, That page couldn't found.")


async def server_error_handler(request, exception):
    return response.text('Oops, Sanic Server Error! Please contact the blog owner',
                         status=500)


# serve index.html, built by Vue-CLI
@app.route('/')
async def handle_request(request):
    return await response.file('dist-pro/index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=Config.DEBUG)
