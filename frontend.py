import streamlit as st

def run_frontend():
    # Advanced Sci-Fi Dashboard CSS Styling for Sidebar & Global Elements
    st.markdown("""
        <style>
        /* Global Background & Font */
        .stApp {
            background-color: #030712;
            color: #f3f4f6;
        }
        
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0b0f19 0%, #030712 100%);
            border-right: 1px solid rgba(56, 189, 248, 0.2);
        }

        /* Sci-Fi Glassmorphism Cards for Metrics */
        .telemetry-card {
            background: rgba(15, 23, 42, 0.75);
            border: 1px solid rgba(56, 189, 248, 0.3);
            border-radius: 12px;
            padding: 15px;
            text-align: center;
            box-shadow: 0 0 15px rgba(56, 189, 248, 0.1);
            backdrop-filter: blur(8px);
            margin-bottom: 10px;
        }
        
        /* Neon Glow Headings */
        .sidebar-title {
            color: #38bdf8;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-shadow: 0 0 10px rgba(56, 189, 248, 0.5);
        }

        /* Customizing Selectbox / Dropdown to look Sci-Fi */
        [data-baseweb="select"] > div {
            background-color: rgba(15, 23, 42, 0.9) !important;
            border: 1px solid rgba(56, 189, 248, 0.4) !important;
            border-radius: 8px !important;
            color: #f3f4f6 !important;
        }
        
        /* Checkbox styling */
        .stCheckbox span {
            color: #e2e8f0;
            font-weight: 500;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar Header
    st.sidebar.markdown("<h3 class='sidebar-title'>🔴 MARS-MAP // OS v4.2</h3>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    
    # Suit Telemetry Section
    st.sidebar.markdown("#### 📊 Suit Telemetry")
    
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.markdown("""
            <div class="telemetry-card">
                <span style="font-size: 12px; color: #94a3b8;">OXYGEN</span>
                <h2 style="color: #38bdf8; margin: 0;">94%</h2>
                <span style="font-size: 11px; color: #ef4444;">▼ -2%</span>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="telemetry-card">
                <span style="font-size: 12px; color: #94a3b8;">BATTERY</span>
                <h2 style="color: #38bdf8; margin: 0;">82%</h2>
                <span style="font-size: 11px; color: #ef4444;">▼ -5%</span>
            </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.sidebar.columns(2)
    with col3:
        st.markdown("""
            <div class="telemetry-card">
                <span style="font-size: 12px; color: #94a3b8;">PRESSURE</span>
                <h4 style="color: #f3f4f6; margin: 5px 0 0 0;">610 Pa</h4>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
            <div class="telemetry-card">
                <span style="font-size: 12px; color: #94a3b8;">TEMP</span>
                <h4 style="color: #f3f4f6; margin: 5px 0 0 0;">-63°C</h4>
            </div>
        """, unsafe_allow_html=True)

    st.sidebar.markdown("---")
    
    # Survival Estimator Section
    st.sidebar.markdown("#### ⏱️ Survival Estimator")
    survival_hours = round((94 * 0.05) + (82 * 0.03), 1)
    st.sidebar.markdown(f"""
        <div style="background: rgba(14, 165, 233, 0.1); border: 1px solid #0ea5e9; padding: 12px; border-radius: 10px; text-align: center;">
            <span style="font-size: 12px; color: #7dd3fc;">Critical Depletion Countdown</span>
            <h3 style="color: #38bdf8; margin: 5px 0 0 0;">~{survival_hours} Hours</h3>
        </div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("---")
    
    # Navigation Controls
    st.sidebar.markdown("#### 🗺️ Navigation Controls")
    dust_storm_active = st.sidebar.checkbox("⚠️ Enable Global Dust Storm Radar", value=True)
    
    return dust_storm_active