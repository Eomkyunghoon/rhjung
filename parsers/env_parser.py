import os

class EnvParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.variables = {}

    def parse(self):
        try:
            with open(self.file_path, 'r') as env_file:
                for line in env_file:
                    # Skip comments and empty lines
                    if line.strip() and not line.startswith('#'):
                        key, value = line.strip().split('=', 1)
                        self.variables[key] = value
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found.")

    def get_variable(self, key):
        return self.variables.get(key, None)

    def __repr__(self):
        return str(self.variables)