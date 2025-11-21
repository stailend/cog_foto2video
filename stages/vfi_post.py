def upscale_fps(client, video_url: str):
    out = client.run(
        "topazlabs/video-upscale",
        input={
            "video": video_url,
            "preset": "standard",
            "resolution": "1080p"
        }
    )
    return out

import subprocess

def film_effect(video_url: str):
    output_path = "/outputs/final.mp4"
    subprocess.run([
        "ffmpeg", "-y",
        "-i", video_url,
        "-vf", "noise=alls=20:allf=t+u,unsharp=5:5:0.8",
        "-c:v", "libx264", "-preset", "fast",
        "-pix_fmt", "yuv420p",
        output_path
    ])
    return output_path