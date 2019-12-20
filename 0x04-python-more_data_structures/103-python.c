#include "/usr/include/python3.4/Python.h"
#include <stdio.h>

void print_python_list(PyObject *p)
{
    int i = 0, list_len = 0;
    PyObject *item;
    PyListObject *clone = (PyListObject *) p;

    printf("[*] Python list info\n");
    list_len = PyList_GET_SIZE(p);
    printf("[*] Size of the Python List = %d\n", list_len);
    printf("[*] Allocated = %d\n", (int) clone->allocated);

    for (; i < list_len; ++i)
    {
        item = PyList_GET_ITEM(p, i);
        printf("Element %d: %s\n", i, item->ob_type->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    PyBytesObject *clone = (PyBytesObject *) p;

    printf("[.] bytes object info\n");
    printf("  size: %d\n", (int) PyBytes_Size(p));
    printf("  trying string: %s\n", clone->ob_sval);
    printf("  first 6 bytes:\n");
}
