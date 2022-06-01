from rest_framework import serializers

from .models import Country


class CountrySerializer(serializers.Serializer):
    name = serializers.JSONField()
    status = serializers.CharField()
    independent = serializers.BooleanField()
    region = serializers.CharField()
    subregion = serializers.CharField()
    tld =  serializers.CharField()
    latlng = serializers.JSONField()

    def validate(self, attrs):

        if not attrs.get('tld'):
            raise serializers.ValidationError("Does not have tld")
        if not attrs.get('name'):
            raise serializers.ValidationError("Does not have name")
        if not(attrs.get('name')).get('common'):
                raise serializers.ValidationError("Does not have common")
        if not attrs.get('status'):
            raise serializers.ValidationError("Does not have status")
        if not attrs.get('independent'):
            raise serializers.ValidationError("Does not have independent")
        if not attrs.get('region'):
            raise serializers.ValidationError("Does not have region")
        if not attrs.get('subregion'):
            raise serializers.ValidationError("Does not have subregion")
        if not attrs.get('latlng'):
            raise serializers.ValidationError("Does not have latlng")
        attrs['name'] = (attrs.get('name')).get('common')
        return super().validate(attrs)

class CountrySaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        exclude = ['created_at', 'updated_at']

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.tld = validated_data.get('tld', instance.tld)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.independent = validated_data.get('independent', instance.independent)
    #     instance.region = validated_data.get('region', instance.region)
    #     instance.subregion = validated_data.get('subregion', instance.subregion)
    #     instance.lat = validated_data.get('lat', instance.lat)
    #     instance.long = validated_data.get('long', instance.long)
    #     instance.save

    #     return instance

class LanguageSerializer(serializers.Serializer):
    latlng = serializers.JSONField
    def validate(self, attrs):
        if not attrs[0]:
            raise serializers.ValidationError("Does not have latitude")
        if not attrs[1]:
            raise serializers.ValidationError("Does not have logitude")
        attrs['latitude'] = attrs[0]
        attrs['longitude'] = attrs[1]
        return super().validate(attrs)
