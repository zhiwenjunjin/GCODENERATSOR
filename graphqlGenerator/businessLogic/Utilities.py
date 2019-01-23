
def capitalize(name):
    return name[:1].upper() + name[1:] if name else ''

def uncapitalize(tablename):
    return tablename[:1].lower() + tablename[1:] if tablename else ''

def lower_case(tablename):
    return tablename.lower()

def check_end_with_s(tbn):
    return tbn.endswith('s') or tbn.endswith('o')

def check_end_with_y(tbn):
    return tbn.endswith('y')

def check_sec_last_end_with_a(tbn):
    return tbn[:-1].endswith('a')