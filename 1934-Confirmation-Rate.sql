SELECT     Signups.user_id, ROUND(AVG(IF(Confirmations.action = "confirmed", 1, 0)), 2) AS confirmation_rate
FROM       Signups
LEFT JOIN  Confirmations
ON         Signups.user_id = Confirmations.user_id
GROUP BY   user_id;