from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from django.urls import path
from .models import Community, Widget, Tutorial, Source, Event


class CommunitySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    description = serializers.CharField()
    irc_link = serializers.URLField()
    community_link = serializers.URLField()


class CommunityView(APIView):
    def get(self, request):
        communities = Community.objects.all()
        serializer = CommunitySerializer(communities, many=True)
        return Response({"communities": serializer.data})


class WidgetSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    description = serializers.CharField()
    image = serializers.ImageField()
    link = serializers.URLField()


class WidgetView(APIView):
    def get(self, request):
        widget = Widget.objects.all()
        serializer = WidgetSerializer(widget, many=True)
        return Response({"widgets": serializer.data})


class TutorialSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    author = serializers.CharField(max_length=200)
    published_date = serializers.DateField()
    link = serializers.URLField()
    source = serializers.StringRelatedField(many=True)


class TutorialView(APIView):
    def get(self, request):
        tutorials = Tutorial.objects.all()
        serializer = WidgetSerializer(tutorials, many=True)
        return Response({"tutorials": serializer.data})


class EventSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    venue = serializers.CharField(max_length=350)
    organizer = serializers.CharField(max_length=350)
    date = serializers.DateField()
    time = serializers.TimeField()
    description = serializers.CharField()
    registration_link = serializers.URLField()
    banner = serializers.ImageField()


class EventView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = WidgetSerializer(events, many=True)
        return Response({"events": serializer.data})


class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=350)
    time = serializers.DateTimeField()
    link = serializers.URLField()
    source = serializers.StringRelatedField(many=True)
    # source = serializers.PrimaryKeyRelatedField(queryset=Source.objects.all(), read_only=True)
    image = serializers.ImageField()


class NewsView(APIView):
    def get(self, request):
        news = Event.objects.all()
        serializer = WidgetSerializer(news, many=True)
        return Response({"events": serializer.data})


urlpatterns = [
    path('communities/', CommunityView.as_view()),
    path('widgets/', WidgetView.as_view()),
    path('tutorials/', TutorialView.as_view()),
    path('events/', EventView.as_view()),
    path('news/', NewsView.as_view()),
]
