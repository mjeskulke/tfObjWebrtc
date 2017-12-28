'''Setup script for object_detection with webrtc'''

from setuptools import find_packages
from setuptools import setup


REQUIRED_PACKAGES = ['Pillow>=1.0', 'Flask', 'tensorflow', 'six', 'matplotlib']

setup(
    name='webrtc_object_detection',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    packages=[p for p in find_packages()],
    description='Tensorflow Object Detection with WebRTC',
)

'''Download the Object Dectection directory'''
import six.moves.urllib as urllib
from zipfile import ZipFile
import os
import sys
import re
import shutil

print("\n\nDownloading the TensorFlow API from Github...")

REPOSITORY_ZIP_URL = 'https://github.com/tensorflow/models/archive/master.zip'

try:
    filename, headers = urllib.request.urlretrieve(REPOSITORY_ZIP_URL)
    #filename = 'models-master.zip'

    print("\n... download complete")

    target_path = os.path.join(os.getcwd(), 'object_detection/')
    temp_path = filename + "_dir"

    with ZipFile(filename, 'r') as zip_file:
        files = zip_file.namelist()
        files_to_extract = [f for f in files if f.startswith(('models-master/research/object_detection/'))]
        zip_file.extractall(temp_path, files_to_extract)
        print("Copying TensorFlow Object API files to %s" % target_path)
        shutil.move(os.path.join(temp_path, 'models-master/research/object_detection/'), target_path)
        os.removedirs(os.path.join(temp_path, 'models-master/research/'))

except:
    print("Problem downloading the TensorFlow Object API. \n"
          "Try running `git clone https://github.com/tensorflow/models.git`.\n"
          "Then `cp /research/object_detection to /object_detection` instead")
    sys.exit(1)


'''Compile Protobufs'''
import subprocess
print("Compiling protobufs")
try:
    subprocess.Popen('protoc object_detection/protos/*.proto --python_out=.', shell=True)

except:
    print("Error compiling Protobufs")
    sys.exit(1)

print("\n\nDownloading pretrained model")
# What model to download.
MODEL_NAME = 'ssd_mobilenet_v1_coco_2017_11_17'
MODEL_FILE = MODEL_NAME + '.tar.gz'
DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'

try:
    opener = urllib.request.URLopener()
    opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
    print("downloading model complete")
except:

    print("Error downloading model")
    sys.exit(1)
