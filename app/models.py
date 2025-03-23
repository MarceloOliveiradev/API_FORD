from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum
from sqlalchemy import Boolean, ForeignKeyConstraint

# Definição dos tipos ENUM
class PropulsionType(enum.Enum):
    eletric = "eletric"
    hybrid = "hybrid"
    gas = "gas"

class PurchanceType(enum.Enum):
    bulk = "bulk"
    warranty = "warranty"

# Modelo Dim_Locations
class DimLocations(Base):
    __tablename__ = "Dim_locations"
    location_id = Column(Integer, primary_key=True, autoincrement=True)
    market = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    province = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)

# Modelo Dim_Suplier
class DimSuplier(Base):
    __tablename__ = "Dim_Suplier"
    suplier_id = Column(Integer, primary_key=True, autoincrement=True)
    suplier_name = Column(String(50), nullable=False)
    location_id = Column(Integer, ForeignKey("Dim_locations.location_id"), nullable=False)
    location = relationship("DimLocations")

# Modelo Dim_Vehicle
class DimVehicle(Base):
    __tablename__ = "Dim_Vehicle"
    vehicle_id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String(255), nullable=False)
    prod_date = Column(Date, nullable=False)
    year = Column(Integer, nullable=False)
    propulsion = Column(Enum(PropulsionType), nullable=False)

# Modelo Dim_Parts
class DimParts(Base):
    __tablename__ = "Dim_Parts"
    part_id = Column(Integer, primary_key=True, autoincrement=True)
    part_name = Column(String(255), nullable=False)
    last_id_purchase = Column(
    Integer,
    ForeignKey("Dim_purchances.purchance_id", use_alter=True, name="fk_parts_purchance", ondelete="SET NULL"),
    nullable=True)
    supplier_id = Column(Integer, ForeignKey("Dim_Suplier.suplier_id"), nullable=False)
    supplier = relationship("DimSuplier")

# Modelo Dim_Purchances
class DimPurchances(Base):
    __tablename__ = "Dim_purchances"
    purchance_id = Column(Integer, primary_key=True, autoincrement=True)
    purchance_type = Column(Enum(PurchanceType), nullable=False)
    purchance_date = Column(Date, nullable=False)
    part_id = Column(Integer, ForeignKey("Dim_Parts.part_id"), nullable=False)
    part = relationship("DimParts", foreign_keys=[part_id])

# Modelo Fact_Warranties
class FactWarranties(Base):
    __tablename__ = "Fact_Warranties"
    claim_key = Column(Integer, primary_key=True, autoincrement=True)
    vehicle_id = Column(Integer, ForeignKey("Dim_Vehicle.vehicle_id"), unique=True, nullable=False)
    repair_date = Column(Date, nullable=False)
    client_comment = Column(String(65535))
    tech_comment = Column(String(65535), nullable=False)
    part_id = Column(Integer, ForeignKey("Dim_Parts.part_id"), nullable=False)
    classifed_failured = Column(String(50), nullable=False)
    location_id = Column(Integer, ForeignKey("Dim_locations.location_id"), nullable=False)
    purchance_id = Column(Integer, ForeignKey("Dim_purchances.purchance_id"), nullable=False)
    
    vehicle = relationship("DimVehicle")
    part = relationship("DimParts")
    location = relationship("DimLocations")
    purchance = relationship("DimPurchances")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    cpf = Column(String(255), nullable=True)


