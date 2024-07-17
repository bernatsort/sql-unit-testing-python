import os
import yaml
import logging
"""
Contiene las reglas de validación organizadas 
en dos secciones principales: common_rules y queries. 
Las common_rules son reglas que se aplican a todos los conjuntos de datos, 
mientras que las reglas específicas de queries se aplican solo a las consultas individuales.
"""

# Configuración básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

def load_validation_rules():
    yaml_path = os.path.join(os.path.dirname(__file__), 'rules_config.yaml')
    with open(yaml_path) as f:
        return yaml.safe_load(f)

def validate_entry(entry, rules):
    for field, rule in rules.items():
        if field in entry:
            value = entry[field]
            if "type" in rule:
                if rule["type"] == "integer":
                    if not isinstance(value, int):
                        logger.info(f"Invalid entry: {entry} - Reason: {field} is not an integer")
                        return False
                    if "min" in rule and value < rule["min"]:
                        logger.info(f"Invalid entry: {entry} - Reason: {field} is less than {rule['min']}")
                        return False
                elif rule["type"] == "string":
                    if not isinstance(value, str):
                        logger.info(f"Invalid entry: {entry} - Reason: {field} is not a string")
                        return False
                    if "allowed" in rule and value not in rule["allowed"]:
                        logger.info(f"Invalid entry: {entry} - Reason: {field} is not in allowed values {rule['allowed']}")
                        return False
    logger.info(f"Valid entry: {entry}")
    return True
