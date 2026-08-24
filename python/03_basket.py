import pandas as pd
from pathlib import Path
from itertools import combinations

BASE = Path(__file__).resolve().parents[1]
RAW = BASE / "data/raw"
OUT = BASE / "data/processed"
OUT.mkdir(exist_ok=True)

items = pd.read_csv(RAW / "order_items.csv")
transactions = items.groupby("order_id")["product_id"].apply(lambda x: sorted(set(x)))

n_orders = len(transactions)
product_order_count = items.groupby("product_id")["order_id"].nunique().to_dict()

pair_counts = {}
for products in transactions:
    for a, b in combinations(products, 2):
        pair_counts[(a,b)] = pair_counts.get((a,b), 0) + 1

rows=[]
for (a,b), count in pair_counts.items():
    support = count / n_orders
    conf_a_b = count / product_order_count[a]
    conf_b_a = count / product_order_count[b]
    expected = (product_order_count[a]/n_orders) * (product_order_count[b]/n_orders)
    lift = support / expected if expected else 0
    if support >= 0.01 and lift >= 1.20:
        rows.append((a,b,support,conf_a_b,conf_b_a,lift))

rules = pd.DataFrame(rows, columns=[
    "product_a","product_b","support","confidence_a_to_b",
    "confidence_b_to_a","lift"
]).sort_values("lift", ascending=False)

rules.to_csv(OUT/"market_basket_rules.csv", index=False)
print(f"Generated {len(rules):,} market-basket pairs.")
