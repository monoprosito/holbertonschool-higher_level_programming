Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 ('radius must be a number')
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     >>   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE