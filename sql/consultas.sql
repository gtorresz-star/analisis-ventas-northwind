-- Top 10 productos por ingresos
SELECT
    p.ProductID,
    SUM(od.Quantity * p.Price) AS ingresos
FROM OrderDetails od
INNER JOIN Products p
    ON od.ProductID = p.ProductID
GROUP BY p.ProductID
ORDER BY ingresos DESC
LIMIT 10;
