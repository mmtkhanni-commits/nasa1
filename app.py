import streamlit as st
import folium
from streamlit_folium import st_folium
import math
import base64

from frontend import run_frontend
from backend import MARS_LOCATIONS, get_location_details

# Run Frontend UI (Sidebar Telemetry)
dust_storm_active = run_frontend()

# --- CUSTOM HANDCRAFTED SCI-FI COMMAND CENTER STYLING ---
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at top center, #0B0F19 0%, #030712 100%);
        color: #F3F4F6;
        font-family: 'Inter', sans-serif;
    }
    
    /* Custom Sleek Sticky Header */
    .command-header {
        position: sticky;
        top: 0;
        z-index: 999;
        background: rgba(3, 7, 18, 0.88);
        backdrop-filter: blur(12px);
        padding: 16px 24px;
        border-bottom: 2px solid rgba(14, 165, 233, 0.4);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        border-radius: 0 0 16px 16px;
        margin-bottom: 25px;
    }

    /* Handcrafted Action Buttons */
    .stButton>button {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.9) 0%, rgba(30, 41, 59, 0.9) 100%);
        color: #38BDF8;
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 10px;
        padding: 12px 20px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, rgba(14, 165, 233, 0.2) 0%, rgba(56, 189, 248, 0.3) 100%);
        border-color: #38BDF8;
        color: #FFFFFF;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
        transform: translateY(-2px);
    }

    @keyframes strobe-flash {
        0% { background-color: rgba(239, 68, 68, 0.15); box-shadow: 0 0 15px rgba(239, 68, 68, 0.3); }
        50% { background-color: rgba(239, 68, 68, 0.45); box-shadow: 0 0 35px rgba(239, 68, 68, 0.7); }
        100% { background-color: rgba(239, 68, 68, 0.15); box-shadow: 0 0 15px rgba(239, 68, 68, 0.3); }
    }
    
    .sos-active {
        animation: strobe-flash 1.2s infinite;
        border: 2px solid #EF4444;
        padding: 24px;
        border-radius: 14px;
        margin-bottom: 20px;
    }

    .crew-card {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(56, 189, 248, 0.2);
        padding: 16px;
        border-radius: 12px;
        text-align: center;
        backdrop-filter: blur(8px);
    }
    </style>

    <div class="command-header">
        <h1 style="color: #38BDF8; margin: 0; font-size: 24px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase;">
            🔴 MARS SURVIVAL COMMAND CENTER <span style="font-size: 14px; color: #94A3B8; font-weight: 400;">// TACTICAL MATRIX v4.2</span>
        </h1>
    </div>
