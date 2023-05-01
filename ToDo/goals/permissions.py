from typing import Any

from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission
from rest_framework.request import Request

from ToDo.goals.models import BoardParticipant, Board, GoalCategory, Goal, GoalComment


class BoardPermissions(IsAuthenticated):
    def has_object_permission(self, request: Request, view, obj: Board) -> bool:
        _filters: dict[str, Any] = {'user': request.user.id, 'board_id': obj.id}
        if request.method not in SAFE_METHODS:
            _filters['role__in'] = BoardParticipant.Role.owner

        return BoardParticipant.objects.filter(**_filters).exists()


class GoalCategoryPermission(IsAuthenticated):
    def has_object_permission(self, request: Request, view, obj: GoalCategory) -> bool:
        _filters: dict[str, Any] = {'user': request.user.id, 'board_id': obj.board_id}
        if request.method not in SAFE_METHODS:
            _filters['role__in'] = [BoardParticipant.Role.owner, BoardParticipant.Role.writer]

        return BoardParticipant.objects.filter(**_filters).exists()


class GoalPermission(IsAuthenticated):
    def has_object_permission(self, request: Request, view, obj: Goal) -> bool:
        _filters: dict[str, Any] = {'user': request.user.id, 'board_id': obj.category.board_id}
        if request.method not in SAFE_METHODS:
            _filters['role'] = BoardParticipant.Role.owner

        return BoardParticipant.objects.filter(**_filters).exists()


class CommentPermission(IsAuthenticated):
    def has_object_permission(self, request: Request, view, obj: GoalComment) -> bool:
        return any((request.method not in SAFE_METHODS, obj.user_id == request.user.id))
