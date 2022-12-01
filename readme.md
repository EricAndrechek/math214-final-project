# UMich Math 214: Linear Algebra

## Fall 2022 Final Project

### Setup

To test this code out, run the following commands in your terminal:

```console
git clone https://github.com/EricAndrechek/math214-final-project.git
cd math214-final-project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Usage

To run the code, run the following command in your terminal:

```console
python3 compress.py
```

This will prompt you to enter the name of any files you want to try compressing (they must be stored in the same local directory), as well as the number of singular values you want to keep.

Alternatively, you can run it with the following command:

```console
python3 compress.py <filename> <k>
```

Where `<filename>` is the name of the file you want to compress and `<k>` is the number of singular values you want to keep.

The compressed file will be stored in the same directory as `compressed-<k>-<filename>`
