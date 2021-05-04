import numpy as np
from jina.executors.encoders.multimodal import BaseMultiModalEncoder

from jina.executors.decorators import batching, as_ndarray


class ConcatenateMultiModalEncoder(BaseMultiModalEncoder):
    batch_size = 10

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @batching(slice_nargs=2)
    @as_ndarray
    def encode(self, *data: 'np.ndarray', **kwargs):
        assert len(data) == 2
        for d in data:
            assert self.batch_size == ConcatenateMultiModalEncoder.batch_size
            assert len(d) == self.batch_size
            assert isinstance(d, np.ndarray)
        modality1 = data[0]
        modality2 = data[1]
        assert len(modality1) == len(modality2)
        return np.concatenate((modality1, modality2), axis=1)