from sqlalchemy.orm import Session
from app.models import DimParts
from app.schemas import PartCreate, PartUpdate

def create_part(db: Session, part: PartCreate):
    db_part = DimParts(**part.dict())
    db.add(db_part)
    db.commit()
    db.refresh(db_part)
    return db_part

def get_parts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DimParts).offset(skip).limit(limit).all()

def get_part_by_id(db: Session, part_id: int):
    return db.query(DimParts).filter(DimParts.part_id == part_id).first()

def update_part(db: Session, part_id: int, part_update: PartUpdate):
    db_part = get_part_by_id(db, part_id)
    if not db_part:
        return None
    for field, value in part_update.dict(exclude_unset=True).items():
        setattr(db_part, field, value)
    db.commit()
    db.refresh(db_part)
    return db_part

def delete_part(db: Session, part_id: int):
    db_part = get_part_by_id(db, part_id)
    if not db_part:
        return None
    db.delete(db_part)
    db.commit()
    return db_part
