from stable_diffusion_cpp import StableDiffusion

# Path to your .gguf file
model_path = "stable-diffusion-v1-5-pruned-emaonly-Q4_0.gguf" 

# Initialize the pipeline with the GGUF model
pipe = StableDiffusion(
    model_path=model_path,
    wtype="default",  # Weight type (default, f16, q4_0, etc. if converting)
)

prompt = "A cat took a fish and running away from the market"

# Generate the image
output = pipe.generate_image(
    prompt=prompt,
    sample_method="euler_a", # DDPMScheduler equivalent often varies, euler_a is common
    width=512,
    height=512,
)

# The output is usually a list of PIL images
image = output[0]
image.save("cat.png")