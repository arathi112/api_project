from rest_framework import serializers
from .models import Destination, DestinationImage


class DestinationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationImage
        fields = ['id', 'image', 'uploaded_at']
        read_only_fields = ['uploaded_at']


class DestinationSerializer(serializers.ModelSerializer):
    images = DestinationImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=100000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )

    class Meta:
        model = Destination
        fields = ['id', 'place_name', 'weather', 'state', 'district', 'description', 'created_at', 'updated_at',
                  'images', 'uploaded_images']

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        destination = Destination.objects.create(**validated_data)

        for image in uploaded_images:
            DestinationImage.objects.create(destination=destination, image=image)

        return destination

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])

        # Update destination fields
        instance.place_name = validated_data.get('place_name', instance.place_name)
        instance.weather = validated_data.get('weather', instance.weather)
        instance.state = validated_data.get('state', instance.state)
        instance.district = validated_data.get('district', instance.district)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        # Add new images
        for image in uploaded_images:
            DestinationImage.objects.create(destination=instance, image=image)

        return instance