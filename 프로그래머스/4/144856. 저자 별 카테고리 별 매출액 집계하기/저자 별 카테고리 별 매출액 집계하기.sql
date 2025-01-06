-- 코드를 입력하세요
SELECT
    A.AUTHOR_ID,          
    A.AUTHOR_NAME,        
    B.CATEGORY,           
    SUM(C.SALES * B.PRICE) AS TOTAL_SALES 
FROM
    AUTHOR A
JOIN
    BOOK B
    ON A.AUTHOR_ID = B.AUTHOR_ID 
JOIN
    BOOK_SALES C
    ON B.BOOK_ID = C.BOOK_ID 
WHERE
    C.SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31' 
GROUP BY
    A.AUTHOR_ID,          
    A.AUTHOR_NAME,        
    B.CATEGORY           
ORDER BY
    A.AUTHOR_ID,      
    B.CATEGORY DESC;      

    
        
     
