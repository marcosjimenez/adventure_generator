import io
import base64
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
from core.options import ConversationOptions

class ImageGenerator:

    def generate(self, input_text: str, options: ConversationOptions):
        pipeline = StableDiffusionPipeline.from_pretrained(
            options.model, torch_dtype=torch.float16, use_safetensors=True
        )
        
        device = 'cpu'
        if options.cuda:
            pipeline = pipeline.to('cuda')
            device = 'cuda'

        generator = torch.Generator(device).manual_seed(0)      
        custom_prompt = input_text + ", " + options.extended_prompt
        image = pipeline(
            prompt=custom_prompt,
            negative_prompt="",
            generator=generator,
            num_inference_steps=options.num_inference_steps,
            guidance_scale=options.guidance_scale).images[0]

        byte_arr = io.BytesIO()
        image.save(byte_arr, format='PNG')
        return str(base64.b64encode(byte_arr.getvalue()).decode('utf-8'))