import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

st.set_page_config(page_title="Matrix Explorer", page_icon="🔬", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .explorer-header {
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .matrix-container {
        background: #1a202c;
        color: #00ff00;
        padding: 1.5rem;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
        margin: 1rem 0;
    }
    
    .property-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 8px;
        color: white;
        margin: 0.5rem 0;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="explorer-header"><h1>🔬 Matrix Explorer Lab</h1><p>Explore and experiment with transformation matrices</p></div>', unsafe_allow_html=True)

# Tabs for different exploration modes
tab1, tab2, tab3, tab4 = st.tabs(["🎛️ Custom Matrix", "🔀 Matrix Operations", "📊 Eigenvalue Analysis", "🎮 Interactive Demo"])

# ========================================
# TAB 1: CUSTOM MATRIX BUILDER
# ========================================
with tab1:
    st.markdown("### 🎛️ Build Your Own Transformation Matrix")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Matrix Elements (2×3)")
        
        st.markdown("**Row 1:**")
        col_r1_1, col_r1_2, col_r1_3 = st.columns(3)
        with col_r1_1:
            a11 = st.number_input("a₁₁", value=1.0, step=0.1, format="%.2f", key="a11")
        with col_r1_2:
            a12 = st.number_input("a₁₂", value=0.0, step=0.1, format="%.2f", key="a12")
        with col_r1_3:
            a13 = st.number_input("a₁₃", value=0.0, step=0.5, format="%.2f", key="a13")
        
        st.markdown("**Row 2:**")
        col_r2_1, col_r2_2, col_r2_3 = st.columns(3)
        with col_r2_1:
            a21 = st.number_input("a₂₁", value=0.0, step=0.1, format="%.2f", key="a21")
        with col_r2_2:
            a22 = st.number_input("a₂₂", value=1.0, step=0.1, format="%.2f", key="a22")
        with col_r2_3:
            a23 = st.number_input("a₂₃", value=0.0, step=0.5, format="%.2f", key="a23")
        
        # Quick presets
        st.markdown("---")
        st.markdown("**Quick Presets:**")
        
        preset_col1, preset_col2 = st.columns(2)
        
        with preset_col1:
            if st.button("↔️ Translate (5,3)", use_container_width=True):
                st.session_state.preset = "translate"
                st.rerun()
            if st.button("🔍 Scale 2x", use_container_width=True):
                st.session_state.preset = "scale"
                st.rerun()
        
        with preset_col2:
            if st.button("🔄 Rotate 45°", use_container_width=True):
                st.session_state.preset = "rotate"
                st.rerun()
            if st.button("↗️ Shear X", use_container_width=True):
                st.session_state.preset = "shear"
                st.rerun()
        
        # Handle presets
        if st.session_state.get('preset') == 'translate':
            a11, a12, a13 = 1.0, 0.0, 5.0
            a21, a22, a23 = 0.0, 1.0, 3.0
            st.session_state.preset = None
        elif st.session_state.get('preset') == 'scale':
            a11, a12, a13 = 2.0, 0.0, 0.0
            a21, a22, a23 = 0.0, 2.0, 0.0
            st.session_state.preset = None
        elif st.session_state.get('preset') == 'rotate':
            a11, a12, a13 = 0.707, -0.707, 0.0
            a21, a22, a23 = 0.707, 0.707, 0.0
            st.session_state.preset = None
        elif st.session_state.get('preset') == 'shear':
            a11, a12, a13 = 1.0, 0.5, 0.0
            a21, a22, a23 = 0.0, 1.0, 0.0
            st.session_state.preset = None
    
    with col2:
        # Build matrix
        M = np.array([[a11, a12, a13], [a21, a22, a23]])
        M_square = np.array([[a11, a12], [a21, a22]])  # For determinant/eigenvalues
        
        # Display matrix
        st.markdown("#### 📐 Your Matrix")
        st.markdown('<div class="matrix-container">', unsafe_allow_html=True)
        st.latex(f"""
        M = \\begin{{bmatrix}}
        {a11:.3f} & {a12:.3f} & {a13:.3f} \\\\
        {a21:.3f} & {a22:.3f} & {a23:.3f}
        \\end{{bmatrix}}
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Matrix properties
        st.markdown("#### 🔍 Matrix Properties")
        
        prop_col1, prop_col2, prop_col3 = st.columns(3)
        
        with prop_col1:
            det = np.linalg.det(M_square)
            st.markdown(f'<div class="property-card"><h4>{det:.3f}</h4><p>Determinant</p></div>', unsafe_allow_html=True)
        
        with prop_col2:
            trace = np.trace(M_square)
            st.markdown(f'<div class="property-card"><h4>{trace:.3f}</h4><p>Trace</p></div>', unsafe_allow_html=True)
        
        with prop_col3:
            rank = np.linalg.matrix_rank(M)
            st.markdown(f'<div class="property-card"><h4>{rank}</h4><p>Rank</p></div>', unsafe_allow_html=True)
        
        # Eigenvalues
        try:
            eigenvalues = np.linalg.eigvals(M_square)
            st.markdown("**Eigenvalues:**")
            eig_col1, eig_col2 = st.columns(2)
            with eig_col1:
                st.info(f"λ₁ = {eigenvalues[0]:.3f}")
            with eig_col2:
                st.info(f"λ₂ = {eigenvalues[1]:.3f}")
        except:
            st.warning("Cannot compute eigenvalues")
        
        # Visualization
        st.markdown("#### 📊 Transformation Visualization")
        
        # Create test points (unit square)
        points = np.array([
            [0, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 1, 1],
            [0, 0, 1]
        ]).T
        
        # Transform points
        transformed = M @ points
        
        # Plot
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Original
        ax.plot(points[0, :], points[1, :], 'b-o', linewidth=2, markersize=8, label='Original', alpha=0.7)
        ax.fill(points[0, :-1], points[1, :-1], 'blue', alpha=0.1)
        
        # Transformed
        ax.plot(transformed[0, :], transformed[1, :], 'r-s', linewidth=2, markersize=8, label='Transformed', alpha=0.7)
        ax.fill(transformed[0, :-1], transformed[1, :-1], 'red', alpha=0.1)
        
        # Grid and formatting
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)
        ax.set_aspect('equal')
        ax.legend()
        ax.set_title('Unit Square Transformation', fontsize=14, fontweight='bold')
        
        # Dynamic limits
        all_pts = np.concatenate([points[:2, :], transformed[:2, :]], axis=1)
        margin = 1
        ax.set_xlim(all_pts[0].min() - margin, all_pts[0].max() + margin)
        ax.set_ylim(all_pts[1].min() - margin, all_pts[1].max() + margin)
        
        st.pyplot(fig)
        plt.close()
        
        # Test specific point
        st.markdown("#### 🎯 Test on Specific Point")
        test_col1, test_col2, test_col3 = st.columns(3)
        
        with test_col1:
            test_x = st.number_input("X coordinate", value=2.0, step=0.5, key="test_x")
        with test_col2:
            test_y = st.number_input("Y coordinate", value=3.0, step=0.5, key="test_y")
        with test_col3:
            test_point = np.array([test_x, test_y, 1])
            result = M @ test_point
            st.markdown(f"""
            **Result:**
            
            ({result[0]:.2f}, {result[1]:.2f})
            """)

# ========================================
# TAB 2: MATRIX OPERATIONS
# ========================================
with tab2:
    st.markdown("### 🔀 Matrix Composition & Operations")
    st.info("Explore how combining matrices creates compound transformations")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("#### Matrix A")
        
        operation_type_a = st.selectbox("Transformation A", 
                                        ["Translation", "Scaling", "Rotation", "Shearing"],
                                        key="op_a")
        
        if operation_type_a == "Translation":
            tx_a = st.slider("TX", -5, 5, 2, key="tx_a")
            ty_a = st.slider("TY", -5, 5, 1, key="ty_a")
            A = np.array([[1, 0, tx_a], [0, 1, ty_a], [0, 0, 1]])
            
        elif operation_type_a == "Scaling":
            s_a = st.slider("Scale", 0.5, 3.0, 1.5, 0.1, key="s_a")
            A = np.array([[s_a, 0, 0], [0, s_a, 0], [0, 0, 1]])
            
        elif operation_type_a == "Rotation":
            angle_a = st.slider("Angle", -180, 180, 45, key="angle_a")
            theta = np.radians(angle_a)
            A = np.array([
                [np.cos(theta), -np.sin(theta), 0],
                [np.sin(theta), np.cos(theta), 0],
                [0, 0, 1]
            ])
            
        else:  # Shearing
            shear_a = st.slider("Shear", -1.0, 1.0, 0.5, 0.1, key="shear_a")
            A = np.array([[1, shear_a, 0], [0, 1, 0], [0, 0, 1]])
        
        st.latex(f"""
        A = \\begin{{bmatrix}}
        {A[0,0]:.2f} & {A[0,1]:.2f} & {A[0,2]:.2f} \\\\
        {A[1,0]:.2f} & {A[1,1]:.2f} & {A[1,2]:.2f} \\\\
        {A[2,0]:.2f} & {A[2,1]:.2f} & {A[2,2]:.2f}
        \\end{{bmatrix}}
        """)
    
    with col2:
        st.markdown("#### Matrix B")
        
        operation_type_b = st.selectbox("Transformation B", 
                                        ["Translation", "Scaling", "Rotation", "Shearing"],
                                        key="op_b")
        
        if operation_type_b == "Translation":
            tx_b = st.slider("TX", -5, 5, 1, key="tx_b")
            ty_b = st.slider("TY", -5, 5, 2, key="ty_b")
            B = np.array([[1, 0, tx_b], [0, 1, ty_b], [0, 0, 1]])
            
        elif operation_type_b == "Scaling":
            s_b = st.slider("Scale", 0.5, 3.0, 0.8, 0.1, key="s_b")
            B = np.array([[s_b, 0, 0], [0, s_b, 0], [0, 0, 1]])
            
        elif operation_type_b == "Rotation":
            angle_b = st.slider("Angle", -180, 180, -30, key="angle_b")
            theta = np.radians(angle_b)
            B = np.array([
                [np.cos(theta), -np.sin(theta), 0],
                [np.sin(theta), np.cos(theta), 0],
                [0, 0, 1]
            ])
            
        else:  # Shearing
            shear_b = st.slider("Shear", -1.0, 1.0, -0.3, 0.1, key="shear_b")
            B = np.array([[1, shear_b, 0], [0, 1, 0], [0, 0, 1]])
        
        st.latex(f"""
        B = \\begin{{bmatrix}}
        {B[0,0]:.2f} & {B[0,1]:.2f} & {B[0,2]:.2f} \\\\
        {B[1,0]:.2f} & {B[1,1]:.2f} & {B[1,2]:.2f} \\\\
        {B[2,0]:.2f} & {B[2,1]:.2f} & {B[2,2]:.2f}
        \\end{{bmatrix}}
        """)
    
    st.markdown("---")
    
    # Matrix multiplication
    st.markdown("#### 🔄 Composite Transformation: B × A")
    st.info("**Order matters!** B × A means: Apply A first, then apply B")
    
    C = B @ A
    
    st.latex(f"""
    C = B \\times A = \\begin{{bmatrix}}
    {C[0,0]:.2f} & {C[0,1]:.2f} & {C[0,2]:.2f} \\\\
    {C[1,0]:.2f} & {C[1,1]:.2f} & {C[1,2]:.2f} \\\\
    {C[2,0]:.2f} & {C[2,1]:.2f} & {C[2,2]:.2f}
    \\end{{bmatrix}}
    """)
    
    # Visualization comparison
    st.markdown("#### 📊 Visual Comparison")
    
    # Test shape
    shape = np.array([[0, 2, 2, 0, 0], [0, 0, 2, 2, 0], [1, 1, 1, 1, 1]])
    
    # Apply transformations
    shape_a = A @ shape
    shape_b = B @ shape
    shape_c = C @ shape
    
    # Plot
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # A only
    axes[0].plot(shape[0], shape[1], 'b-o', linewidth=2, label='Original', alpha=0.5)
    axes[0].plot(shape_a[0], shape_a[1], 'r-s', linewidth=2, label='After A')
    axes[0].set_title(f'{operation_type_a} (A only)', fontweight='bold')
    axes[0].grid(True, alpha=0.3)
    axes[0].legend()
    axes[0].set_aspect('equal')
    
    # B only
    axes[1].plot(shape[0], shape[1], 'b-o', linewidth=2, label='Original', alpha=0.5)
    axes[1].plot(shape_b[0], shape_b[1], 'g-^', linewidth=2, label='After B')
    axes[1].set_title(f'{operation_type_b} (B only)', fontweight='bold')
    axes[1].grid(True, alpha=0.3)
    axes[1].legend()
    axes[1].set_aspect('equal')
    
    # C = B × A
    axes[2].plot(shape[0], shape[1], 'b-o', linewidth=2, label='Original', alpha=0.3)
    axes[2].plot(shape_a[0], shape_a[1], 'r--', linewidth=1, label='After A', alpha=0.5)
    axes[2].plot(shape_c[0], shape_c[1], 'm-D', linewidth=2, label='After B×A')
    axes[2].set_title('Composite (B × A)', fontweight='bold')
    axes[2].grid(True, alpha=0.3)
    axes[2].legend()
    axes[2].set_aspect('equal')
    
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

# ========================================
# TAB 3: EIGENVALUE ANALYSIS
# ========================================
with tab3:
    st.markdown("### 📊 Eigenvalue & Eigenvector Analysis")
    st.info("Understand the geometric meaning of eigenvalues and eigenvectors in transformations")
    
    # Preset transformation selector
    eigen_transform = st.selectbox(
        "Select transformation to analyze",
        ["Scaling (2x, 3x)", "Rotation (45°)", "Shearing (0.5)", "Custom"]
    )
    
    if eigen_transform == "Scaling (2x, 3x)":
        M_eigen = np.array([[2, 0], [0, 3]])
    elif eigen_transform == "Rotation (45°)":
        theta = np.radians(45)
        M_eigen = np.array([[np.cos(theta), -np.sin(theta)], 
                            [np.sin(theta), np.cos(theta)]])
    elif eigen_transform == "Shearing (0.5)":
        M_eigen = np.array([[1, 0.5], [0, 1]])
    else:
        col1, col2 = st.columns(2)
        with col1:
            m11_e = st.number_input("m₁₁", value=2.0, key="m11_e")
            m12_e = st.number_input("m₁₂", value=1.0, key="m12_e")
        with col2:
            m21_e = st.number_input("m₂₁", value=0.0, key="m21_e")
            m22_e = st.number_input("m₂₂", value=2.0, key="m22_e")
        M_eigen = np.array([[m11_e, m12_e], [m21_e, m22_e]])
    
    # Display matrix
    st.markdown("#### Matrix:")
    st.latex(f"""
    M = \\begin{{bmatrix}}
    {M_eigen[0,0]:.3f} & {M_eigen[0,1]:.3f} \\\\
    {M_eigen[1,0]:.3f} & {M_eigen[1,1]:.3f}
    \\end{{bmatrix}}
    """)
    
    # Compute eigenvalues and eigenvectors
    try:
        eigenvalues, eigenvectors = np.linalg.eig(M_eigen)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Eigenvalues:")
            st.success(f"λ₁ = {eigenvalues[0]:.4f}")
            st.success(f"λ₂ = {eigenvalues[1]:.4f}")
            
            st.markdown("#### Interpretation:")
            st.write(f"**Determinant:** {np.linalg.det(M_eigen):.4f} (= λ₁ × λ₂)")
            st.write(f"**Trace:** {np.trace(M_eigen):.4f} (= λ₁ + λ₂)")
            
        with col2:
            st.markdown("#### Eigenvectors:")
            st.success(f"v₁ = [{eigenvectors[0,0]:.3f}, {eigenvectors[1,0]:.3f}]")
            st.success(f"v₂ = [{eigenvectors[0,1]:.3f}, {eigenvectors[1,1]:.3f}]")
            
            st.markdown("#### Meaning:")
            st.write("Eigenvectors show the **principal directions** of transformation")
            st.write("Eigenvalues show **how much stretching** occurs along each direction")
        
        # Visualization
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Draw eigenvectors
        scale = 3
        ax.arrow(0, 0, eigenvectors[0,0]*scale, eigenvectors[1,0]*scale, 
                head_width=0.2, head_length=0.2, fc='red', ec='red', linewidth=3, label=f'v₁ (λ={eigenvalues[0]:.2f})')
        ax.arrow(0, 0, eigenvectors[0,1]*scale, eigenvectors[1,1]*scale, 
                head_width=0.2, head_length=0.2, fc='blue', ec='blue', linewidth=3, label=f'v₂ (λ={eigenvalues[1]:.2f})')
        
        # Transform eigenvectors
        v1_transformed = M_eigen @ (eigenvectors[:,0] * scale)
        v2_transformed = M_eigen @ (eigenvectors[:,1] * scale)
        
        ax.arrow(0, 0, v1_transformed[0], v1_transformed[1], 
                head_width=0.2, head_length=0.2, fc='red', ec='red', linewidth=3, linestyle='--', alpha=0.5)
        ax.arrow(0, 0, v2_transformed[0], v2_transformed[1], 
                head_width=0.2, head_length=0.2, fc='blue', ec='blue', linewidth=3, linestyle='--', alpha=0.5)
        
        # Grid
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)
        ax.set_aspect('equal')
        ax.legend()
        ax.set_title('Eigenvectors and Their Transformations', fontsize=14, fontweight='bold')
        ax.set_xlim(-8, 8)
        ax.set_ylim(-8, 8)
        
        st.pyplot(fig)
        plt.close()
        
    except Exception as e:
        st.error(f"Cannot compute eigenvalues: {str(e)}")

# ========================================
# TAB 4: INTERACTIVE DEMO
# ========================================
with tab4:
    st.markdown("### 🎮 Interactive Transformation Demo")
    st.info("Play with transformations and see their effects in real-time!")
    
    # Create a smiley face or simple shape
    demo_col1, demo_col2 = st.columns([1, 2])
    
    with demo_col1:
        st.markdown("#### Controls")
        
        demo_transform = st.radio("Transformation", 
                                  ["Translation", "Scaling", "Rotation", "Shearing", "All Combined"])
        
        if demo_transform == "Translation":
            tx_demo = st.slider("Translate X", -5, 5, 0, key="tx_demo")
            ty_demo = st.slider("Translate Y", -5, 5, 0, key="ty_demo")
            M_demo = np.array([[1, 0, tx_demo], [0, 1, ty_demo], [0, 0, 1]])
            
        elif demo_transform == "Scaling":
            s_demo = st.slider("Scale Factor", 0.1, 3.0, 1.0, 0.1, key="s_demo")
            M_demo = np.array([[s_demo, 0, 0], [0, s_demo, 0], [0, 0, 1]])
            
        elif demo_transform == "Rotation":
            angle_demo = st.slider("Angle", 0, 360, 0, 5, key="angle_demo")
            theta = np.radians(angle_demo)
            M_demo = np.array([
                [np.cos(theta), -np.sin(theta), 0],
                [np.sin(theta), np.cos(theta), 0],
                [0, 0, 1]
            ])
            
        elif demo_transform == "Shearing":
            shear_demo = st.slider("Shear Factor", -1.0, 1.0, 0.0, 0.1, key="shear_demo")
            M_demo = np.array([[1, shear_demo, 0], [0, 1, 0], [0, 0, 1]])
            
        else:  # All combined
            tx_all = st.slider("Translate X", -5, 5, 0, key="tx_all")
            ty_all = st.slider("Translate Y", -5, 5, 0, key="ty_all")
            s_all = st.slider("Scale", 0.5, 2.0, 1.0, 0.1, key="s_all")
            angle_all = st.slider("Rotate", 0, 360, 0, 5, key="angle_all")
            
            # Compose transformations
            T = np.array([[1, 0, tx_all], [0, 1, ty_all], [0, 0, 1]])
            S = np.array([[s_all, 0, 0], [0, s_all, 0], [0, 0, 1]])
            theta = np.radians(angle_all)
            R = np.array([
                [np.cos(theta), -np.sin(theta), 0],
                [np.sin(theta), np.cos(theta), 0],
                [0, 0, 1]
            ])
            
            M_demo = T @ R @ S
        
        st.markdown("**Current Matrix:**")
        st.code(f"""
M = [[{M_demo[0,0]:.2f}, {M_demo[0,1]:.2f}, {M_demo[0,2]:.2f}],
     [{M_demo[1,0]:.2f}, {M_demo[1,1]:.2f}, {M_demo[1,2]:.2f}]]
        """)
    
    with demo_col2:
        st.markdown("#### Visualization")
        
        # Create a simple house shape
        house = np.array([
            # Base
            [0, 4, 4, 0, 0],
            [0, 0, 3, 3, 0],
            [1, 1, 1, 1, 1]
        ])
        
        # Roof
        roof = np.array([
            [0, 2, 4],
            [3, 5, 3],
            [1, 1, 1]
        ])
        
        # Door
        door = np.array([
            [1.5, 2.5, 2.5, 1.5, 1.5],
            [0, 0, 2, 2, 0],
            [1, 1, 1, 1, 1]
        ])
        
        # Transform
        house_t = M_demo @ house
        roof_t = M_demo @ roof
        door_t = M_demo @ door
        
        # Plot
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Original
        ax.plot(house[0], house[1], 'b-', linewidth=2, alpha=0.3, label='Original')
        ax.plot(roof[0], roof[1], 'b-', linewidth=2, alpha=0.3)
        ax.plot(door[0], door[1], 'b-', linewidth=2, alpha=0.3)
        ax.fill(house[0], house[1], 'lightblue', alpha=0.2)
        
        # Transformed
        ax.plot(house_t[0], house_t[1], 'r-', linewidth=2, label='Transformed')
        ax.plot(roof_t[0], roof_t[1], 'r-', linewidth=2)
        ax.plot(door_t[0], door_t[1], 'r-', linewidth=2)
        ax.fill(house_t[0], house_t[1], 'lightcoral', alpha=0.3)
        
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)
        ax.set_aspect('equal')
        ax.legend()
        ax.set_title('House Transformation', fontsize=14, fontweight='bold')
        
        # Auto-scale
        all_x = np.concatenate([house[0], house_t[0], roof[0], roof_t[0]])
        all_y = np.concatenate([house[1], house_t[1], roof[1], roof_t[1]])
        margin = 2
        ax.set_xlim(all_x.min() - margin, all_x.max() + margin)
        ax.set_ylim(all_y.min() - margin, all_y.max() + margin)
        
        st.pyplot(fig)
        plt.close()

st.markdown("---")
st.success("💡 **Tip:** Use this explorer to understand how different matrix values affect transformations before applying them to real images!")