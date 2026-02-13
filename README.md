# NotebookLM Videos Auto-Uploader 🚀

An automated Python script to batch upload local MP4 videos to Google NotebookLM.

## Motivation

When uploading a large number of video files (e.g., >10) to Google NotebookLM, users often encounter **upload failures** or **network errors** due to rate limits.

The traditional manual method is inefficient:
* You have to manually select files in small batches.
* You must "babysit" the screen to check for errors.
* If an upload fails, you lose track of progress.

**This tool solves these problems.** It runs in the background, automatically uploading videos in safe batches with random sleep intervals (mimicking human behavior), freeing you from staring at the progress bar.

## Features
* **Batch Upload**: Process videos in groups (default: 1).
* **Anti-Bot Protection**: Randomized cooldowns (10-60s).
* **Auto-Archiving**: Automatically moves uploaded files to an `uploaded` folder.

## Prerequisites
1. **Python 3.13+** (Required)
2. **notebooklm-py**: This script relies on the unofficial API wrapper.

## Installation
1. **Install Python 3.13** (if you haven't already).
2. **Install the required library**:
   ```bash
   # Clone the dependency
   git clone [https://github.com/teng-lin/notebooklm-py.git](https://github.com/teng-lin/notebooklm-py.git)
   cd notebooklm-py
   
   # Install with pip
   pip install .
   playwright install chromium

## Usage
1. Open `notebooklm_auto_uploader.py` and set your `VIDEO_FOLDER` and `NOTEBOOK_ID`.
2. Run: `python3.13 upload_videos.py`
