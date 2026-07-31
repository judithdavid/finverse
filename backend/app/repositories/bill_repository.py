from sqlalchemy.orm import Session

from backend.app.models.bill import Bill
from backend.app.schemas.bill import BillCreate


class BillRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, bill: BillCreate) -> Bill:
        db_bill = Bill(
            name=bill.name,
            amount=bill.amount,
            due_date=bill.due_date,
            is_paid=bill.is_paid,
            user_id=bill.user_id,
        )

        self.db.add(db_bill)
        self.db.commit()
        self.db.refresh(db_bill)

        return db_bill

    def get_by_id(self, bill_id: int):
        return (
            self.db.query(Bill)
            .filter(Bill.id == bill_id)
            .first()
        )

    def get_all(self):
        return self.db.query(Bill).all()

    def delete(self, bill_id: int):
        bill = self.get_by_id(bill_id)

        if bill:
            self.db.delete(bill)
            self.db.commit()

        return bill
