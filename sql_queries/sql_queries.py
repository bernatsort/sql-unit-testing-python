def query1():
    return "SELECT study, site, active_sites FROM clinical_trials WHERE active_sites > 0;"

def query2():
    return "SELECT study, site, randomized_patients, trial_status FROM clinical_trials WHERE randomized_patients >= 0;"
