
-- List of unique "mother's job" for male students younger than 20 years old.
SELECT DISTINCT Mjob
FROM student
WHERE sex = 'M' AND age < 20;

-- Most frequent "travel time" among students that live in rural areas
SELECT traveltime, COUNT(traveltime) AS freq
FROM student
WHERE address = 'R'
GROUP BY traveltime
ORDER BY freq DESC
LIMIT 1;

-- Top 3 "father's job" for students grouped by parent's cohabitation status.
WITH RankedJobs AS (
    SELECT Pstatus
        , Fjob
        , COUNT(*) AS cnt_fjob
        , DENSE_RANK() OVER (PARTITION BY Pstatus ORDER BY COUNT(Fjob) DESC) AS rank
    FROM student
    WHERE Pstatus IS NOT NULL AND Fjob IS NOT NULL
    GROUP BY Pstatus, Fjob
)
SELECT Pstatus, Fjob, cnt_fjob
FROM RankedJobs
WHERE rank <= 3;


-- Most frequent "class failures" label grouped by family sizes.
SELECT famsize
    , failures
    , COUNT(failures) AS freq
FROM student
GROUP BY famsize, failures
ORDER BY famsize, freq DESC;

-- Median "absences" for average and low family relationship qualities, group by sex.
SELECT sex
    , famrel
	, AVG(absences) AS freq
-- 	, PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER BY absences) AS median_absences
FROM student
WHERE famrel <= 3
GROUP BY sex, famrel;

