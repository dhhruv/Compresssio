import os
import shutil
import sys
import tinify
import settings

SUPPORTED_FORMATS = ("jpg", "jpeg", "png")


def create_dirs(
    raw_images_dir=settings.USER_INPUT_PATH, save_dir=settings.USER_OUTPUT_PATH
):

    if not os.path.isdir(raw_images_dir):
        os.makedirs(raw_images_dir)

    custom_dirs = []
    for root, directories, files in os.walk(raw_images_dir):
        for directory in directories:
            custom_path = os.path.join(save_dir, directory)
            custom_dirs.append(custom_path)

    compress_dirs = (save_dir, (*custom_dirs))
    for dir_ in compress_dirs:
        if not os.path.isdir(dir_):
            os.makedirs(dir_)


def get_raw_images(raw_images_dir=settings.USER_INPUT_PATH):

    print("Searching for images within supported formats...\n")

    raw_images = []

    for root, directories, files in os.walk(raw_images_dir):
        for filename in files:
            if not filename.startswith("."):
                file_type = filename.split(".")[-1]
                if file_type in SUPPORTED_FORMATS:
                    filepath = os.path.join(root, filename)
                    raw_images.append(filepath)

    if not raw_images:
        try:
            raise OSError("No images found within supported formats!!!")
        except OSError:
            dir_name = os.path.basename(raw_images_dir)
            print(
                f"Please add images to “{dir_name}” within the dupported formats and try Again...\n"
            )
            sys.exit()

    return raw_images


def change_dir(
    abs_image_path,
    raw_images_dir=settings.USER_INPUT_PATH,
    save_dir=settings.USER_OUTPUT_PATH,
):

    if os.path.dirname(abs_image_path) == raw_images_dir:
        os.chdir(save_dir)

    else:
        custom_dir_path = os.path.dirname(abs_image_path)
        custom_dir_name = os.path.basename(custom_dir_path)
        compressed_custom_dir_path = os.path.join(save_dir, custom_dir_name)
        os.chdir(compressed_custom_dir_path)


def compress_and_save(abs_image_path, ct):

    only_image_path, image_info = os.path.split(abs_image_path)
    image_name, image_type = image_info.split(".")

    optimized_filename = f"{image_name}_optimized.{image_type}"
    if not os.path.isfile(optimized_filename):
        print("Image " + str(ct) + f": Compressing {image_name}")
        source = tinify.from_file(abs_image_path)

        print("Image " + str(ct) + f": Saving {optimized_filename}\n")
        source.to_file(optimized_filename)


def main():
    try:

        tinify.key = settings.API_KEY
        tinify.validate()
        ct = 1

        create_dirs()
        raw_image_pull = get_raw_images()
        for image in raw_image_pull:
            change_dir(image)
            compress_and_save(image, ct)
            ct += 1
        print("All optimized images have been saved")

    except tinify.AccountError:
        print("AccountError: Please verify your Tinify API key and account limit...")
    except tinify.ClientError:
        print("ClientError: Please check your source image...")
    except tinify.ServerError:
        print(
            "ServerError: Temporary issue with the Tinify API. Please try again later...\n"
        )
    except tinify.ConnectionError:
        print(
            "ConnectionError: A network connection error occurred. Please try again later...\n"
        )
    except Exception as e:
        print("UnknownError: Something went wrong. Please try again later...\n", e)


if __name__ == "__main__":
    main()
