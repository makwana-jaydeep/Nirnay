import gradio as gr
from utils import load_model, build_prompt
import re

pipe = load_model()

def generate_advice(degree, discipline, skills, experience, cgpa, exam, goal, interest, finance):
    inputs = {
        "degree": degree,
        "discipline": discipline,
        "skills": skills,
        "experience": experience,
        "cgpa": cgpa,
        "exam": exam,
        "goal": goal,
        "interest": interest,
        "finance": finance,
    }
    prompt = build_prompt(inputs)
    output = pipe(prompt, max_new_tokens=250, do_sample=True, temperature=0.7)[0]['generated_text']
    cleaned_output = re.split("Explanation",output.split("Output:")[-1].strip(), maxsplit=1)[0].strip()
    return cleaned_output

iface = gr.Interface(
    fn=generate_advice,
    title="🎓 Career Advice Generator for Engineering Students",
    inputs=[
        gr.Dropdown(["BTech", "MTech", "MCA", "BSc", "BCA", "MSc", "BS", "MSR"], label="Degree"),
        gr.Textbox(label="Discipline (shortform eg: CS)"),
        gr.Textbox(label="Skills (comma separated)"),
        gr.Slider(0.0, 10.0, step=0.5, label="Experience (in years)"),
        gr.Slider(0.0, 10.0, step=0.1, label="CGPA"),
        gr.Textbox(label="Competitive Exam Cracked (or 'None')"),
        gr.Textbox(label="Future Goal"),
        gr.Textbox(label="Interest Area"),
        gr.Slider(0.0, 10.0, step=1.0, label="Financial Support"),
    ],
    outputs=gr.Textbox(label="Career Advice"),
)

iface.launch(share=True)
