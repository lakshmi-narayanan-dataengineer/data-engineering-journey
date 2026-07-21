# ==========================================
# 1. Reading a File ('r')
# Real-World Use Case: Reading system configuration or user settings
# ==========================================
try:
    with open("config.txt", "r") as file:
        content = file.read()
        print("File Content Loaded:")
        print(content)
except FileNotFoundError:
    print("Error: The file 'config.txt' does not exist yet.")


# ==========================================
# 2. Writing to a File ('w')
# Real-World Use Case: Exporting a report (Overwrites existing file)
# ==========================================
report_data = "Daily Sales Report\nTotal Revenue: $1,250\nStatus: Target Achieved"

with open("daily_report.txt", "w") as file:
    file.write(report_data)

print("Report created successfully.")


# ==========================================
# 3. Appending to a File ('a')
# Real-World Use Case: Maintaining an ongoing system log
# ==========================================
import datetime

# Format: 21 July 2026 at 09:45 PM
timestamp = datetime.datetime.now().strftime("%d %B %Y at %I:%M %p")

log_entry = f"User 'Anu' logged in successfully on {timestamp}.\n"
print(log_entry)
# Output: User 'Anu' logged in successfully on 21 July 2026 at 09:45 PM.

# Mode 'a' attaches the new line to the bottom without deleting past data
with open("system_logs.txt", "a") as file:
    file.write(log_entry)

print("Log entry recorded.")


# ==========================================
# 4. Copying Content Between Files ('r' + 'w')
# Real-World Use Case: Creating a backup copy of a script or file
# ==========================================
source_path = "snippets.py"
backup_path = "snippets_backup.py"

try:
    with open(source_path, "r") as source:
        data = source.read()

    with open(backup_path, "w") as destination:
        destination.write(data)

    print(f"Successfully copied '{source_path}' to '{backup_path}'.")
except FileNotFoundError:
    print(f"Source file '{source_path}' not found. Backup skipped.")


# ==========================================
# 5. Line-by-Line File Processing
# Real-World Use Case: Processing large datasets memory-efficiently
# ==========================================
# Useful when a file is too large to read into memory all at once with read()
with open("daily_report.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"Line {line_number}: {line.strip()}")