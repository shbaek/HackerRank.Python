import re
print "".join((i[:1].upper()+i[1:]) if i[0].isalpha() else i for i in re.split(r'(\s+)',raw_input()))