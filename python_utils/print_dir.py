def dir_print(object):
    """This method returns the list of attributes and methods except dunder methods"""
    return list(name for name in dir(object) if not name.startswith('__'))