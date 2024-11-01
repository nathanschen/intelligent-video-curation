# intelligent-video-curation
Flawless + DataRes Project Fall

# Development Guide

## Structure
Four stages:

0. Reading in arguments
1. Preprocessing
2. Filtering
3. Outputting

## First time setup

Step 0: install ffmpeg

Step 1: Set up an environment with the requisite Python version

This is one suggested way to do it. You'll need conda installed. You can do it another way, such as having python 3.10 installed and pointing poetry to the executable with: `poetry env use <python exe path>`

`conda create -n py310 python=3.10`
`conda deactivate; conda activate py310`
Get the python path: `where python` if you're on windows, `which python` if you're on linux. copy the path.
`poetry env use <path>`

Step 2: setup poetry environment

This command creates a virtual environment to install all related python packages (you can view them in pyproject.toml)

`poetry install`

This command activates the virtual environment with all the installed packages. Make sure to call this before running anything.

`poetry shell`

This installs some linters, formatters, etc. that will automatically run when you git commit.
`pre-commit install`

Step 3: Try it out!

Run the full pipeline:
- Make sure to create a copy of config.yaml and modify the input directory to your own directory of MP4s
- The results will output in results/ folder.
`python -m intelligent_video_curation.main --config ".\sample_configs\config.yaml"`

## Development Tips

As you're likely working with developing individual filtering components, please see this file to understand how filtering components will fit in the pipeline.
`intelligent_video_curation\filters\dummy\dummy_filter.py`

the next time you're working on this, just do
`conda deactivate; conda activate py310`
`poetry shell`
& run any python programs

if you want to step through your code and inspect it a-la CS 33 gdb, then try pdb :)
`import pdb; pdb.set_trace()`

## todo/wishlist

the code is close to parallelizable on video objects. try multiprocessing

in the future, dynamically determine which filters (not all of them!) to apply.
