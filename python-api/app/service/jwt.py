# from sanic import Sanic, request, response
# from sanic_jwt import initialize, Configuration, Responses, exceptions, Authentication
#
# from app.dao.user import User
#
#
# async def authenticate(request):
#     username = request.json.get("username", None)
#     password = request.json.get("password", None)
#
#     if not username or not password:
#         raise exceptions.AuthenticationFailed("用户名或密码为空！")
#     user = await User.get_or_none(name=username)
#     if user is None:
#         raise exceptions.AuthenticationFailed("用户名或密码不正确！")
#     if password != user.password:
#         raise exceptions.AuthenticationFailed("用户名或密码不正确！")
#     return user
#
#
# class MyJWTConfig(Configuration):
#     # -------------- url_prefix ---------------------
#     # [描述] 获取授权的路由地址
#     # [默认] '/auth'
#     url_prefix = '/login'
#
#     # -------------- secret -------------------------
#     # [描述] 加密密码
#     # [默认] 'This is a big secret. Shhhhh'
#     # [建议] 该密码是 JWT 的安全核心所在，需要保密，尽量使用更长更复杂的密码
#     secret = ',$FCyFZ^b16#m:ragM#d-!;4!U5zgZDF(EhswOL_HGV#xN1Ll%MaBU42AN=jXgp7'
#
#     # -------------- expiration_delta ----------------------
#     # [描述] 过期时间，单位为秒
#     # [默认] 30 分钟，即：60 * 30
#     # [建议] 该时间不宜过长，同时建议开启 refresh_token_enabled 以便自动更新 token
#     expiration_delta = 60 * 60  # 改为 10 分钟过期
#
#     # -------------- cookie_set ---------------------
#     # [描述] 是否将获取到的 token 信息写入到 cookie
#     # [默认] False，即不写入cookie
#     # 只有该项为 True，其它 cookie 相关设置才会起效。
#     # cookie_set = True
#
#     # -------------- cookie_access_token_name ---------------
#     # [描述] cookie 中存储 token 的名称。
#     # [默认] 'access_token'
#     # cookie_access_token_name = "token"
#
#     #  -------------- cookie_access_token_name ---------------
#     # [描述] 包含用户 id 的用户对象的键或属性，这里对应 User 类的用户唯一标识
#     # [默认] 'user_id'
#     user_id = "id"
#
#     claim_iat = True  # 显示签发时间，JWT的默认保留字段，在 sanic-jwt 中默认不显示该项
#
#
# class MyJWTAuthentication(Authentication):
#
#     # 从 payload 中解析用户信息，然后返回查找到的用户
#     # args[0]: request
#     # args[1]: payload
#     async def retrieve_user(self, *args, **kwargs):
#         user_id_attribute = self.config.user_id()
#         if not args or len(args) < 2 or user_id_attribute not in args[1]:
#             return {}
#         user_id = dict(args[1]).get(user_id_attribute)
#         # TODO: 根据项目实际情况进行修改
#         user = User.get_or_none(pk=user_id)
#         return user
#
#     # 拓展 payload
#     async def extend_payload(self, payload, *args, **kwargs):
#         # 可以获取 User 中的一些属性添加到 payload 中
#         # 注意：payload 信息是公开的，这里不要添加敏感信息
#         user_id_attribute = self.config.user_id()
#         user_id = payload.get(user_id_attribute)
#         # TODO: 根据项目实际情况进行修改
#         user: User = await User.get(pk = user_id)
#         payload.update({'sex': user.sex})  # 比如添加性别属性
#         return payload
#
#     async def extract_payload(self, req, verify=True, *args, **kwargs):
#         return await super().extract_payload(req, verify)
#
#
# class MyJWTResponse(Responses):
#
#     # 自定义发生异常的返回数据
#     @staticmethod
#     def exception_response(req: request.Request, exception: exceptions):
#         # sanic-jwt.exceptions 下面定义的异常类型：
#         # AuthenticationFailed
#         # MissingAuthorizationHeader
#         # MissingAuthorizationCookie
#         # InvalidAuthorizationHeader
#         # MissingRegisteredClaim
#         # Unauthorized
#         msg = str(exception)
#         if exception.status_code == 500:
#             msg = str(exception)
#         elif isinstance(exception, exceptions.AuthenticationFailed):
#             msg = str(exception)
#         else:
#             if "expired" in msg:
#                 msg = "授权已失效，请重新登录！"
#             else:
#                 msg = "未授权，请先登录！"
#         result = {
#             "status": exception.status_code,
#             "data": None,
#             "msg": msg
#         }
#         return response.json(result, status=exception.status_code)
#
#
# app = Sanic("my_auth_app")
# initialize(app, authenticate=authenticate,
#            authentication_class=MyJWTAuthentication, configuration_class=MyJWTConfig, responses_class=MyJWTResponse)
