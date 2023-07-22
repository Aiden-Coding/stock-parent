from sanic import Blueprint
from sanic import response
from sanic_jwt import exceptions

from app.constant import SUCCESS
from app.dao.user import User

userApi = Blueprint('userApi', url_prefix='/user')





@userApi.route("/loginOut")
async def logout(request):
    return response.json({'data': {'api_bp_v1 blueprint': 'root'}, 'code': SUCCESS})


@userApi.route("/login", methods=['POST'])
async def login(request):
    return response.json({'data': {
        'username': 'admin',
        'password': 'admin',
        'role': 'admin',
        'roleId': '1',
        'permissions': ['*.*.*']
    }, 'code': SUCCESS})
