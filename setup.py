from setuptools import find_packages, setup

setup(
    name="tfrecorder",
    version="0.0.1",
    description="Covert CSV, TSV files to TFRecord and upload to Google Cloud Storage automatically",
    install_requires=["tensorflow==2.1.0", "tqdm"],
    entry_points={"console_scripts": ["tfr=tfrecorder.entrypoint:main"]},
    url="https://github.com/harrydrippin/tfrecorder.git",
    author="Seunghwan Hong",
    author_email="harrydrippin@gmail.com",
    packages=find_packages(exclude=["tests"]),
)
