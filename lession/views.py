from rest_framework import generics, filters
from .models import Lesson
from .serializers import LessonSerializer
from .pagination import LessonPagination

class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all().order_by('-created_at')
    serializer_class = LessonSerializer
    pagination_class = LessonPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']




