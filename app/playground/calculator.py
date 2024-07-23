import gradio as gr


def build_calculator_demo() -> gr.Blocks:

    with gr.Blocks(title="Subnet Calculator") as demo:

        gr.HTML("<h1 align=center>🌏 Subnet Calculator</h1>")

    return demo
