from typing import Union

# Refactored Python 3.9 compatible code for string to boolean conversion

def str2bool(value: Union[str, None], raise_exc: bool = False) -> Union[bool, None]:
    true_set = {'yes', 'true', 't', 'y', '1'}
    false_set = {'no', 'false', 'f', 'n', '0'}
    
    if isinstance(value, str):
        value = value.lower()
        if value in true_set:
            return True
        if value in false_set:
            return False
    
    if raise_exc:
        raise ValueError(f'Expected one of: {", ".join(true_set | false_set)}')
    
    return None

def str2bool_exc(value: Union[str, None]) -> bool:
    return str2bool(value, raise_exc=True)
