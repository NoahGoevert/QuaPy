from . import error
from . import data
from quapy.data import datasets
from . import functional
# from . import method
from . import evaluation
from . import protocol
from . import plot
from . import util
from . import model_selection
from . import classification

__version__ = '0.1.7'

environ = {
    'SAMPLE_SIZE': None,
    'UNK_TOKEN': '[UNK]',
    'UNK_INDEX': 0,
    'PAD_TOKEN': '[PAD]',
    'PAD_INDEX': 1,
    'SVMPERF_HOME': './svm_perf_quantification',
    'N_JOBS': 1
}


def get_njobs(n_jobs):
    return environ['N_JOBS'] if n_jobs is None else n_jobs




