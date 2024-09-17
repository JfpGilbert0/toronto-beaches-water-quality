import pandas as pd
import pytest

# Sample test dataset creation
@pytest.fixture
def sample_data():
    data = {
        'beachid': [1, 2, 3],
        'beachname': ['Beach A', 'Beach B', 'Beach C'],
        'sitename': ['Site 1', 'Site 2', 'Site 3'],
        'collectiondate': ['2023-09-10', '2023-09-11', '2023-09-12'],
        'ecoli': [10.5, 20.3, -1.0],  # one invalid value
        'comments': ['Clean', 'Moderate', None],
        'loc_type': ['Beach', 'Lake', 'River'],
        'longitude': [-79.3832, -79.2, 200.0],  # one invalid value
        'latitude': [43.6532, 43.7, 90.0]  # one edge case
    }
    df = pd.DataFrame(data)
    df['collectiondate'] = pd.to_datetime(df['collectiondate'])  # Convert to datetime
    return df

# Test for correct data types
def test_data_types(sample_data):
    assert sample_data['beachid'].dtype == 'int64'
    assert sample_data['beachname'].dtype == 'object'
    assert sample_data['sitename'].dtype == 'object'
    assert sample_data['collectiondate'].dtype == 'datetime64[ns]'
    assert sample_data['ecoli'].dtype == 'float64'
    assert sample_data['comments'].dtype == 'object'
    assert sample_data['loc_type'].dtype == 'object'
    assert sample_data['longitude'].dtype == 'float64'
    assert sample_data['latitude'].dtype == 'float64'

# Test that ecoli levels are non-negative
def test_ecoli_non_negative(sample_data):
    assert (sample_data['ecoli'] >= 0).all(), "E. coli values should be non-negative."

# Test for valid longitude and latitude ranges
def test_longitude_latitude_ranges(sample_data):
    assert sample_data['longitude'].between(-180, 180).all(), "Longitude should be between -180 and 180."
    assert sample_data['latitude'].between(-90, 90).all(), "Latitude should be between -90 and 90."

# Test for non-null fields
def test_non_null_values(sample_data):
    assert sample_data['beachid'].notna().all(), "beachid should not contain null values."
    assert sample_data['beachname'].notna().all(), "beachname should not contain null values."
    assert sample_data['sitename'].notna().all(), "sitename should not contain null values."
    assert sample_data['collectiondate'].notna().all(), "collectiondate should not contain null values."
    assert sample_data['longitude'].notna().all(), "longitude should not contain null values."
    assert sample_data['latitude'].notna().all(), "latitude should not contain null values."

# Test for valid data logic (custom logic as needed)
def test_data_logic(sample_data):
    # Ensure loc_type only contains known valid types
    valid_loc_types = ['Beach', 'Lake', 'River', 'Ocean']
    assert sample_data['loc_type'].isin(valid_loc_types).all(), "Invalid loc_type found."

