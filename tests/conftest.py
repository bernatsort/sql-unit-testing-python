import pytest
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
import os

@pytest.fixture(scope='module')
def db_connection():
    engine = create_engine('sqlite:///:memory:')
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'validated_reference_dataset.xlsx')
    df = pd.read_excel(file_path, sheet_name="trials")
    df.to_sql('clinical_trials', engine, if_exists='replace', index=False)

    connection = engine.connect()
    yield connection
    connection.close()

@pytest.fixture(scope='module')
def db_connection_negative():
    engine = create_engine('sqlite:///:memory:')
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'validated_reference_dataset_errors.xlsx')
    df = pd.read_excel(file_path)
    df.to_sql('clinical_trials', engine, if_exists='replace', index=False)

    connection = engine.connect()
    yield connection
    connection.close()

