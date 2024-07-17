# Validation functions: 
import logging

# Configuración básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

def is_valid_entry_query1(entry):
    return True  # No validation needed for query1 fields

def is_valid_entry_query2(entry):
    if "randomized_patients" not in entry or entry["randomized_patients"] < 0:
        logger.info(f"Invalid entry: {entry} - Reason: randomized_patients < 0 or missing")
        print(f"Invalid entry: {entry} - Reason: randomized_patients < 0 or missing")
        return False
    if "trial_status" not in entry or entry["trial_status"] not in ["recruitment", "ongoing", "completed"]:
        logger.info(f"Invalid entry: {entry} - Reason: trial_status not in ['recruitment', 'ongoing', 'completed'] or missing")
        print(f"Invalid entry: {entry} - Reason: trial_status not in ['recruitment', 'ongoing', 'completed'] or missing")
        return False
    logger.info(f"Valid entry: {entry}")
    print(f"Valid entry: {entry}")
    return True



# import logging

# # Configuración básica de logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# logger = logging.getLogger(__name__)

# def is_valid_entry(entry):
#     if entry["randomized_patients"] < 0:
#         logger.info(f"Invalid entry: {entry} - Reason: randomized_patients < 0")
#         return False
#     if entry["trial_status"] not in ["recruitment", "ongoing", "completed"]:
#         logger.info(f"Invalid entry: {entry} - Reason: trial_status not in ['recruitment', 'ongoing', 'completed']")
#         return False
#     return True

# def is_valid_entry(entry):
#     if entry["randomized_patients"] < 0:
#         return False
#     if entry["trial_status"] not in ["recruitment", "ongoing", "completed"]:
#         return False
#     return True
