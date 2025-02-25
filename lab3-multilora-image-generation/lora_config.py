LORA = [
    {"model_id": "SDXL-LoRA/alvdansen-the-point", "prompt": "<subject>", "name": "Point style", "file_name": "araminta_k_the_point.safetensors", "weight": 0.6},
    {
        "model_id": "SDXL-LoRA/KappaNeuro-ukiyo-e-art",
        "prompt": "an illustration of <subject> in Ukiyo-e Art style",
        "negative": "realistic, portrait, 3d",
        "file_name": "Ukiyo-e Art.safetensors",
        "weight": 0.8,
        "name": "Ukiyo-e Style",
    },
    {
        "model_id": "SDXL-LoRA/DoctorDiffusion-doctor-diffusion-s-controllable-vector-art-xl-lora",
        "prompt": "vector <subject>",
        "file_name": "DD-vector-v2.safetensors",
        "weight": 0.8,
        "name": "Vector Art",
    },
    {
        "model_id": "SDXL-LoRA/Norod78-sdxl-chalkboarddrawing-lora",
        "prompt": "A colorful chalkboard drawing of <subject>",
        "name": "Chalkboard drawing",
        "file_name": "SDXL_ChalkBoardDrawing_LoRA_r8.safetensors",
        "weight": 0.45,
    },
]
