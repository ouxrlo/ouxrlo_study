-- 코드를 입력하세요
SELECT 
    P.PRODUCT_ID, 
    P.PRODUCT_NAME,
    SUM(O.AMOUNT* P.PRICE) AS TOTAL_PRICE
FROM
    FOOD_PRODUCT P
JOIN
    FOOD_ORDER O
ON
    P.PRODUCT_ID = O.PRODUCT_ID
WHERE 
    DATE_FORMAT(O.PRODUCE_DATE, '%Y-%m') = '2022-05'
GROUP BY
    P.PRODUCT_ID, P.PRODUCT_NAME
ORDER BY
    TOTAL_PRICE DESC, P.PRODUCT_ID ;
    
    