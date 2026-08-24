import pandas as pd,numpy as np
from pathlib import Path
B=Path(__file__).resolve().parents[1];R=B/'data/raw';O=B/'data/processed'
a=pd.read_csv(O/'product_abc.csv');l=pd.read_csv(R/'store_layout.csv');x=a.merge(l,on='product_id')
x['velocity_score']=x.units_sold/x.units_sold.max();x['distance_score']=x.distance_from_packing_m/x.distance_from_packing_m.max()
x['optimization_score']=.6*x.velocity_score+.4*x.distance_score
x['proposed_distance_m']=np.where(x.abc_class.eq('A'),x.distance_from_packing_m*.6,x.distance_from_packing_m)
x['distance_saved_m']=x.distance_from_packing_m-x.proposed_distance_m
x['estimated_minutes_saved_per_pick']=x.distance_saved_m/1.2/60
x.sort_values('optimization_score',ascending=False).to_csv(O/'layout_optimization.csv',index=False)
