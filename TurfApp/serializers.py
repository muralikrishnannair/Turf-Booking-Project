
from rest_framework import serializers
from TurfApp.models import TurfDb


class Turf_Serializer(serializers.ModelSerializer):

    class Meta:
        model = TurfDb
        fields = "__all__"
        read_only_fields = ["id"]
