from django.core.checks import messages
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import *
from .models import *
from .utils.token import getToken
from .utils.auth import LoginAuth
from .utils.permission import *
import json
# Create your views here.

# 登录API
class LoginViewSet(APIView):
    def post(self, request, *args, **kwargs):
        # 校验请求参数
        user_post=request.data
        try:
            username = user_post['username']
            pwd = user_post['pwd']
        except KeyError:
            return JsonResponse({
                            'result':False,
                            'code':400,
                            'message':'请求参数有误'
                        })
        if not (user_post['username'] and user_post['pwd']):
            return JsonResponse({
                'result':False,
                'code':400,
                'message':'请求参数不能为空'
            })
        # 查询
        user = clubAdmin.objects.filter(username=user_post['username'],pwd=user_post['pwd']).first()
        if not user:
            return JsonResponse({
                'result':False,
                'code':404,
                'message':'用户名或密码错误'
            })
        # 验证成功，分配token
        token = getToken(user_post['username'])
        # 获取token序列化对象存储token
        usertokenserializer=userTokenSerializer()
        usertokenserializer.setToken({'token':token,'username':user_post['username']})
        # 返回登录成功和token
        return JsonResponse({
            'result':True,
            'code':200,
            'data':{
                'token':token,
                'level':user.level
            }
        })


# 完善社团信息API
class ClubInfo(APIView):
    # 身份认证
    authentication_classes = [LoginAuth,]
    # 权限校验
    permission_classes_map = {
        'post':[clubAddPermission,],
        'put':[clubUpdatePermission,]
    }
    # 重写权限控制initial方法
    def initial(self,request,*args,**kwargs):
        # 校验请求方法是否合法
        if request.method.lower() in self.http_method_names:
            # 是否是允许的方法
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        # 校验是否有该方法的实现
        if hasattr(handler, '__name__'):
            handler_name = handler.__name__
        elif hasattr(handler, '__func__'):
            handler_name = handler.__func__.__name__
        else:
            handler_name = None
        # 校验是否存在对应的权限控制类
        if handler_name and handler_name in self.permission_classes_map:
            if isinstance(self.permission_classes_map.get(handler_name), (tuple, list)):
                self.permission_classes = self.permission_classes_map.get(handler_name)
        return super().initial(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # 校验请求参数
        try:
            # request.data = request.data.pop('username')
            # request.data = request.data.pop('token')
            name = request.data['name']
            logo = request.data['logo']
            departments = request.data['departments']
            belong = request.data['belong']
            detail = request.data['detail']
            pic1 = request.data['pic1']
            pic2 = request.data['pic2']
            pic3 = request.data['pic3']
            pic4 = request.data['pic4']
            admin = request.data['admin']
        except KeyError:
            return JsonResponse({
                'code':400,
                'result':False,
                'message':'请求参数不合法',
            })
        # 检查参数正确性
        club = clubInfoSerializer(data=request.data)
        clubTrue = club.is_valid(raise_exception=True)
        # 通过校验，返回创建出的社团id,并在clubAdmin上添加社团id
        id = club.create(validated_data=request.data).id
        clubadmin = clubAdmin.objects.filter(username=request.data['admin']).first()
        clubadmin.ownerClubId=id
        clubadmin.save()
        return JsonResponse({
            'result':True,
            'code':200,
            'data':{
                'id':id
            }
        })
    def put(self, request, *args, **kwargs):
        # 校验请求参数
        try:
            name = request.data['name']
            logo = request.data['logo']
            departments = request.data['departments']
            belong = request.data['belong']
            detail = request.data['detail']
            pic1 = request.data['pic1']
            pic2 = request.data['pic2']
            pic3 = request.data['pic3']
            pic4 = request.data['pic4']
            admin = request.data['admin']
        except KeyError:
            return JsonResponse({
                'code':400,
                'result':False,
                'message':'请求参数不合法',
            })
        # 校验参数正确性（反序列化校验）
        club = clubInfoSerializer(data=request.data)
        clubTrue = club.is_valid(raise_exception=True)
        # 校验存在性，调用update方法
        print(request.data['admin'])
        clubinstance = clubInfo.objects.filter(admin=request.data['admin']).first()
        if not clubinstance:
            return JsonResponse({
                'code':404,
                'result':False,
                'message':'你要修改的数据不存在',
            })
        club.update(instance=clubinstance,validated_data=request.data)
        return JsonResponse({
                'code':200,
                'result':True,
            })

# 账号分配api
class clubLowerAdmin(APIView):
    # 身份认证
    authentication_classes = [LoginAuth,]
    # 权限校验
    permission_classes_map = {
        'post':[addLowerAdminPermission,],
        'put':[editLowerAdminPermission,]
    }
    # 重写initial分配不同方法的权限控制类
    def initial(self,request,*args,**kwargs):
            # 校验请求方法是否合法
        if request.method.lower() in self.http_method_names:
            # 是否是允许的方法
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        # 校验是否有该方法的实现
        if hasattr(handler, '__name__'):
            handler_name = handler.__name__
        elif hasattr(handler, '__func__'):
            handler_name = handler.__func__.__name__
        else:
            handler_name = None
        # 校验是否存在对应的权限控制类
        if handler_name and handler_name in self.permission_classes_map:
            if isinstance(self.permission_classes_map.get(handler_name), (tuple, list)):
                self.permission_classes = self.permission_classes_map.get(handler_name)
        return super().initial(request, *args, **kwargs)
    # 添加账号
    def post(self,request,*args,**kwargs):
        # 校验请求参数
        # if not (hasattr(request.data,'username') and hasattr(request.data,'pwd') and hasattr(request.data,'clubadmin') and hasattr(request.data,'email')):
        #     return JsonResponse({
        #         'result':False,
        #         'code':400,
        #         'message':'Bad Request,please check your parames!'
        #     })
        # 反序列化校验
        level2admin=clubAdminSerializer(data=request.data)
        if not level2admin.is_valid():
            return JsonResponse({
                'result':False,
                'code':400,
                'message':'Bad Request,please check your parames!'
            })
        # CRUD-create
        level2user=level2admin.create(request.data)
        return JsonResponse({
            'result':True,
            'code':200,
            'data':{
                id:level2user.id
            }
        })
    # 修改账号密码
    def put(self,request,*args,**kwargs):
        # 校验请求参数
        if not (hasattr(request.data,'pwd') and hasattr(request.data,'username')):
            return JsonResponse({
                'result':False,
                'code':400,
                'message':'Bad Request,please check your parames!'
            })
        # 创建空序列化对象，查询数据实体
        level2userSerializer = clubAdminSerializer()
        level2user = clubAdmin.objects.filter(username=request.data['username']).first()
        # 确认用户名正确性
        if not level2user:
            return JsonResponse({
                'result':False,
                'code':404,
                'message':'Bad Request,your username commited is not exists!'
            })
        # CRUD-update
        level2userSerializer.update(instance=level2user,validated_data=request.data)
        # 正常响应
        return JsonResponse({
                'result':True,
                'code':200
            })