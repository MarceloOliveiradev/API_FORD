from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from pydantic import BaseModel
from typing import List
from app.database import get_db
from app.models import DimSuplier, DimParts, DimPurchances, FactWarranties, PurchanceType, User
from app.auth import get_current_user

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

class SupplierPurchaseStats(BaseModel):
    suplier_name: str
    total_purchases: int

class PartPurchaseStats(BaseModel):
    part_name: str
    total_purchases: int

class SupplierWarrantyStats(BaseModel):
    suplier_name: str
    total_warranties: int

class AvgPurchanceStats(BaseModel):
    purchance_type: str
    average_value: float

@router.get("/total-purchases-by-supplier", response_model=List[SupplierPurchaseStats])
def total_purchases_by_supplier(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    results = (
        db.query(DimSuplier.suplier_name, func.count(DimPurchances.purchance_id).label("total_purchases"))
        .join(DimParts, DimSuplier.suplier_id == DimParts.supplier_id)
        .join(DimPurchances, DimParts.part_id == DimPurchances.part_id)
        .group_by(DimSuplier.suplier_name)
        .order_by(func.count(DimPurchances.purchance_id).desc())
        .all()
    )
    if not results:
        raise HTTPException(status_code=404, detail="Nenhum dado encontrado.")
    return results

@router.get("/total-purchases-by-part", response_model=List[PartPurchaseStats])
def total_purchases_by_part(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    results = (
        db.query(DimParts.part_name, func.count(DimPurchances.purchance_id).label("total_purchases"))
        .join(DimPurchances, DimParts.part_id == DimPurchances.part_id)
        .group_by(DimParts.part_name)
        .order_by(func.count(DimPurchances.purchance_id).desc())
        .all()
    )
    if not results:
        raise HTTPException(status_code=404, detail="Nenhum dado encontrado.")
    return results

@router.get("/warranties-by-supplier", response_model=List[SupplierWarrantyStats])
def warranties_by_supplier(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    results = (
        db.query(DimSuplier.suplier_name, func.count(FactWarranties.claim_key).label("total_warranties"))
        .join(DimParts, DimSuplier.suplier_id == DimParts.supplier_id)
        .join(FactWarranties, DimParts.part_id == FactWarranties.part_id)
        .group_by(DimSuplier.suplier_name)
        .order_by(func.count(FactWarranties.claim_key).desc())
        .all()
    )
    if not results:
        raise HTTPException(status_code=404, detail="Nenhum dado encontrado.")
    return results

@router.get("/average-purchance-by-type", response_model=List[AvgPurchanceStats])
def average_purchance_by_type(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    results = (
        db.query(DimPurchances.purchance_type, func.avg(DimPurchances.purchance_id).label("average_value"))
        .group_by(DimPurchances.purchance_type)
        .order_by(DimPurchances.purchance_type)
        .all()
    )
    if not results:
        raise HTTPException(status_code=404, detail="Nenhum dado encontrado.")
    return results
