from rest_framework import serializers

from board.models import Board, Post, Comment


class BoardListSerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField()

    class Meta:
        model = Board
        fields = (
            'id',
            'title',
            'is_anonymous',
            'is_active',
            'created_at',
            'updated_at',
            'post_count',
        )


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = (
            'id',
            'title',
            'is_anonymous',
            'is_active',
            'created_at',
            'updated_at',
        )


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'author',
            'content',
            'is_blind',
            'created_at',
            'updated_at',
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'author',
            'content',
            'is_blind',
            'created_at',
            'updated_at',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'post',
            'author',
            'parent_comment',
            'comment',
            'is_blind',
            'created_at',
            'updated_at',
        )