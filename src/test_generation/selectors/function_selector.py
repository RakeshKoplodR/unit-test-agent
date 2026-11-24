class FunctionSelector:
    EXCLUDE_FUNCTIONS = {
        "__init__",
        "__str__",
        "__repr__",
        "__eq__"
    }

    def select_functions(self, inventory):
        selected = []
        for function in inventory.functions:
            if(function.name in self.EXCLUDE_FUNCTIONS):
                continue
            if function.name.startswith("_"):
                continue
            selected.append(function)
        return selected