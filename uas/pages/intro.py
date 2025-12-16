import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import io

st.set_page_config(page_title="Introduction to Matrix Transformations", page_icon="📚", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .concept-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    
    .math-section {
        background: #edf2f7;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #4299e1;
        margin: 1rem 0;
    }
    
    .example-box {
        background: #fff5f5;
        border: 2px dashed #fc8181;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.title("📚 Pengenalan Matrix Transformations")

st.markdown("""
<div class="concept-box">
    <h3>🎯 Apa itu Matrix Transformation?</h3>
    <p>Matrix transformation adalah cara matematis untuk mengubah posisi, ukuran, atau orientasi 
    dari objek dalam ruang 2D atau 3D. Dalam image processing, kita menggunakan matriks untuk 
    memanipulasi setiap pixel dalam gambar.</p>
</div>
""", unsafe_allow_html=True)

# Tabs untuk organized content
tab1, tab2, tab3, tab4 = st.tabs(["🔢 Dasar Matriks", "🎨 Jenis Transformasi", "🧮 Contoh Perhitungan", "🎬 Visualisasi"])

# ========================================
# TAB 1: DASAR MATRIKS
# ========================================
with tab1:
    st.markdown("### 🔢 Fundamental Matrix Transformations")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        #### Koordinat Homogen
        
        Untuk melakukan transformasi affine, kita menggunakan **homogeneous coordinates** 
        yang menambahkan dimensi ekstra:
        """)
        
        st.latex(r"""
        \text{Point 2D: } (x, y) \rightarrow \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
        """)
        
        st.markdown("""
        Mengapa perlu koordinat homogen?
        - ✅ Memungkinkan translasi dinyatakan sebagai perkalian matriks
        - ✅ Menyederhanakan komposisi transformasi
        - ✅ Unified representation untuk semua transformasi affine
        """)
        
    with col2:
        st.markdown("""
        #### Affine Transformation Matrix
        
        Bentuk umum matriks transformasi affine 2D:
        """)
        
        st.latex(r"""
        M = \begin{bmatrix}
        m_{00} & m_{01} & m_{02} \\
        m_{10} & m_{11} & m_{12}
        \end{bmatrix}
        """)
        
        st.markdown("""
        **Cara Kerja:**
        """)
        
        st.latex(r"""
        \begin{bmatrix} x' \\ y' \end{bmatrix} = 
        \begin{bmatrix}
        m_{00} & m_{01} & m_{02} \\
        m_{10} & m_{11} & m_{12}
        \end{bmatrix}
        \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
        """)
    
    st.markdown("---")
    
    # Interactive Matrix Calculator
    st.markdown("### 🧮 Interactive Matrix Calculator")
    st.markdown("Coba masukkan nilai matriks dan lihat hasilnya!")
    
    calc_col1, calc_col2, calc_col3 = st.columns(3)
    
    with calc_col1:
        st.markdown("**Matrix Elements:**")
        m00 = st.number_input("m₀₀", value=1.0, step=0.1, key="m00")
        m01 = st.number_input("m₀₁", value=0.0, step=0.1, key="m01")
        m02 = st.number_input("m₀₂ (tx)", value=0.0, step=0.5, key="m02")
    
    with calc_col2:
        st.write("")  # spacing
        st.write("")  # spacing
        m10 = st.number_input("m₁₀", value=0.0, step=0.1, key="m10")
        m11 = st.number_input("m₁₁", value=1.0, step=0.1, key="m11")
        m12 = st.number_input("m₁₂ (ty)", value=0.0, step=0.5, key="m12")
    
    with calc_col3:
        st.markdown("**Input Point:**")
        x_in = st.number_input("X coordinate", value=3.0, step=0.5)
        y_in = st.number_input("Y coordinate", value=2.0, step=0.5)
    
    # Calculate transformation
    matrix = np.array([[m00, m01, m02], [m10, m11, m12]])
    point_in = np.array([x_in, y_in, 1])
    point_out = matrix @ point_in
    
    st.markdown("---")
    result_col1, result_col2 = st.columns(2)
    
    with result_col1:
        st.markdown("**Calculation:**")
        st.latex(f"""
        \\begin{{bmatrix}} x' \\\\ y' \\end{{bmatrix}} = 
        \\begin{{bmatrix}}
        {m00} & {m01} & {m02} \\\\
        {m10} & {m11} & {m12}
        \\end{{bmatrix}}
        \\begin{{bmatrix}} {x_in} \\\\ {y_in} \\\\ 1 \\end{{bmatrix}}
        """)
    
    with result_col2:
        st.markdown("**Result:**")
        st.success(f"""
        **Input Point:** ({x_in}, {y_in})
        
        **Output Point:** ({point_out[0]:.2f}, {point_out[1]:.2f})
        """)

# ========================================
# TAB 2: JENIS TRANSFORMASI
# ========================================
with tab2:
    st.markdown("### 🎨 5 Jenis Transformasi Geometri Utama")
    
    # Translation
    with st.expander("🔵 1. TRANSLATION (Pergeseran)", expanded=True):
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            **Definisi:** Menggeser semua titik dengan jarak yang sama
            
            **Matrix Form:**
            """)
            st.latex(r"""
            T(t_x, t_y) = \begin{bmatrix}
            1 & 0 & t_x \\
            0 & 1 & t_y
            \end{bmatrix}
            """)
            
            st.markdown("""
            **Parameter:**
            - `tx`: pergeseran horizontal (+ = kanan, - = kiri)
            - `ty`: pergeseran vertikal (+ = bawah, - = atas)
            
            **Sifat:**
            - Mempertahankan bentuk dan ukuran
            - Tidak mengubah orientasi
            """)
        
        with col2:
            st.markdown("**Contoh:**")
            st.code("""
# Translation matrix
tx, ty = 50, 30
M = [[1, 0, tx],
     [0, 1, ty]]
     
# Point (100, 100) → (150, 130)
            """, language="python")
    
    # Scaling
    with st.expander("🟢 2. SCALING (Penskalaan)"):
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            **Definisi:** Mengubah ukuran objek dengan faktor skala
            
            **Matrix Form:**
            """)
            st.latex(r"""
            S(s_x, s_y) = \begin{bmatrix}
            s_x & 0 & 0 \\
            0 & s_y & 0
            \end{bmatrix}
            """)
            
            st.markdown("""
            **Parameter:**
            - `sx`: faktor skala horizontal
            - `sy`: faktor skala vertikal
            
            **Sifat:**
            - sx = sy → uniform scaling
            - sx ≠ sy → non-uniform scaling
            - sx, sy > 1 → pembesaran
            - sx, sy < 1 → pengecilan
            """)
        
        with col2:
            st.markdown("**Contoh:**")
            st.code("""
# Scaling matrix (2x horizontal, 1.5x vertical)
sx, sy = 2.0, 1.5
M = [[sx, 0, 0],
     [0, sy, 0]]
     
# Point (10, 20) → (20, 30)
            """, language="python")
    
    # Rotation
    with st.expander("🟡 3. ROTATION (Rotasi)"):
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            **Definisi:** Memutar objek terhadap titik pusat
            
            **Matrix Form:**
            """)
            st.latex(r"""
            R(\theta) = \begin{bmatrix}
            \cos\theta & -\sin\theta & 0 \\
            \sin\theta & \cos\theta & 0
            \end{bmatrix}
            """)
            
            st.markdown("""
            **Parameter:**
            - `θ`: sudut rotasi (derajat atau radian)
            
            **Sifat:**
            - θ > 0 → counter-clockwise
            - θ < 0 → clockwise
            - Mempertahankan ukuran
            - Pusat rotasi default: origin (0,0)
            """)
        
        with col2:
            st.markdown("**Contoh:**")
            st.code("""
# Rotation 45° counter-clockwise
import math
theta = math.radians(45)
M = [[math.cos(theta), -math.sin(theta), 0],
     [math.sin(theta),  math.cos(theta), 0]]
     
# Rotasi dari origin
            """, language="python")
    
    # Shearing
    with st.expander("🟠 4. SHEARING (Pergeseran Miring)"):
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            **Definisi:** Membuat efek "miring" pada objek
            
            **Matrix Form (X-shear):**
            """)
            st.latex(r"""
            H_x(sh_x) = \begin{bmatrix}
            1 & sh_x & 0 \\
            0 & 1 & 0
            \end{bmatrix}
            """)
            
            st.markdown("**Matrix Form (Y-shear):**")
            st.latex(r"""
            H_y(sh_y) = \begin{bmatrix}
            1 & 0 & 0 \\
            sh_y & 1 & 0
            \end{bmatrix}
            """)
            
            st.markdown("""
            **Sifat:**
            - Mempertahankan luas area
            - Mengubah sudut
            - Paralel lines tetap paralel
            """)
        
        with col2:
            st.markdown("**Contoh:**")
            st.code("""
