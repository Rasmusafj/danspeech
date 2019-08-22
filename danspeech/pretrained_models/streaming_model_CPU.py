import torch

from danspeech.deepspeech.model import DeepSpeech
from danspeech.utils.data_utils import get_model

MODEL_PACKAGE = "toDo"

# ToDO: Create
def CPUStreamingRNN(cache_dir=None):
    """
    Instantiates the most complex DanSpeech model with a lot of parameters

    :return: Pretrained DeepSpeech model
    """
    model_path = get_model(model_name="CPUStreamingRNN.pth", origin=MODEL_PACKAGE, file_hash="ba514ec96b511c0797dc643190a80269", cache_dir=cache_dir)
    model = DeepSpeech.load_model(model_path)
    return model
