#include "dcblock.hpp"
#include "types.hpp"

#include <csdr/dcblock.hpp>

static int DcBlock_init(DcBlock* self, PyObject* args, PyObject* kwds) {
    static char* kwlist[] = {
        (char*) "sampleRate",
        (char*) "cutoff",
        (char*) "fadeTime",
        NULL
    };
    float sampleRate = 48000.0f;
    float cutoff = 15.0f;
    float fadeTime = 0.05f;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|fff", kwlist, &sampleRate, &cutoff, &fadeTime)) {
        return -1;
    }

    self->setModule(new Csdr::DcBlock(sampleRate, cutoff, fadeTime));

    self->inputFormat = FORMAT_FLOAT;
    self->outputFormat = FORMAT_FLOAT;

    return 0;
}

static PyType_Slot DcBlockSlots[] = {
    {Py_tp_init, (void*) DcBlock_init},
    {0, 0}
};

PyType_Spec DcBlockSpec = {
    "pycsdr.modules.DcBlock",
    sizeof(DcBlock),
    0,
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_FINALIZE,
    DcBlockSlots
};
