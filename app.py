import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="AstroCare | Astronaut Health Monitor",
    page_icon="🚀",
    layout="wide"
)

# -------------------------------------------------
# CUSTOM STYLING
# -------------------------------------------------

st.markdown("""
<style>
    .main {
        background-color: #0b1020;
    }

    [data-testid="stMetric"] {
        background-color: #17233b;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #263b5e;
    }

    .info-box {
        background-color: #17233b;
        padding: 18px;
        border-radius: 12px;
        border-left: 4px solid #38bdf8;
        margin-bottom: 15px;
    }

    .warning-box {
        background-color: #3b2530;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #ef4444;
    }

    .success-box {
        background-color: #17352e;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #22c55e;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SESSION DATA
# -------------------------------------------------

if "health_history" not in st.session_state:
    st.session_state.health_history = []

if "wellness_history" not in st.session_state:
    st.session_state.wellness_history = []

if "current_reading" not in st.session_state:
    st.session_state.current_reading = None

# -------------------------------------------------
# SIDEBAR NAVIGATION
# -------------------------------------------------

st.sidebar.title("🚀 AstroCare")

st.sidebar.caption(
    "Astronaut Health Monitoring and Decision Support"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Health Monitoring",
        "Health Trends",
        "Mental Wellness",
        "Health Report",
        "About AstroCare"
    ]
)

st.sidebar.divider()

st.sidebar.warning(
    "DEMO MODE: All health readings are simulated. "
    "No real astronaut or sensor data is being collected."
)

# -------------------------------------------------
# SIMULATED HEALTH DATA
# -------------------------------------------------

def generate_health_reading():

    return {
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Heart Rate": int(np.random.randint(60, 111)),
        "SpO2": int(np.random.randint(90, 100)),
        "Temperature": round(
            float(np.random.uniform(36.0, 38.0)), 1
        ),
        "Sleep": round(
            float(np.random.uniform(4.0, 9.0)), 1
        )
    }


def get_health_status(reading):

    warnings = []

    # Illustrative prototype thresholds only.
    if reading["Heart Rate"] > 100:
        warnings.append(
            "Heart rate is above the demonstration threshold."
        )

    if reading["SpO2"] < 94:
        warnings.append(
            "SpO₂ is below the demonstration threshold."
        )

    if reading["Temperature"] > 37.5:
        warnings.append(
            "Temperature is above the demonstration threshold."
        )

    if reading["Sleep"] < 6:
        warnings.append(
            "Sleep duration is below the demonstration target."
        )

    return warnings


def save_reading(reading):

    st.session_state.health_history.append(reading)

    st.session_state.current_reading = reading


# -------------------------------------------------
# DASHBOARD
# -------------------------------------------------

if page == "Dashboard":

    st.title("🚀 AstroCare")
    st.subheader(
        "Astronaut Health Monitoring and Decision Support System"
    )

    st.markdown("""
    <div class="info-box">
    AstroCare helps astronauts monitor important physical and
    behavioral health indicators during long-duration space missions.
    It presents health information, trends and warning indicators
    to support self-awareness and informed decisions.
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "This prototype uses simulated data for demonstration. "
        "It is not connected to real sensors or astronaut health records."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Physical Health")
        st.write("• Heart rate")
        st.write("• Blood oxygen saturation (SpO₂)")
        st.write("• Body temperature")
        st.write("• Sleep duration")

    with col2:
        st.markdown("### Behavioral Wellness")
        st.write("• Stress self-assessment")
        st.write("• Mood check-in")
        st.write("• Sleep-related awareness")
        st.write("• Health trend monitoring")

    st.divider()

    st.markdown("### Generate a Demonstration Reading")

    if st.button("Generate New Health Reading", type="primary"):

        reading = generate_health_reading()
        save_reading(reading)

        st.success("New simulated health reading generated!")

    if st.session_state.current_reading is not None:

        reading = st.session_state.current_reading

        st.markdown("### Latest Health Reading")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Heart Rate",
            f'{reading["Heart Rate"]} bpm'
        )

        c2.metric(
            "SpO₂",
            f'{reading["SpO2"]}%'
        )

        c3.metric(
            "Temperature",
            f'{reading["Temperature"]} °C'
        )

        c4.metric(
            "Sleep",
            f'{reading["Sleep"]} hours'
        )

        warnings = get_health_status(reading)

        if warnings:

            st.markdown(
                '<div class="warning-box"><b>Attention Indicators</b></div>',
                unsafe_allow_html=True
            )

            for warning in warnings:
                st.warning(warning)

        else:

            st.markdown(
                '<div class="success-box"><b>No demonstration '
                'threshold alerts detected.</b></div>',
                unsafe_allow_html=True
            )

    else:

        st.info(
            "Generate a reading to see the health monitoring dashboard."
        )

