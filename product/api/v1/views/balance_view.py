from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from api.v1.permissions import OnlyStaffCanChangedBalance
from api.v1.serializers.course_serializer import (CourseSerializer,
                                                  CreateCourseSerializer,
                                                  CreateGroupSerializer,
                                                  CreateLessonSerializer,
                                                  GroupSerializer,
                                                  LessonSerializer)
from api.v1.serializers.balance_serializer import BalanceSerializer
from courses.models import Balance


class BalanceViewSet(viewsets.ModelViewSet):
    permission_classes = (OnlyStaffCanChangedBalance, )
