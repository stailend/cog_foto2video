# stages/video_gen.py

import replicate
import requests

def generate_video(image_path: str, scene_prompt: str, out_path="output_wan.mp4"):
    print("== STEP 3: WAN 2.1 VIDEO ==")

    with open(image_path, "rb") as f:
        image_bytes = f.read()

    output = replicate.run(
        "wan-video/wan-2.1-1.3b",
        input={
            "prompt": scene_prompt,
            "image": image_bytes,
            "fps": 24,
            "num_frames": 48,
        }
    )

    video_url = output

    video_data = requests.get(video_url).content
    with open(out_path, "wb") as f:
        f.write(video_data)

    print(f"WAN video saved: {out_path}")
    return out_path