# X-axis shearing
shx = 0.5
M = [[1, shx, 0],
     [0, 1,   0]]
     
# Y-axis shearing
shy = 0.3
M = [[1,   0, 0],
     [shy, 1, 0]]
            """, language="python")
    
    # Reflection
    with st.expander("🔴 5. REFLECTION (Pencerminan)"):
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            **Definisi:** Mencerminkan objek terhadap sumbu/garis
            
            **Matrix Form (X-axis):**
            """)
            st.latex(r"""
            M_x = \begin{bmatrix}
            1 & 0 & 0 \\
            0 & -1 & 0
            \end{bmatrix}
            """)
            
            st.markdown("**Matrix Form (Y-axis):**")
            st.latex(r"""
            M_y = \begin{bmatrix}
            -1 & 0 & 0 \\
            0 & 1 & 0
            \end{bmatrix}
            """)
            
            st.markdown("**Matrix Form (y=x):**")
            st.latex(r"""
            M_{y=x} = \begin{bmatrix}
            0 & 1 & 0 \\
            1 & 0 & 0
            \end{bmatrix}
            """)
        
        with col2:
            st.markdown("**Contoh:**")
            st.code("""
# Reflection across X-axis
M = [[1,  0, 0],
     [0, -1, 0]]
     
# Reflection across Y-axis  
M = [[-1, 0, 0],
     [0,  1, 0]]
     
# Reflection across y=x
M = [[0, 1, 0],
     [1, 0, 0]]
            """, language="python")

