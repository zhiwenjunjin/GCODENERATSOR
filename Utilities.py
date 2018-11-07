
def uncapitalize(tablename):
    return tablename[:1].lower() + tablename[1:] if tablename else ''