def test_db_connection(db_connection):
    assert db_connection is not None, "Failed to create a database connection"