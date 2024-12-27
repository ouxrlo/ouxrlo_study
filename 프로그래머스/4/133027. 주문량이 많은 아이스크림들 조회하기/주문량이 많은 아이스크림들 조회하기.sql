# Table1: FIRST_HALF = 상반기 주문 정보
# 기본키: FLAVOR

# Table2: JULY = 7월 아이스크림 주문 정보
# 기본키 SHIPMENT_ID
# 외래키 FLAVOR
# 서로 다른 두 공장에서 아이스크림 생산가능 = 같은 맛의 아이스크림이 다른 출하 번호
# FIRST_HALF(일) -- (다)JULY


SELECT FLAVOR
FROM FIRST_HALF F
JOIN JULY J USING (FLAVOR) # using = 두 테이블에 공통열 기반으로 join할때 사용
GROUP BY FLAVOR
ORDER BY SUM(F.TOTAL_ORDER + J.TOTAL_ORDER) DESC
LIMIT 3;