""", unsafe_allow_html=True)

# --- NAVIGATION BUTTONS ---
if "current_page" not in st.session_state:
    st.session_state.current_page = "🗺️ Command Center & Map"

nav_col1, nav_col2, nav_col3 = st.columns(3)

with nav_col1:
    if st.button("🗺️ Command Center", use_container_width=True):
        st.session_state.current_page = "🗺️ Command Center & Map"
with nav_col2:
    if st.button("📖 Survival Manual", use_container_width=True):
        st.session_state.current_page = "📖 Survival Manual"
with nav_col3:
    if st.button("📊 Telemetry & Crew", use_container_width=True):
        st.session_state.current_page = "📊 Detailed Telemetry"

page_selection = st.session_state.current_page
st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

# --- PAGE 1: COMMAND CENTER & MAP ---
if page_selection == "🗺️ Command Center & Map":
    
    location_choice = st.sidebar.selectbox("🎯 Target Safe Haven:", list(MARS_LOCATIONS.keys()))
    selected_loc = get_location_details(location_choice)

    st.sidebar.markdown("---")
    st.sidebar.markdown("#### 🌪️ Atmospheric Hazard Timeline")
    storm_severity = st.sidebar.slider("Dust Storm Intensity Index", 0.0, 10.0, 7.5 if dust_storm_active else 1.0)

    if storm_severity > 6.0:
        st.markdown("""
            <div style="background: rgba(239, 68, 68, 0.12); border-left: 4px solid #EF4444; padding: 14px; border-radius: 8px; margin-bottom: 20px;">
                <h4 style="color: #EF4444; margin: 0; font-size: 16px;">🚨 CRITICAL HAZARD ALERT (Severity: """ + str(storm_severity) + """)</h4>
                <p style="margin: 5px 0 0 0; color: #FCA5A5; font-size: 14px;">High wind shear active across Sector 4. Complete protocol before deployment.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("### ⚡ Emergency Response Wizard")

    if "step1_done" not in st.session_state:
        st.session_state.step1_done = False
    if "step2_done" not in st.session_state:
        st.session_state.step2_done = False
    if "step3_done" not in st.session_state:
        st.session_state.step3_done = False

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**Phase 1: Suit Seals**")
        if not st.session_state.step1_done:
            if st.button("🔒 Lock Regulators", use_container_width=True, key="btn_step1"):
                st.session_state.step1_done = True
                st.rerun()
        else:
            st.success("✔ Sealed (610 Pa)")

    with col2:
        st.markdown("**Phase 2: Thermal Shield**")
        if st.session_state.step1_done and not st.session_state.step2_done:
            if st.button("⛺ Deploy Shield", use_container_width=True, key="btn_step2"):
                st.session_state.step2_done = True
                st.rerun()
        elif st.session_state.step2_done:
            st.success("✔ Shield Active")
        else:
            st.info("🔒 Complete Phase 1")

    with col3:
        st.markdown("**Phase 3: Evac Route & SOS**")
        if st.session_state.step2_done and not st.session_state.step3_done:
            if st.button("📡 Broadcast SOS", use_container_width=True, key="btn_step3"):
                st.session_state.step3_done = True
                st.rerun()
        elif st.session_state.step3_done:
            st.success("✔ Beacon Live")
        else:
            st.info("🔒 Complete Phase 2")

    st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)

    if st.session_state.step3_done:
        st.markdown("""
            <div class="sos-active">
                <h3 style="color: #F87171; margin: 0; font-size: 18px;">📡 EMERGENCY SOS BEACON ACTIVE // TRANSMITTING STROBE SIGNAL</h3>
                <p style="color: #CBD5E1; margin: 5px 0 0 0; font-size: 14px;">Audio distress pulses broadcasting on frequency 432.5 MHz to orbital relay.</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <audio autoplay loop>
              <source src="https://assets.mixkit.co/active_storage/sfx/2869/2869-preview.mp3" type="audio/mpeg">
            </audio>
        """, unsafe_allow_html=True)
        st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)

    start_lat, start_lng = -15.0, -30.0
    target_lat, target_lng = selected_loc["lat"], selected_loc["lng"]

    dlat = math.radians(target_lat - start_lat)
    dlng = math.radians(target_lng - start_lng)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(start_lat)) * math.cos(math.radians(target_lat)) * math.sin(dlng/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance_km = round(3389.5 * c, 1)
    walking_hours = round(distance_km / 4.2, 1)

    col_m1, col_m2 = st.columns(2)
    col_m1.metric("📍 Distance to " + location_choice, f"{distance_km} km")
    col_m2.metric("⏱️ Est. Travel Time", f"~{walking_hours} Hours")

    st.subheader("🗺️ Tactical Planetary Map & Safe Havens")

    m = folium.Map(location=[0.0, 15.0], zoom_start=3, tiles=None, world_copy_jump=False)
    folium.TileLayer(
        tiles="https://trek.nasa.gov/tiles/Mars/EQ/Mars_MGS_MOLA_ClrShade_merge_global_463m/1.0.0//default/default028mm/{z}/{y}/{x}.jpg",
        attr="NASA Mars Topography", name="Mars Topography", overlay=True, control=True, max_zoom=6, no_wrap=True
    ).add_to(m)

    folium.Marker([start_lat, start_lng], popup="<b>Explorer Current Position</b>", icon=folium.Icon(color="red", icon="user", prefix="fa")).add_to(m)

    for name, loc in MARS_LOCATIONS.items():
        is_selected = (name == location_choice)
        marker_color = "green" if is_selected else "cadetblue"
        icon_name = "home" if is_selected else "shield"
        folium.Marker([loc["lat"], loc["lng"]], popup=f"<b>{name}</b><br>{loc['desc']}", icon=folium.Icon(color=marker_color, icon=icon_name, prefix="fa")).add_to(m)

    if dust_storm_active or storm_severity > 5.0:
        folium.Circle(location=[0.0, -5.0], radius=int(1500000 * (storm_severity/5.0)), color="#EF4444", fill=True, fill_color="#EF4444", fill_opacity=0.4).add_to(m)
        if st.session_state.step3_done:
            safe_path = [[start_lat, start_lng], [-10.0, 10.0], [target_lat, target_lng]]
            folium.PolyLine(safe_path, color="#38BDF8", weight=5, tooltip=f"Evacuation Route to {location_choice}").add_to(m)

    st_folium(m, width=1100, height=480)

    st.markdown("---")
    st.subheader("🎒 Life Support & Resource Inventory Log")
    inv_col1, inv_col2, inv_col3, inv_col4 = st.columns(4)
    inv_col1.metric("💧 Water Reserve", "1.8 Liters", "-0.2L")
    inv_col2.metric("💊 Medkits", "2 Units", "Nominal")
    inv_col3.metric("🔋 Emergency Cells", "3 Packs", "-1 Pack")
    inv_col4.metric("🍫 Nutrient Rations", "5 Bars", "-2 Bars")

    st.markdown("---")
    st.subheader("📥 Export Mission Report")
    report_content = f"""=== MARS SURVIVAL MISSION REPORT ===
Target Haven: {location_choice}
Coordinates: Lat {target_lat}, Lng {target_lng}
Distance: {distance_km} km
Est. Travel Time: {walking_hours} Hours
Dust Storm Severity Index: {storm_severity}
SOS Beacon Status: {"ACTIVE" if st.session_state.step3_done else "STANDBY"}
Suit Telemetry: Oxygen 94% | Battery 82% | Pressure 610 Pa | Temp -63°C
====================================
"""
    b64 = base64.b64encode(report_content.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="Mars_Mission_Report.txt" style="background: linear-gradient(135deg, #0EA5E9, #2563EB); color: white; padding: 12px 24px; border-radius: 10px; text-decoration: none; font-weight: bold; box-shadow: 0 4px 12px rgba(14,165,233,0.3);">📥 Download Official Mission Report (.txt)</a>'
    st.markdown(href, unsafe_allow_html=True)

# --- PAGE 2: SURVIVAL MANUAL ---
elif page_selection == "📖 Survival Manual":
    st.title("📖 Martian Survival Manual & Emergency Protocols")
    st.markdown("Comprehensive guidelines for extreme Martian environmental hazards.")
    
    tab1, tab2, tab3 = st.tabs(["🌪️ Dust Storms", "🔋 Power & Thermal Failure", "🧊 Resource Scarcity"])
    with tab1:
        st.subheader("Dust Storm Procedures")
        st.markdown("- Stop all movement to conserve oxygen.\n- Seal all helmet neck rings and glove seals.\n- Seek natural depressions or lava tubes.")
    with tab2:
        st.subheader("Thermal Management")
        st.markdown("- Enable low-power eco mode on life support.\n- Deploy auxiliary thin-film solar blankets.")
    with tab3:
        st.subheader("Resource Harvesting")
        st.markdown("- Target subsurface glacial ice deposits.\n- Use thermal drills and filtration units.")

# --- PAGE 3: DETAILED TELEMETRY & CREW MANAGEMENT ---
elif page_selection == "📊 Detailed Telemetry":
    st.title("📊 Detailed Suit Telemetry & Crew Status")
    st.markdown("Real-time diagnostic metrics and multi-crew member health monitoring matrix.")
    
    col1, col2 = st.columns(2)
    col1.metric("Primary Oxygen Tank", "94%", "-2%")
    col2.metric("Main Battery Core", "82%", "-5%")
    
    col3, col4 = st.columns(2)
    col3.metric("Suit Internal Pressure", "610 Pa", "Nominal")
    col4.metric("External Ambient Temp", "-63°C", "Stable")
    
    st.markdown("---")
    st.subheader("👥 Multi-Crew Telemetry & Status Matrix")
    
    crew_col1, crew_col2, crew_col3 = st.columns(3)
    with crew_col1:
        st.markdown("""
            <div class="crew-card">
                <h4 style="color: #38BDF8; margin: 0;">Commander Alex</h4>
                <p style="color: #4ADE80; margin: 5px 0;">Status: Nominal</p>
                <p style="font-size: 13px; color: #94A3B8; margin: 0;">O2: 96% | Sector 1</p>
            </div>
        """, unsafe_allow_html=True)
    with crew_col2:
        st.markdown("""
            <div class="crew-card">
                <h4 style="color: #38BDF8; margin: 0;">Engineer Sarah</h4>
                <p style="color: #FACC15; margin: 5px 0;">Status: Caution</p>
                <p style="font-size: 13px; color: #94A3B8; margin: 0;">O2: 88% | Sector 3</p>
            </div>
        """, unsafe_allow_html=True)
    with crew_col3:
        st.markdown("""
            <div class="crew-card">
                <h4 style="color: #38BDF8; margin: 0;">Pilot David</h4>
                <p style="color: #4ADE80; margin: 5px 0;">Status: Nominal</p>
                <p style="font-size: 13px; color: #94A3B8; margin: 0;">O2: 92% | Sector 2</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("💬 Direct Link to Jezero Base Operator")
    base_msg = st.text_input("Transmit emergency dispatch message to base:")
    if base_msg:
        st.success(f"Transmission sent: '{base_msg}' — Awaiting operator acknowledgment...")