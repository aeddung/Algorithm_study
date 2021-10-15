-- https://www.hackerrank.com/challenges/the-pads/problem

-- 조건 1
SELECT
CONCAT (
    Name,
    '(',
    SUBSTR(Occupation, 1, 1),
    ')'
    )
FROM Occupations
ORDER BY Name;

-- 조건 2
SELECT
CONCAT (
    'There are a total of ',
    COUNT(Occupation),
    ' ',
    LOWER(Occupation),
    's.'
    )
FROM Occupations
GROUP BY Occupation
ORDER BY COUNT(Occupation), Occupation;
