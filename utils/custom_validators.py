def is_int(x):
    try:
        return int(x)
    except ValueError:
        return False

def yes_or_no_validator(x):
    if x in ('y', 'n'):
        return True
    return False
    