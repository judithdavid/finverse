from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.repositories.notification_repository import (
    NotificationRepository,
)
from backend.app.schemas.notification import (
    NotificationCreate,
    NotificationResponse,
)
from backend.app.services.notification_service import (
    NotificationService,
)

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"],
)


@router.post("/", response_model=NotificationResponse, status_code=201)
def create_notification(
    notification: NotificationCreate,
    db: Session = Depends(get_db),
):
    repository = NotificationRepository(db)
    service = NotificationService(repository)

    return service.create_notification(notification)


@router.get("/", response_model=list[NotificationResponse])
def get_notifications(
    db: Session = Depends(get_db),
):
    repository = NotificationRepository(db)
    service = NotificationService(repository)

    return service.get_notifications()


@router.get("/{notification_id}", response_model=NotificationResponse)
def get_notification(
    notification_id: int,
    db: Session = Depends(get_db),
):
    repository = NotificationRepository(db)
    service = NotificationService(repository)

    notification = service.get_notification(notification_id)

    if notification is None:
        raise HTTPException(
            status_code=404,
            detail="Notification not found",
        )

    return notification


@router.delete("/{notification_id}")
def delete_notification(
    notification_id: int,
    db: Session = Depends(get_db),
):
    repository = NotificationRepository(db)
    service = NotificationService(repository)

    notification = service.delete_notification(
        notification_id
    )

    if notification is None:
        raise HTTPException(
            status_code=404,
            detail="Notification not found",
        )

    return {
        "message": "Notification deleted successfully"
    }
