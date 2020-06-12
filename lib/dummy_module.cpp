#include <Python.h>

static PyMethodDef NoMethods[] = {
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef dummymodule = {
	PyModuleDef_HEAD_INIT,
	"_xbrz",
	NULL,
	-1,
	NoMethods
};

PyMODINIT_FUNC
PyInit__xbrz(void) {
	return PyModule_Create(&dummymodule);
}
