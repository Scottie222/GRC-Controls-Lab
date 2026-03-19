import sys
import os

# Add the root directory to Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Add the Scripts directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'Scripts')))
```

If it looks like that ✅ → go to **Actions** tab and wait for the new run

---

## Also still need `Scripts/tests/__init__.py`

1. Click **"Add file"** → **"Create new file"**
2. Type in name box:
```
Scripts/tests/__init__.py
