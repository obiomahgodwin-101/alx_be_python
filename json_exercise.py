import json

def process_json(data: dict, filename: str) -> dict:
    """
    This function serializes a dictionary to a JSON file,
    then deserializes it back into a dictionary and returns it.
    """
    # Serialize (write) the dictionary to a JSON file
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data has been written to {filename}")

    # Deserialize (read) the JSON file back into a dictionary
    with open(filename, 'r') as json_file:
        loaded_data = json.load(json_file)
    print(f"Data has been read back from {filename}")

    return loaded_data


# Example test run (you can delete this before committing)
if __name__ == "__main__":
    sample_data = {
        "name": "Godwin Obiomah",
        "course": "ALX Backend Engineering",
        "score": 99.22
    }

    result = process_json(sample_data, "output.json")
    print("Deserialized Data:", result)
