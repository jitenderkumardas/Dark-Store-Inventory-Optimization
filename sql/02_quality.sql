SELECT 'stores' table_name,COUNT(*) rows FROM stores UNION ALL SELECT 'products',COUNT(*) FROM products UNION ALL SELECT 'orders',COUNT(*) FROM orders UNION ALL SELECT 'order_items',COUNT(*) FROM order_items UNION ALL SELECT 'inventory',COUNT(*) FROM inventory UNION ALL SELECT 'picking_logs',COUNT(*) FROM picking_logs;
SELECT order_id,COUNT(*) FROM orders GROUP BY order_id HAVING COUNT(*)>1;
SELECT * FROM orders WHERE picking_completed_at<picking_started_at;
SELECT * FROM order_items WHERE quantity<=0;
