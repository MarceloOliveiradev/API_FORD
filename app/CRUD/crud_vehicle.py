from sqlalchemy.orm import Session
from app.models import DimVehicle
from app.schemas import VehicleCreate, VehicleUpdate

def create_vehicle(db: Session, vehicle: VehicleCreate):
    db_vehicle = DimVehicle(**vehicle.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def get_vehicles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DimVehicle).offset(skip).limit(limit).all()

def get_vehicle_by_id(db: Session, vehicle_id: int):
    return db.query(DimVehicle).filter(DimVehicle.vehicle_id == vehicle_id).first()

def update_vehicle(db: Session, vehicle_id: int, vehicle_update: VehicleUpdate):
    db_vehicle = get_vehicle_by_id(db, vehicle_id)
    if not db_vehicle:
        return None
    for field, value in vehicle_update.dict(exclude_unset=True).items():
        setattr(db_vehicle, field, value)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def delete_vehicle(db: Session, vehicle_id: int):
    db_vehicle = get_vehicle_by_id(db, vehicle_id)
    if not db_vehicle:
        return None
    db.delete(db_vehicle)
    db.commit()
    return db_vehicle
