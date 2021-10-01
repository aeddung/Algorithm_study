-- 문제 보기(https://moondol-ai.tistory.com/282?category=921465)

-- 본인이 작성한 쿼리문
SELECT A.NAME FROM(
SELECT * FROM ANIMAL_INS
ORDER BY DATETIME
) AS A
LIMIT 1;

-- 참고 쿼리문
SELECT NAME FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;
