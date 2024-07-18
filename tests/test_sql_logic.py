# tests/test_sql_logic.py
import sys
import os
import pytest
import json
from sqlalchemy import text

@pytest.fixture(scope='module')
def expected_results():
    return load_expected_results()

def fetch_results_as_dict(results):
    return [dict(row._mapping) for row in results] # convert results to dictionaries. Use _mapping to avoid deprecation warnings. 

def load_expected_results():
    json_path = os.path.join(os.path.dirname(__file__), '..', 'expected_results/expected_results.json')
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
    results = db_connection.execute(text(query_sql))
    results_dict = fetch_results_as_dict(results)

    # Compare with expected results
    expected = expected_results[query_name]["expected"]
    assert results_dict == expected, f"Error in {query_name}: {results_dict} != {expected}"

# Tests
def test_active_sites_positive(db_connection, expected_results):
    run_query_test(db_connection, expected_results, "active_sites_positive", "active_sites_positive.sql")

def test_randomized_patients_positive(db_connection, expected_results):
    run_query_test(db_connection, expected_results, "randomized_patients_positive", "randomized_patients_positive.sql")

def test_active_patients_date(db_connection, expected_results):
    run_query_test(db_connection, expected_results, "active_patients_date", "active_patients_date.sql")

# Test that will fail
def test_failing_active_patients_date(db_connection, expected_results):
    run_query_test(db_connection, expected_results, "active_patients_study_1368_0004", "failing_query_active_patients_date.sql")





