"""
Core logic for the JSON Flattener.
Separated from the Streamlit app for testing and reusability.
"""

def json_flattener(data, parent_key="", sep="."):
    """
    Recursively flattens a nested JSON-like structure (dict or list) 
    into a single-level dictionary.

    Args:
        data: The dict or list to flatten.
        parent_key (str): The base key to prepend to flattened keys.
        sep (str): The separator to use between nested keys.

    Returns:
        dict: A flattened dictionary.
    """
    items = {}

    if isinstance(data, dict):
        # If it's a dictionary, iterate over its items
        if not data:
            # If the dict is empty, we still might need to record it
            # if it has a parent key. But typically, we just return empty.
             pass
        for key, value in data.items():
            # Create the new key
            full_key = f"{parent_key}{sep}{key}" if parent_key else key
            # Recurse with the new key and value
            items.update(json_flattener(value, full_key, sep=sep))

    elif isinstance(data, list):
        # If it's a list, iterate over its items with an index
        if not data:
            # If the list is empty, same as empty dict
            pass
        for idx, item in enumerate(data):
            # Create the new key using the index
            full_key = f"{parent_key}{sep}{idx}" if parent_key else str(idx)
            # Recurse with the new key and item
            items.update(json_flattener(item, full_key, sep=sep))

    else:
        # Base case: data is a primitive (str, int, bool, None, etc.)
        # Assign it to the current parent_key
        # We must check if parent_key exists, otherwise a top-level
        # primitive (e.g., just "123") would be `{"": 123}` which is valid.
        items[parent_key] = data

    return items