from enum import unique
from django.db import models
from django.db.models.expressions import F
from django.utils.six import MAXSIZE

# Create your models here.

# 社团管理员用户表
class clubAdmin(models.Model):
    ##### 字段声明
    # 主键，管理员id
    id = models.AutoField(primary_key=True,auto_created=True,unique=True,verbose_name='id')
    # 账号权限等级:  2:二级用户/1:一级用户
    level = models.SmallIntegerField(verbose_name='level')
    # 所属社团id,可以为空
    ownerClubId = models.SmallIntegerField(null=True)
    # 用户名，登陆账号
    username = models.CharField(max_length=10,unique=True,verbose_name='username')
    # 登陆密码
    pwd = models.CharField(verbose_name='password',max_length=32)
    # 邮箱号
    email = models.CharField(verbose_name='email',unique=True,max_length=50)
    # 所属部门
    depart = models.CharField(verbose_name='depart',max_length=10,default=None)
    ##### 索引
    class Meta:
        # 联合唯一索引,用户名和邮箱号
        unique_together = (
            ('username','email'),
        )

# 小程序用户表
class studentUser(models.Model):
    ##### 字段声明
    # 自增主键
    id = models.AutoField(primary_key=True,auto_created=True,unique=True,verbose_name='id')
    # 小程序openid
    openid = models.CharField(max_length=30,unique=True,verbose_name='openid')
    # 简历id，默认为空
    resumeid=models.SmallIntegerField(verbose_name='resumeid')

    #### 索引
    class Meta:
        # 联合索引
        index_together=(
            ('openid','resumeid'),
        )

# 简历表
class resume(models.Model):
    ##### 字段声明
    # 自增主键,简历id
    id = models.AutoField(primary_key=True,auto_created=True,unique=True,verbose_name='id')
    # 姓名
    name = models.CharField(max_length=5,verbose_name='name')
    # 性别
    sex = {
        (1,'男'),
        (2,'女')
    }
    gender = models.IntegerField(choices=sex,verbose_name='gender')
    # 手机号
    phone = models.CharField(max_length=11,verbose_name='phone',unique=True)
    # 邮箱号
    email = models.CharField(max_length=50,verbose_name='email',unique=True)
    # QQ号
    qq = models.CharField(max_length=10,verbose_name='qq',unique=True)
    # 个人简介
    profile = models.CharField(max_length=300,verbose_name='profile')
    # 照片URL
    photo = models.URLField(verbose_name='photo')
    # 学院
    college = models.CharField(max_length=10)
    # 学号
    stuid = models.CharField(max_length=10)
    # 专业
    major = models.CharField(max_length=10)
    ##### 索引
    class Meta:
        # 联合唯一索引
        unique_together=(
            ('id','phone','qq','email'),
        )

# 社团信息表
class clubInfo(models.Model):
    ##### 字段声明
    # 社团id
    id = models.AutoField(primary_key=True,auto_created=True,unique=True,verbose_name='id')
    # 社团名称
    name = models.CharField(max_length=20,verbose_name='name')
    # logo
    logo = models.URLField(verbose_name='logo')
    # 拥有的部门，以逗号分隔的字符串存储
    departments = models.CharField(max_length=100,verbose_name='departments')
    # 归属学院
    belong = models.CharField(max_length=10,verbose_name='belong')
    # 详细介绍
    detail = models.CharField(max_length=1000,verbose_name='detail')
    # 照片
    pic1 = models.URLField(verbose_name='pic1')
    pic2 = models.URLField(verbose_name='pic2')
    pic3 = models.URLField(verbose_name='pic3')
    pic4 = models.URLField(verbose_name='pic4')
    admin = models.CharField(max_length=10,unique=True,verbose_name='username')
    ##### 索引
    class Meta:
        # 联合唯一索引
        unique_together = (
            ('belong','name')
        )

# 简历投递表 (社团-简历关系)
class deliveried(models.Model):
    #### 字段声明
    # 关系id
    id = models.AutoField(primary_key=True,auto_created=True,unique=True,verbose_name='id')
    # 社团id
    clubid = models.SmallIntegerField(verbose_name='clubid')
    # 投递部门
    departOne = models.CharField(max_length=10)
    departTwo = models.CharField(max_length=10)
    # 简历id
    resumeid = models.SmallIntegerField(verbose_name='resumeid')
    # 投递时间
    createTime = models.DateTimeField(auto_now=False,auto_now_add=True)
    # 状态变更时间
    updateTime = models.DateTimeField(auto_now=True,auto_now_add=False)
    # 当前所处轮次,
    current = models.SmallIntegerField(verbose_name='current')
    # 最终状态
    finalFlag = {
        (1,'进行中'),
        (2,'通过'),
        (3,'淘汰')
    }
    final = models.IntegerField(choices=finalFlag,verbose_name='final')

    ##### 索引
    class Meta:
        unique_together = (
            ('clubid','resumeid','current'),
        )


# 学院表
class college(models.Model):
    ##### 字段声明
    # id
    id = models.AutoField(primary_key=True,auto_created=True,unique=True,verbose_name='id')
    # 学院名
    name = models.CharField(max_length=10,unique=True,verbose_name='name')

    ##### 索引
    class Meta:
        # 联合唯一索引
        unique_together = (
            ('name',),
        )

# token
class userToken(models.Model):
    
    id = models.AutoField(primary_key=True,unique=True)
    token = models.CharField(max_length=128,unique=True)
    username = models.CharField(max_length=10,unique=True,verbose_name='username')