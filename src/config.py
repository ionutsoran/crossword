"""
Copyright Ionut Soran 2021. ALL RIGHTS RESERVED.
Authors: [Ionut Soran]
Maintainers: [Ionut Soran]
Configuration file for crosswords project
"""
import pathlib

# TODO ADD CONFIGS FOR TESTS AND FOR BUILING
IMAGE_MODE = "RGBA"
IMAGE_FORMAT = "PNG"
TRANSPARENT_BACKGROUND = (255, 0, 0, 0)
SRC_PATH = pathlib.Path(__file__).parent.resolve()
PROJECT_PATH = SRC_PATH.parent
RESOURCE_PATH = SRC_PATH / "resources"
FONTS_PAH = RESOURCE_PATH / "fonts"
BUILD_PATH = PROJECT_PATH / "build"
TARGET_PATH = PROJECT_PATH / "target"
FONTS = {
    "arial": {
        "normal": "ARIAL",
        "bold": "ARIALBD",
        "bold_italic": "ARIALBI",
        "italic": "ARIALI",
        "black": "ARIBLK"
    }
}
