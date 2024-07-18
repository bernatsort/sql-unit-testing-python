import sys
import os
import pytest
import json
import yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from validation_rules_yaml import validate_entry, load_validation_rules

@pytest.fixture(scope='module')
def expected_results():
    return load_expected_results()


@pytest.fixture(scope='module')
def validation_rules():
    return load_validation_rules()

def fetch_results_as_dict(results):
    return [dict(row) for row in results]

def load_expected_results():
    json_path = os.path.join(os.path.dirname(__file__), '..', 'expected_results/expected_results.json')
    with open(json_path) as f:
        return json.load(f)

def load_sql_query(file_name):
    sql_path = os.path.join(os.path.dirname(__file__), '..', 'sql_queries', file_name)
    with open(sql_path, 'r') as file:
        return file.read()

# Positive Testing
def run_query_test(db_connection, expected_results, validation_rules, query_name, sql_file):
    query_sql = load_sql_query(sql_file)
    results = db_connection.execute(query_sql)
    results_dict = fetch_results_as_dict(results)

    # Obtener las reglas específicas de la consulta
    query_rules = validation_rules["queries"].get(query_name, {}).get("rules", {})
    
    # Combinar las reglas comunes con las reglas específicas de la consulta
    combined_rules = {**validation_rules["common_rules"], **query_rules}
    
    # Filtrar resultados válidos
    filtered_results = [result for result in results_dict if validate_entry(result, combined_rules)]
    
    # Convert lists to sets for comparison:
    """
    En lugar de hacer: 
    # Comparar con los resultados esperados: expected = expected_results[query_name]["expected"]
    Mejor hacer: 
    Ignorar el orden de las filas y se enfoque en el contenido de los datos.
    Convertir Diccionarios en Tuplas Ordenadas: tuple(sorted(d.items())) convierte cada diccionario 
    en una lista de pares clave-valor ordenados, luego en una tupla. Esto asegura que 
    cada diccionario tenga una representación única e independiente del orden de los campos.
    Crear Conjuntos: set(...) convierte las listas de tuplas en conjuntos. 
    Esto permite que la comparación ignore el orden de las filas.
    Comparación de Conjuntos: La comparación de los conjuntos filtered y expected asegura que ambos 
    contienen exactamente los mismos elementos, independientemente del orden en que aparecen.
    """
    expected = set(tuple(sorted(d.items())) for d in expected_results[query_name]["expected"])
    filtered = set(tuple(sorted(d.items())) for d in filtered_results)

    assert filtered == expected, f"Error in {query_name}: {filtered} != {expected}"

def test_active_sites_positive(db_connection, expected_results, validation_rules):
    run_query_test(db_connection, expected_results, validation_rules, "active_sites_positive", "active_sites_positive.sql")

def test_randomized_patients_positive(db_connection, expected_results, validation_rules):
    run_query_test(db_connection, expected_results, validation_rules, "randomized_patients_positive", "randomized_patients_positive.sql")

def test_active_patients_date(db_connection, expected_results, validation_rules):
    run_query_test(db_connection, expected_results, validation_rules, "active_patients_date", "active_patients_date.sql")

