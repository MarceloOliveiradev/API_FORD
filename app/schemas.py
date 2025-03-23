from enum import Enum
from typing import Optional
from datetime import date
from pydantic import BaseModel

# =========================================
# 🔐 User & Token (Auth)
# =========================================

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    cpf: str 
    email: str

class UserOut(UserBase):
    id: int
    cpf: Optional[str] = None
    
    model_config = {"from_attributes": True}

class Token(BaseModel):
    access_token: str
    token_type: str

# =========================================
# 🌍 Dim_Locations (não tem schema de rota por enquanto)
# =========================================
# Caso precise futuramente, podemos adicionar.

# =========================================
# 🧩 Parts
# =========================================

class PartBase(BaseModel):
    part_name: str
    last_id_purchase: int
    supplier_id: int

class PartCreate(PartBase):
    pass

class PartUpdate(BaseModel):
    part_name: Optional[str] = None
    last_id_purchase: Optional[int] = None
    supplier_id: Optional[int] = None

class PartOut(PartBase):
    part_id: int

    model_config = {"from_attributes": True}

# =========================================
# 🚗 Vehicles
# =========================================

class PropulsionType(str, Enum):
    eletric = "eletric"
    hybrid = "hybrid"
    gas = "gas"

class VehicleBase(BaseModel):
    model: str
    prod_date: date
    year: int
    propulsion: PropulsionType

class VehicleCreate(VehicleBase):
    pass

class VehicleUpdate(BaseModel):
    model: Optional[str] = None
    prod_date: Optional[date] = None
    year: Optional[int] = None
    propulsion: Optional[PropulsionType] = None

class VehicleOut(VehicleBase):
    vehicle_id: int

    model_config = {"from_attributes": True}

# =========================================
# 🛒 Purchances
# =========================================

class PurchanceType(str, Enum):
    bulk = "bulk"
    warranty = "warranty"

class PurchanceBase(BaseModel):
    purchance_type: PurchanceType
    purchance_date: date
    part_id: int

class PurchanceCreate(PurchanceBase):
    pass

class PurchanceUpdate(BaseModel):
    purchance_type: Optional[PurchanceType] = None
    purchance_date: Optional[date] = None
    part_id: Optional[int] = None

class PurchanceOut(PurchanceBase):
    purchance_id: int

    model_config = {"from_attributes": True}

# =========================================
# 🧾 Warranties
# =========================================

class WarrantyBase(BaseModel):
    vehicle_id: int
    repair_date: date
    client_comment: Optional[str] = None
    tech_comment: str
    part_id: int
    classifed_failured: str
    location_id: int
    purchance_id: int

class WarrantyCreate(WarrantyBase):
    pass

class WarrantyUpdate(BaseModel):
    vehicle_id: Optional[int] = None
    repair_date: Optional[date] = None
    client_comment: Optional[str] = None
    tech_comment: Optional[str] = None
    part_id: Optional[int] = None
    classifed_failured: Optional[str] = None
    location_id: Optional[int] = None
    purchance_id: Optional[int] = None

class WarrantyOut(WarrantyBase):
    claim_key: int

    model_config = {"from_attributes": True}

# =========================================
# 🧾 Supliers
# =========================================

class SuplierBase(BaseModel):
    suplier_name: str
    location_id: int

class SuplierCreate(SuplierBase):
    pass

class SuplierUpdate(BaseModel):
    suplier_name: Optional[str] = None
    location_id: Optional[int] = None

class SuplierOut(SuplierBase):
    suplier_id: int

    model_config = {"from_attributes": True}
