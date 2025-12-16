import streamlit as st
from PIL import Image

# Page config - MUST be first
st.set_page_config(
    page_title="Matrix Image Transformer",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk styling yang berbeda
st.markdown("""
<style>
    /* Header styling */
    .big-title {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1rem 0;
    }
    
    /* Card styling */
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Info box */
    .info-container {
        background: #f7fafc;
        border-left: 4px solid #667eea;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
</style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<h1 class="big-title">🎯 Matrix Image Transformer</h1>', unsafe_allow_html=True)

st.markdown("""
<div class="info-container">
    <h3>🌟 Welcome to Advanced Matrix Transformation App</h3>
    <p>Aplikasi ini memungkinkan kamu untuk mentransformasi gambar menggunakan operasi matriks matematika.
    Setiap perubahan yang kamu lihat adalah hasil dari perhitungan matriks 2D!</p>
</div>
""", unsafe_allow_html=True)

# Features overview dengan columns
st.markdown("### ✨ Apa yang Bisa Dilakukan?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h4>🔄 Geometric Transforms</h4>
        <ul>
            <li>Translation (Geser)</li>
            <li>Scaling (Skala)</li>
            <li>Rotation (Putar)</li>
            <li>Shearing (Miring)</li>
            <li>Reflection (Cermin)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h4>🎨 Image Filters</h4>
        <ul>
            <li>Gaussian Blur</li>
            <li>Sharpen</li>
            <li>Edge Detection</li>
            <li>Brightness Control</li>
            <li>Contrast Adjustment</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h4>🔬 Advanced Features</h4>
        <ul>
            <li>Multi-transform Combo</li>
            <li>Matrix Visualization</li>
            <li>Real-time Preview</li>
            <li>Export Results</li>
            <li>Transformation History</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# How it works section
st.markdown("---")
st.markdown("### 🧮 Bagaimana Cara Kerjanya?")

col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown("""
    #### Matrix Transformation Basics
    
    Setiap transformasi geometri dapat direpresentasikan sebagai perkalian matriks:
    
    **Affine Transformation Matrix (2×3):**
    """)
    
    st.latex(r"""
    \begin{bmatrix}
    x' \\
    y'
    \end{bmatrix}
    =
    \begin{bmatrix}
    a & b & t_x \\
    c & d & t_y
    \end{bmatrix}
    \begin{bmatrix}
    x \\
    y \\
    1
    \end{bmatrix}
    """)
    
    st.markdown("""
    Di mana:
    - **(x, y)** = koordinat pixel original
    - **(x', y')** = koordinat pixel setelah transformasi
    - **a, b, c, d** = parameter transformasi
    - **tₓ, tᵧ** = parameter translasi
    """)

with col_right:
    st.markdown("""
    #### Contoh Transformasi
    
    **1. Translation (Pergeseran)**
    """)
    st.latex(r"""
    M = \begin{bmatrix}
    1 & 0 & t_x \\
    0 & 1 & t_y
    \end{bmatrix}
    """)
    
    st.markdown("**2. Scaling (Penskalaan)**")
    st.latex(r"""
    M = \begin{bmatrix}
    s_x & 0 & 0 \\
    0 & s_y & 0
    \end{bmatrix}
    """)
    
    st.markdown("**3. Rotation (Rotasi)**")
    st.latex(r"""
    M = \begin{bmatrix}
    \cos\theta & -\sin\theta & 0 \\
    \sin\theta & \cos\theta & 0
    \end{bmatrix}
    """)

# Quick start guide
st.markdown("---")
st.markdown("### 🚀 Cara Menggunakan")

st.info("""
**Step 1:** Pilih menu **🎨 Transform Tool** di sidebar kiri
**Step 2:** Upload gambar yang ingin ditransformasi

**Step 3:** Pilih jenis transformasi dan atur parametera

**Step 4:** Lihat hasil real-time dan download jika puas!

**Bonus:** Coba menu **🔬 Matrix Explorer** untuk memahami lebih dalam tentang matriks transformasi
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #718096; padding: 2rem 0;'>
    <p><strong>Matrix Image Transformer</strong> v1.0</p>
    <p>Built with Streamlit + OpenCV + NumPy</p>
    <p>Dibuat dengan ❤️ untuk pembelajaran Matrix Transformations</p>
</div>
""", unsafe_allow_html=True)

# Sidebar info
with st.sidebar:
    st.markdown("---")
    st.markdown("### 📌 Navigation Guide")
    st.markdown("""
    **📚 Introduction** - Halaman ini
    
    **🎨 Transform Tool** - Transformasi gambar
    
    **🔬 Matrix Explorer** - Eksplorasi matriks
    
    **👤 About** - Info pembuat
    """)
    
    st.markdown("---")
    st.markdown("### 💡 Quick Tips")
    st.info("Upload gambar berukuran kecil-sedang untuk performa optimal (max 2MB)")