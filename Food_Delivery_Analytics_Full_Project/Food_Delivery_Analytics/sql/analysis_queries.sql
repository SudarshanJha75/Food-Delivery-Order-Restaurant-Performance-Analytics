USE food_delivery_analytics;

-- 1. Total orders and delivered orders
SELECT COUNT(*) AS total_orders,
       SUM(order_status = 'Delivered') AS delivered_orders
FROM orders;

-- 2. Revenue by area
SELECT area, ROUND(SUM(food_revenue), 2) AS food_revenue
FROM orders
GROUP BY area
ORDER BY food_revenue DESC;

-- 3. Busiest ordering hours
SELECT order_hour, COUNT(*) AS total_orders
FROM orders
GROUP BY order_hour
ORDER BY total_orders DESC;

-- 4. Restaurant performance
SELECT restaurant_name,
       COUNT(*) AS orders,
       ROUND(SUM(food_revenue), 2) AS revenue,
       ROUND(AVG(restaurant_rating), 2) AS avg_rating
FROM orders
GROUP BY restaurant_name
ORDER BY revenue DESC;

-- 5. Average delivery time by traffic
SELECT traffic, ROUND(AVG(delivery_time_min), 2) AS avg_delivery_minutes
FROM orders
GROUP BY traffic;
