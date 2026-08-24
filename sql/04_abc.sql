CREATE OR REPLACE VIEW vw_product_abc AS
WITH s AS(SELECT product_id,COUNT(DISTINCT order_id) order_count,SUM(quantity) units_sold,SUM(quantity*unit_price) sales_value FROM order_items GROUP BY product_id),
c AS(SELECT *,SUM(units_sold) OVER(ORDER BY units_sold DESC) cumulative_units,SUM(units_sold) OVER() total_units FROM s)
SELECT c.product_id,p.sku_code,p.product_name,p.category,p.subcategory,c.order_count,c.units_sold,c.sales_value,ROUND((100*c.cumulative_units/NULLIF(c.total_units,0))::numeric,2) cumulative_pct,
CASE WHEN 100*c.cumulative_units/NULLIF(c.total_units,0)<=70 THEN 'A' WHEN 100*c.cumulative_units/NULLIF(c.total_units,0)<=90 THEN 'B' ELSE 'C' END abc_class,DENSE_RANK() OVER(ORDER BY c.order_count DESC) velocity_rank FROM c JOIN products p USING(product_id);
