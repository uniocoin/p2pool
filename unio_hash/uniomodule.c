#include <Python.h>

#include "unio.h"

static PyObject *unio_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
#if PY_MAJOR_VERSION >= 3
    PyBytesObject *input;
#else
    PyStringObject *input;
#endif
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

#if PY_MAJOR_VERSION >= 3
    unio_hash((char *)PyBytes_AsString((PyObject*) input), output);
#else
    unio_hash((char *)PyString_AsString((PyObject*) input), output);
#endif
    Py_DECREF(input);
#if PY_MAJOR_VERSION >= 3
    value = Py_BuildValue("y#", output, 32);
#else
    value = Py_BuildValue("s#", output, 32);
#endif
    PyMem_Free(output);
    return value;
}

static PyMethodDef UnioMethods[] = {
    { "getPoWHash", unio_getpowhash, METH_VARARGS, "Returns the proof of work hash using unio hash" },
    { NULL, NULL, 0, NULL }
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef UnioModule = {
    PyModuleDef_HEAD_INIT,
    "unio_hash",
    "...",
    -1,
    UnioMethods
};

PyMODINIT_FUNC PyInit_unio_hash(void) {
    return PyModule_Create(&UnioModule);
}

#else

PyMODINIT_FUNC initunio_hash(void) {
    (void) Py_InitModule("unio_hash", UnioMethods);
}
#endif
