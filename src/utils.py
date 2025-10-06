import pickle
import os

def save_object(file_path, obj):
	"""Save a Python object to a file using pickle."""
	os.makedirs(os.path.dirname(file_path), exist_ok=True)
	with open(file_path, 'wb') as file:
		pickle.dump(obj, file)
