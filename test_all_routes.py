import requests

BASE_URL = "http://localhost:8000"

# Usuário de teste
test_user = {
    "username": "ronaldinho",
    "email": "ronaldinho@example.com",
    "password": "123456",
    "cpf": "00011122233"
}

# ======================
# 1. Criar usuário
# ======================
register_response = requests.post(f"{BASE_URL}/auth/register", json=test_user)
print("🔐 Register:", register_response.status_code, register_response.text)

# ======================
# 2. Login
# ======================
login_response = requests.post(
    f"{BASE_URL}/auth/login",
    data={
        "username": test_user["username"],
        "password": test_user["password"]
    },
    headers={"Content-Type": "application/x-www-form-urlencoded"}
)
print("🔐 Login:", login_response.status_code, login_response.text)

if login_response.status_code != 200:
    exit()

access_token = login_response.json()["access_token"]
headers = {"Authorization": f"Bearer {access_token}"}

# ======================
# 3. Criar Supplier
# ======================
location_id = 1
supplier_payload = {
    "suplier_name": "Fornecedor Teste",
    "location_id": location_id
}
supplier_response = requests.post(f"{BASE_URL}/supliers/", json=supplier_payload, headers=headers)
print("🚚 Criar Supplier:", supplier_response.status_code, supplier_response.text)
suplier_id = supplier_response.json().get("suplier_id", 1)

# ======================
# 4. Criar Parte
# ======================
part_payload = {
    "part_name": "Parte Teste",
    "last_id_purchase": 1,
    "supplier_id": suplier_id
}
part_response = requests.post(f"{BASE_URL}/parts/", json=part_payload, headers=headers)
print("🔩 Criar Parte:", part_response.status_code, part_response.text)
part_id = part_response.json().get("part_id", 1)

# ======================
# 5. Criar Veículo
# ======================
vehicle_payload = {
    "vin": "123456789ABCDEF",
    "model": "Fusion",
    "prod_date": "2023-01-01",
    "year": 2023,
    "propulsion": "gas"
}
vehicle_response = requests.post(f"{BASE_URL}/vehicle/", json=vehicle_payload, headers=headers)
print("🚗 Criar Veículo:", vehicle_response.status_code, vehicle_response.text)
vehicle_id = vehicle_response.json().get("vehicle_id", 1)

# ======================
# 6. Criar Compras (Purchance)
# ======================
purchance_payload = {
    "purchance_type": "bulk",
    "purchance_date": "2023-05-01",
    "part_id": part_id
}
purchance_response = requests.post(f"{BASE_URL}/purchances/", json=purchance_payload, headers=headers)
print("🛒 Criar Purchance:", purchance_response.status_code, purchance_response.text)
purchance_id = purchance_response.json().get("purchance_id", 1)

# ======================
# 7. Criar Garantia (Warranty)
# ======================
warranty_payload = {
    "vehicle_id": vehicle_id,
    "repair_date": "2023-06-01",
    "client_comment": "Barulho estranho",
    "tech_comment": "Substituição feita",
    "part_id": part_id,
    "classifed_failured": "Desgaste",
    "location_id": location_id,
    "purchance_id": purchance_id
}
warranty_response = requests.post(f"{BASE_URL}/warranties/", json=warranty_payload, headers=headers)
print("🛠️ Criar Garantia:", warranty_response.status_code, warranty_response.text)

# ======================
# 8. Testar Endpoints GET
# ======================
for endpoint in ["parts", "vehicle", "supliers", "purchances", "warranties"]:
    res = requests.get(f"{BASE_URL}/{endpoint}/", headers=headers)
    print(f"📥 GET /{endpoint}/:", res.status_code, res.text)
