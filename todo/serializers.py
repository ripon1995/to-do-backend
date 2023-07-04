from rest_framework import serializers
from todo.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = ToDo
        fields = '__all__'


class ToDoTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'title')
