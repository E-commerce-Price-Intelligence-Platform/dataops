import pandas as pd

# Créer un DataFrame simulant les données de prix e-commerce
data = {
    "product_id": ["P001", "P002", "P003", "P004", "P005"],
    "product_name": ["iPhone 15", "Samsung S24", "Xiaomi 14", "OnePlus 12", "Pixel 8"],
    "price": [9999.0, 8499.0, 5999.0, 7499.0, 6999.0],
    "platform": ["Jumia", "Avito", "Jumia", "Avito", "Jumia"],
    "timestamp": ["2026-05-20", "2026-05-20", "2026-05-20", "2026-05-20", "2026-05-20"]
}

df = pd.DataFrame(data)

print("=" * 50)
print("   DATA QUALITY CHECKS - Price Intelligence")
print("=" * 50)

# Règle 1: product_id ne doit pas être vide
check1 = df["product_id"].notnull().all()
print(f"✅ product_id not null:     {check1}")

# Règle 2: price doit être positif
check2 = (df["price"] > 0).all()
print(f"✅ price is positive:       {check2}")

# Règle 3: platform dans liste valide
valid_platforms = ["Jumia", "Avito", "Amazon"]
check3 = df["platform"].isin(valid_platforms).all()
print(f"✅ platform is valid:       {check3}")

# Règle 4: product_name ne doit pas être vide
check4 = df["product_name"].notnull().all()
print(f"✅ product_name not null:   {check4}")

# Règle 5: pas de prix dupliqués
check5 = not df["product_id"].duplicated().any()
print(f"✅ no duplicate products:   {check5}")

# Résultat final
print("=" * 50)
all_passed = all([check1, check2, check3, check4, check5])
if all_passed:
    print("🎉 ALL CHECKS PASSED! Data quality is OK!")
else:
    print("❌ SOME CHECKS FAILED!")
print("=" * 50)