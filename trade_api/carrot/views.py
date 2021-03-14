from django.shortcuts import get_object_or_404
from .models import Board, Sell, Comment
from rest_framework.decorators import api_view
from .serializers import BoardSerializer, SellSerializer, CommentSerializer
from rest_framework.response import Response

@api_view(['GET'])
def board_list(request):
    boards = Board.objects.all()
    serializer = BoardSerializer(boards, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def sell_detail(request, sell_id):
    sell = get_object_or_404(Sell, id=sell_id)
    serializer = SellSerializer(sell)
    return Response(serializer.data)

@api_view(['POST'])
def sell_create(request, sell_id):
    serializer = SellSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(id=sell_id)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def sell_update_and_delete(request, sell_id):
    sell = get_object_or_404(Sell, id=sell_id)
    if request.method == 'PUT':
        serializer = SellSerializer(data=request.data, instance=sell)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': ' sell_update'})
    else:
        sell.delete()
        return Response({'message': 'sell_delete'})


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, comment_id):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(sell_id=comment_id)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def comment_update_and_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': ' comment_update'})
    else:
        comment.delete()
        return Response({'message': 'comment_delete'})
