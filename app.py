import tkinter as tk
from tkinter import filedialog, Text
import pdfplumber
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import torch

# Função para extrair texto de um PDF
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() or ''
    return full_text

# Configuração do modelo GPT-Neo
model_name = "EleutherAI/gpt-neo-2.7B"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPTNeoForCausalLM.from_pretrained(model_name)

# Função para gerar resposta
def generate_response(question, context):
    input_ids = tokenizer.encode(question + tokenizer.eos_token + context, return_tensors="pt")
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
    output_ids = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_new_tokens=150  # Gera no máximo 150 novos tokens
    )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

# Funções de interface
def add_pdf():
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("PDF files", "*.pdf"), ("all files", "*.*")))
    if filename:
        pdf_files.append(filename)
        pdf_text.insert(tk.END, filename + '\n')

def clear_files():
    pdf_files.clear()
    pdf_text.delete('1.0', tk.END)

def ask_question():
    context = ' '.join([extract_text_from_pdf(pdf) for pdf in pdf_files])
    answer_text.delete('1.0', tk.END)
    response = generate_response(question_entry.get(), context)
    answer_text.insert(tk.END, response)

# Configuração da interface gráfica
root = tk.Tk()
root.title("PDF Assistant")

frame = tk.Frame(root)
frame.pack()

open_file_btn = tk.Button(root, text="Open PDF", padx=10, pady=5, fg="white", bg="#263D42", command=add_pdf)
open_file_btn.pack()

clear_btn = tk.Button(root, text="Clear PDFs", padx=10, pady=5, fg="white", bg="#263D42", command=clear_files)
clear_btn.pack()

pdf_text = Text(root, height=10)
pdf_text.pack()

question_label = tk.Label(root, text="Enter your question:")
question_label.pack()

question_entry = tk.Entry(root, width=50)
question_entry.pack()

submit_btn = tk.Button(root, text="Submit Question", command=ask_question)
submit_btn.pack()

answer_label = tk.Label(root, text="Response:")
answer_label.pack()

answer_text = Text(root, height=10)
answer_text.pack()

pdf_files = []

root.mainloop()
