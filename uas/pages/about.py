import streamlit as st
import datetime

st.set_page_config(page_title="About", page_icon="👤", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .about-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .profile-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        margin: 1rem;
        border: 2px solid #e2e8f0;
        transition: transform 0.3s;
    }
    
    .profile-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
    }
    
    .tech-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        font-weight: bold;
    }
    
    .feature-list {
        background: #f7fafc;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="about-header">
    <h1>👤 About This Project</h1>
    <p>Matrix Image Transformation Web Application</p>
</div>
""", unsafe_allow_html=True)

# Project Info
st.markdown("### 📋 Project Information")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-list">
        <h4>🎯 Project Goals</h4>
        <ul>
            <li>Demonstrate practical applications of linear algebra</li>
            <li>Visualize matrix transformations interactively</li>
            <li>Provide educational tool for understanding image processing</li>
            <li>Combine mathematical theory with real-world applications</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-list">
        <h4>✨ Key Features</h4>
        <ul>
            <li>5 geometric transformations (Translation, Scaling, Rotation, Shearing, Reflection)</li>
            <li>Multiple transformation modes (Single, Multiple, Filters)</li>
            <li>Interactive matrix explorer</li>
            <li>Real-time visualization</li>
            <li>Eigenvalue analysis</li>
            <li>Download transformed images</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Technologies
st.markdown("---")
st.markdown("### 🛠️ Technologies Used")

tech_col1, tech_col2, tech_col3, tech_col4 = st.columns(4)

with tech_col1:
    st.markdown('<div class="tech-badge">🐍 Python 3.8+</div>', unsafe_allow_html=True)
with tech_col2:
    st.markdown('<div class="tech-badge">🎨 Streamlit</div>', unsafe_allow_html=True)
with tech_col3:
    st.markdown('<div class="tech-badge">🔢 NumPy</div>', unsafe_allow_html=True)
with tech_col4:
    st.markdown('<div class="tech-badge">📷 OpenCV</div>', unsafe_allow_html=True)

st.markdown("")

tech_col5, tech_col6, tech_col7, tech_col8 = st.columns(4)

with tech_col5:
    st.markdown('<div class="tech-badge">📊 Matplotlib</div>', unsafe_allow_html=True)
with tech_col6:
    st.markdown('<div class="tech-badge">🖼️ Pillow</div>', unsafe_allow_html=True)
with tech_col7:
    st.markdown('<div class="tech-badge">🐼 Pandas</div>', unsafe_allow_html=True)
with tech_col8:
    st.markdown('<div class="tech-badge">🧮 SciPy</div>', unsafe_allow_html=True)

# Team Section
st.markdown("---")
st.markdown("### 👥 Development Team")

# Ganti dengan info Bryan atau teamnya
team_col1, team_col2, team_col3, team_col4 = st.columns(4)

with team_col1:
    st.markdown("""
    <div class="profile-card">
        <div style="font-size: 4rem; margin-bottom: 1rem;">👨‍💻</div>
        <h3 style="color: #667eea; margin: 0;">Bryan</h3>
        <p style="color: #718096; margin: 0.5rem 0;">Lead Developer</p>
        <p style="font-size: 0.9rem; color: #a0aec0;">NIM: 004202400038</p>
    </div>
    """, unsafe_allow_html=True)

with team_col2:
    st.markdown("""
    <div class="profile-card">
        <div style="font-size: 4rem; margin-bottom: 1rem;">👨‍💼</div>
        <h3 style="color: #667eea; margin: 0;">Angelina Pakpahan </h3>
        <p style="color: #718096; margin: 0.5rem 0;">UI/UX Designer</p>
        <p style="font-size: 0.9rem; color: #a0aec0;">NIM:004202400119</p>
    </div>
    """, unsafe_allow_html=True)

with team_col3:
    st.markdown("""
    <div class="profile-card">
        <div style="font-size: 4rem; margin-bottom: 1rem;">👩‍💻</div>
        <h3 style="color: #667eea; margin: 0;">Evelen Ridwan </h3>
        <p style="color: #718096; margin: 0.5rem 0;">Documentation</p>
        <p style="font-size: 0.9rem; color: #a0aec0;">NIM:004202400097 </p>
    </div>
    """, unsafe_allow_html=True)

with team_col4:
    st.markdown("""
    <div class="profile-card">
        <div style="font-size: 4rem; margin-bottom: 1rem;">👨‍🔬</div>
        <h3 style="color: #667eea; margin: 0;">Rafa Akbari </h3>
        <p style="color: #718096; margin: 0.5rem 0;">Tester</p>
        <p style="font-size: 0.9rem; color: #a0aec0;">NIM:004202500006 </p>
    </div>
    """, unsafe_allow_html=True)

# Mathematical Background
st.markdown("---")
st.markdown("### 📐 Mathematical Foundation")

math_col1, math_col2 = st.columns(2)

with math_col1:
    st.markdown("#### Linear Transformations")
    st.write("""
    This application is built on the principles of **linear algebra** and **affine transformations**.
    Every geometric transformation can be represented as a matrix multiplication:
    """)
    
    st.latex(r"""
    \begin{bmatrix} x' \\ y' \end{bmatrix} = 
    \begin{bmatrix} a & b \\ c & d \end{bmatrix}
    \begin{bmatrix} x \\ y \end{bmatrix} +
    \begin{bmatrix} t_x \\ t_y \end{bmatrix}
    """)
    
    st.write("""
    Using **homogeneous coordinates**, we can represent this as:
    """)
    
    st.latex(r"""
    \begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = 
    \begin{bmatrix} a & b & t_x \\ c & d & t_y \\ 0 & 0 & 1 \end{bmatrix}
    \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
    """)

with math_col2:
    st.markdown("#### Image Processing")
    st.write("""
    In digital image processing, transformations are applied to every pixel in an image:
    
    - **Geometric transformations** change the spatial arrangement of pixels
    - **Filtering operations** modify pixel values using convolution matrices
    - **Color transformations** use matrix operations on RGB channels
    
    **Applications:**
    - Computer vision
    - Medical imaging
    - Photo editing
    - Computer graphics
    - Augmented reality
    """)

# Usage Guide
st.markdown("---")
st.markdown("### 📖 How to Use This App")

with st.expander("🎨 Transform Tool", expanded=False):
    st.write("""
    **Step 1:** Upload an image (PNG, JPG, or JPEG)
    
    **Step 2:** Choose transformation mode:
    - **Single Transformation:** Apply one transformation at a time
    - **Multiple Transformations:** Combine several transformations
    - **Filters:** Apply image filters
    
    **Step 3:** Adjust parameters using sliders
    
    **Step 4:** Click "Apply" to see results
    
    **Step 5:** Download your transformed image
    """)

with st.expander("🔬 Matrix Explorer", expanded=False):
    st.write("""
    **Custom Matrix Tab:**
    - Build your own transformation matrix
    - See real-time visualization
    - Test on specific points
    
    **Matrix Operations Tab:**
    - Combine two transformations
    - Understand matrix multiplication
    - Compare individual vs composite transformations
    
    **Eigenvalue Analysis Tab:**
    - Analyze transformation properties
    - Visualize eigenvectors
    - Understand scaling factors
    
    **Interactive Demo Tab:**
    - Play with transformations
    - See effects on shapes
    - Experiment freely
    """)

# Version & Updates
st.markdown("---")
st.markdown("### 🔄 Version History")

version_data = {
    "Version": ["v1.0", "v0.9", "v0.5"],
    "Date": ["Dec 2024", "Nov 2024", "Oct 2024"],
    "Updates": [
        "Full release with all features",
        "Added matrix explorer and filters",
        "Initial prototype with basic transformations"
    ]
}

st.table(version_data)

# Contact & Feedback
st.markdown("---")
st.markdown("### 📧 Contact & Feedback")

contact_col1, contact_col2 = st.columns(2)

with contact_col1:
    st.info("""
    **Have questions or suggestions?**
    
    📧 Email: bryan.linson@student.president.ac.id
    
    🐙 GitHub: https://github.com/linlinson8888-sketch/matrix-transformer-
    
 
    """)

with contact_col2:
    st.success("""
    **Found this useful?**
    
    ⭐ Star the repository
    
    🔀 Fork and contribute
    
    📢 Share with classmates
    
    💡 Suggest new features
    """)

# Footer
st.markdown("---")
current_year = datetime.datetime.now().year

st.markdown(f"""
<div style="text-align: center; padding: 2rem 0; color: #718096;">
    <h4 style="color: #667eea;">Matrix Image Transformer</h4>
    <p>Created with ❤️ for Linear Algebra Course</p>
    <p>© {current_year} Bryan & Team. Built with Streamlit.</p>
    <p style="font-size: 0.9rem; margin-top: 1rem;">
        This project demonstrates the practical application of linear algebra in image processing
    </p>
</div>
""", unsafe_allow_html=True)