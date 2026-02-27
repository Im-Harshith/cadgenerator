# AI-Assisted CAD Prompt Generator

**VNR College Hakathon - Challenge 3**  
**Vector Technics Private Limited**

A simple Streamlit application that converts natural-language engineering instructions into OpenSCAD code using a local Llama LLM via Ollama.

## 🎯 Project Overview

This tool allows engineers and CAD users to describe mechanical components in plain English and receive ready-to-use OpenSCAD code. It leverages local LLM inference for privacy and offline capability.

**Example:**
- **Input:** "Create a 120 mm long shaft with a 20 mm diameter and add a 4 mm keyway"
- **Output:** Clean, executable OpenSCAD code

## 📋 Prerequisites

Before running this application, ensure you have the following installed:

1. **Python 3.10 or higher**
   - Download from [python.org](https://www.python.org/downloads/)

2. **Ollama** (for local LLM inference)
   - Download from [ollama.ai](https://ollama.ai/)
   - Install and verify: `ollama --version`

3. **Llama Model** (via Ollama)
   - After installing Ollama, pull a Llama model:
   ```bash
   ollama pull llama3.2
   ```
   - Or use another variant: `llama3.1`, `llama2`

4. **OpenSCAD** (optional, for testing generated code)
   - Download from [openscad.org](https://openscad.org/)

## 🚀 Installation

### Step 1: Clone or Download the Project

Navigate to the project directory:


### Step 2: Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the virtual environment:
```bash
# Windows
.\venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Verify Ollama is Running

Make sure the Ollama service is running:
```bash
ollama serve
```

In another terminal, verify your model is available:
```bash
ollama list
```

You should see your Llama model listed (e.g., `llama3.2`).

## 🎮 Usage

### Running the Application

1. Make sure Ollama is running (see Step 4 above)

2. Start the Streamlit app:
```bash
streamlit run app.py
```

3. Your default browser should open automatically to `http://localhost:8501`

### Using the Application

1. **Configure the Model** (Sidebar)
   - Select your installed Llama model from the dropdown

2. **Customize System Prompt** (Sidebar, Optional)
   - Modify the system prompt to guide the LLM's behavior
   - Click "Reset to Default Prompt" to restore defaults

3. **Enter Your Instruction** (Left Column)
   - Type your engineering instruction in natural language
   - Or select an example from the dropdown

4. **Generate Code** (Left Column)
   - Click "🚀 Generate OpenSCAD Code"
   - Wait for the LLM to process your request

5. **View and Use Output** (Right Column)
   - Review the generated OpenSCAD code
   - Click "📋 Copy to Clipboard" to copy the code
   - Click "💾 Download .scad" to save as a file
   - Expand "🔍 View Full LLM Response" to see the complete LLM output

### Testing Generated Code

1. Copy the generated OpenSCAD code
2. Open OpenSCAD application
3. Paste the code into the editor
4. Press F5 to preview the 3D model
5. Press F6 to render the final model

## 📝 Example Prompts

See [examples.txt](examples.txt) for a comprehensive list of example prompts, including:

- Basic shapes (cube, cylinder, sphere)
- Mechanical components (shafts, plates, brackets)
- Complex shapes (hollow cylinders, filleted boxes, gears)
- Multi-part assemblies (hinges, connectors, clamps)

## 🛠️ Troubleshooting

### Issue: "Error calling Ollama"

**Solution:**
- Ensure Ollama is running: `ollama serve`
- Verify the model is installed: `ollama list`
- Pull the model if missing: `ollama pull llama3.2`

### Issue: "Model not found"

**Solution:**
- Check available models: `ollama list`
- Update the model selection in the Streamlit sidebar
- Pull the required model: `ollama pull <model-name>`

### Issue: Generated code doesn't compile in OpenSCAD

**Solution:**
- Try refining your prompt to be more specific
- Adjust the system prompt to emphasize syntax correctness
- Use a different Llama model (e.g., try `llama3.1` instead of `llama3.2`)
- Manually review and fix minor syntax issues

### Issue: Streamlit app won't start

**Solution:**
- Verify Python version: `python --version` (should be 3.10+)
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`
- Check for port conflicts (default is 8501)

## 🏗️ Project Structure

```
cad-prompt-generator/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── examples.txt       # Example prompts
```

## 🎓 Architecture

- **Frontend:** Streamlit (local web interface)
- **LLM:** Local Llama via Ollama
- **Output:** OpenSCAD code
- **Simplicity:** Single-file application with user-configurable prompts

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Ollama Documentation](https://github.com/ollama/ollama)
- [OpenSCAD Documentation](https://openscad.org/documentation.html)
- [Llama Models](https://ollama.ai/library/llama3.2)

## 🤝 Contributing

This is a hackathon project. Feel free to extend it with:
- Additional CAD platforms (FreeCAD, Onshape)
- Validation and error checking
- 3D preview integration
- More sophisticated prompt engineering
- Fine-tuned models for CAD generation


---

**Built with ❤️ using Streamlit + Ollama + Llama**
