File Sorter
A simple Python script that organizes files into folders by type.
How it works
The script scans a directory and moves files into categorized subfolders based on their extension.
FolderFile typesImages.jpg .png .jpeg .webp .heic .avif .svgVideo.mp4 .webmDocs.pdf .docx .xlsx .txtAudio.mp3Archives.zip .7z .gz .tar .xzApps.dmg .pkg .appWeb.htm .html
Setup

Clone the repo:

bashgit clone https://github.com/nizar223/filesorter-.git
cd filesorter-

Set your target folder path in sorter.py:

pythonpath = Path("/your/path/here")

Run:

bashpython sorter.py
Files

sorter.py — main script that sorts files
config.py — file extension categories (easy to customize)

Customize
Add or change categories in config.py:
pythonEXTENSIONS = {
    "Images": [".jpg", ".png", ".jpeg"],
    "MyCustomFolder": [".xyz", ".abc"],
}
Requirements

Python 3.6+
No external dependencies
