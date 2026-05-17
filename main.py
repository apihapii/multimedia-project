from PIL import Image
import numpy as np
import os

# Load gambar
img = Image.open("gambar.jpg")

print("Ukuran:", img.size)
print("Mode:", img.mode)

# Convert ke numpy
img_np = np.array(img)

# Ambil channel RGB
R = img_np[:, :, 0]
G = img_np[:, :, 1]
B = img_np[:, :, 2]

# Convert grayscale
gray = (0.299 * R + 0.587 * G + 0.114 * B).astype(np.uint8)

# Simpan grayscale
gray_img = Image.fromarray(gray)
gray_img.save("grayscale.png")

print("Grayscale selesai")

# Bitplane
for i in range(8):
    bitplane = ((gray >> i) & 1) * 255
    Image.fromarray(bitplane.astype(np.uint8)).save(f"bitplane_{i}.png")

print("Bitplane selesai")

# Split RGB
zeros = np.zeros_like(R)

red_img = np.stack([R, zeros, zeros], axis=2)
green_img = np.stack([zeros, G, zeros], axis=2)
blue_img = np.stack([zeros, zeros, B], axis=2)

Image.fromarray(red_img).save("red_channel.png")
Image.fromarray(green_img).save("green_channel.png")
Image.fromarray(blue_img).save("blue_channel.png")

print("Split RGB selesai")

# Kompresi JPEG
qualities = [10, 50, 90]

for q in qualities:
    filename = f"compressed_Q{q}.jpg"

    img.save(filename, "JPEG", quality=q)

    size_kb = os.path.getsize(filename) / 1024

    print(f"Q={q} -> {size_kb:.2f} KB")

# Analisis raw size
width, height = img.size

channels = 3
bit_depth = 8

raw_size = width * height * channels * bit_depth / 8

print(f"Raw size: {raw_size / 1024:.2f} KB")