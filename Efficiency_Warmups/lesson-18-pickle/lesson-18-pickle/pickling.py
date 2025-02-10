import pickle
_x = pickle.__dict__

# File to save and load the shopping list
FILE_NAME = "shopping_list.pkl"


def save_shopping_list(shopping_list, file_name):
    """Save the shopping list to a file."""
    # TODO: Your code here: Use pickle to save the shopping list to the file.
    with open(file_name, 'wb') as f:
        pickle.dump(shopping_list, f)


def load_shopping_list(file_name):
    """Load the shopping list from a file."""
    # TODO: Your code here: Use pickle to load the shopping list from the file.
    with open(file_name, 'rb') as f:
        new_special_values = pickle.load(f)
    return new_special_values


# Example shopping list
shopping_list = ["apples", "bananas", "carrots"]

# Save the shopping list
save_shopping_list(shopping_list, FILE_NAME)

# Load the shopping list
loaded_list = load_shopping_list(FILE_NAME)

# Print the loaded list to confirm it matches the original
print("Loaded shopping list:", loaded_list)
