def faceswap(client, base_image_url: str, face_url: str):
    out = client.run(
        "easel/advanced-face-swap",
        input={
            "target_image": base_image_url,
            "face_image": face_url
        }
    )
    return out["output"] 