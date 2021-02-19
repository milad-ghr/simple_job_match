from rest_framework import serializers

from positions.models import Position, PositionCategory, PositionLocation


class PositionLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = PositionLocation
        fields = ['country', 'city', 'address_detail', 'full_address']
        read_only_fields = ['full_address']


class PositionCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PositionCategory
        fields = ['category', 'detail']


class PositionSerializer(serializers.ModelSerializer):
    category = PositionCategorySerializer()
    location = PositionLocationSerializer()
    education = serializers.ChoiceField(choices=['bachelor', 'master'])
    gender = serializers.ChoiceField(choices=['Male', 'Female'])

    class Meta:
        model = Position
        fields = ['title', 'category', 'min_age', 'max_age', 'education', 'gender', 'salary', 'location',
                  'created_at', 'expired_at', 'lived_at']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        category = validated_data['category']['category']
        category_detail = validated_data['category']['detail']
        category_object = PositionCategory.objects.create(category=category, detail=category_detail)
        validated_data['category'] = category_object
        category_location_country = validated_data['location']['country']
        category_location_city = validated_data['location']['city']
        category_location_detail = validated_data['location']['address_detail']
        location_object = PositionLocation.objects.create(
            country=category_location_country,
            city=category_location_city,
            address_detail=category_location_detail
        )
        validated_data['location'] = location_object
        return super().create(validated_data)