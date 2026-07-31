from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.repositories.bill_repository import BillRepository
from backend.app.schemas.bill import BillCreate, BillResponse
from backend.app.services.bill_service import BillService

router = APIRouter(
    prefix="/bills",
    tags=["Bills"],
)


@router.post("/", response_model=BillResponse, status_code=201)
def create_bill(
    bill: BillCreate,
    db: Session = Depends(get_db),
):
    repository = BillRepository(db)
    service = BillService(repository)

    return service.create_bill(bill)


@router.get("/", response_model=list[BillResponse])
def get_bills(
    db: Session = Depends(get_db),
):
    repository = BillRepository(db)
    service = BillService(repository)

    return service.get_bills()


@router.get("/{bill_id}", response_model=BillResponse)
def get_bill(
    bill_id: int,
    db: Session = Depends(get_db),
):
    repository = BillRepository(db)
    service = BillService(repository)

    bill = service.get_bill(bill_id)

    if bill is None:
        raise HTTPException(
            status_code=404,
            detail="Bill not found",
        )

    return bill


@router.delete("/{bill_id}")
def delete_bill(
    bill_id: int,
    db: Session = Depends(get_db),
):
    repository = BillRepository(db)
    service = BillService(repository)

    bill = service.delete_bill(bill_id)

    if bill is None:
        raise HTTPException(
            status_code=404,
            detail="Bill not found",
        )

    return {"message": "Bill deleted successfully"}
