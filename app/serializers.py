# iris_api/serializers.py

from rest_framework import serializers

class IrisInputSerializer(serializers.Serializer):
    sepal_length = serializers.FloatField()
    sepal_width = serializers.FloatField()
    petal_length = serializers.FloatField()
    petal_width = serializers.FloatField()

