def generate_character_image(client, prompt: str):
    out = client.run(
        "black-forest-labs/flux-canny-dev",
        input={
            "prompt": prompt,
        }
    )
    return out[0]