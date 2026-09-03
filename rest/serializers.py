from rest_framework import serializers
from .models import Top, Tovar


class TopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Top
        fields = "__all__"


class TovarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tovar
        fields = "__all__"