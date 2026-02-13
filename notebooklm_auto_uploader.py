import os
import time
import subprocess
import math
import shutil
import random

# ================= CONFIGURATION =================

# 1. Path to your video folder
#    IMPORTANT: Change this to your local path before running!
VIDEO_FOLDER = "/path/to/your/video/folder" 

# 2. Your Notebook ID
#    IMPORTANT: Change this to your specific notebook ID!
#    (Keep the quotes, replace with the ID from the end of your NotebookLM URL)
NOTEBOOK_ID = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

# 3. Batch size (Number of videos to upload per batch)
#    Recommendation: Keep it under 3 to avoid rate limits.
BATCH_SIZE = 1

# 4. Cooldown range in seconds (Min, Max)
#    Random sleep between batches to mimic human behavior.
COOLDOWN_MIN = 10
COOLDOWN_MAX = 60

# ===============================================

def main():
    # Check if the folder exists
    if not os.path.exists(VIDEO_FOLDER):
        print(f"❌ Error: Folder not found: {VIDEO_FOLDER}")
        print("💡 Hint: Please update the 'VIDEO_FOLDER' path in the script.")
        return

    # Create a sub-folder for archiving uploaded files
    done_folder = os.path.join(VIDEO_FOLDER, "uploaded")
    if not os.path.exists(done_folder):
        os.makedirs(done_folder)

    # Get all MP4 files
    all_files = [f for f in os.listdir(VIDEO_FOLDER) if f.lower().endswith(".mp4")]
    all_files.sort()
    
    total_files = len(all_files)
    if total_files == 0:
        print(f"🎉 No MP4 files found. All tasks completed!")
        return

    print(f"✅ Found {total_files} videos to upload.")
    print(f"📦 Strategy: {BATCH_SIZE} videos per batch. Sleep {COOLDOWN_MIN}-{COOLDOWN_MAX}s between batches.\n")

    # Process in batches
    for i in range(0, total_files, BATCH_SIZE):
        current_batch = all_files[i : i + BATCH_SIZE]
        batch_num = (i // BATCH_SIZE) + 1
        total_batches = math.ceil(total_files / BATCH_SIZE)
        
        print(f"🚀 [Batch {batch_num}/{total_batches}] Processing...")

        files_uploaded_in_this_batch = 0

        for filename in current_batch:
            file_path = os.path.join(VIDEO_FOLDER, filename)
            
            # Double check if file exists
            if not os.path.exists(file_path):
                continue

            print(f"   Uploading: {filename} ...", end="", flush=True)
            
            try:
                # Call the notebooklm CLI
                cmd = [
                    "notebooklm", "source", "add", 
                    file_path, "--notebook", NOTEBOOK_ID
                ]
                
                result = subprocess.run(cmd, capture_output=True, text=True)
                
                if result.returncode == 0:
                    print(" ✅ Success -> Archiving")
                    # Move the uploaded file to the 'uploaded' folder
                    shutil.move(file_path, os.path.join(done_folder, filename))
                    files_uploaded_in_this_batch += 1
                else:
                    print(f" ❌ Failed")
                    print(f"      Error Details: {result.stderr.strip()}")
            except Exception as e:
                print(f" ❌ Script Error: {e}")

        # Logic: Only sleep if there are more files to process
        if i + BATCH_SIZE < total_files:
            sleep_time = random.randint(COOLDOWN_MIN, COOLDOWN_MAX)
            print(f"☕️ Batch complete. Sleeping for {sleep_time}s (Anti-bot protection)...")
            time.sleep(sleep_time)
        else:
            print("\n🎉 All uploads completed!")

if __name__ == "__main__":
    main()
