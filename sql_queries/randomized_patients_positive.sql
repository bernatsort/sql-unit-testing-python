SELECT study, site, randomized_patients, trial_status 
FROM clinical_trials 
WHERE randomized_patients >= 0;