import pandas as pd
from pathlib import Path
B=Path(__file__).resolve().parents[1];R=B/'data/raw';O=B/'data/processed';O.mkdir(exist_ok=True)
x=pd.read_csv(R/'orders.csv')
for c in ['order_datetime','order_created_at','picking_started_at','picking_completed_at','packed_at','dispatched_at']:x[c]=pd.to_datetime(x[c])
x['picking_time_minutes']=(x.picking_completed_at-x.picking_started_at).dt.total_seconds()/60
x['fulfillment_time_minutes']=(x.dispatched_at-x.order_created_at).dt.total_seconds()/60
x.to_csv(O/'orders_clean.csv',index=False)
