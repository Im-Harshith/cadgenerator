import streamlit as st
import ollama
import re

# Page configuration
st.set_page_config(
    page_title="AI CAD Prompt Generator",
    page_icon="🔧",
    layout="wide"
)

# Title and description
st.title("🔧 AI-Assisted CAD Prompt Generator")
st.markdown("Convert natural language engineering instructions into OpenSCAD code using local Llama LLM")

# Sidebar for configuration
st.sidebar.header("⚙️ Configuration")

# Model selection
available_models = ["deepseek-r1:14b", "qwen2.5-coder:7b", "codellama:7b", "llama3.2", "llama3.1", "llama2"]
selected_model = st.sidebar.selectbox(
    "Select Model",
    available_models,
    help="Choose the model installed on your system. Qwen2.5-coder and CodeLlama are faster alternatives."
)

# System prompt configuration
st.sidebar.header("📝 System Prompt")
default_system_prompt = """You are an expert OpenSCAD code generator. Generate ONLY valid, syntactically correct OpenSCAD code.

CRITICAL RULES:
1. Output ONLY OpenSCAD code wrapped in ```openscad blocks
2. NO explanations, NO thinking process, NO markdown outside code blocks
3. Use correct OpenSCAD syntax - semicolons after every statement
4. All dimensions in millimeters

CORRECT EXAMPLES:

Example 1 - Simple Cylinder:
Input: "Create a cylinder 30mm diameter and 100mm height"
```openscad
// Cylinder: 30mm diameter, 100mm height
cylinder(h=100, d=30, $fn=50);
```

Example 2 - Cube:
Input: "Make a cube with 50mm sides"
```openscad
// Cube: 50mm sides
cube([50, 50, 50]);
```

Example 3 - Shaft with Keyway:
Input: "Create a 120mm shaft, 20mm diameter with 4mm keyway"
```openscad
// Shaft with keyway
difference() {
    // Main shaft
    cylinder(h=120, d=20, $fn=50);
    
    // Keyway slot (4mm wide, 2mm deep)
    translate([8, -2, 0])
        cube([4, 4, 120]);
}
```

Example 4 - Plate with Holes:
Input: "Rectangular plate 100x50x5mm with four 6mm corner holes"
```openscad
// Plate with corner holes
difference() {
    // Base plate
    cube([100, 50, 5]);
    
    // Corner holes (10mm from edges)
    translate([10, 10, -1]) cylinder(h=7, d=6, $fn=30);
    translate([90, 10, -1]) cylinder(h=7, d=6, $fn=30);
    translate([10, 40, -1]) cylinder(h=7, d=6, $fn=30);
    translate([90, 40, -1]) cylinder(h=7, d=6, $fn=30);
}
```

Now generate code following these exact patterns. Use proper syntax, semicolons, and $fn for smooth circles."""

system_prompt = st.sidebar.text_area(
    "System Prompt",
    value=default_system_prompt,
    height=300,
    help="Customize the system prompt to guide the LLM's behavior"
)

# Reset button for system prompt
if st.sidebar.button("Reset to Default Prompt"):
    st.rerun()

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📥 Input")
    
    # Example prompts
    st.subheader("Example Prompts")
    examples = [
        "Create a 120 mm long shaft with a 20 mm diameter and add a 4 mm keyway",
        "Make a cube with 50mm sides",
        "Design a cylinder 30mm diameter and 100mm height",
        "Create a rectangular plate 100x50x5 mm with four 6mm holes at the corners"
    ]
    
    selected_example = st.selectbox("Choose an example (optional)", [""] + examples)
    
    # User instruction input
    user_instruction = st.text_area(
        "Enter your engineering instruction",
        value=selected_example if selected_example else "",
        height=200,
        placeholder="e.g., Create a 120 mm long shaft with a 20 mm diameter and add a 4 mm keyway"
    )
    
    # Generate button
    generate_button = st.button("🚀 Generate OpenSCAD Code", type="primary", use_container_width=True)

with col2:
    st.header("📤 Output")
    
    # Placeholder for generated code
    code_placeholder = st.empty()

