SELECT DATETIME AS 시간
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1;

-- 문제 의도대로 푼 코드
SELECT MIN(DATETIME) AS 시간
FROM ANIMAL_INS;
