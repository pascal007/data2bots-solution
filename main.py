import json, os


class SchemaGenerator:
    
    def __init__(self) -> None:
        """specify paths for files"""
        self.read_path = os.getcwd() + '/data/'
        self.write_path = os.getcwd() + '/schema/'
        self.files = os.listdir(self.read_path)

    def generate_schema(self):
        """read files and generate schema"""
        for count, file in enumerate(self.files, start=1):
            f = open(self.read_path + file)    
            data = json.load(f)
            if data.get('message') is None:
                raise Exception("json has no message key")
            schema_output = {
                key: {"type": "", "tag": "", "description": "", "required": False} for key in data.get('message')
            }
            
            for key in schema_output:
                schema_output[key]['type'] = self.__validate_data_type(data['message'][key])
        
            with open(f"{self.write_path}/schema_{count}.json", "w") as convert_file:
                convert_file.write(json.dumps(schema_output, indent=4))
        
        f.close()
                    
    @staticmethod
    def __validate_data_type(value):
        """validates and returns data type of values"""
        match type(value).__name__:
            case str.__name__:
                return "string"
            case int.__name__:
                return "integer"
            case list.__name__:
                for item in value:
                    if isinstance(item, str):
                        return "enum"
                    elif isinstance(item, dict):
                        return "array"
                return "array"
            case dict.__name__:
                return "object"
            case bool.__name__:
                return "boolean"            
            case _:
                print(value)
                raise Exception("JSON data has unrecognized data format")
                           
schema_generator = SchemaGenerator()
schema_generator.generate_schema()

    
    
    
    

