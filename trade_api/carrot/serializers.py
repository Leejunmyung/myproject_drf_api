from rest_framework import serializers
from .models import Board, Sell, Comment

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'photo', 'title', 'price', 'area', 'created_at',
                  'comment_number', 'like_number']

class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = ['id', 'sell_id', 'description',
                  'photo', 'title', 'price']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment_id', 'content', 'created_at', 'area']