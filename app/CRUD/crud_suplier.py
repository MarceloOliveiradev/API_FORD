from sqlalchemy.orm import Session
from app.models import DimSuplier
from app.schemas import SuplierCreate, SuplierUpdate

def create_suplier(db: Session, suplier: SuplierCreate):
    db_suplier = DimSuplier(**suplier.dict())
    db.add(db_suplier)
    db.commit()
    db.refresh(db_suplier)
    return db_suplier

def get_supliers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DimSuplier).offset(skip).limit(limit).all()

def get_suplier_by_id(db: Session, suplier_id: int):
    return db.query(DimSuplier).filter(DimSuplier.suplier_id == suplier_id).first()

def update_suplier(db: Session, suplier_id: int, suplier_update: SuplierUpdate):
    db_suplier = get_suplier_by_id(db, suplier_id)
    if not db_suplier:
        return None
    for field, value in suplier_update.dict(exclude_unset=True).items():
        setattr(db_suplier, field, value)
    db.commit()
    db.refresh(db_suplier)
    return db_suplier

def delete_suplier(db: Session, suplier_id: int):
    db_suplier = get_suplier_by_id(db, suplier_id)
    if not db_suplier:
        return None
    db.delete(db_suplier)
    db.commit()
    return db_suplier
