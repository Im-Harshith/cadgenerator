# 🚀 Quick Start Guide

## What You Need to Do

### 1️⃣ Install Prerequisites (One-Time Setup)

#### Install Ollama
1. Go to [https://ollama.ai/download](https://ollama.ai/download)
2. Download and install Ollama for Windows
3. Verify installation by opening PowerShell and running:
   ```powershell
   ollama --version
   ```

#### Pull Llama Model
After installing Ollama, download the Llama model:
```powershell
ollama pull llama3.2
```
This will download ~2GB of data and may take a few minutes.

---

### 2️⃣ Run the Automated Setup

Open PowerShell in the project directory and run:
```powershell
.\setup.ps1
```

This script will:
- ✅ Check Python installation
- ✅ Check Ollama installation
- ✅ Verify Llama model is available
- ✅ Create Python virtual environment
- ✅ Install all dependencies

---

### 3️⃣ Run the Application

After setup is complete, simply run:
```powershell
.\run.ps1
```

Or manually:
```powershell
.\venv\Scripts\Activate.ps1
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 🎮 Using the App

1. **Select Model** - Choose your Llama model from the sidebar (default: llama3.2)
2. **Enter Instruction** - Type your engineering description or select an example
3. **Generate Code** - Click the "Generate OpenSCAD Code" button
4. **Copy/Download** - Use the buttons to copy or download the generated code
5. **Test in OpenSCAD** - Paste the code into OpenSCAD to see your 3D model

---

## 🧪 Testing Your Setup

Try this example prompt:
```
Create a 120 mm long shaft with a 20 mm diameter and add a 4 mm keyway
```

Expected result: Valid OpenSCAD code that creates a cylindrical shaft with a keyway slot.

---

## ⚠️ Troubleshooting

### "Ollama not found"
- Install Ollama from [ollama.ai](https://ollama.ai/download)
- Restart PowerShell after installation

### "Model not found"
- Run: `ollama pull llama3.2`
- Wait for download to complete

### "Ollama service not running"
- Run: `ollama serve` in a separate PowerShell window
- Or the run.ps1 script will start it automatically

### Generated code has errors
- Try a more specific prompt
- Use a different model (llama3.1 instead of llama3.2)
- Adjust the system prompt in the sidebar

---

## 📁 Project Files

- `app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `setup.ps1` - Automated setup script
- `run.ps1` - Quick run script
- `examples.txt` - Example prompts
- `README.md` - Full documentation

---

## 🎯 Next Steps

1. Run `.\setup.ps1` to set up the environment
2. Run `.\run.ps1` to start the app
3. Try the example prompts
4. Experiment with your own engineering descriptions
5. Test generated code in OpenSCAD (optional)

---

**Need help?** Check the full [README.md](README.md) for detailed documentation.
