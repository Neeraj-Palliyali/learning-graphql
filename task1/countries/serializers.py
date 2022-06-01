from rest_framework import serializers

from .models import Country


class CountrySerializer(serializers.Serializer):
    name = serializers.JSONField()
    status = serializers.CharField()
    independent = serializers.BooleanField(default=False)
    region = serializers.CharField()
    subregion = serializers.CharField(allow_blank  = True, default = '')
    tld =  serializers.CharField(allow_blank = True,default = '')
    latlng = serializers.JSONField()
    capital = serializers.CharField(allow_blank  = True, default = '')

    def validate(self, attrs):
        if not attrs.get('name'):
            raise serializers.ValidationError("Does not have name")
        if not(attrs.get('name')).get('common'):
                raise serializers.ValidationError("Does not have common")
        attrs['name'] = (attrs.get('name')).get('common')
        return super().validate(attrs)

class CountrySaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        exclude = ['created_at', 'updated_at']

    def validate(self, attrs):
        return super().validate(attrs)