import pytest
import pandas as pd
from sqlalchemy import create_engine
import os

@pytest.fixture(scope='module')
def db_engine():
    # Create in-memory SQLite database for testing
    engine = create_engine('sqlite:///:memory:')
    # Use absolute path for the Excel file
    file_path = os.path.abspath('validated_reference_dataset.xlsx')
    df = pd.read_excel(file_path)
    df.to_sql('clinical_trials', engine, index=False, if_exists='replace')
    yield engine
    engine.dispose()

@pytest.mark.parametrize("query,valid_column", [
    ("SELECT * FROM clinical_trials WHERE trial_status = 'recruitment'", 'is_valid_recruitment'),
    ("SELECT * FROM clinical_trials WHERE randomized_patients > 40", 'is_valid_randomized_above_40'),
    ("SELECT * FROM clinical_trials WHERE active_patients > 45", 'is_valid_active_patients_above_45')
])
def test_queries(db_engine, query, valid_column):
    file_path = os.path.abspath('validated_reference_dataset.xlsx')
    df = pd.read_excel(file_path)
    result = pd.read_sql(query, db_engine)
    
    # Filter and drop the validation columns from the expected DataFrame
    expected = df[df[valid_column]].drop(columns=[
        'expected_recruitment', 'is_valid_recruitment',
        'expected_randomized_above_40', 'is_valid_randomized_above_40',
        'expected_active_patients_above_45', 'is_valid_active_patients_above_45'
    ])
    
    # Select only the columns in the expected DataFrame
    result = result[expected.columns]
    
    # Reset index for both DataFrames before comparison
    result = result.reset_index(drop=True)
    expected = expected.reset_index(drop=True)
    
    pd.testing.assert_frame_equal(result, expected)
