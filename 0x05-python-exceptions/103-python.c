#include "/usr/include/python3.4/Python.h"
#include <stdio.h>
#include <stdlib.h>

void print_hexn(const char *str, int n);
void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

void print_hexn(const char *str, int n)
{
	int i = 0;

	for (; i < n - 1; ++i)
		printf("%02x ", (unsigned char) str[i]);

	printf("%02x", str[i]);
    fflush(stdout);
}

void print_python_bytes(PyObject *p)
{
    PyBytesObject *clone = (PyBytesObject *) p;
	int calc_bytes, clone_size = 0;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    clone_size = PyBytes_Size(p);
    calc_bytes = clone_size + 1;

    if (calc_bytes >= 10)
        calc_bytes = 10;

    printf("  size: %d\n", clone_size);
    printf("  trying string: %s\n", clone->ob_sval);
    printf("  first %d bytes: ", calc_bytes);
    print_hexn(clone->ob_sval, calc_bytes);
    printf("\n");

    fflush(stdout);
}

void print_python_list(PyObject *p)
{   
    int i = 0, list_len = 0;
	PyObject *item;
	PyListObject *clone = (PyListObject *) p;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

	list_len = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", (int) clone->allocated);

	for (; i < list_len; ++i)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
        else if (PyFloat_Check(item))
            print_python_float(item);
	}

    fflush(stdout);
}

void print_python_float(PyObject *p)
{
    PyFloatObject *clone = (PyFloatObject *) p;
    float n = 0;

    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    n = clone->ob_fval;

    if ((int) n == n)
        printf("  value: %0.1f\n", clone->ob_fval);
    else
        printf("  value: %0.16g\n", clone->ob_fval);

    fflush(stdout);
}
