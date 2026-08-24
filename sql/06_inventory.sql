WITH av AS(SELECT store_id,product_id,AVG(stock_qty) avg_stock FROM inventory GROUP BY 1,2),sales AS(SELECT o.store_id,oi.product_id,SUM(oi.quantity) units_sold FROM orders o JOIN order_items oi USING(order_id) GROUP BY 1,2)
SELECT s.store_id,s.product_id,s.units_sold,av.avg_stock,ROUND((s.units_sold/NULLIF(av.avg_stock,0))::numeric,2) inventory_turnover FROM sales s JOIN av USING(store_id,product_id);
SELECT store_id,ROUND((100*AVG(stockout_flag::int))::numeric,2) stockout_rate_pct FROM inventory GROUP BY store_id;
