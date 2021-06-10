from django.db import models
from rest_framework.authentication import BaseAuthentication
from django.http import JsonResponse
from club.models import userToken,clubAdmin
from rest_framework.views import APIView
from rest_framework import exceptions

class LoginAuth(BaseAuthentication,APIView):
    """
    在请求参数中获取token并验证
    """
    # 重写authenticate方法
    def authenticate(self,request):
        # 获取token和username
        try:
            token = request.headers['token']
            username = request.headers['username']
        except KeyError:
            # return JsonResponse({
            #     'result':False,
            #     'message':'请先登录并携带token和username发起请求',
            #     'code':10001
            # })
            raise exceptions.APIException('请携带token和username')
        # 验证token
        usertoken = userToken.objects.filter(token=token,username=username).first()
        if not usertoken:
            # return JsonResponse({
            #     'result':False,
            #     'message':'你没有权限访问该api',
            #     'code':10002
            # })
            raise exceptions.APIException('认证失败,请重新登陆！')
        # 返回当前认证用户
        user = clubAdmin.objects.filter(username=username).first()
        return user,usertoken
