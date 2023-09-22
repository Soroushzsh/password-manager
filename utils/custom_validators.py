def is_int(x):
    try:
        return int(x)
    except ValueError:
        return False

def yes_or_no_validator(x):
    if x.lower() in ('y', 'n', 'no', 'yes', 'yup', 'nope'):
        return True
    return False
    