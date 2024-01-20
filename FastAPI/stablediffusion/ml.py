from pathlib import Path
from typing import Union
import torch
from diffusers import DiffusionPipeline
from diffusers import StableDiffusionPipeline
from diffusers import DPMSolverMultistepScheduler
from PIL.Image import Image

token_path = Path("token.txt")
token = token_path.read_text().strip()

model_id = "stabilityai/stable-diffusion-2-1"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32, cache_dir="model", use_auth_token=token)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = pipe.to(device)

# prompt = "a photo of an astronaut swimming in the ocean"
# image = pipe(prompt).images[0]
    
# image.save("astronaut_swimming_ocean.png")

def obtain_image(prompt: str, *, seed: Union[int, None] = None, num_inference_steps: int = 50, guidance_scale: float = 7.5) -> Image:
    
    generator = None if seed is None else torch.Generator("cpu")
    print(f"using device: {pipe.device}")
    image: Image = pipe(prompt, guidance_scale=guidance_scale, seed=seed, num_inference_steps=num_inference_steps, generator=generator).images[0]
    return image

# image = obtain_image(prompt, num_inference_steps=5, seed=1024)

