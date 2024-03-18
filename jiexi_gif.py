from PIL import Image

def save_gif_frames(gif_path, output_folder):
    # Open the GIF file
    gif_image = Image.open(gif_path)

    # Iterate through each frame in the GIF
    for frame_number in range(gif_image.n_frames):
        # Select the current frame
        gif_image.seek(frame_number)

        # Convert the frame to RGB format
        rgb_frame = gif_image.convert('RGBA')

        # Save the frame as a separate image
        output_path = f"{output_folder}/frame_{frame_number + 1:03d}.png"
        rgb_frame.save(output_path, format="PNG")

if __name__ == "__main__":
    # Specify the path to the GIF file
    gif_path = r"G:\markdown\研究生实验\小论文-冲突-w欲何为_Win11.assets\tanet.gif"

    # Specify the output folder
    output_folder = r"gif\2"

    # Create the output folder if it doesn't exist
    import os
    os.makedirs(output_folder, exist_ok=True)

    # Call the function to save GIF frames
    save_gif_frames(gif_path, output_folder)

    print("GIF frames saved successfully.")
