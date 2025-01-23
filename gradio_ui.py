from ray.serve.gradio_integrations import GradioServer
import gradio as gr
import requests

def ui_builder():

    def model_infer(text):
        resp = requests.get(f"localhost:8000/infer?text={text}")
        return resp.text

    return gr.Interface(
        fn=model_infer,
        inputs=[gr.Textbox(value="Once upon a time", label="Начните предложение")],
        outputs=[gr.Textbox(label="Ответ модели")],
        clear_btn=gr.Button("Очистить", variant="secondary"),
        submit_btn=gr.Button("Сгенерировать", variant="primary"),
        flagging_options=[],
        theme=gr.themes.Soft(),
        title="Gradio — Тестовый интерфейс генератора текста",
        description="Inference API: <pre>/infer?text=[text]</pre>"
    )

app = GradioServer.options(route_prefix="/web", ray_actor_options={"num_cpus": 1}).bind(ui_builder)