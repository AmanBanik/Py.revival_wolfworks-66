import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Compressor & Pixelator")
        self.root.geometry("600x600")

        # Variables
        self.image_path = None
        self.compression_var = tk.DoubleVar(value=75.0)  # Default compression quality
        self.pixelation_var = tk.IntVar(value=10)  # Default pixelation level
        self.format_var = tk.StringVar(value="JPEG")  # Default output format

        # GUI Elements
        tk.Label(root, text="Image Compressor & Pixelator").pack(pady=10)

        tk.Button(root, text="Select Image", command=self.load_image).pack(pady=5)

        tk.Label(root, text="Compression Quality (0-100, lower = more compression):").pack()
        tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, variable=self.compression_var).pack()

        tk.Label(root, text="Pixelation Level (1-50, higher = more blocky):").pack()
        tk.Scale(root, from_=1, to=50, orient=tk.HORIZONTAL, variable=self.pixelation_var).pack()

        tk.Label(root, text="Output Format:").pack()
        tk.OptionMenu(root, self.format_var, "JPEG", "PNG").pack()

        tk.Button(root, text="Process Image", command=self.process_image).pack(pady=10)

        # Size labels
        self.size_label = tk.Label(root, text="Original Size: N/A | New Size: N/A")
        self.size_label.pack(pady=10)

        # Image preview labels
        self.original_preview = tk.Label(root)
        self.original_preview.pack(side=tk.LEFT, padx=10)
        self.processed_preview = tk.Label(root)
        self.processed_preview.pack(side=tk.RIGHT, padx=10)

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if self.image_path:
            self.display_preview(self.image_path, self.original_preview, "Original")

    def display_preview(self, path, label, title):
        img = Image.open(path)
        img.thumbnail((200, 200))  # Resize for preview
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo, text=title, compound=tk.TOP)
        label.image = photo  # Keep a reference

    def pixelate(self, image, pixel_size):
        # Resize down to create blocky effect, then resize back up
        small = image.resize((image.width // pixel_size, image.height // pixel_size), Image.NEAREST)
        pixelated = small.resize(image.size, Image.NEAREST)
        return pixelated

    def process_image(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image first!")
            return

        try:
            # Load original image
            img = Image.open(self.image_path)
            original_size = os.path.getsize(self.image_path) / 1024  # Size in KB

            # Apply pixelation
            pixel_size = self.pixelation_var.get()
            img = self.pixelate(img, pixel_size)

            # Prepare output path
            output_path = "processed_image." + self.format_var.get().lower()
            output_format = self.format_var.get()

            # Save with compression
            if output_format == "JPEG":
                img.save(output_path, "JPEG", quality=int(self.compression_var.get()))
            else:
                img.save(output_path, "PNG")  # PNG ignores quality parameter

            # Get new size
            new_size = os.path.getsize(output_path) / 1024  # Size in KB

            # Update size label
            self.size_label.config(text=f"Original Size: {original_size:.2f} KB | New Size: {new_size:.2f} KB")

            # Display processed image preview
            self.display_preview(output_path, self.processed_preview, "Processed")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to process image: {str(e)}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()