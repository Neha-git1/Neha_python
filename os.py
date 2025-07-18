import os

# Print the current working directory
print("Current Working Directory:", os.getcwd())

# List files and directories in the current directory
print("\nDirectory Contents:")
for item in os.listdir():
    print(" -", item)

# Create a new directory (if it doesn't already exist)
new_dir = "demo_folder"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"\nCreated directory: {new_dir}")
else:
    print(f"\nDirectory already exists: {new_dir}")

# Rename the directory
renamed_dir = "renamed_folder"
if os.path.exists(new_dir):
    os.rename(new_dir, renamed_dir)
    print(f"Renamed '{new_dir}' to '{renamed_dir}'")

# Remove the renamed directory
if os.path.exists(renamed_dir):
    os.rmdir(renamed_dir)
    print(f"Removed directory: {renamed_dir}")
