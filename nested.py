def get_value_from_nested_object(nested_object, key):
    keys = key.split('/')
    value = nested_object
    for k in keys:
        if isinstance(value, dict) and k in value:
            value = value[k]
        else:
            return None
    return value


# Example 1
object_1 = {"a": {"b": {"c": "d"}}}
key_1 = "a/b/c"
result_1 = get_value_from_nested_object(object_1, key_1)
print(result_1)  # Output: d

# Example 2
object_2 = {"x": {"y": {"z": "a"}}}
key_2 = "x/y/z"
result_2 = get_value_from_nested_object(object_2, key_2)
print(result_2)  # Output: a
