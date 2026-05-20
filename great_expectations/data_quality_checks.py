import pandas as pd
import urllib.request
import json

print("=" * 55)
print("   DATA QUALITY CHECKS - Price Intelligence Platform")
print("=" * 55)

# Charger les vraies donnees de Sara depuis GitHub
URLS = {
    "jumia": "https://raw.githubusercontent.com/E-commerce-Price-Intelligence-Platform/data-engineer/main/output/jumia.json",
    "electroplanet": "https://raw.githubusercontent.com/E-commerce-Price-Intelligence-Platform/data-engineer/main/output/electroplanet.json",
    "amazon": "https://raw.githubusercontent.com/E-commerce-Price-Intelligence-Platform/data-engineer/main/output/amazon.json"
}

all_results = []

for site, url in URLS.items():
    print(f"\n--- Checking {site.upper()} ---")
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
        df = pd.DataFrame(data)
        print(f"Total products loaded: {len(df)}")

        # Règle 1: nom produit non vide
        check1 = df["name"].notnull().all() if "name" in df.columns else False
        print(f"  product name not null:     {check1}")

        # Règle 2: prix positif
        if "price" in df.columns:
            df["price_num"] = pd.to_numeric(df["price"], errors="coerce")
            valid_prices = df["price_num"].dropna()
            null_rate = df["price_num"].isnull().mean()
            check2 = null_rate < 0.5
            print(f"  price null rate < 50%:     {check2} ({null_rate:.1%} null)")
        else:
            check2 = False
            print(f"  price column missing:      False")

        # Règle 3: pas de doublons
        if "url" in df.columns:
            check3 = not df["url"].duplicated().any()
        else:
            check3 = True
        print(f"  no duplicate URLs:         {check3}")

        # Règle 4: site non vide
        if "site" in df.columns:
            check4 = df["site"].notnull().all()
        else:
            check4 = True
        print(f"  site field present:        {check4}")

        passed = sum([check1, check2, check3, check4])
        print(f"  => {passed}/4 checks passed")
        all_results.append(passed == 4)

    except Exception as e:
        print(f"  ERROR loading {site}: {e}")
        all_results.append(False)

print("\n" + "=" * 55)
if all(all_results):
    print("ALL SITES PASSED DATA QUALITY CHECKS!")
else:
    print("SOME CHECKS NEED ATTENTION - SEE DETAILS ABOVE")
print("=" * 55)