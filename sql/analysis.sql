-- Portfolio SQL analysis

-- 1. Volume and average duration by specialty
SELECT specialty,
       COUNT(*) AS surgeries,
       ROUND(AVG(duration_minutes), 1) AS avg_duration,
       ROUND(AVG(waiting_minutes), 1) AS avg_waiting
FROM surgeries
GROUP BY specialty
ORDER BY surgeries DESC;

-- 2. Monthly activity
SELECT DATE_TRUNC('month', scheduled_date) AS month,
       COUNT(*) AS surgeries,
       ROUND(AVG(duration_minutes), 1) AS avg_duration
FROM surgeries
GROUP BY 1
ORDER BY 1;

-- 3. Emergency share by hospital
SELECT hospital,
       COUNT(*) AS surgeries,
       ROUND(100.0 * AVG(CASE WHEN emergency THEN 1 ELSE 0 END), 2) AS emergency_pct
FROM surgeries
GROUP BY hospital
ORDER BY emergency_pct DESC;

-- 4. Rank specialties by average duration
SELECT specialty,
       ROUND(AVG(duration_minutes), 1) AS avg_duration,
       RANK() OVER (ORDER BY AVG(duration_minutes) DESC) AS duration_rank
FROM surgeries
GROUP BY specialty;
