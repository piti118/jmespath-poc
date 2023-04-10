import json
import jmespath


class CustomFunctions(jmespath.functions.Functions):
    @jmespath.functions.signature({'types': ['object']}, {'types': ['array']})
    def _func_map_merge(self, obj, arg):
        result = []
        for element in arg:
            merged_object = super()._func_merge(obj, element)
            result.append(merged_object)
        return result


options = jmespath.Options(custom_functions=CustomFunctions())


def search(expression: str, data: object):
    return jmespath.search(expression, data, options=options)
