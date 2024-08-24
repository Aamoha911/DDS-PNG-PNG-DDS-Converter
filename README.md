# DDS to PNG Converter

This tool is a simple PyQt5 application for converting DDS (DirectDraw Surface) image files to PNG (Portable Network Graphics) format. It provides a graphical user interface to easily perform batch conversions between these two formats.

### Features

1. **Image Conversion**:
   - **DDS to PNG**: Converts DDS (DirectDraw Surface) images to PNG format.
   - **PNG to DDS**: Converts PNG images to DDS format.

2. **Advanced Image Processing** (Available when "Enable Advanced Settings" is checked):
   - **Resize Output**: Adjusts the dimensions of the image during conversion.
   - **Brightness Adjustment**: Changes the brightness level of the image.
   - **Contrast Adjustment**: Modifies the contrast of the image.
   - **Saturation Adjustment**: Alters the color saturation of the image.
   - **Sharpening**: Enhances the sharpness of the image.
   - **Blurring**: Applies a blur effect to the image.

3. **PNG Compression Options**:
   - **Lossless Compression**: Saves PNG images with no compression loss.
   - **Lossy Compression**: Saves PNG images with reduced quality for smaller file sizes.

4. **User Interface**:
   - **Radio Buttons**: Select between DDS to PNG and PNG to DDS conversion modes.
   - **Directory Selection**: Browse and select source and output directories.
   - **Checkboxes**: Enable or disable advanced settings and specific processing options.
   - **Spin Boxes**: Set values for image processing parameters like resizing dimensions and adjustment levels.
   - **Start Conversion Button**: Initiates the conversion process.

5. **Error Handling**:
   - **Warnings**: Alerts users if required directories are not selected.
   - **Error Messages**: Displays errors if conversion fails.

## Requirements

- Python 3.x
- PyQt5
- Pillow
- imageio
