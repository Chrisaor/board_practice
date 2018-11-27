from django.db.models import Count
from django.shortcuts import render
from rest_framework import viewsets

from board.models import Board
from board.serializers import BoardSerializer


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all().annotate(post_count=Count('post'))

    def list(self, request, *args, **kwargs):
        pass
