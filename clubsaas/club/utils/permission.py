# from django.core.exceptions import BadRequest
from django.db import models
from django.http.response import BadHeaderError
from rest_framework.permissions import BasePermission
from club.models import clubAdmin,clubInfo
# 自定义权限控制类--一级用户可添加
class clubAddPermission(BasePermission):
    def has_permission(self,request,view):
        # 获取username
        username = request.headers['username']
        # 查询权限等级
        user = clubAdmin.objects.filter(username=username,level=1).first()
        if not user:
            return False
        return True

# 自定义权限控制类--验证是否一级用户and是否属于正确的管理员
class clubUpdatePermission(BasePermission):
    def has_permission(self,request,view):
        # 获取username
        username = request.headers['username']
        # 查询权限等级
        user = clubAdmin.objects.filter(username=username,level=1).first()
        if not user:
            return False
        # 查询要修改的是否是自己的社团
        club = clubInfo.objects.filter(admin=username).first()
        if club.id != user.ownerClubId:
            return False
        return True

# 账号分配权限控制类
class addLowerAdminPermission(clubUpdatePermission):
    pass
    # def has_permission(self,request,view):
    #     return super().has_permission(self,request,view)
# 二级账号密码修改权限控制类
class editLowerAdminPermission(clubUpdatePermission):
    def has_permission(self,request,view):
        try:
        # 获取请求头的username：admin
            admin = request.headers['username']
        # 获取请求体的username：lowerAdmin
            lowerAdmin=request.data['username']
        except KeyError:
            return False
        
        # 查询请求头的admin是否level=1 and lowerAdmin's level=2 and admin's ownerClubId == lowerAdmin's ownerClubId
        adminUser = clubAdmin.objects.filter(username=admin).first()
        lowerAdminUser = clubAdmin.objects.filter(username=lowerAdmin).first()

        if adminUser.level!=1:
            return False
        if lowerAdmin.level!=2:
            return False
        if adminUser.ownerClubId != lowerAdmin.ownerClubId:
            return False
        return True