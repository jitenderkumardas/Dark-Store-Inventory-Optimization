\copy stores FROM 'data/raw/stores.csv' CSV HEADER;
\copy products FROM 'data/raw/products.csv' CSV HEADER;
\copy orders FROM 'data/raw/orders.csv' CSV HEADER;
\copy order_items FROM 'data/raw/order_items.csv' CSV HEADER;
\copy inventory FROM 'data/raw/inventory.csv' CSV HEADER;
\copy store_layout FROM 'data/raw/store_layout.csv' CSV HEADER;
\copy picking_logs FROM 'data/raw/picking_logs.csv' CSV HEADER;
\copy dispatch_logs FROM 'data/raw/dispatch_logs.csv' CSV HEADER;
