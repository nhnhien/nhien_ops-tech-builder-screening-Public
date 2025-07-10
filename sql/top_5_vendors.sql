-- CREATE TABLE invoices (
--     id SERIAL PRIMARY KEY,
--     vendor VARCHAR(255),
--     amount NUMERIC,
--     status VARCHAR(50),
--     created_at DATE
-- );

-- INSERT INTO invoices (vendor, amount, status, created_at) VALUES
-- ('Vendor A', 1000, 'paid', '2025-07-05'),
-- ('Vendor B', 1500, 'unpaid', '2025-07-01'),
-- ('Vendor A', 2000, 'paid', '2025-06-20'),
-- ('Vendor C', 800,  'paid', '2025-07-08'),
-- ('Vendor B', 1200, 'paid', '2025-06-15'),
-- ('Vendor D', 3000, 'paid', '2025-07-09'),
-- ('Vendor E', 500,  'paid', '2025-07-10');

SELECT vendor, SUM(amount) AS total_paid
FROM invoices
WHERE status = 'paid'
  AND created_at >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY vendor
ORDER BY total_paid DESC
LIMIT 5;

-- Output:

-- vendor	    total_paid
-- Vendor A	    3000
-- Vendor D	    3000
-- Vendor B	    1200
-- Vendor C	    800
-- Vendor E	    500
