SELECT week, active_patients
FROM clinical_trials
WHERE week = "2017-31"

-- Como hacer para que el test podamos generalizarlo para que sea active_patients en una fecha concreta. 
-- De esta forma podemos pasarle distintas fechas y mirar si en todas el test passa. 