# ========================================
# TAB 3: CONTOH PERHITUNGAN
# ========================================
with tab3:
    st.markdown("### 🧮 Contoh Perhitungan Manual")
    
    st.markdown("""
    <div class="example-box">
        <h4>📝 Problem: Rotasi Point (3, 2) sebesar 90° counter-clockwise</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**Step 1: Tentukan matriks rotasi**")
    st.markdown("Untuk θ = 90°:")
    st.latex(r"""
    \cos(90°) = 0, \quad \sin(90°) = 1
    """)
    
    st.latex(r"""
    R(90°) = \begin{bmatrix}
    0 & -1 & 0 \\
    1 & 0 & 0
    \end{bmatrix}
    """)
    
    st.markdown("**Step 2: Bentuk homogeneous coordinates**")
    st.latex(r"""
    P = \begin{bmatrix} 3 \\ 2 \\ 1 \end{bmatrix}
    """)
    
    st.markdown("**Step 3: Kalikan matriks dengan point**")
    st.latex(r"""
    P' = R \cdot P = 
    \begin{bmatrix}
    0 & -1 & 0 \\
    1 & 0 & 0
    \end{bmatrix}
    \begin{bmatrix} 3 \\ 2 \\ 1 \end{bmatrix}
    """)
    
    st.latex(r"""
    = \begin{bmatrix}
    (0)(3) + (-1)(2) + (0)(1) \\
    (1)(3) + (0)(2) + (0)(1)
    \end{bmatrix}
    = \begin{bmatrix} -2 \\ 3 \end{bmatrix}
    """)
    
    st.success("**Hasil: Point (3, 2) setelah rotasi 90° menjadi (-2, 3)**")
    
    st.markdown("---")
    
    # Multiple transformations example
    st.markdown("### 🔄 Komposisi Transformasi")
    st.markdown("""
    <div class="example-box">
        <h4>📝 Problem: Apply Translation KEMUDIAN Rotation</h4>
        <p>Point (1, 1) → Translate (2, 1) → Rotate 45°</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**Step 1: Translation matrix**")
    st.latex(r"""
    T = \begin{bmatrix}
    1 & 0 & 2 \\
    0 & 1 & 1
    \end{bmatrix}
    """)
    
    st.markdown("**Step 2: Rotation matrix (45°)**")
    st.latex(r"""
    R = \begin{bmatrix}
    0.707 & -0.707 & 0 \\
    0.707 & 0.707 & 0
    \end{bmatrix}
    """)
    
    st.markdown("**Step 3: Composite transformation (R × T)**")
    st.info("""
    ⚠️ **PENTING:** Order matters! 
    
    Untuk apply T kemudian R: gunakan **R × T**
    
    (baca dari kanan ke kiri dalam perkalian matriks)
    """)

# ========================================
# TAB 4: VISUALISASI
# ========================================
with tab4:
    st.markdown("### 🎬 Visualisasi Transformasi Interaktif")
    
    viz_col1, viz_col2 = st.columns([1, 2])
    
    with viz_col1:
        st.markdown("**Pilih Transformasi:**")
        viz_type = st.selectbox(
            "Transformation Type",
            ["Translation", "Scaling", "Rotation", "Shearing", "Reflection"],
            key="viz_transform"
        )
        
        if viz_type == "Translation":
            tx_viz = st.slider("Translation X", -5, 5, 2, key="tx_viz")
            ty_viz = st.slider("Translation Y", -5, 5, 1, key="ty_viz")
            M_viz = np.array([[1, 0, tx_viz], [0, 1, ty_viz], [0, 0, 1]])
            
        elif viz_type == "Scaling":
            sx_viz = st.slider("Scale X", 0.1, 3.0, 1.5, 0.1, key="sx_viz")
            sy_viz = st.slider("Scale Y", 0.1, 3.0, 1.5, 0.1, key="sy_viz")
            M_viz = np.array([[sx_viz, 0, 0], [0, sy_viz, 0], [0, 0, 1]])
            
        elif viz_type == "Rotation":
            angle_viz = st.slider("Angle (degrees)", -180, 180, 45, key="angle_viz")
            theta = np.radians(angle_viz)
            M_viz = np.array([
                [np.cos(theta), -np.sin(theta), 0],
                [np.sin(theta), np.cos(theta), 0],
                [0, 0, 1]
            ])
            
        elif viz_type == "Shearing":
            shear_viz = st.slider("Shear factor", -1.0, 1.0, 0.5, 0.1, key="shear_viz")
            axis_viz = st.radio("Shear axis", ["X", "Y"], key="shear_axis")
            if axis_viz == "X":
                M_viz = np.array([[1, shear_viz, 0], [0, 1, 0], [0, 0, 1]])
            else:
                M_viz = np.array([[1, 0, 0], [shear_viz, 1, 0], [0, 0, 1]])
        
        else:  # Reflection
            ref_axis = st.radio("Reflection axis", ["X-axis", "Y-axis", "y=x"], key="ref_axis")
            if ref_axis == "X-axis":
                M_viz = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
            elif ref_axis == "Y-axis":
                M_viz = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
            else:
                M_viz = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    
    with viz_col2:
        # Create visualization
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Original square points
        square = np.array([
            [0, 0, 1],
            [2, 0, 1],
            [2, 2, 1],
            [0, 2, 1],
            [0, 0, 1]  # close the shape
        ]).T
        
        # Transform
        transformed = M_viz @ square
        
        # Plot
        ax.plot(square[0, :], square[1, :], 'b-o', linewidth=2, markersize=8, label='Original', alpha=0.7)
        ax.plot(transformed[0, :], transformed[1, :], 'r-s', linewidth=2, markersize=8, label='Transformed', alpha=0.7)
        
        # Add grid and axes
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)
        ax.set_aspect('equal')
        ax.legend()
        ax.set_title(f'{viz_type} Transformation', fontsize=14, fontweight='bold')
        
        # Set limits
        all_points = np.concatenate([square[:2, :], transformed[:2, :]], axis=1)
        margin = 1
        ax.set_xlim(all_points[0].min() - margin, all_points[0].max() + margin)
        ax.set_ylim(all_points[1].min() - margin, all_points[1].max() + margin)
        
        st.pyplot(fig)
        plt.close()

# Footer
st.markdown("---")
st.info("""
💡 **Tips:** 
- Pahami setiap jenis transformasi secara individual sebelum mengkombinasikannya
- Perhatikan order transformasi ketika melakukan komposisi
- Gunakan **Matrix Explorer** untuk eksperimen lebih lanjut!
""")