- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest



# SQL 
## Запрос первый
SELECT COUNT(or.inDelivery), co.login
FROM "Couriers" AS co
INNER JOIN "Orders" AS or ON co.id=or.courierId
WHERE or.inDelivery='true'
GROUP BY or.inDelivery;


## Запрос второй
SELECT track, inDelivery, finished, cancelled
       CASE
           WHEN finished='true' THEN 2
           WHEN cancelled='true' THEN -1
           WHEN inDelivery='true' THEN 1
           ELSE 0
       END
FROM "Orders"
GROUP BY track;
