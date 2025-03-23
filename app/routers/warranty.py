from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas
from app.CRUD import crud_warranty
from app.database import get_db
from app.auth import get_current_user
from app.models import User
from app.auth import get_current_admin_user



router = APIRouter(
    prefix="/warranties",
    tags=["Warranties"]
)

@router.post("/", response_model=schemas.WarrantyOut)
def create(w: schemas.WarrantyCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user), ):
    return crud_warranty.create_warranty(db, w)

@router.get("/", response_model=List[schemas.WarrantyOut])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_warranty.get_warranties(db, skip=skip, limit=limit)

@router.get("/{claim_key}", response_model=schemas.WarrantyOut)
def read_one(claim_key: int, db: Session = Depends(get_db)):
    w = crud_warranty.get_warranty_by_id(db, claim_key)
    if not w:
        raise HTTPException(status_code=404, detail="Warranty not found")
    return w

@router.put("/{claim_key}", response_model=schemas.WarrantyOut)
def update(claim_key: int, data: schemas.WarrantyUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user), ):
    w = crud_warranty.update_warranty(db, claim_key, data)
    if not w:
        raise HTTPException(status_code=404, detail="Warranty not found")
    return w

@router.delete("/{claim_key}", response_model=schemas.WarrantyOut)
def delete(claim_key: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user), ):
    w = crud_warranty.delete_warranty(db, claim_key)
    if not w:
        raise HTTPException(status_code=404, detail="Warranty not found")
    return w
