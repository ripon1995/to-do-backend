from rest_framework import serializers
from todo.models import ToDo
from django.utils import timezone


class ToDoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=20, default='New Task')
    createdDate = serializers.DateTimeField(default=timezone.now)
    completed = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return ToDo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
