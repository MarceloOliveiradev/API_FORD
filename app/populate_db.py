from datetime import date
from app.database import SessionLocal
from app.models import (
    DimSuplier, DimLocations, DimParts, DimPurchances,
    PurchanceType
)

# Conecta ao banco
db = SessionLocal()

try:
    # 1. Cria uma localização
    location = DimLocations(
        market="Europe",
        country="Germany",
        province="Bavaria",
        city="Munich"
    )
    db.add(location)
    db.commit()
    db.refresh(location)

    # 2. Cria um supplier atrelado à localização
    suplier = DimSuplier(
        suplier_name="Suplier Alpha",
        location_id=location.location_id
    )
    db.add(suplier)
    db.commit()
    db.refresh(suplier)

    # 3. Cria a Part sem last_id_purchase (temporariamente nulo)
    part = DimParts(
        part_name="Motor Turbo",
        supplier_id=suplier.suplier_id,
        last_id_purchase=None  # deixamos em branco por enquanto
    )
    db.add(part)
    db.commit()
    db.refresh(part)

    # 4. Cria a Purchance referenciando a Part
    purchance = DimPurchances(
        purchance_type=PurchanceType.bulk,
        purchance_date=date(2024, 1, 10),
        part_id=part.part_id
    )
    db.add(purchance)
    db.commit()
    db.refresh(purchance)

    # 5. Atualiza a Part com o ID da Purchance
    part.last_id_purchase = purchance.purchance_id
    db.commit()

    print("✅ Banco populado com sucesso!")

except Exception as e:
    print(f"❌ Erro ao popular o banco: {e}")
    db.rollback()
finally:
    db.close()
