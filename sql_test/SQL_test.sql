CREATE OR REPLACE VIEW interview.invoices_view AS
SELECT
    i.date,
    i.id,
    SUM(CASE WHEN ii.description = 'carnes' THEN ii.amount ELSE 0 END) AS carnes,
    SUM(CASE WHEN ii.description = 'cereales' THEN ii.amount ELSE 0 END) AS cereales,
    SUM(CASE WHEN ii.description NOT IN ('carnes', 'cereales') THEN ii.amount ELSE 0 END) AS others,
    SUM(ii.amount) AS total_amount
FROM
    interview.invoices_items AS ii
LEFT JOIN
    interview.invoices AS i ON ii.auto_transfer = i.id
GROUP BY
    i.date, i.id;