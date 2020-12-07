def check_email(string):
    if " " in string:
        return False
    if "@" not in string:
        return False
    if "." not in string:
        return False
    if "@." in string:
        return False
    if ".@" in string:
        return False
    if string.rfind(".") > string.find("@") + 1:
        return True
    return False
