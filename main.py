from fastapi import FastAPI
from llama_cpp import Llama
import time

app = FastAPI()

# Initialize LLM
# Note: vLLM usually requires a GPU.
start_time = time.time()
# llm = LLM(model="google/gemma-2-2b")
# params = SamplingParams(temperature=0.7, max_tokens=200)
llm = Llama(
    model_path="gemma-2-2b-it-Q8_0.gguf",  # download GGUF model
    n_gpu_layers=0,                   # CPU only
    n_threads=8                       # adjust to your CPU
)

end_time = time.time()
print(f"Model loading time: {end_time - start_time} seconds")

@app.get("/query")
def query(prompt: str):
    out = llm(prompt, max_tokens=200)
    return {"reply": out["choices"][0]["text"]}