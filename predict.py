# predict.py

from typing import Any
from cog import BasePredictor, Input
from stages.sdxl import generate_character_image
from stages.faceswap import faceswap
from stages.video_gen import generate_video
from stages.vfi_post import upscale_fps

class Predictor(BasePredictor):

    def setup(self):
        print("Predictor ready")
        
    def predict(
        self,
        face_img: str = Input(),
        character_prompt: str = Input(),
        scene_prompt: str = Input()
    )-> Any:
        o1 = generate_character_image(character_prompt)
        o2 = faceswap(o1, face_img)
        o3 = generate_video(o2, scene_prompt)
        o4_raw = upscale_fps(o3, "output_60fps.mp4")
        o4 = film_effect(o4_raw, "output_final.mp4")

        return {
            "output_1_image": o1,
            "output_2_faceswap": o2,
            "output_3_video_raw": o3,
            "output_4_60fps": o4,
            "output_5_final": o5
        }