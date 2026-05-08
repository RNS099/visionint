```text
██╗   ██╗██╗███████╗██╗ ██████╗ ███╗   ██╗██╗███╗   ██╗████████╗
██║   ██║██║██╔════╝██║██╔═══██╗████╗  ██║██║████╗  ██║╚══██╔══╝
██║   ██║██║███████╗██║██║   ██║██╔██╗ ██║██║██╔██╗ ██║   ██║
╚██╗ ██╔╝██║╚════██║██║██║   ██║██║╚██╗██║██║██║╚██╗██║   ██║
 ╚████╔╝ ██║███████║██║╚██████╔╝██║ ╚████║██║██║ ╚████║   ██║
  ╚═══╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝   ╚═╝

              Visual Intelligence Toolkit
```
<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

## Overview

VisionInt is a command-line based Image OSINT (Open Source Intelligence) tool designed for investigators, cybersecurity enthusiasts, and digital forensics learners.

The tool helps analyze images by extracting:
- EXIF metadata
- GPS coordinates
- Embedded text using OCR
- Reverse image search results

It is built for educational and lawful OSINT investigations.

---

## Features

- Metadata extraction from images
- GPS coordinate extraction from EXIF
- OCR text extraction using Tesseract
- Reverse image searching
- Clean terminal UI with colored output
- Lightweight and modular structure
- Docker support

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/visionint.git
cd visionint
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

# Tesseract OCR Setup

VisionInt automatically detects the Tesseract OCR executable from your system PATH.

No manual configuration is required if Tesseract is installed correctly.

---

## Windows

### Download Tesseract

https://github.com/UB-Mannheim/tesseract/wiki

### Install It

Install Tesseract using the installer.

### Verify Installation

```powershell
tesseract --version
```

If the command works, VisionInt will automatically detect Tesseract.

---

## Linux

### Install Tesseract

```bash
sudo apt install tesseract-ocr
```

### Verify Installation

```bash
tesseract --version
```

---

## Optional: Custom Tesseract Path

If automatic detection fails, you can manually configure the path:

```python
configure_tesseract(
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
```

---

# Usage

## Basic Scan

```bash
python main.py image.jpg
```

---

## Extract exif metadata

```bash
python main.py image.jpg --exif
```

---

## Extract OCR Text

```bash
python main.py image.jpg --ocr
```

---

## Reverse Image Search

```bash
python main.py image.jpg --rsearch
```

---

## Full Scan

```bash
python main.py image.jpg 
```

# Requirements

- Python 3.x
- Tesseract OCR
- Internet connection (for reverse image search)

---

# Technologies Used

- Python
- Pillow
- pytesseract
- requests
- exif
- colorama
- Docker

---

# Legal Disclaimer

This project is intended strictly for:

- Educational purposes
- Ethical cybersecurity learning
- Lawful OSINT investigations

The user is solely responsible for complying with applicable laws and regulations.

---

# Future Improvements

- Face detection
- Geolocation mapping
- AI-based object detection
- Multi-engine reverse search
- Report generation
- GUI version


# License

This project is licensed under the MIT License.

---

# Author

Developed by **Rapaka Naga Sai**

**Cybersecurity • OSINT • Digital Forensics**
