---
title: "REFACTOR: Remove duplicate Python files in basics directory"
labels: ["refactor", "cleanup", "good first issue"]
assignees: []
---

## Refactoring Issue

Many directories in `basics/` contain duplicate files - the same code exists in both numbered files (e.g., `01_hello_world.py`) and descriptive names (e.g., `hello_world_first.py`).

## Current State

Example from `basics/01_introduction/`:
```
01_hello_world.py
hello_world_first.py          # Duplicate of 01_hello_world.py
02_user_input_addition.py
user_input_addition.py        # Duplicate of 02_user_input_addition.py
```

This pattern exists across most directories:

| Directory | Numbered Files | Named Files | Duplicates |
|-----------|---------------|-------------|------------|
| 01_introduction | 2 | 2 | 2 |
| 02_variables_types | 13 | 13 | 13 |
| 03_control_flow | 10 | 10 | 10 |
| 04_functions | 11 | 11 | 11 |
| 05_data_structures | 21 | 21 | 21 |
| 06_strings | 8 | 8 | 8 |
| 07_file_handling | 13 | 13 | 13 |
| 08_oop | 15 | 15 | 15 |
| 10_advanced | 11 | 11 | 11 |
| 11_projects | 6 | 6 | 6 |

**Total: ~110 duplicate files**

## Problems

- Confusing for learners (which file to run?)
- Harder to maintain (fix bug in two places)
- Bloated repository
- Inconsistent updates (one file updated, other not)

## Solution

Keep only the numbered files and remove duplicates.

### Naming Convention

Numbered files are better because:
- Clear learning order
- Easy to reference in documentation
- Consistent with README structure
- Standard in educational content

## Implementation

### Script to Identify Duplicates

```python
# scripts/find_duplicates.py
import os
from pathlib import Path
from difflib import SequenceMatcher

def find_duplicates(directory):
    files = list(Path(directory).glob("*.py"))
    duplicates = []
    
    for i, file1 in enumerate(files):
        for file2 in files[i+1:]:
            if file1.name == file2.name:
                continue
            
            with open(file1) as f1, open(file2) as f2:
                content1 = f1.read()
                content2 = f2.read()
                
                similarity = SequenceMatcher(None, content1, content2).ratio()
                if similarity > 0.95:  # 95% similar
                    duplicates.append((file1, file2, similarity))
    
    return duplicates
```

### Files to Delete

Keep files matching pattern `NN_*.py`, delete others:

```bash
# Example for 01_introduction
cd basics/01_introduction
rm hello_world_first.py
rm user_input_addition.py

# Repeat for all directories
```

### Update References

Check and update any references to deleted files in:
- README files
- Comments in other files
- Documentation

## Verification

After cleanup:
```bash
# Count Python files
find basics -name "*.py" | wc -l
# Should be ~110 (down from ~220)

# Verify no duplicates
python scripts/find_duplicates.py basics/
```

## Files to Modify

- [ ] All `basics/*/` directories (remove duplicates)
- [ ] `basics/README.md` (verify file counts)
- [ ] Create cleanup script (optional)

## Benefits

- ✅ Clearer structure for learners
- ✅ Easier maintenance
- ✅ Smaller repository
- ✅ Consistent with documentation
