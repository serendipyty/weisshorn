import toml

__all__ = ['Parameter']

class Parameter():

    def __init__(self, input_file: str=None):
        
        self.input_file = input_file
        if input_file is not None:
            self.input_dict = toml.load(self.input_file)

    @property
    def desc(self):
        return "This is the parameter stuff"

