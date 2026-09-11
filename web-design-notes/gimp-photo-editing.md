# Gimp Photo Editing

---

## Table of Contents
* [Navigation](#navigation)
* [Rotating, Cropping, and Layers](#rotating-cropping-and-layers)
* [Exposure and Shadows-Highlights Function](#exposure-and-shadows-highlights-function)
* [Color Temperature and Hue-Saturation Functions](#color-temperature-and-hue-saturation-functions)
* [Histogram and Color Balance Functions](#histogram-and-color-balance-functions)
* [Clone Tool to Remove Distractions](#clone-tool-to-remove-distractions)
* [Adding a Watermark and Exporting the Final Edit](#adding-a-watermark-and-exporting-the-final-edit)

---

## Navigation
* Open a file - drag photo file in Gimp
* Zoom in/out - `ctrl + mouse wheel`
* Move around - hold `spacebar`
* Zoom fit - `ctrl + shift + J`
* Undo history window - `Window -> Dockable Dialogs -> Undo History`
* Tool Options window - `Window -> Dockable Dialogs -> Tool Options`
* Save the project as an **xcf** to save your layers

---

## Rotating, Cropping, and Layers
* Rotate - `shift + R`
* Crop - `shift + C`
* Duplicate layer - `ctrl + shift + D`

---

## Exposure and Shadows-Highlights Function
* **Note:** Create a new layer first before adjusting the brightness/exposure of an image.

* To adjust the **overall** brightess or exposure of the whole image:
    - `Colors -> Exposure...`
        - Increase the **Exposure** option to increase the brightness of the whole image.

* To adjust the brightness of just a **part** of the image:
    - `Colors -> Shadows-Highlights...`
        - Increase the value of **Shadows** option to increase the brightness of the dark parts
        - Optional: Lower the **Highlights** value to make the bright parts darker
        - **Note**: It is better to increase the brightness of the photo as lowering it too much will lose its quality.

---

## Color Temperature and Hue-Saturation Functions
* **Note:** Create again a new layer first before adjusting the temperature and saturation of an image.

* Adjust the **Color Temperature** to adjust the **warmness** of an image (increase or decrease orange/red)
    - `Colors -> Color Temperature...`
        - Play with the **Original temperature** and **Intended temperature** options to eyeball the desired warmness.

* Adjust the **Hue-Saturation** to select a primary color to adjust.
    - `Colors -> Hue-Saturation...`

---

## Histogram and Color Balance Functions
* **Note:** Create a new layer.

* `Colors -> Info -> Histogram` - to view the image balance (if the luminance is balanced, which color is dominating, etc.)
    - Left side - dark tones
    - Right side - light tones
    - Middle - middle tones

* You can then adjust and balance them using `Colors -> Color Balance...`

![alt text](images/gimp-photo-editing/2026-09-10_15-12.png)

---

## Clone Tool to Remove Distractions
* **Note:** Create a new layer.
* Press `C`
    - Adjust the brush size in the **Tool Options** (or press-hold `[]`)
    - Hold `ctrl` then click the part that you want to clone
    - Then click on the areas that you want to be painted.

---

## Adding a Watermark and Exporting the Final Edit
* Open your watermark image (png) in Gimp.
* Drag its **tab** to your target image.
* Resize / scale it - `shift + S`
* Use the move tool (press `M`) to your desired location.
* On the layer window, adjust its opacity.
* `File -> Export As...` then choose a file type (example: jpg)

---