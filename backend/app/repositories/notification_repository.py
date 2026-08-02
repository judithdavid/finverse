from sqlalchemy.orm import Session

from backend.app.models.notification import Notification
from backend.app.schemas.notification import NotificationCreate


class NotificationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        notification: NotificationCreate,
    ) -> Notification:
        db_notification = Notification(
            title=notification.title,
            message=notification.message,
            is_read=notification.is_read,
            user_id=notification.user_id,
        )

        self.db.add(db_notification)
        self.db.commit()
        self.db.refresh(db_notification)

        return db_notification

    def get_by_id(self, notification_id: int):
        return (
            self.db.query(Notification)
            .filter(Notification.id == notification_id)
            .first()
        )

    def get_all(self):
        return self.db.query(Notification).all()

    def delete(self, notification_id: int):
        notification = self.get_by_id(notification_id)

        if notification:
            self.db.delete(notification)
            self.db.commit()

        return notification
