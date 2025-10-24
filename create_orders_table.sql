-- Create target table for JDBC sink
CREATE TABLE IF NOT EXISTS public.orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    amount NUMERIC(10,2) NOT NULL,
    status TEXT NOT NULL
);
