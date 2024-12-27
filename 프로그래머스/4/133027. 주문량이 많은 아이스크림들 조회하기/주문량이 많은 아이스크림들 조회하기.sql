# Table1: FIRST_HALF = 상반기 주문 정보
# 기본키: FLAVOR

# Table2: JULY = 7월 아이스크림 주문 정보
# 기본키 SHIPMENT_ID
# 외래키 FLAVOR
# 서로 다른 두 공장에서 아이스크림 생산가능 = 같은 맛의 아이스크림이 다른 출하 번호
# FIRST_HALF(일) -- (다)JULY

SELECT F.FLAVOR
FROM FIRST_HALF F
    INNER JOIN (SELECT FLAVOR, sum(TOTAL_ORDER) AS JULY_TOTAL_ORDER
                FROM JULY
                GROUP BY FLAVOR) J
        ON F.FLAVOR = J.FLAVOR
ORDER BY TOTAL_ORDER + JULY_TOTAL_ORDER DESC
LIMIT 3;