<p align="center">
  <img src="https://user-images.githubusercontent.com/72680045/100545837-fbb54e80-3283-11eb-92ce-c82ed48f19e9.png">
  <h2 align="center" style="margin-top: -4px !important;">Streamline your Images to Save lots of storage space...</h2>
  <p align="center">
    <a href="https://github.com/dhhruv/Compresssio/blob/master/LICENSE">
      <img src="https://img.shields.io/badge/license-MIT-blue.svg">
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/python-v3.8-blue.svg">
    </a>
  </p>
</p>

# Compresssio:

The above script uses TinyPNG's savvy lossy compression methods to reduce the document size of your JPG/PNG files. This is achieved by specifically decreasing the number of colors in the image, therefore lesser number of bytes are required to store the information. The impact of the script is nearly invisible but it makes an exceptionally enormous effect in file size of the image.

## Setup (Windows):

1. Install Python
2. Clone this repository
```
git clone https://github.com/dhhruv/Compresssio.git
```

3. Install, create and activate virtual environment.
For instance we create a virtual environment named 'venv'.
```
pip install virtualenv
python -m virtualenv venv
venv\bin\activate.bat
```

4. Install dependencies
```
pip install -r requirements.txt
```

## Initial Settings required:

1. Open `settings.py` in text editor of your choice.
2. Add the API_KEY key from [tinypng.com/developers](https://tinypng.com/developers/) to the `API_KEY` field.
3. In the `USER_INPUT_PATH` field add the path of the directory with original images (images to be compressed).
4. In the `USER_OUTPUT_PATH` field add the path of the directory with compressed files (where the compressed images will be saved).

## Easy way to use: (Windows) (Optional)

Create `compression.bat` file with:
```
@echo off
cmd /c "path\to\venv\Scripts\python.exe path\to\Compresssio.py"
pause
```

Now run the Batch Script (.bat file) from any path you want.

## Important Note:

-	**The limit you'll have at first is of 500 images per month on the Free plan. You can change this according to your requirement at [tinypng.com/dashboard/api](https://tinypng.com/dashboard/api)**
-	**This Script is just a Prototype so Metadata is not stored in the Compressed Images from the Original Images.**
-	**The Authors will not be responsible for any kind of loss of data so it is essential to have a Backup of Original Data placed in the Input Folder. Read the [LICENSE](https://github.com/dhhruv/Compresssio/blob/master/LICENSE) for more information.**
