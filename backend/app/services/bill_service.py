from backend.app.repositories.bill_repository import BillRepository
from backend.app.schemas.bill import BillCreate


class BillService:
    def __init__(self, repository: BillRepository):
        self.repository = repository

    def create_bill(self, bill: BillCreate):
        return self.repository.create(bill)

    def get_bill(self, bill_id: int):
        return self.repository.get_by_id(bill_id)

    def get_bills(self):
        return self.repository.get_all()

    def delete_bill(self, bill_id: int):
        return self.repository.delete(bill_id)
