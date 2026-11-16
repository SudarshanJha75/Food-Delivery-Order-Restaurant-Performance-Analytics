CREATE DATABASE IF NOT EXISTS food_delivery_analytics;
USE food_delivery_analytics;

CREATE TABLE IF NOT EXISTS orders (
    order_id VARCHAR(20) PRIMARY KEY,
    order_date DATE,
    order_hour TINYINT,
    customer_id VARCHAR(20),
    restaurant_id VARCHAR(30),
    restaurant_name VARCHAR(100),
    area VARCHAR(80),
    cuisine VARCHAR(80),
    order_amount DECIMAL(10,2),
    discount DECIMAL(10,2),
    delivery_fee DECIMAL(10,2),
    distance_km DECIMAL(6,2),
    weather VARCHAR(30),
    traffic VARCHAR(30),
    vehicle_type VARCHAR(30),
    restaurant_rating DECIMAL(2,1),
    delivery_rating DECIMAL(2,1),
    delivery_time_min INT,
    order_status VARCHAR(20),
    food_revenue DECIMAL(10,2)
);
