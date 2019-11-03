clientes = {123456789: ('Juan',      'Mendoza', 'M', 3),
            147258369: ('Jane',      'Smith',   'F', 8),
            145236987: ('Gonzalo',   'Sanchez', 'M', 0),
            125478963: ('Sarah',     'Jonhson', 'F', 2),
            951478632: ('Francisco', 'Omar',    'M', 7),
            965478123: ('April',     'Stone',   'F', 13)}

ver = int(input())

if clientes[ver][3] > 5:
    print(True)
else:
    print(False)