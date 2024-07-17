# Validation functions: 

import logging

# Basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

def validate_entry(entry, rules):
    """
    General validation function that validates an entry based on provided rules.

    Parameters:
    - entry (dict): The entry to validate.
    - rules (dict): The validation rules. Keys are field names and values are validation functions.

    Returns:
    - bool: True if the entry is valid, False otherwise.
    """
    for field, validation_fn in rules.items():
        if field in entry and not validation_fn(entry[field]):
            logger.info(f"Invalid entry: {entry} - Reason: {field} failed validation")
            print(f"Invalid entry: {entry} - Reason: {field} failed validation")
            return False
    logger.info(f"Valid entry: {entry}")
    print(f"Valid entry: {entry}")
    return True

# Common validation rules for all queries
def is_positive(value):
    return value >= 0

def is_valid_trial_status(value):
    return value in ["recruitment", "ongoing", "completed"]

# Common validation rules
common_rules = {
    "randomized_patients": is_positive,
    "trial_status": is_valid_trial_status
}

# Specific validation rules for different queries (if needed)
# Include them in the testing script (test_sql_logic.py): from validation import validate_entry, common_rules, query1_rules, query2_rules
active_sites_positive_rules = {}  
randomized_patients_positive_rules = {}  

