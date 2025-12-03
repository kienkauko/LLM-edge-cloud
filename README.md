# LLM Edge Cloud

This repository contains the code for deploying open-source LLM models locally as microservices using the `llama_cpp` library. The model must be downloaded beforehand via Hugging Face in the GGUF format. The recommended model for edge deployment is [`gemma-2-2b-it-Q8_0.gguf`](https://huggingface.co/bartowski/gemma-2-2b-it-GGUF).

## Setup Instructions

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

3. Test the deployment from another terminal:
   ```bash
   curl "http://localhost:8000/query?prompt=hello"
   ```
   Or with quotes:
   ```bash
   curl --get "http://localhost:8000/query" --data-urlencode "prompt=Write me a poem about winter"
   ```
