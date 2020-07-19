import re

def alphanumeric(input):
    return re.sub(r'[\W_]+', '-', input)