# Function to call Llama via Ollama with streaming
def call_llama_stream(system_prompt: str, user_prompt: str, model: str, status_container):
    """Call the local Llama model via Ollama with streaming support"""
    try:
        # Configure options based on model
        options = {
            'temperature': 0.7,
        }
        
        # Aggressive speed optimization for DeepSeek models
        if 'deepseek' in model.lower():
            options['num_predict'] = 300  # Very short responses
            options['num_ctx'] = 2048  # Smaller context
            options['top_p'] = 0.95
            options['top_k'] = 50
            options['repeat_penalty'] = 1.1
            # Force it to stop thinking
            options['stop'] = ['<think>', '<thinking>', 'Let me think']
            # Modify prompt to be very direct
            user_prompt = f"Generate ONLY OpenSCAD code. No explanations, no thinking, just code.\n\nTask: {user_prompt}"
            system_prompt = "You are a code generator. Output ONLY OpenSCAD code wrapped in ```openscad blocks. No thinking, no explanations."
        else:
            options['num_predict'] = 500
        
        # Update status
        status_container.info("🔄 Connecting to Ollama service...")
        
        # Call Ollama with streaming
        full_response = ""
        chunk_count = 0
        
        status_container.info(f"🤖 Generating with {model}...")
        
        stream = ollama.chat(
            model=model,
            messages=[
                {
                    'role': 'system',
                    'content': system_prompt
                },
                {
                    'role': 'user',
                    'content': user_prompt
                }
            ],
            options=options,
            stream=True
        )
        
        for chunk in stream:
            chunk_count += 1
            if 'message' in chunk and 'content' in chunk['message']:
                content = chunk['message']['content']
                full_response += content
                
                # Update status every 10 chunks to show progress
                if chunk_count % 10 == 0:
                    tokens_so_far = len(full_response.split())
                    status_container.info(f"✍️ Generating... ({tokens_so_far} tokens, {chunk_count} chunks)")
        
        status_container.success(f"✅ Generation complete! ({len(full_response.split())} tokens)")
        
        return full_response
        
    except ollama.ResponseError as e:
        error_msg = f"❌ Ollama Response Error: {str(e)}\n\nTry:\n1. Check if model is installed: ollama list\n2. Pull the model: ollama pull {model}"
        status_container.error(error_msg)
        return error_msg
    except ConnectionError as e:
        error_msg = f"❌ Connection Error: Cannot connect to Ollama service.\n\nTry:\n1. Check if Ollama is running (it should auto-start)\n2. Restart Ollama service\n3. Check if port 11434 is accessible"
        status_container.error(error_msg)
        return error_msg
    except Exception as e:
        error_msg = f"❌ Error calling Ollama: {str(e)}\n\nModel: {model}\nError Type: {type(e).__name__}"
        status_container.error(error_msg)
        return error_msg

# Function to extract OpenSCAD code from response
def extract_code(response: str) -> str:
    """Extract OpenSCAD code from LLM response"""
    # Try to find code between ```openscad and ```
    pattern = r'```openscad\s*(.*?)\s*```'
    match = re.search(pattern, response, re.DOTALL)
    
    if match:
        return match.group(1).strip()
    
    # Try to find code between ``` and ```
    pattern = r'```\s*(.*?)\s*```'
    match = re.search(pattern, response, re.DOTALL)
    
    if match:
        return match.group(1).strip()
    
    # If no code blocks found, return the entire response
    return response.strip()

# Generate code when button is clicked
if generate_button:
    if not user_instruction.strip():
        st.error("⚠️ Please enter an engineering instruction")
    else:
        # Create a status container for real-time updates
        status_container = st.empty()
        
        # Call Llama with streaming
        response = call_llama_stream(system_prompt, user_instruction, selected_model, status_container)
        
        # Extract code
        generated_code = extract_code(response)
        
        # Store in session state
        st.session_state['generated_code'] = generated_code
        st.session_state['full_response'] = response

# Display generated code
if 'generated_code' in st.session_state:
    with col2:
        st.code(st.session_state['generated_code'], language='openscad')
        
        # Action buttons
        col_copy, col_download = st.columns(2)
        
        with col_copy:
            st.button(
                "📋 Copy to Clipboard",
                help="Copy the generated code",
                use_container_width=True
            )
        
        with col_download:
            st.download_button(
                label="💾 Download .scad",
                data=st.session_state['generated_code'],
                file_name="generated_model.scad",
                mime="text/plain",
                use_container_width=True
            )
        
        # Show full response in expander
        with st.expander("🔍 View Full LLM Response"):
            st.text(st.session_state['full_response'])

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
    <p>VNR College Hakathon - Challenge 3 | Vector Technics Private Limited</p>
    <p>Built with Streamlit + Ollama + Llama</p>
    </div>
    """,
    unsafe_allow_html=True
)
