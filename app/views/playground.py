import gradio as gr


def build_calculator_demo() -> gr.Blocks:

    with gr.Blocks(title="IP Subnet Calculator") as demo:

        gr.HTML("<h1 align=center>🌏 IP Subnet Calculator</h1>")
        with gr.Tab(label="IPv4 Subnet Calculator"):
            gr.HTML("<h1 align=center>🌏 IPv4 Subnet Calculator</h1>")
        with gr.Tab(label="CIDR Calculator"):
            gr.HTML("<h1 align=center>🌏 CIDR Calculator</h1>")
        with gr.Tab(label="Contact Us"):
            gr.HTML("<h1 align=center>🌏 Contact Us</h1>")

    return demo
