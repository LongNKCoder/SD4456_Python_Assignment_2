from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )
    class Meta:
        model = Post
        fields = ["description", "owner", "date_post", "privacy"]


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["description", "owner", "date_post", "privacy"]
