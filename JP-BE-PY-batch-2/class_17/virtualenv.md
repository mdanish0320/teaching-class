## Activating a Virtual Environment on Windows and macOS

### For Windows:

1. **Open PowerShell as Administrator**:
   - Right-click on the Start menu and select "Windows PowerShell (Admin)".
   - Run the following command to allow the execution of scripts:
     ```sh
     Set-ExecutionPolicy Unrestricted
     ```

2. **Create a Virtual Environment**:
   - Open your project directory and then open the integrated terminal in your code editor (e.g., VS Code).
   - Run the following command to create a virtual environment:
     ```sh
     python -m venv venv
     ```
   - You will see a new folder named `venv` created in your project directory.

3. **Activate the Virtual Environment**:
   - Run the following command in the terminal:
     ```sh
     venv\Scripts\activate
     ```

### For macOS:

1. **Open Terminal**:
   - Press `Cmd + Space`, type "Terminal", and hit Enter.

2. **Create a Virtual Environment**:
   - Navigate to your project directory in the terminal.
   - Run the following command to create a virtual environment:
     ```sh
     python3 -m venv venv
     ```
   - A new folder named `venv` will appear in your project directory.

3. **Activate the Virtual Environment**:
   - Run the following command in the terminal:
     ```sh
     source venv/bin/activate
     ```

### Deactivating the Virtual Environment:

- For both Windows and macOS, to deactivate the virtual environment, simply run:
  ```sh
  deactivate
