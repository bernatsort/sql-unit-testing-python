# tests/test_queries.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import json
from sql_queries.sql_queries import query1, query2
from validation import validate_entry, common_rules

def fetch_results_as_dict(results):
    return [dict(row) for row in results]

def load_expected_results():
    json_path = os.path.join(os.path.dirname(__file__), '..', 'expected_results.json')
    with open(json_path) as f:
        return json.load(f)

expected_results = load_expected_results()

def test_query1(db_connection):
    query_name = "query1"
    query_sql = query1()
    results = db_connection.execute(query_sql)
    results_dict = fetch_results_as_dict(results)

    # Filtrar resultados válidos
    filtered_results = [result for result in results_dict if validate_entry(result, common_rules)]

    # Comparar con resultados esperados
    expected = expected_results[query_name]["expected"]
    assert filtered_results == expected, f"Error in {query_name}: {filtered_results} != {expected}"

def test_query2(db_connection):
    query_name = "query2"
    query_sql = query2()
    results = db_connection.execute(query_sql)
    results_dict = fetch_results_as_dict(results)

    # Filtrar resultados válidos
    filtered_results = [result for result in results_dict if validate_entry(result, common_rules)]

    # Comparar con resultados esperados
    expected = expected_results[query_name]["expected"]
    assert filtered_results == expected, f"Error in {query_name}: {filtered_results} != {expected}"
