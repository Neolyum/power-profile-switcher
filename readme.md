# Power Profile Switcher

On my system, the fans keep running nonstop unless it’s in power-saving mode. But using power-saving mode makes gaming and other tasks difficult, which means I have to go into the settings app, navigate around, grumble, and change it each time. It’s a lot of hassle for something I need to adjust frequently, so here’s…
A lightweight Python-based system tray application for managing power profiles on Windows. This tool allows users to quickly switch between power plans, such as "Power Saver," "Balanced," and "High Performance," directly from the system tray. It uses Windows' `powercfg` command to list and switch between power profiles.

## Features

- **Easy Access via System Tray**: Quickly change between power profiles directly from a tray icon.
- **Automatic Detection of Profiles**: Dynamically detects available power profiles and highlights the currently active one.
- **Icon Customization**: Choose custom icons for each power profile, displayed dynamically based on the active profile.

## Prerequisites

- **Windows 10/11**
- **Python 3.6+**
- **Dependencies**:
  - `pystray`: For system tray icon functionality. Install via pip:
    ```bash
    pip install pystray
    ```
  - `Pillow`: For handling image icons. Install via pip:
    ```bash
    pip install pillow
    ```

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/neolyum/power-profile-switcher.git
   cd power-profile-switcher
   ```

2. **Run the Script**:
   ```bash
   pythonw power_profile_switcher.py
   ```

## Usage

- **System Tray Menu**: The application appears as an icon in the Windows system tray. Right-click the icon to open the menu and select a power profile.
- **Power Profiles**: Automatically detects the power profiles available on your system and shows the current active profile.
- **Exit**: Select "Quit" from the menu to close the application.

## Known Issues

- **Administrator Access**: On some systems, `powercfg` commands may require elevated privileges. If you encounter issues, try running Python as an administrator.
- **Compatibility**: This tool is designed for Windows and relies on the `powercfg` command, which may behave differently across Windows versions.
- **The icon**: This icon was made by me in 5 minutes, including the search for the pictures. Hence.. well, it's not beautiful
- **Linux compatibility** should be easy, when changing the tool to a linux one and do the parsing accordingly



## automated startup in windows

### Method 1: Create a Shortcut in the Startup Folder

1. **Locate the Startup Folder**:
   - Press `Win + R` to open the Run dialog.
   - Type `shell:startup` and press `Enter`. This opens the Startup folder where you can place any shortcuts or applications to run on startup.

2. **Create a Shortcut to Your Python Script**:
   - Right-click inside the Startup folder and select **New > Shortcut**.
   - For the shortcut target, enter the path to `python.exe` followed by the full path to your script, like so:
     ```plaintext
     "C:\Path\To\Python\pythonw.exe" "C:\Path\To\Script\power_profile_switcher.py"
     ```
     Adjust the paths as needed based on the location of `pythonw.exe` and your script.
     Also set this script to run in the folder of the python file.

   - Click **Next**, give the shortcut a name (e.g., "Power Profile Switcher"), and click **Finish**.

3. **Test**: Restart your computer or log out and log back in to ensure the application launches on startup.

### Method 2: Use a `.bat` File in the Startup Folder

If you find that using a shortcut does not work as expected, you can create a `.bat` (batch) file to run your script.

1. **Create a Batch File**:
   - Open a text editor like Notepad.
   - Enter the following command in the file, replacing paths as necessary:
     ```plaintext
     "C:\Path\To\Python\pythonw.exe" "C:\Path\To\Script\power_profile_switcher.py"
     ```
   - Save the file with a `.bat` extension, for example, `run_power_switcher.bat`.

2. **Place the `.bat` File in the Startup Folder**:
   - Move the `.bat` file into the Startup folder (as explained in Method 1).
   - Test by restarting your computer or logging out and logging back in.


## attributions
The scale, which is the base of the icon, is from [JoyPixels](https://creazilla.com/de/media/emoji/46036/waage), Creative Commons Attribution 4.0 (CC BY 4.0)
