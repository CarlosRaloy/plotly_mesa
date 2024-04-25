select * from report r order by r.id desc;


-- Promedio de la respuesta de tickets
SELECT 
    TO_CHAR(
        INTERVAL '1 minute' * AVG(
            CASE 
                WHEN r.onhold_time ~ '\d+hrs \d+min' THEN
                    CAST(SPLIT_PART(r.onhold_time, 'hrs ', 1) AS INTEGER) * 60 +
                    CAST(SPLIT_PART(SPLIT_PART(r.onhold_time, 'hrs ', 2), 'min', 1) AS INTEGER)
                ELSE
                    0
            END
        ), 
        'HH24:MI'
    ) AS promedio_tiempo
FROM 
    report r
WHERE 
    r.onhold_time ~ '\d+hrs \d+min';
   
   
--- Promedio de cada tecnico
SELECT 
    r.technician_name,
    TO_CHAR(
        INTERVAL '1 minute' * AVG(
            CASE 
                WHEN r.onhold_time ~ '\d+hrs \d+min' THEN
                    CAST(SPLIT_PART(r.onhold_time, 'hrs ', 1) AS INTEGER) * 60 +
                    CAST(SPLIT_PART(SPLIT_PART(r.onhold_time, 'hrs ', 2), 'min', 1) AS INTEGER)
                ELSE
                    0
            END
        ), 
        'HH24:MI'
    ) AS promedio_tiempo
FROM 
    report r
WHERE 
    r.onhold_time ~ '\d+hrs \d+min'
GROUP BY 
    r.technician_name;

 
  --- Tempo maximo y tiempo minimo
   SELECT 
    r.technician_name,
    TO_CHAR(
        INTERVAL '1 minute' * MIN(
            CASE 
                WHEN r.onhold_time ~ '\d+hrs \d+min' THEN
                    CAST(SPLIT_PART(r.onhold_time, 'hrs ', 1) AS INTEGER) * 60 +
                    CAST(SPLIT_PART(SPLIT_PART(r.onhold_time, 'hrs ', 2), 'min', 1) AS INTEGER)
                ELSE
                    0
            END
        ), 
        'HH24:MI'
    ) AS tiempo_minimo,
    TO_CHAR(
        INTERVAL '1 minute' * MAX(
            CASE 
                WHEN r.onhold_time ~ '\d+hrs \d+min' THEN
                    CAST(SPLIT_PART(r.onhold_time, 'hrs ', 1) AS INTEGER) * 60 +
                    CAST(SPLIT_PART(SPLIT_PART(r.onhold_time, 'hrs ', 2), 'min', 1) AS INTEGER)
                ELSE
                    0
            END
        ), 
        'HH24:MI'
    ) AS tiempo_maximo
FROM 
    report r
WHERE 
    r.onhold_time ~ '\d+hrs \d+min'
GROUP BY 
    r.technician_name;
   
  
  
--- Promedio de respuesta por tecnico por dias , horas   
SELECT 
    technician_name,
    CONCAT(
        TO_CHAR(AVG(total_seconds) / (24 * 3600), 'FM999999990D'), ' días ',
        TO_CHAR((AVG(total_seconds) % (24 * 3600)) / 3600, 'FM09'), ' horas ',
        TO_CHAR((AVG(total_seconds) % 3600) / 60, 'FM09'), ' minutos ',
        TO_CHAR(AVG(total_seconds) % 60, 'FM09.99'), ' segundos'
    ) AS tiempo_promedio ,  count(*) as totaL_tickets
FROM (
    SELECT 
        technician_name,
        CASE 
            WHEN onhold_time ~ '\d+hrs \d+min' THEN
                CAST(SPLIT_PART(onhold_time, 'hrs ', 1) AS INTEGER) * 3600 +
                CAST(SPLIT_PART(SPLIT_PART(onhold_time, 'hrs ', 2), 'min', 1) AS INTEGER) * 60
            ELSE
                0
        END AS total_seconds
    FROM 
        report
    WHERE 
        onhold_time ~ '\d+hrs \d+min'
) AS subquery
GROUP BY 
    technician_name
ORDER BY 
    AVG(total_seconds) DESC;


   
 
SELECT 
    technician_name,
    ROUND(
        LEAST(
            100,
            GREATEST(
                0,
                1 - (AVG(total_days) / 31)
            ) * 100
        ),
        2
    ) AS eficiencia
FROM (
    SELECT 
        technician_name,
        AVG(total_days) AS total_days
    FROM (
        SELECT 
            technician_name,
            CASE 
                WHEN onhold_time ~ '\d+hrs \d+min' THEN
                    CAST(SPLIT_PART(onhold_time, 'hrs ', 1) AS INTEGER) / 24 +
                    CAST(SPLIT_PART(SPLIT_PART(onhold_time, 'hrs ', 2), 'min', 1) AS INTEGER) / (24 * 60)
                ELSE
                    0
            END AS total_days
        FROM 
            report
        WHERE 
            onhold_time ~ '\d+hrs \d+min'
    ) AS subquery
    GROUP BY 
        technician_name
) AS subquery2
GROUP BY 
    technician_name
ORDER BY 
    eficiencia DESC;



select r.technician_name, 
r.resolved_time 
from report r;


select r.technician_name ,count(*) from report r 
group by r.technician_name 
order by count(r.technician_name) desc;



select r.requester_name  ,count(*) from report r 
group by r.requester_name 
order by count(r.requester_name) desc;