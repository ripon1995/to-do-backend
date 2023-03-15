from rest_framework import serializers
from hobby.models import Hobby


class HobbySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=20, default='New Hobby')

    def create(self, validated_data):
        return Hobby.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
