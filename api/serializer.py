from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Research, Reviews, Authors

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ResearchSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True,
        write_only=True
    )

    class Meta:
        model = Research
        fields = '__all__'

    def create(self, validated_data):
        authors = validated_data.pop('authors', [])
        research = Research.objects.create(**validated_data)

        for author in authors:
            Authors.objects.create(research=research, user=author)

        return research


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'