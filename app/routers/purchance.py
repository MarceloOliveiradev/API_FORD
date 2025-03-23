from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas
from app.CRUD import crud_purchance
from app.database import get_db
from app.auth import get_current_user
from app.models import User
from app.auth import get_current_admin_user



router = APIRouter(
    prefix="/purchances",
    tags=["Purchances"]
)

@router.post("/", response_model=schemas.PurchanceOut)
def create(purchance: schemas.PurchanceCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user), ):
    return crud_purchance.create_purchance(db, purchance)

@router.get("/", response_model=List[schemas.PurchanceOut])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_purchance.get_purchances(db, skip=skip, limit=limit)

@router.get("/{purchance_id}", response_model=schemas.PurchanceOut)
def read_one(purchance_id: int, db: Session = Depends(get_db)):
    p = crud_purchance.get_purchance_by_id(db, purchance_id)
    if not p:
        raise HTTPException(status_code=404, detail="Purchance not found")
    return p

@router.put("/{purchance_id}", response_model=schemas.PurchanceOut)
def update(purchance_id: int, purchance_data: schemas.PurchanceUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user), ):
    p = crud_purchance.update_purchance(db, purchance_id, purchance_data)
    if not p:
        raise HTTPException(status_code=404, detail="Purchance not found")
    return p

@router.delete("/{purchance_id}", response_model=schemas.PurchanceOut)
def delete(purchance_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user), ):
    p = crud_purchance.delete_purchance(db, purchance_id)
    if not p:
        raise HTTPException(status_code=404, detail="Purchance not found")
    return p
