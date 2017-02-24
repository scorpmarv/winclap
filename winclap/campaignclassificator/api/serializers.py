from rest_framework import serializers


class UserDataSerializer(serializers.Serializer):
    gender = serializers.ChoiceField(['Male', 'Female', 'All'])
    age = serializers.IntegerField(min_value=0)
    platform = serializers.ChoiceField(['iOS', 'Android', 'Windows Phone'])
    connection = serializers.ChoiceField(['WiFi', 'Mobile data'])
