
def capitalize(name):
    return name[:1].upper() + name[1:] if name else ''

def uncapitalize(tablename):
    return tablename[:1].lower() + tablename[1:] if tablename else ''

def lower_case(tablename):
    return tablename.lower()