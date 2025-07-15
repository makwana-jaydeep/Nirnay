from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def load_model():

    
    tokenizer = AutoTokenizer.from_pretrained("quantized_model")
    model = AutoModelForCausalLM.from_pretrained("quantized_model")
    
    return pipeline("text-generation", model=model, tokenizer=tokenizer)

def build_prompt(inputs):
    prompt = f"""
    Input: degree: {inputs['degree']}, discipline: {inputs['discipline']}, skills: {inputs['skills']}, experience: {inputs['experience']}, CGPA: {inputs['cgpa']}, competitive_exam: {inputs['exam']}, future_goal: {inputs['goal']}, interest: {inputs['interest']}, financial_support: {inputs['finance']}
    Output:
    """
    return prompt

if __name__ == "__main__":
    pipe = load_model()
    print(pipe("what is the capital of india", max_new_tokens=250, do_sample=True, temperature=0.7)[0]['generated_text'])

