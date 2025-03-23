from sqlalchemy.orm import Session
from app.models import DimPurchances
from app.schemas import PurchanceCreate, PurchanceUpdate

def create_purchance(db: Session, p: PurchanceCreate):
    db_p = DimPurchances(**p.dict())
    db.add(db_p)
    db.commit()
    db.refresh(db_p)
    return db_p

def get_purchances(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DimPurchances).offset(skip).limit(limit).all()

def get_purchance_by_id(db: Session, purchance_id: int):
    return db.query(DimPurchances).filter(DimPurchances.purchance_id == purchance_id).first()

def update_purchance(db: Session, purchance_id: int, data: PurchanceUpdate):
    db_p = get_purchance_by_id(db, purchance_id)
    if not db_p:
        return None
    for field, value in data.dict(exclude_unset=True).items():
        setattr(db_p, field, value)
    db.commit()
    db.refresh(db_p)
    return db_p

def delete_purchance(db: Session, purchance_id: int):
    db_p = get_purchance_by_id(db, purchance_id)
    if not db_p:
        return None
    db.delete(db_p)
    db.commit()
    return db_p
