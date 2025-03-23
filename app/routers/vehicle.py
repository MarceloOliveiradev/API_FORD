from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas
from app.CRUD import crud_vehicle
from app.database import get_db
from app.auth import get_current_admin_user, get_current_user
from app.models import User




router = APIRouter(
    prefix="/vehicle",
    tags=["Vehicle"]
)

@router.post("/", response_model=schemas.VehicleOut)
def create(vehicle: schemas.VehicleCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user), ):
    return crud_vehicle.create_vehicle(db, vehicle)

@router.get("/", response_model=List[schemas.VehicleOut])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_vehicle.get_vehicles(db, skip=skip, limit=limit)

@router.get("/{vehicle_id}", response_model=schemas.VehicleOut)
def read_one(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = crud_vehicle.get_vehicle_by_id(db, vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.put("/{vehicle_id}", response_model=schemas.VehicleOut)
def update(vehicle_id: int, vehicle_data: schemas.VehicleUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user), ):
    vehicle = crud_vehicle.update_vehicle(db, vehicle_id, vehicle_data)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.delete("/{vehicle_id}", response_model=schemas.VehicleOut)
def delete(vehicle_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user), ):
    vehicle = crud_vehicle.delete_vehicle(db, vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle
