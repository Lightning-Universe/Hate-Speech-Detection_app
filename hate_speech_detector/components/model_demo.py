"""
Model credits to Sai Saketh Aluru, Binny Mathew, Punyajoy Saha and Animesh Mukherjee for
their work [DE-LIMIT](https://github.com/hate-alert/DE-LIMIT)
"""
import gradio as gr
from lightning.app.components.serve import ServeGradio
from loguru import logger

from hate_speech_detector.hpd_model import HPDModel


class ModelDemo(ServeGradio):
    """Serve model with Gradio UI.

    You need to define i. `build_model` and ii. `predict` method and Lightning `ServeGradio` component will
    automatically launch the Gradio interface.
    """

    inputs = gr.inputs.Textbox(default="Going into the space", label="Abusive text detection")
    outputs = "text"
    enable_queue = False
    examples = [["You are a terrible person!"], ["Going into the space"]]

    def __init__(self):
        super().__init__(parallel=True)

    def build_model(self) -> HPDModel:
        logger.info("loading model...")
        model = HPDModel()
        logger.info("built model!")
        return model

    def predict(self, query: str) -> str:
        return self.model.predict(query)
