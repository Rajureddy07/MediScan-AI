import streamlit as st

st.set_page_config(
    page_title="MediScan AI",
    page_icon="💊",
    layout="wide"
)

st.markdown("""
<style>

.hero{
    text-align:center;
    padding-top:30px;
    padding-bottom:20px;
}

.hero h1{
    font-size:60px;
}

.hero p{
    font-size:22px;
    color:#B0B0B0;
}

.card{
    text-decoration:none;
}

.card div{
    padding:25px;
    border-radius:20px;
    text-align:center;
    color:white;
    font-size:24px;
    font-weight:bold;
    margin-top:15px;
    transition:0.3s;
}

.card div:hover{
    transform:scale(1.03);
}

.scan{
    background:linear-gradient(135deg,#00C853,#64DD17);
}

.search{
    background:linear-gradient(135deg,#2962FF,#00B0FF);
}

.history{
    background:linear-gradient(135deg,#FF6D00,#FFAB00);
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hero'>
    <h1>💊 MediScan AI</h1>
    <p>AI Powered Medicine Recognition System</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <a href="/medicine_scan" target="_self" class="card">
        <div class="scan">
            🚀<br>
            Scan Medicine
        </div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a href="/medicine_search" target="_self" class="card">
        <div class="search">
            🔍<br>
            Search Medicine
        </div>
    </a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <a href="/scan_history" target="_self" class="card">
        <div class="history">
            📜<br>
            Scan History
        </div>
    </a>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.info("""
✔ Full Medicine Strips

✔ Partial / Cut Strips

✔ Pill Imprint Detection

✔ OCR Powered Recognition
""")