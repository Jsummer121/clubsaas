from django.db.models import fields
from rest_framework import serializers
from .models import *

class clubAdminSerializer(serializers.Serializer):
    # pwd = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username = serializers.CharField(max_length=10,min_length=6)
    pwd = serializers.CharField(max_length=32,min_length=8)
    email=serializers.CharField(max_length=50)
    ownerClubId = serializers.IntegerField()
    depart = serializers.CharField(max_length=10)


    class Meta:
        model = clubAdmin
    def create(self,validated_data):
        return clubAdmin.objects.create(level=2,**validated_data)
    def update(self,instance,validated_data):
        instance.pwd = validated_data.get('pwd',instance.pwd)
        instance.save()

class userTokenSerializer(serializers.Serializer):

    class Meta:
        fields= "__all__"
        model = userToken
    def setToken(self,validated_data):
        """
            创建usertoken
        """
        usertoken = userToken.objects.filter(username=validated_data['username']).first()
        if not usertoken:
            return userToken.objects.create(**validated_data)
        return userToken.objects.filter(id=usertoken.id).update(token=validated_data['token'])


class clubInfoSerializer(serializers.Serializer):
    
    # 字段合法性
    name = serializers.CharField(max_length=15)
    logo = serializers.URLField()
    departments=serializers.CharField(max_length=100)
    belong = serializers.CharField(max_length=10)
    detail = serializers.CharField(max_length=1000,min_length=300)
    pic1 = serializers.URLField()
    pic2 = serializers.URLField()
    pic3 = serializers.URLField()
    pic4 = serializers.URLField()
    admin = serializers.CharField()
    class Meta:
        model=clubInfo
    
    # 重写create方法
    def create(self,validated_data):
        return clubInfo.objects.create(**validated_data)
    # 重写update方法
    def update(self,instance,validated_data):
        
        instance.name = validated_data.get('name',instance.name)
        instance.logo = validated_data.get('logo',instance.logo)
        instance.deparments = validated_data.get('departments',instance.departments)
        instance.detail = validated_data.get('detail',instance.detail)
        instance.pic1 = validated_data.get('pic1',instance.pic1)
        instance.pic2 = validated_data.get('pic2',instance.pic2)
        instance.pic3 = validated_data.get('pic3',instance.pic3)
        instance.pic4 = validated_data.get('pic4',instance.pic4)
        instance.save()
        return instance