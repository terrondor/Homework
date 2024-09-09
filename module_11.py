import inspect

def introspection_info(obj):
    obj_type = type(obj).__name__
    
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    
    module = obj.__mod__
    
    base_classes = []
    if isinstance(obj, type):
        base_classes = [base.__name__ for base in obj.__bases__]
    
    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
        'base_classes': base_classes
    }

number_info = introspection_info(42)
print(number_info)