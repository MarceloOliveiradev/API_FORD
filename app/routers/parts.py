from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas
from app.CRUD import crud_parts
from app.database import get_db
from app.auth import get_current_user
from app.models import User
from app.auth import get_current_admin_user



router = APIRouter(
    prefix="/parts",
    tags=["Parts"]
)

@router.post("/", response_model=schemas.PartOut)
def create(part: schemas.PartCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user),
):
    return crud_parts.create_part(db, part)

@router.get("/", response_model=List[schemas.PartOut])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_parts.get_parts(db, skip=skip, limit=limit)

@router.get("/{part_id}", response_model=schemas.PartOut)
def read_one(part_id: int, db: Session = Depends(get_db)):
    part = crud_parts.get_part_by_id(db, part_id)
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    return part

@router.put("/{part_id}", response_model=schemas.PartOut)
def update(part_id: int, part_data: schemas.PartUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user), ):
    part = crud_parts.update_part(db, part_id, part_data)
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    return part

@router.delete("/{part_id}", response_model=schemas.PartOut)
def delete(part_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user), ):
    part = crud_parts.delete_part(db, part_id)
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    return part
