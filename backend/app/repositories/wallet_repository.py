from sqlalchemy.orm import Session

from backend.app.models.wallet import Wallet
from backend.app.schemas.wallet import WalletCreate


class WalletRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, wallet: WalletCreate) -> Wallet:
        db_wallet = Wallet(
            name=wallet.name,
            balance=wallet.balance,
            user_id=wallet.user_id,
        )

        self.db.add(db_wallet)
        self.db.commit()
        self.db.refresh(db_wallet)

        return db_wallet

    def get_by_id(self, wallet_id: int):
        return (
            self.db.query(Wallet)
            .filter(Wallet.id == wallet_id)
            .first()
        )

    def get_all(self):
        return self.db.query(Wallet).all()

    def delete(self, wallet_id: int):
        wallet = self.get_by_id(wallet_id)

        if wallet:
            self.db.delete(wallet)
            self.db.commit()

        return wallet
