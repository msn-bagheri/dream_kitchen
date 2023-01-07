from rest_framework import serializers

from app.models import UserForm


class UserFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserForm
        fields = (
            'layout',
            'a',
            'b',
            'c',
            'd',
            'email',
            'budget',
            'current_kitchen',
            'desired_kitchen',
            'is_island',
        )
