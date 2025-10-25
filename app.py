# BiasGuard-ALBERT Application
import gradio as gr

def check_bias(text):
    bias_words = ['young', 'energetic', 'rockstar', 'ninja', 'guys']
    found = [w for w in bias_words if w.lower() in text.lower()]
    if found:
        return f"⚠️ Bias detected: {', '.join(found)}"
    return "✅ No obvious bias"

demo = gr.Interface(
    fn=check_bias,
    inputs=gr.Textbox(label="Job Description", lines=10),
    outputs=gr.Textbox(label="Result"),
    title="🎯 BiasGuard-ALBERT"
)

if __name__ == "__main__":
    demo.launch()
