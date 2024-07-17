# tests/test_sql_logic.py
import sys
import os
# Add the parent directory to sys.path to locate validation_rules.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import json
from validation_rules import validate_entry, common_rules

@pytest.fixture(scope='module')
def expected_results():
    return load_expected_results()

def fetch_results_as_dict(results):
    return [dict(row) for row in results]

def load_expected_results():
    json_path = os.path.join(os.path.dirname(__file__), '..', 'expected_results.json')
    with open(json_path) as f:
        return json.load(f)

def load_sql_query(file_name):
    sql_path = os.path.join(os.path.dirname(__file__), '..', 'sql_queries', file_name)
    with open(sql_path, 'r') as file:
        return file.read()

def run_query_test(db_connection, expected_results, query_name, sql_file):
    """
    Helper function to run a SQL query and validate its results.
    It encapsulates the common logic for running a SQL query, fetching results, 
    filtering valid results, and comparing them with expected results. 
    This function is called by the individual test functions to perform the shared logic.
    """
    query_sql = load_sql_query(sql_file)
    results = db_connection.execute(query_sql)
    results_dict = fetch_results_as_dict(results)

    # Filter valid results
    filtered_results = [result for result in results_dict if validate_entry(result, common_rules)]

    # Compare with expected results
    expected = expected_results[query_name]["expected"]
    assert filtered_results == expected, f"Error in {query_name}: {filtered_results} != {expected}"

def test_active_sites_positive(db_connection, expected_results):
    run_query_test(db_connection, expected_results, "active_sites_positive", "active_sites_positive.sql")

def test_randomized_patients_positive(db_connection, expected_results):
    run_query_test(db_connection, expected_results, "randomized_patients_positive", "randomized_patients_positive.sql")



# @pytest.mark.parametrize("query_name, sql_file", [
#     ("active_sites_positive", "active_sites_positive.sql"),
#     ("randomized_patients_positive", "randomized_patients_positive.sql"),
# ])
# def test_sql_queries(db_connection, expected_results, query_name, sql_file):
#     query_sql = load_sql_query(sql_file)
#     results = db_connection.execute(query_sql)
#     results_dict = fetch_results_as_dict(results)

#     # Filter valid results
#     filtered_results = [result for result in results_dict if validate_entry(result, common_rules)]

#     # Compare with expected results
#     expected = expected_results[query_name]["expected"]
#     assert filtered_results == expected, f"Error in {query_name}: {filtered_results} != {expected}"




# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# import pytest
# import json
# from validation_rules import validate_entry, common_rules

# def fetch_results_as_dict(results):
#     return [dict(row) for row in results]

# def load_expected_results():
#     json_path = os.path.join(os.path.dirname(__file__), '..', 'expected_results.json')
#     with open(json_path) as f:
#         return json.load(f)

# expected_results = load_expected_results()

# def load_sql_query(file_name):
#     sql_path = os.path.join(os.path.dirname(__file__), '..', 'sql_queries', file_name)
#     with open(sql_path, 'r') as file:
#         return file.read()

# def test_active_sites_positive(db_connection):
#     query_name = "active_sites_positive"
#     query_sql = load_sql_query("active_sites_positive.sql")
#     results = db_connection.execute(query_sql)
#     results_dict = fetch_results_as_dict(results)

#     # Filtrar resultados válidos
#     filtered_results = [result for result in results_dict if validate_entry(result, common_rules)]

#     # Comparar con resultados esperados
#     expected = expected_results[query_name]["expected"]
#     assert filtered_results == expected, f"Error in {query_name}: {filtered_results} != {expected}"

# def test_randomized_patients_positive(db_connection):
#     query_name = "randomized_patients_positive"
#     query_sql = load_sql_query("randomized_patients_positive.sql")
#     results = db_connection.execute(query_sql)
#     results_dict = fetch_results_as_dict(results)

#     # Filtrar resultados válidos
#     filtered_results = [result for result in results_dict if validate_entry(result, common_rules)]

#     # Comparar con resultados esperados
#     expected = expected_results[query_name]["expected"]
#     assert filtered_results == expected, f"Error in {query_name}: {filtered_results} != {expected}"


