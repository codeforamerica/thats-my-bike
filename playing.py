# Get data from HTML form.
# ========================

import cgi

form = cgi.FieldStorage()
owner_name = form["owner_name"].value

# File must be named the case number plus a unique identifier to allow multiple
# reports for the same case number to reside in the same upload directory 
# without overwriting each other. e.g. 0611-1234.1.txt
filename = owner_name + ".txt"

print filename

try:
    # Create text file.
    f = open(filename, "w")
    try:
        # Write form data to the casefile
        f.writelines(lines)
    finally:
        f.close()
except IOError:
    pass