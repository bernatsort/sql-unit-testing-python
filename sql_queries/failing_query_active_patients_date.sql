SELECT week, active_patients
FROM clinical_trials
WHERE week = "2017-XX" AND study = "1368-0004" 
-- error introduced week = "2017-XX" should be week = "2017-34"