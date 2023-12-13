from rest_framework import serializers
from .models import MovieModel, ActorModel
from django.db import transaction


from rest_framework import serializers
from .models import MovieModel, ActorModel, MovieActorModel

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorModel
        fields = ('id', 'fname', 'lname')

class MovieSerializer(serializers.ModelSerializer):
    actor_ids = serializers.ListField(child=serializers.IntegerField(), required=False)
    # actor_idss = serializers.SerializerMethodField()
    # def get_actor_idss(self, obj):
    #     # Retrieve the list of actor IDs associated with the movie
    #     movie_actor_relations = MovieActorModel.objects.filter(movie_id=obj)
    #     return [relation.actor_id.fname for relation in movie_actor_relations]
    
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = MovieModel
        fields = ('id', 'title', 'description', 'release_date', 'year', 'created_at', 'actor_ids', 'actors')

    def create(self, validated_data):
      # Use transaction.atomic to wrap the database operations in a transaction
        with transaction.atomic():
            try:
                # Pop actor_ids from validated_data and handle it separately
                actor_ids = validated_data.pop('actor_ids', [])
                movie = super().create(validated_data)

                # Associate actors with the movie
                actors = ActorModel.objects.filter(id__in=actor_ids)
                for actor in actors:
                    MovieActorModel.objects.create(movie_id=movie, actor_id=actor)
            except Exception as e:
                # Handle the exception (you might want to log it or take other actions)
                print(f"Error creating movie: {str(e)}")

                # Rollback the transaction
                transaction.set_rollback(True)

        return movie


    