# -------------------------------------------------
# HEALTH MONITORING
# -------------------------------------------------

elif page == "Health Monitoring":

    st.title("🩺 Physical Health Monitoring")

    st.write(
        "Monitor important health indicators relevant to "
        "long-duration space missions."
    )

    st.info(
        "The following values are randomly generated demonstration "
        "readings. They are not real medical measurements."
    )

    if st.button("Generate Health Reading", type="primary"):

        reading = generate_health_reading()
        save_reading(reading)

        st.success("Reading generated successfully!")

    if st.session_state.current_reading is not None:

        reading = st.session_state.current_reading

        st.subheader("Current Demonstration Readings")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Heart Rate",
                f'{reading["Heart Rate"]} bpm'
            )

            st.metric(
                "Blood Oxygen Saturation",
                f'{reading["SpO2"]}%'
            )

        with col2:
            st.metric(
                "Body Temperature",
                f'{reading["Temperature"]} °C'
            )

            st.metric(
                "Sleep Duration",
                f'{reading["Sleep"]} hours'
            )

        st.subheader("Monitoring Results")

        warnings = get_health_status(reading)

        if warnings:

            for warning in warnings:
                st.warning(warning)

        else:

            st.success(
                "No demonstration threshold alerts detected."
            )

        st.caption(
            "Thresholds are illustrative software-demo settings, "
            "not clinically validated astronaut limits."
        )

    else:

        st.info("Generate a reading to begin monitoring.")

# -------------------------------------------------
# HEALTH TRENDS
# -------------------------------------------------

elif page == "Health Trends":

    st.title("📊 Health Trend Analysis")

    st.write(
        "Track changes in health indicators over multiple "
        "demonstration readings."
    )

    history = st.session_state.health_history

    if len(history) >= 1:

        df = pd.DataFrame(history)

        st.subheader("Health Monitoring History")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.subheader("Heart Rate Trend")

        fig1 = px.line(
            df,
            x="Time",
            y="Heart Rate",
            markers=True,
            title="Heart Rate Variation"
        )

        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("SpO₂ Trend")

        fig2 = px.line(
            df,
            x="Time",
            y="SpO2",
            markers=True,
            title="Blood Oxygen Saturation Variation"
        )

        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Temperature Trend")

        fig3 = px.line(
            df,
            x="Time",
            y="Temperature",
            markers=True,
            title="Body Temperature Variation"
        )

        st.plotly_chart(fig3, use_container_width=True)

        st.subheader("Sleep Trend")

        fig4 = px.line(
            df,
            x="Time",
            y="Sleep",
            markers=True,
            title="Sleep Duration Variation"
        )

        st.plotly_chart(fig4, use_container_width=True)

        st.markdown("### Demonstration Baseline Comparison")

        st.write(
            "The average of the readings collected in this session "
            "is shown as a simple reference for observing changes. "
            "It is not a medically established personal baseline."
        )

        numeric_columns = [
            "Heart Rate",
            "SpO2",
            "Temperature",
            "Sleep"
        ]

        averages = df[numeric_columns].mean()

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Average Heart Rate",
            f'{averages["Heart Rate"]:.1f} bpm'
        )

        c2.metric(
            "Average SpO₂",
            f'{averages["SpO2"]:.1f}%'
        )

        c3.metric(
            "Average Temperature",
            f'{averages["Temperature"]:.1f} °C'
        )

        c4.metric(
            "Average Sleep",
            f'{averages["Sleep"]:.1f} hours'
        )

    else:

        st.info(
            "No health history available. Generate readings "
            "from the Dashboard or Health Monitoring page."
        )

# -------------------------------------------------
# MENTAL WELLNESS
# -------------------------------------------------

elif page == "Mental Wellness":

    st.title("🧠 Mental Wellness Check-in")

    st.write(
        "Isolation, confinement, workload and disrupted sleep "
        "can affect behavioral health during long-duration missions."
    )

    st.info(
        "This section is a self-reported wellness check-in. "
        "It does not diagnose mental health conditions."
    )

    st.subheader("How are you feeling today?")

    mood = st.selectbox(
        "Select your current mood",
        [
            "Very Good",
            "Good",
            "Neutral",
            "Low",
            "Very Low"
        ]
    )

    stress = st.slider(
        "Stress Level",
        min_value=1,
        max_value=10,
        value=5,
        help="1 = Very Low, 10 = Very High"
    )

    sleep_quality = st.select_slider(
        "How would you rate your sleep quality?",
        options=[
            "Very Poor",
            "Poor",
            "Average",
            "Good",
            "Very Good"
        ]
    )

    energy = st.slider(
        "Energy Level",
        min_value=1,
        max_value=10,
        value=5
    )

    if st.button("Submit Wellness Check-in", type="primary"):

        wellness_entry = {
            "Time": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "Mood": mood,
            "Stress": stress,
            "Sleep Quality": sleep_quality,
            "Energy": energy
        }

        st.session_state.wellness_history.append(
            wellness_entry
        )

        st.success("Wellness check-in recorded.")

        if stress >= 8:

            st.warning(
                "Your self-reported stress level is high. "
                "Consider using available support resources "
                "and discussing your concerns with an appropriate "
                "health professional."
            )

        elif mood in ["Low", "Very Low"]:

            st.warning(
                "You reported a low mood. Consider reaching out "
                "to an appropriate support resource."
            )

        else:

            st.success(
                "Your check-in has been recorded. "
                "Continue monitoring your well-being."
            )

    if st.session_state.wellness_history:

        st.subheader("Previous Wellness Check-ins")

        wellness_df = pd.DataFrame(
            st.session_state.wellness_history
        )

        st.dataframe(
            wellness_df,
            use_container_width=True,
            hide_index=True
        )

