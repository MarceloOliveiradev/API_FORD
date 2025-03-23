from sqlalchemy.orm import Session
from app.models import FactWarranties
from app.schemas import WarrantyCreate, WarrantyUpdate

def create_warranty(db: Session, w: WarrantyCreate):
    db_w = FactWarranties(**w.dict())
    db.add(db_w)
    db.commit()
    db.refresh(db_w)
    return db_w

def get_warranties(db: Session, skip: int = 0, limit: int = 100):
    return db.query(FactWarranties).offset(skip).limit(limit).all()

def get_warranty_by_id(db: Session, claim_key: int):
    return db.query(FactWarranties).filter(FactWarranties.claim_key == claim_key).first()

def update_warranty(db: Session, claim_key: int, data: WarrantyUpdate):
    db_w = get_warranty_by_id(db, claim_key)
    if not db_w:
        return None
    for field, value in data.dict(exclude_unset=True).items():
        setattr(db_w, field, value)
    db.commit()
    db.refresh(db_w)
    return db_w

def delete_warranty(db: Session, claim_key: int):
    db_w = get_warranty_by_id(db, claim_key)
    if not db_w:
        return None
    db.delete(db_w)
    db.commit()
    return db_w
