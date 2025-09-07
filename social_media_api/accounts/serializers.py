from rest_framework import serializers
from django.contrib.auth import get_user_model


UserCustom = get_user_model()

class UserCustom(serializers.ModelSerializer):
    followers_counts=serializers.IntegerField(source='followers.count', read_only=True)
    following_counts =serializers.IntegerField(source='following.count', read_only=True)
    
    class Meta:
        model = UserCustom
        
        fields=[
            'id', 'username', 'email', 'bio', 'profile_picture',
            'followers_count', 'following_count'
        ]
     