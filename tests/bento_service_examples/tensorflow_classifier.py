import bentoml
from bentoml.adapters import TfTensorInput
from bentoml.frameworks.tensorflow import TensorflowSavedModelArtifact


@bentoml.env(infer_pip_packages=True)
@bentoml.artifacts([TensorflowSavedModelArtifact('model')])
class Tensorflow2Classifier(bentoml.BentoService):
    @bentoml.api(input=TfTensorInput())
    def predict(self, tensor):
        return self.artifacts.model(tensor)
