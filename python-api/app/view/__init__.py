""" API Blueprint Application """

from sanic import Blueprint

from app.view.akshare_api import akshareApi
from app.view.stock_api import stockApi
from app.view.user_api import userApi
from app.view.stock_pic_tag_api import stockPicTagApi

# --> '/api/v1/'
# api_bp = Blueprint('api_bp_v1', url_prefix='/api/v1')

# @api_bp.route('/')
# async def bp_root(request):
#     return response.json({'api_bp_v1 blueprint': 'root'})

# Import resources to ensure view is registered
