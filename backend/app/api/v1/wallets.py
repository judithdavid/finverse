from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.repositories.wallet_repository import WalletRepository
from backend.app.schemas.wallet import WalletCreate, WalletResponse
from backend.app.services.wallet_service import WalletService

router = APIRouter(prefix="/wallets", tags=["Wallets"])


@router.post("/", response_model=WalletResponse, status_code=201)
def create_wallet(
    wallet: WalletCreate,
    db: Session = Depends(get_db),
):
    repository = WalletRepository(db)
    service = WalletService(repository)

    return service.create_wallet(wallet)


@router.get("/", response_model=list[WalletResponse])
def get_wallets(
    db: Session = Depends(get_db),
):
    repository = WalletRepository(db)
    service = WalletService(repository)

    return service.get_wallets()


@router.get("/{wallet_id}", response_model=WalletResponse)
def get_wallet(
    wallet_id: int,
    db: Session = Depends(get_db),
):
    repository = WalletRepository(db)
    service = WalletService(repository)

    wallet = service.get_wallet(wallet_id)

    if wallet is None:
        raise HTTPException(status_code=404, detail="Wallet not found")

    return wallet


@router.delete("/{wallet_id}")
def delete_wallet(
    wallet_id: int,
    db: Session = Depends(get_db),
):
    repository = WalletRepository(db)
    service = WalletService(repository)

    wallet = service.delete_wallet(wallet_id)

    if wallet is None:
        raise HTTPException(status_code=404, detail="Wallet not found")

    return {"message": "Wallet deleted successfully"}
