from backend.app.repositories.notification_repository import (
    NotificationRepository,
)
from backend.app.schemas.notification import NotificationCreate


class NotificationService:
    def __init__(
        self,
        repository: NotificationRepository,
    ):
        self.repository = repository

    def create_notification(
        self,
        notification: NotificationCreate,
    ):
        return self.repository.create(notification)

    def get_notification(
        self,
        notification_id: int,
    ):
        return self.repository.get_by_id(notification_id)

    def get_notifications(self):
        return self.repository.get_all()

    def delete_notification(
        self,
        notification_id: int,
    ):
        return self.repository.delete(notification_id)
