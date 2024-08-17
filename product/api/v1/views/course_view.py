from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, permissions

from api.v1.permissions import IsStudentOrIsAdmin, ReadOnlyOrIsAdmin
from api.v1.serializers.course_serializer import (CourseSerializer,
                                                  CreateCourseSerializer,
                                                  CreateGroupSerializer,
                                                  CreateLessonSerializer,
                                                  GroupSerializer,
                                                  LessonSerializer)
from api.v1.serializers.user_serializer import PurchaseSerializer
from courses.models import Course, Purchase
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta


class LessonViewSet(viewsets.ModelViewSet):
    """Уроки."""

    permission_classes = (IsStudentOrIsAdmin,)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LessonSerializer
        return CreateLessonSerializer

    def perform_create(self, serializer):
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))
        serializer.save(course=course)

    def get_queryset(self):
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))
        return course.lessons.all()


class GroupViewSet(viewsets.ModelViewSet):
    """Группы."""

    permission_classes = (permissions.IsAdminUser,)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return GroupSerializer
        return CreateGroupSerializer

    def perform_create(self, serializer):
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))
        serializer.save(course=course)

    def get_queryset(self):
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))
        return course.groups.all()


class AvailableForPurchaseCourseViewSet(viewsets.ModelViewSet):
    """Курсы доступные к покупке"""

    queryset = Course.objects.all()
    permission_classes = (ReadOnlyOrIsAdmin,)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CourseSerializer
        return CreateCourseSerializer

    def get_queryset(self):
        if Purchase.objects.filter(user=self.request.user).exists():
            return Course.objects.all()
        else:
            purchases = Purchase.objects.select_related('course').filter(user=self.request.user)
            return Course.objects.all().exclude(id__in=[purchase.course.id for purchase in purchases])

    @action(
        methods=['post'],
        detail=True,
        permission_classes=(IsAuthenticated,)
    )
    def pay(self, request, pk=None):
        """Покупка доступа к курсу (подписка на курс)."""
        user = request.user
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(
                {"detail": "Курс не найден."},
                status=status.HTTP_404_NOT_FOUND
            )

        if Purchase.objects.filter(course=course, user=user).exists():
            return Response(
                {"detail": "Вы уже купили этот курс."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if course.price is None:
            subscription_end = None
        else:
            subscription_end = datetime.now() + timedelta(days=30)

# хардкод подписки на 30 дней, потому что вот так. :) В идеале автор курса будет сам устанавливать сроки подписки и
# ценники для неё, для этого нужно будет внести изменения в модели Course и Purchase

        Purchase.objects.create(
            course=course,
            user=user,
            is_subscription=(subscription_end is not None),
            subscription_end=subscription_end
        )

        return Response(
            {"detail": "Курс успешно приобретен."},
            status=status.HTTP_201_CREATED
        )


class PurchasedCoursesViewSet(viewsets.ModelViewSet):
    """Курсы, которые купил пользователь."""

    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        purchases = Purchase.objects.select_related('course').filter(user=self.request.user)
        return Course.objects.filter(id__in=[purchase.course.id for purchase in purchases])
