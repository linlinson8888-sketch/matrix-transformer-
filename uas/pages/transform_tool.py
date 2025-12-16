import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

st.set_page_config(page_title="Transform Tool", page_icon="🎨", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .transform-header {
        background: linear-gradient(90deg, #fa709a 0%, #fee140 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .parameter-box {
        background: #f7fafc;
        padding: 1rem;
        border-radius: 8px;
        border: 2px solid #e2e8f0;
        margin: 0.5rem 0;
    }
    
    .result-metric {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'transformation_history' not in st.session_state:
    st.session_state.transformation_history = []
if 'original_image' not in st.session_state:
    st.session_state.original_image = None
if 'current_image' not in st.session_state:
    st.session_state.current_image = None

st.markdown('<div class="transform-header"><h1>🎨 Image Transformation Tool</h1></div>', unsafe_allow_html=True)

# ========================================
# SIDEBAR - UPLOAD & CONTROLS
# ========================================
with st.sidebar:
    st.header("📤 Upload Image")
    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=["png", "jpg", "jpeg", "bmp"],
        help="Upload an image to start transforming"
    )
    
    if uploaded_file is not None:
        # Load image
        image = Image.open(uploaded_file).convert("RGB")
        img_array = np.array(image)
        
        # Store original if first time
        if st.session_state.original_image is None:
            st.session_state.original_image = img_array.copy()
            st.session_state.current_image = img_array.copy()
        
        st.success("✅ Image loaded successfully!")
        
        # Image info
        st.markdown("### 📊 Image Info")
        st.info(f"""
        **Dimensions:** {img_array.shape[1]} × {img_array.shape[0]} px
        
        **Size:** {uploaded_file.size / 1024:.2f} KB
        
        **Format:** {uploaded_file.type}
        """)
        
        st.markdown("---")
        
        # Reset button
        if st.button("🔄 Reset to Original", use_container_width=True):
            st.session_state.current_image = st.session_state.original_image.copy()
            st.session_state.transformation_history = []
            st.rerun()
    else:
        st.warning("⚠️ Please upload an image to begin")
        st.stop()

# ========================================
# MAIN CONTENT
# ========================================

# Mode selection
mode = st.radio(
    "**Choose Mode:**",
    ["🎯 Single Transformation", "🔗 Multiple Transformations", "🎨 Filters"],
    horizontal=True
)

st.markdown("---")

# ========================================
# MODE 1: SINGLE TRANSFORMATION
# ========================================
if mode == "🎯 Single Transformation":
    st.markdown("### 🎯 Single Transformation Mode")
    st.info("Apply one transformation at a time. Use Multiple Transformations mode to combine effects.")
    
    # Transformation selection
    transform_type = st.selectbox(
        "Select Transformation Type",
        ["Translation", "Scaling", "Rotation", "Shearing", "Reflection"]
    )
    
    st.markdown("---")
    
    # Get current image
    img_array = st.session_state.current_image
    rows, cols = img_array.shape[:2]
    
    # Parameters section
    param_col1, param_col2 = st.columns([1, 2])
    
    with param_col1:
        st.markdown('<div class="parameter-box">', unsafe_allow_html=True)
        st.markdown("#### ⚙️ Parameters")
        
        if transform_type == "Translation":
            tx = st.slider("Translate X (pixels)", -cols, cols, 0, step=10, 
                          help="Positive = right, Negative = left")
            ty = st.slider("Translate Y (pixels)", -rows, rows, 0, step=10,
                          help="Positive = down, Negative = up")
            
            # Create matrix
            M = np.float32([[1, 0, tx], [0, 1, ty]])
            transformed = cv2.warpAffine(img_array, M, (cols, rows))
            
            # Display matrix
            st.markdown("**Matrix:**")
            st.latex(f"""
            M = \\begin{{bmatrix}}
            1 & 0 & {tx} \\\\
            0 & 1 & {ty}
            \\end{{bmatrix}}
            """)
            
        elif transform_type == "Scaling":
            scale_mode = st.radio("Scaling Mode", ["Uniform", "Non-uniform"])
            
            if scale_mode == "Uniform":
                scale = st.slider("Scale Factor", 0.1, 3.0, 1.0, 0.1,
                                help="1.0 = original size")
                sx = sy = scale
            else:
                sx = st.slider("Scale X", 0.1, 3.0, 1.0, 0.1)
                sy = st.slider("Scale Y", 0.1, 3.0, 1.0, 0.1)
            
            M = np.float32([[sx, 0, 0], [0, sy, 0]])
            new_cols = int(cols * sx)
            new_rows = int(rows * sy)
            transformed = cv2.warpAffine(img_array, M, (new_cols, new_rows))
            
            st.markdown("**Matrix:**")
            st.latex(f"""
            M = \\begin{{bmatrix}}
            {sx:.2f} & 0 & 0 \\\\
            0 & {sy:.2f} & 0
            \\end{{bmatrix}}
            """)
            
        elif transform_type == "Rotation":
            angle = st.slider("Rotation Angle (degrees)", -180, 180, 0, step=5,
                            help="Positive = counter-clockwise")
            
            rotation_center = st.radio("Rotation Center", ["Image Center", "Origin (0,0)"])
            
            if rotation_center == "Image Center":
                center = (cols / 2, rows / 2)
            else:
                center = (0, 0)
            
            scale_rot = st.slider("Scale", 0.1, 2.0, 1.0, 0.1,
                                help="Scale during rotation")
            
            M = cv2.getRotationMatrix2D(center, angle, scale_rot)
            transformed = cv2.warpAffine(img_array, M, (cols, rows))
            
            theta_rad = np.radians(angle)
            st.markdown("**Matrix:**")
            st.latex(f"""
            M = \\begin{{bmatrix}}
            {np.cos(theta_rad)*scale_rot:.3f} & {-np.sin(theta_rad)*scale_rot:.3f} & {M[0,2]:.1f} \\\\
            {np.sin(theta_rad)*scale_rot:.3f} & {np.cos(theta_rad)*scale_rot:.3f} & {M[1,2]:.1f}
            \\end{{bmatrix}}
            """)
            
        elif transform_type == "Shearing":
            shear_axis = st.radio("Shear Direction", ["X-axis (horizontal)", "Y-axis (vertical)"])
            shear_factor = st.slider("Shear Factor", -1.0, 1.0, 0.0, 0.1,
                                    help="Amount of shearing")
            
            if shear_axis == "X-axis (horizontal)":
                M = np.float32([[1, shear_factor, 0], [0, 1, 0]])
                new_cols = int(cols + abs(shear_factor) * rows)
                transformed = cv2.warpAffine(img_array, M, (new_cols, rows))
                
                st.markdown("**Matrix:**")
                st.latex(f"""
                M = \\begin{{bmatrix}}
                1 & {shear_factor:.2f} & 0 \\\\
                0 & 1 & 0
                \\end{{bmatrix}}
                """)
            else:
                M = np.float32([[1, 0, 0], [shear_factor, 1, 0]])
                new_rows = int(rows + abs(shear_factor) * cols)
                transformed = cv2.warpAffine(img_array, M, (cols, new_rows))
                
                st.markdown("**Matrix:**")
                st.latex(f"""
                M = \\begin{{bmatrix}}
                1 & 0 & 0 \\\\
                {shear_factor:.2f} & 1 & 0
                \\end{{bmatrix}}
                """)
                
        else:  # Reflection
            reflection_axis = st.radio(
                "Reflection Axis",
                ["Vertical (flip left-right)", "Horizontal (flip up-down)", "Both axes"]
            )
            
            if reflection_axis == "Vertical (flip left-right)":
                M = np.float32([[-1, 0, cols], [0, 1, 0]])
                st.markdown("**Matrix:**")
                st.latex(f"""
                M = \\begin{{bmatrix}}
                -1 & 0 & {cols} \\\\
                0 & 1 & 0
                \\end{{bmatrix}}
                """)
            elif reflection_axis == "Horizontal (flip up-down)":
                M = np.float32([[1, 0, 0], [0, -1, rows]])
                st.markdown("**Matrix:**")
                st.latex(f"""
                M = \\begin{{bmatrix}}
                1 & 0 & 0 \\\\
                0 & -1 & {rows}
                \\end{{bmatrix}}
                """)
            else:  # Both
                M = np.float32([[-1, 0, cols], [0, -1, rows]])
                st.markdown("**Matrix:**")
                st.latex(f"""
                M = \\begin{{bmatrix}}
                -1 & 0 & {cols} \\\\
                0 & -1 & {rows}
                \\end{{bmatrix}}
                """)
            
            transformed = cv2.warpAffine(img_array, M, (cols, rows))
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Apply button
        if st.button("✨ Apply Transformation", use_container_width=True, type="primary"):
            st.session_state.current_image = transformed
            st.session_state.transformation_history.append({
                'type': transform_type,
                'matrix': M,
                'timestamp': st.session_state.get('transform_count', 0) + 1
            })
            st.session_state.transform_count = st.session_state.get('transform_count', 0) + 1
            st.success(f"✅ {transform_type} applied!")
            st.rerun()
    
    with param_col2:
        # Display images
        st.markdown("#### 🖼️ Result Preview")
        
        col_before, col_after = st.columns(2)
        
        with col_before:
            st.markdown("**Original**")
            st.image(img_array, use_container_width=True, channels="RGB")
        
        with col_after:
            st.markdown("**Transformed**")
            st.image(transformed, use_container_width=True, channels="RGB")

# ========================================
# MODE 2: MULTIPLE TRANSFORMATIONS
# ========================================
elif mode == "🔗 Multiple Transformations":
    st.markdown("### 🔗 Multiple Transformations Mode")
    st.info("Combine multiple transformations sequentially. Each transformation is applied to the result of the previous one.")
    
    img_array = st.session_state.current_image
    rows, cols = img_array.shape[:2]
    
    # Transformation pipeline
    st.markdown("#### 🔧 Build Transformation Pipeline")
    
    num_transforms = st.number_input("Number of transformations", min_value=1, max_value=5, value=2, step=1)
    
    transforms_list = []
    
    for i in range(num_transforms):
        with st.expander(f"🔹 Transformation {i+1}", expanded=(i==0)):
            trans_type = st.selectbox(
                "Type",
                ["Translation", "Scaling", "Rotation", "Shearing", "Reflection"],
                key=f"trans_type_{i}"
            )
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                if trans_type == "Translation":
                    tx = st.slider("TX", -200, 200, 0, 10, key=f"tx_{i}")
                    ty = st.slider("TY", -200, 200, 0, 10, key=f"ty_{i}")
                    M = np.float32([[1, 0, tx], [0, 1, ty]])
                    
                elif trans_type == "Scaling":
                    sx = st.slider("Scale X", 0.1, 3.0, 1.0, 0.1, key=f"sx_{i}")
                    sy = st.slider("Scale Y", 0.1, 3.0, 1.0, 0.1, key=f"sy_{i}")
                    M = np.float32([[sx, 0, 0], [0, sy, 0]])
                    
                elif trans_type == "Rotation":
                    angle = st.slider("Angle", -180, 180, 0, 5, key=f"angle_{i}")
                    center = (cols / 2, rows / 2)
                    M = cv2.getRotationMatrix2D(center, angle, 1.0)
                    
                elif trans_type == "Shearing":
                    shear = st.slider("Shear", -1.0, 1.0, 0.0, 0.1, key=f"shear_{i}")
                    axis = st.radio("Axis", ["X", "Y"], key=f"shear_axis_{i}")
                    if axis == "X":
                        M = np.float32([[1, shear, 0], [0, 1, 0]])
                    else:
                        M = np.float32([[1, 0, 0], [shear, 1, 0]])
                        
                else:  # Reflection
                    ref_type = st.radio("Axis", ["Vertical", "Horizontal"], key=f"ref_{i}")
                    if ref_type == "Vertical":
                        M = np.float32([[-1, 0, cols], [0, 1, 0]])
                    else:
                        M = np.float32([[1, 0, 0], [0, -1, rows]])
            
            with col2:
                st.markdown("**Matrix:**")
                st.code(str(M), language="python")
            
            transforms_list.append({'type': trans_type, 'matrix': M})
    
    # Apply all transformations
    if st.button("✨ Apply All Transformations", type="primary", use_container_width=True):
        result = st.session_state.original_image.copy()
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for idx, trans in enumerate(transforms_list):
            status_text.text(f"Applying {trans['type']}...")
            M = trans['matrix']
            
            # Calculate new dimensions for scaling/shearing
            h, w = result.shape[:2]
            result = cv2.warpAffine(result, M, (w, h))
            
            progress_bar.progress((idx + 1) / len(transforms_list))
        
        st.session_state.current_image = result
        status_text.text("✅ All transformations applied!")
        st.balloons()
        st.rerun()
    
    # Display result
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Original Image**")
        st.image(st.session_state.original_image, use_container_width=True, channels="RGB")
    
    with col2:
        st.markdown("**Current Result**")
        st.image(st.session_state.current_image, use_container_width=True, channels="RGB")

# ========================================
# MODE 3: FILTERS
# ========================================
else:  # Filters mode
    st.markdown("### 🎨 Image Filters")
    st.info("Apply various filters to enhance or modify your image.")
    
    img_array = st.session_state.current_image
    
    filter_type = st.selectbox(
        "Select Filter",
        ["Gaussian Blur", "Sharpen", "Edge Detection", "Brightness/Contrast", "Grayscale"]
    )
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### ⚙️ Filter Parameters")
        
        if filter_type == "Gaussian Blur":
            kernel_size = st.slider("Kernel Size", 1, 15, 5, step=2,
                                   help="Must be odd number")
            if kernel_size % 2 == 0:
                kernel_size += 1
            
            filtered = cv2.GaussianBlur(img_array, (kernel_size, kernel_size), 0)
            
            st.markdown("**Kernel Matrix (simplified):**")
            st.latex(r"""
            K = \frac{1}{16}\begin{bmatrix}
            1 & 2 & 1 \\
            2 & 4 & 2 \\
            1 & 2 & 1
            \end{bmatrix}
            """)
            
        elif filter_type == "Sharpen":
            strength = st.slider("Sharpening Strength", 0.0, 2.0, 1.0, 0.1)
            
            kernel = np.array([
                [0, -1, 0],
                [-1, 5, -1],
                [0, -1, 0]
            ]) * strength
            
            filtered = cv2.filter2D(img_array, -1, kernel)
            
            st.markdown("**Sharpen Kernel:**")
            st.latex(r"""
            K = \begin{bmatrix}
            0 & -1 & 0 \\
            -1 & 5 & -1 \\
            0 & -1 & 0
            \end{bmatrix}
            """)
            
        elif filter_type == "Edge Detection":
            method = st.radio("Method", ["Sobel", "Canny"])
            
            if method == "Sobel":
                gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
                sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
                filtered = np.uint8(np.sqrt(sobelx**2 + sobely**2))
                filtered = cv2.cvtColor(filtered, cv2.COLOR_GRAY2RGB)
                
                st.markdown("**Sobel X Kernel:**")
                st.latex(r"""
                K_x = \begin{bmatrix}
                -1 & 0 & 1 \\
                -2 & 0 & 2 \\
                -1 & 0 & 1
                \end{bmatrix}
                """)
            else:
                threshold1 = st.slider("Threshold 1", 0, 255, 100)
                threshold2 = st.slider("Threshold 2", 0, 255, 200)
                gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                edges = cv2.Canny(gray, threshold1, threshold2)
                filtered = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
        
        elif filter_type == "Brightness/Contrast":
            brightness = st.slider("Brightness", -100, 100, 0)
            contrast = st.slider("Contrast", 0.5, 3.0, 1.0, 0.1)
            
            filtered = cv2.convertScaleAbs(img_array, alpha=contrast, beta=brightness)
            
            st.markdown("**Formula:**")
            st.latex(r"""
            I' = \alpha \cdot I + \beta
            """)
            st.markdown(f"α (contrast) = {contrast:.2f}")
            st.markdown(f"β (brightness) = {brightness}")
            
        else:  # Grayscale
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
            filtered = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
            
            st.markdown("**Conversion Formula:**")
            st.latex(r"""
            Gray = 0.299R + 0.587G + 0.114B
            """)
        
        if st.button("✨ Apply Filter", use_container_width=True, type="primary"):
            st.session_state.current_image = filtered
            st.success(f"✅ {filter_type} applied!")
            st.rerun()
    
    with col2:
        st.markdown("#### 🖼️ Result Preview")
        
        col_b, col_a = st.columns(2)
        
        with col_b:
            st.markdown("**Before**")
            st.image(img_array, use_container_width=True, channels="RGB")
        
        with col_a:
            st.markdown("**After**")
            st.image(filtered, use_container_width=True, channels="RGB")

# ========================================
# BOTTOM SECTION - HISTORY & DOWNLOAD
# ========================================
st.markdown("---")

bottom_col1, bottom_col2 = st.columns([2, 1])

with bottom_col1:
    if st.session_state.transformation_history:
        st.markdown("### 📜 Transformation History")
        
        for idx, trans in enumerate(st.session_state.transformation_history[-5:]):
            with st.expander(f"Transform {idx+1}: {trans['type']}"):
                st.code(str(trans['matrix']), language="python")

with bottom_col2:
    st.markdown("### 💾 Download Results")
    
    if st.session_state.current_image is not None:
        # Convert to PIL Image
        result_image = Image.fromarray(st.session_state.current_image)
        
        # Save to bytes
        buf = io.BytesIO()
        result_image.save(buf, format='PNG')
        byte_im = buf.getvalue()
        
        st.download_button(
            label="📥 Download Transformed Image",
            data=byte_im,
            file_name="transformed_image.png",
            mime="image/png",
            use_container_width=True
        )
        
        # Statistics
        st.markdown("**Image Stats:**")
        st.metric("Width", f"{st.session_state.current_image.shape[1]} px")
        st.metric("Height", f"{st.session_state.current_image.shape[0]} px")
        st.metric("Transforms Applied", len(st.session_state.transformation_history))