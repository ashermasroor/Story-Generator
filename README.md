# Story Generator

This repository provides a setup guide for running a locally hosted LLM-powered story generator using `text-generation-webui` and `FastAPI`. Follow the instructions below to set up the environment, backend, and frontend.

## LLM Setup

To run the LLM locally, follow these steps:

1. **Download text-generation-webui:**
   ```sh
   git clone https://github.com/oobabooga/text-generation-webui
   ```
2. **Navigate to the directory:**
   ```sh
   cd text-generation-webui
   ```
3. **Modify `CMD_FLAGS.txt`:**
   ```sh
   sudo nano CMD_FLAGS.txt
   ```
   Replace the content with:
   ```sh
   # Only used by the one-click installer.
   # Example:
   --listen --api --extensions openai --trust-remote-code
   ```
4. **Run `text-generation-webui`**
5. **Download the LLM Model:**
   - Navigate to the "Models" tab.
   - In the "Download model or LoRA" section, paste:
     ```
     microsoft/Phi-3.5-mini-instruct
     ```
   - Click "Download" to install the model locally.
6. **Select the model from the dropdown.**
7. **Adjust settings as needed. My Settings:**

    <img src="https://github.com/user-attachments/assets/01750826-e69d-4341-b10e-a286e3a70646" alt="TextGen-Settings-Image" width="300" >

9. **Load the Model!**

## Backend Setup

1. **Navigate to the backend directory:**
   ```sh
   cd <your-directory>/Story-Generator/
   ```
2. **(Optional) Create a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Navigate back to the root directory:**
   ```sh
   cd ..
   ```
5. **Run the backend:**
   - For development:
     ```sh
     fastapi dev Story-Generator
     ```
   - For deployment:
     ```sh
     fastapi run Story-Generator
     ```
   - For a custom port:
     ```sh
     fastapi dev/run Story-Generator --port <port>
     ```

   The backend should now be running on **port 8000** or the chosen port.

## Frontend Setup

1. **Navigate to the frontend directory:**
   ```sh
   cd <your-directory>/Story-Generator/
   ```
2. **Start a Web Server:**
   - For **Python 3.x**:
     ```sh
     python -m http.server <port>
     ```
   - For **Python 2.x**:
     ```sh
     python -m SimpleHTTPServer <port>
     ```
3. **Access the Frontend:**
   - Open a browser and navigate to:
     ```
     localhost:<port>
     ```

Your Story Generator is now up and running!
