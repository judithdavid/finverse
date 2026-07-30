from backend.app.repositories.wallet_repository import WalletRepository
from backend.app.schemas.wallet import WalletCreate


class WalletService:
    def __init__(self, repository: WalletRepository):
        self.repository = repository

    def create_wallet(self, wallet: WalletCreate):
        return self.repository.create(wallet)

    def get_wallet(self, wallet_id: int):
        return self.repository.get_by_id(wallet_id)

    def get_wallets(self):
        return self.repository.get_all()

    def delete_wallet(self, wallet_id: int):
        return self.repository.delete(wallet_id)
