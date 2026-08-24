import pandas as pd
from pathlib import Path
B=Path(__file__).resolve().parents[1];R=B/'data/raw';O=B/'data/processed';O.mkdir(exist_ok=True)
i=pd.read_csv(R/'order_items.csv');p=pd.read_csv(R/'products.csv')
s=i.groupby('product_id').agg(order_count=('order_id','nunique'),units_sold=('quantity','sum')).reset_index()
s['sales_value']=i.assign(v=i.quantity*i.unit_price).groupby('product_id').v.sum().reindex(s.product_id).values
s=s.sort_values('units_sold',ascending=False).reset_index(drop=True);s['cum_pct']=100*s.units_sold.cumsum()/s.units_sold.sum()
s['abc_class']=pd.cut(s.cum_pct,[-float('inf'),70,90,float('inf')],labels=['A','B','C'])
s['velocity_rank']=s.order_count.rank(method='dense',ascending=False)
s.merge(p,on='product_id').to_csv(O/'product_abc.csv',index=False)