# -------------------------------------------------
# HEALTH REPORT
# -------------------------------------------------

elif page == "Health Report":

    st.title("📄 Health Report")

    st.write(
        "View and download the health and wellness information "
        "collected during this application session."
    )

    health_df = pd.DataFrame(
        st.session_state.health_history
    )

    wellness_df = pd.DataFrame(
        st.session_state.wellness_history
    )

    st.subheader("Physical Health Records")

    if not health_df.empty:

        st.dataframe(
            health_df,
            use_container_width=True,
            hide_index=True
        )

        csv_health = health_df.to_csv(index=False)

        st.download_button(
            label="Download Physical Health Report",
            data=csv_health,
            file_name="astrocare_health_report.csv",
            mime="text/csv"
        )

    else:

        st.info("No physical health records available.")

    st.divider()

    st.subheader("Mental Wellness Records")

    if not wellness_df.empty:

        st.dataframe(
            wellness_df,
            use_container_width=True,
            hide_index=True
        )

        csv_wellness = wellness_df.to_csv(index=False)

        st.download_button(
            label="Download Wellness Report",
            data=csv_wellness,
            file_name="astrocare_wellness_report.csv",
            mime="text/csv"
        )

    else:

        st.info("No wellness check-ins available.")

    st.caption(
        "Reports contain demonstration data only. "
        "Session records are not permanently stored."
    )

# -------------------------------------------------
# ABOUT ASTROCARE
# -------------------------------------------------

elif page == "About AstroCare":

    st.title("🌌 About AstroCare")

    st.subheader("The Challenge")

    st.write("""
    Long-duration space missions expose astronauts to several
    environmental and behavioral challenges:

    - Space radiation exposure
    - Altered gravity
    - Isolation and confinement
    - Disrupted sleep patterns
    - Changes in cardiovascular and immune function
    - Bone loss and other physiological changes
    - Behavioral health challenges
    """)

    st.subheader("Our Proposed Solution")

    st.write("""
    AstroCare is designed as an astronaut health monitoring
    and decision-support application.

    It brings physical health indicators and self-reported
    wellness information into one interface. Through monitoring,
    visual trends and warning indicators, it aims to help astronauts
    recognize changes in their health and decide when to seek
    appropriate support.
    """)

    st.subheader("Key Features")

    st.write("""
    1. Physical health monitoring
    2. Sleep duration tracking
    3. Mental wellness self-assessment
    4. Health trend visualization
    5. Demonstration warning indicators
    6. Downloadable health reports
    """)

    st.subheader("Technology Used")

    st.write("""
    - Python
    - Streamlit
    - NumPy
    - Pandas
    - Plotly
    """)

    st.subheader("NASA Research References")

    st.markdown(
        "[NASA Human Research Program – Evidence Reports]"
        "(https://humanresearchroadmap.nasa.gov/Evidence/)"
    )

    st.markdown(
        "[NASA Human Research Program – Risks of Human Spaceflight]"
        "(https://www.nasa.gov/hrp/risks/)"
    )

    st.markdown(
        "[NASA Open Science Data Repository]"
        "(https://osdr.nasa.gov/)"
    )

    st.subheader("Future Scope")

    st.write("""
    - Integration with wearable health sensors
    - Use of relevant publicly available NASA research datasets
    - More robust personal baseline analysis
    - Long-term health trend analysis
    - Improved alert and decision-support logic
    - Secure storage of health records
    """)

    st.divider()

    st.caption(
        "AstroCare is a student prototype. It is not a certified "
        "medical device and does not replace professional medical "
        "assessment or emergency support."
    )

# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.sidebar.divider()

st.sidebar.caption(
    "AstroCare | Student Prototype"
)

st.sidebar.caption(
    "Simulated data • Not for medical diagnosis"
)