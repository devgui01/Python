---
title: "BUG: File handling example references non-existent file in basics/07_file_handling/01_file_handling_basics.py"
labels: ["bug", "good first issue"]
assignees: []
---

## Bug Description

The file handling basics example tries to read `newfile.txt` which doesn't exist, causing a `FileNotFoundError` when beginners run the code.

## Problem

```python
# Read a File
with open("newfile.txt", "r") as f:
    data = f.read()
    print(data, type(data))
```

The file is created later in the script, but the read attempt happens first.

## Expected Behavior

The example should either:
1. Create the file first, then read it
2. Handle the FileNotFoundError gracefully
3. Use a file that already exists

## Current Behavior

Running the script raises:
```
FileNotFoundError: [Errno 2] No such file or directory: 'newfile.txt'
```

## Files Affected

- `basics/07_file_handling/01_file_handling_basics.py`

## Suggested Fix

Reorder the operations to write first, then read:

```python
# Write a File first
with open("newfile.txt", "w") as f:
    f.write("This is the New File.\nReads one line at a time from the file.")

# Then read it
with open("newfile.txt", "r") as f:
    data = f.read()
    print(data, type(data))
```

Or add error handling:

```python
try:
    with open("newfile.txt", "r") as f:
        data = f.read()
        print(data, type(data))
except FileNotFoundError:
    print("File doesn't exist yet. Creating it...")
    # Create the file
```

## How to Test

1. Delete `newfile.txt` if it exists
2. Run `python 01_file_handling_basics.py`
3. Should not raise an error
