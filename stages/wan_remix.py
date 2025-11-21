def generate_video(client, image_url: str, scene_prompt: str):
    out = client.run(
        "wan-video/wan-2.1-1.3b",
        input={
            "image": image_url,
            "prompt": scene_prompt,
            "num_frames": 30,
            "fps": 30
        }
    )
    return out 