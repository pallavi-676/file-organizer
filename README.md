# 📂 File Organizer (Python)

A simple and efficient Python script to automatically organize files in your Downloads folder based on file extensions.

---

## 🚀 Features

- 📁 Organizes files by type (Images, Documents, Videos, etc.)
- ⚡ Automatically creates folders if they don't exist
- 🧹 Cleans up messy Downloads directory
- 🧠 Beginner-friendly Python project

---

## 🛠️ Technologies Used

- Python
- os module
- shutil module

---

## 📦 How It Works

The script scans your Downloads folder and moves files into categorized folders based on their extensions.

Example:
- `.jpg` → Images
- `.pdf` → Documents
- `.mp4` → Videos

---
## 📂 Supported File Types

| Category   | Extensions                  |
|------------|----------------------------|
| Images     | .jpg, .png, .jpeg, .gif    |
| Documents  | .pdf, .docx, .txt          |
| Videos     | .mp4, .mkv                 |
| Music      | .mp3, .wav                 |
| Code       | .py, .js, .cpp             |
---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/pallavi-676/file-organizer.git
```

2. Navigate to the project folder:
```bash
cd file-organizer
```

3. Run the script:
```bash
python organizer.py
```

---
## 🖥️ Example Output

Moved: photo.jpg → Images  
Moved: resume.pdf → Documents  
Moved: song.mp3 → Music  

✅ Files organized successfully!
---

## ⚙️ Customization

You can modify file categories inside the script:

```python
FILE_TYPES = {
    "Images": [".jpg", ".png"],
    "Documents": [".pdf", ".docx"]
}
```

---
## ⚠️ Important Note

- This script moves files permanently.
- Make sure to backup important files before running.
---

## 📌 Future Improvements

- GUI version using Tkinter
- Auto-run scheduler (daily cleanup)
- Undo functionality
- Log file tracking
- Drag-and-drop folder selection

---

## 👤 Author

**Pallavi Sarovar**
