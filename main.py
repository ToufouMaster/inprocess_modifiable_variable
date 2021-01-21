import re

# --Début De La Classe--

class CVariables:

    
    def __init__(self):
        self.___Variables___ = {}

    def add_CVariable(self, variable_name : str, variable_value : str):
        data = {}
        
        if variable_value.isdigit():
            data["value"] = int(variable_value)
            data["type"] = "int"
        else:
            is_float = re.compile('\d+(\.\d+)?')
            if variable_value == "None":
                data["value"] = None
                data["type"] = "NoneType"
            elif is_float.match(variable_value):
                data["value"] = float(variable_value)
                data["type"] = "float"
            elif variable_value == "True" or variable_value == "False":
                data["value"] = bool(variable_value)
                data["type"] = "bool"
            else:
                data["value"] = variable_value
                data["type"] = "str"
        
        self.___Variables___[variable_name] = data
    
    def get_CVariables(self):
        for v in self.___Variables___:
            variable = self.___Variables___[v]
            print(v+":")
            print("    value: "+str(variable["value"]))
            print("    type: "+variable["type"]+"\n")
        
# --Fin De La Classe--
        
cvariables = CVariables()

def input_cmd():
    command = input("> ")
    command = command.split(" ")
    for i in command:
        if i == "":
            command.remove(i)
    return command

def main():
    command = input_cmd()
    while command[0] != "exit":
        if command[0] == "new_variable":
            if len(command) >= 3:
                cvariables.add_CVariable(command[1], command[2])
            else:
                print("ERROR: This command need at least 2 arguments!")
        elif command[0] == "view_variables":
            if len(command) >= 2:
                print("not yet implemented")
            else:
                cvariables.get_CVariables()
        else:
            print("ERROR: No command found try something else or write 'help' for help!")
        command = input_cmd()

main()
input() # Waiting for user input
