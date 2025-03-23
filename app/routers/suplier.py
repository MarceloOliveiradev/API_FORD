from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas
from app.CRUD import crud_suplier
from app.database import get_db
from app.auth import get_current_user
from app.models import User
from app.auth import get_current_admin_user


router = APIRouter(
    prefix="/supliers",
    tags=["Suppliers"]
)

@router.post("/", response_model=schemas.SuplierOut)
def create(suplier: schemas.SuplierCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user), 
):

    return crud_suplier.create_suplier(db, suplier)

@router.get("/", response_model=List[schemas.SuplierOut])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db) ):
    return crud_suplier.get_supliers(db, skip=skip, limit=limit)

@router.get("/{suplier_id}", response_model=schemas.SuplierOut)
def read_one(suplier_id: int, db: Session = Depends(get_db) ):
    suplier = crud_suplier.get_suplier_by_id(db, suplier_id)
    if not suplier:
        raise HTTPException(status_code=404, detail="Suplier not found")
    return suplier

@router.put("/{suplier_id}", response_model=schemas.SuplierOut)
def update(suplier_id: int, suplier_data: schemas.SuplierUpdate, db: Session = Depends(get_db),  current_user: User = Depends(get_current_admin_user), ):
    suplier = crud_suplier.update_suplier(db, suplier_id, suplier_data)
    if not suplier:
        raise HTTPException(status_code=404, detail="Suplier not found")
    return suplier

@router.delete("/{suplier_id}", response_model=schemas.SuplierOut)
def delete(suplier_id: int, db: Session = Depends(get_db),  current_user: User = Depends(get_current_admin_user), ):
    suplier = crud_suplier.delete_suplier(db, suplier_id)
    if not suplier:
        raise HTTPException(status_code=404, detail="Suplier not found")
    return suplier
