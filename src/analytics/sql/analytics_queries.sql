
-- Total gasto por categoria por mês — GROUP BY básico
select sum(valor) as valor, item from raw_gastos
group by item;

-- Ranking de categorias mais caras — ORDER BY + agregação
select mes, item, sum(valor) as total
from raw_gastos
group by mes, item 
order by mes, total desc;

-- Receita vs Gasto por mês — JOIN entre as duas tabelas
SELECT r.mes, r.total_receitas, g.total_gastos
FROM (SELECT mes, SUM(valor) AS total_receitas 
FROM raw_receitas
GROUP BY mes) r
JOIN (SELECT mes, SUM(valor) AS total_gastos
FROM raw_gastos
GROUP BY mes) g
ON r.mes = g.mes
ORDER BY r.mes;

-- Percentual de cada categoria sobre o total

SELECT
    item,
    SUM(valor) AS total_categoria,
    ROUND(CAST(SUM(valor) * 100.0 / SUM(SUM(valor)) OVER () AS NUMERIC), 2) AS percentual
FROM raw_gastos
where mes = 'jan'
GROUP BY item
ORDER BY percentual DESC;