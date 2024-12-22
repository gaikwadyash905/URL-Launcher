# URL Launcher GUI

This Python project provides a graphical interface to load URLs from a text file and open them in a selected browser. The program dynamically detects installed browsers and allows adding custom browser commands.

## Features
- Load URLs from a `.txt` file (one URL per line).
- Detect installed browsers dynamically.
- Open URLs in the selected browser.
- Add custom browser commands.
- Simple and user-friendly GUI.

## Prerequisites
- Python 3.x
- Installed browsers (e.g., Google Chrome, Mozilla Firefox, etc.)
- Required Python modules: `tkinter`, `webbrowser`, `shutil`

## Installation
1. Clone the repository:
  ```bash
  git clone https://github.com/gaikwadyash905/URL-Launcher.git
  cd tkinter_open_urls
  ```
2. Install required modules:
  ```bash
  pip install -r requirements.txt
  ```

## Usage
1. Run the program:
  ```bash
  python url_launcher.py
  ```

2. Follow these steps:
   - Select a .txt file containing URLs (one URL per line).
   - Choose a browser from the listed options or add a custom browser.
   - Click "Open URLs" to open all URLs in the selected browser.

## Screenshots
![Image 1](screenshots/url_launcher.png "URL Launcher")

![Image 2](screenshots/url_launcher_file_loaded_msg.png "URL Launcher file loaded message")

![Image 3](screenshots/url_launcher_success_msg.png "URL Launcher - All URLs opened message")

![Image 3](screenshots/url_launcher_no_file_error_msg.png "URL Launcher - No file opened message")

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE "Licence file") file for details.

## Contributing
Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
