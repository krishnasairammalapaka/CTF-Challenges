import base64
import os

# Base64-encoded minimal 1×1 PNG image (transparent).
png_base64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8z8BQDwAD/wH+zlVEAAAAAElFTkSuQmCC"
)

# Decode the PNG image bytes.
png_data = base64.b64decode(png_base64)

# Define the secret hidden message (this could be your flag).
hidden_message = b"\nflag{hidden_in_plain_sight}"

# Combine the valid PNG data with the appended hidden message.
final_data = png_data + hidden_message

# Ensure that the /files directory exists.
os.makedirs("files", exist_ok=True)

# Write the final binary content to the secret.png file.
with open("files/secret.png", "wb") as f:
    f.write(final_data)

print("Secret image created at files/secret.png") 