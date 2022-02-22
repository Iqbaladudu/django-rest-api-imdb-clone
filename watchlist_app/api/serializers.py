from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ('watchlist',)


class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    # Add connection
    # nama variabelnya harus sama dengan related_name
    watchlist = WatchListSerializer(many=True, read_only=True)

    # Return __str__ return object Whatchlist alih2 semua data
    # Penting!! liat dokumentasi serializer relation
    # watchlist = serializers.StringRelatedField(many=True)

    # Hyperlink Connection
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name='movie-details')

    class Meta:
        model = StreamPlatform
        fields = "__all__"

    # def get_len_name(self, objects: Movie):
    #     return len(objects.name)

    # def validate(self, data):
    #     if data['title'] == data['storyline']:
    #         raise serializers.ValidationError(
    #             "Title and Description should be different!")
    #     else:
    #         return data

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError(
    #             "Name must be at least 2 characters")
    #     else:
    #         return value

# # validators
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance: Movie, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     # Object Level Validation
#     def validate(data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError(
#                 "Title and Description should be different!")
#         else:
#             return data

    # Field Level Validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     return value
