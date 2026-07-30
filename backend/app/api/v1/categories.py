from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.repositories.category_repository import CategoryRepository
from backend.app.schemas.category import (
    CategoryCreate,
    CategoryResponse,
)
from backend.app.services.category_service import CategoryService

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.post("/", response_model=CategoryResponse, status_code=201)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
):
    repository = CategoryRepository(db)
    service = CategoryService(repository)

    return service.create_category(category)


@router.get("/", response_model=list[CategoryResponse])
def get_categories(
    db: Session = Depends(get_db),
):
    repository = CategoryRepository(db)
    service = CategoryService(repository)

    return service.get_categories()


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(
    category_id: int,
    db: Session = Depends(get_db),
):
    repository = CategoryRepository(db)
    service = CategoryService(repository)

    category = service.get_category(category_id)

    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found",
        )

    return category


@router.delete("/{category_id}")
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
):
    repository = CategoryRepository(db)
    service = CategoryService(repository)

    category = service.delete_category(category_id)

    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found",
        )

    return {"message": "Category deleted successfully"}
