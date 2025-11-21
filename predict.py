import os
from typing import Any, Dict
from cog import BasePredictor, Input
import replicate

from stages.sdxl import generate_character_image
from stages.faceswap import faceswap
from stages.wan_remix import generate_video
from stages.vfi_post import upscale_fps, film_effect


class Predictor(BasePredictor):
    def setup(self):
        self.client = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])

    def predict(
        self,
        face_img: str = Input(description="face URL"),
        character_prompt: str = Input(description="description of the character"),
        scene_prompt: str = Input(description="description of the scene"),
    ) -> Dict[str, Any]:

        img1 = generate_character_image(self.client, character_prompt)

        img2 = faceswap(self.client, img1, face_img)

        video_raw = generate_video(self.client, img2, scene_prompt)

        video_60fps = upscale_fps(self.client, video_raw)
        final_video = film_effect(video_60fps)

        return {
            "image_raw": img1,
            "image_faceswapped": img2,
            "video_raw": video_raw,
            "video_final": final_video,
        }