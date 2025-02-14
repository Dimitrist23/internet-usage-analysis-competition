import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="Internet Usage Analysis", layout="wide", page_icon="🌐")

# Custom theme styling
st.markdown("""
    <style>
    /* Global app background and font style */
    .stApp {
        background-color: black;
        color: white;
        font-family: 'Times New Roman', serif;
        margin: 0 auto;
    }

    /* Button styles and hover effects */
    .stButton>button {
        background-color: #0000FF;
        color: white;
        width: 100%;
        max-width: 530px;
        height: 50px;
        font-size: 20px;
        font-weight: bold;
        transition: background-color 0.3s ease;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 10px auto; /* Center buttons */
    }

    .stButton>button:hover {
        background-color: #00008B;
    }

    /* Social icons style */
    .social-icons img {
        background-color: #e0e0e0;
        border-radius: 50%;
        padding: 8px;
        width: 50px;
        height: 50px;
        transition: transform 0.3s ease;
    }

    .social-icons img:hover {
        filter: brightness(0.9);
        transform: scale(1.1);
    }

    /* Header styling */
    .header-title {
        font-size: 36px;
        font-weight: bold;
        color: white;
        margin-top: 10px;
        text-align: center;
    }
        /* Header styling2 */
    header {
        background-color: #2E2E2E !important;
        padding: 15px;
        border-bottom: 3px solid #999;
        font-size: 20px;
        font-weight: bold;
        color: #333;
        text-align: center;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .stButton>button {
            width: 100%;
            font-size: 16px;
        }

        .header-title {
            font-size: 28px;
        }
    }

    @media (max-width: 1024px) {
        .stButton>button {
            width: 80%;
        }

        .header-title {
            font-size: 32px;
        }
    }

    /* Center the tabs in the header for large screens */
    @media (min-width: 1920px) {
        .stButton>button {
            width: 530px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Title in header section
st.markdown("<h1 class='header-title'>🌐 The Evolution of Internet</h1>", unsafe_allow_html=True)

# Navigation Tabs using columns
col1, col_center, col2 = st.columns([1, 0.5, 1])

with col1:
    continent_tab = st.button("🌍 Continents")

with col_center:
    # Social media links
    st.markdown("""
        <div style="display: flex; justify-content: center; gap: 10px;" class="social-icons">
            <a href="https://www.linkedin.com/in/dimitrisstou/" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="50"/>
            </a>
            <a href="https://github.com/Dimitrist23/internet-usage-analysis-competition" target="_blank">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="50"/>
            </a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    country_tab = st.button("🏳️ Countries")

# Continent Tab content
if continent_tab:
    st.header("Analysis of Internet Usage by Continent:")

    # Graph 1: Global Internet Usage & Events
    st.components.v1.html(
        open("Workbook/Global.html", "r", encoding="utf-8").read(),
        height=400
    )
    st.markdown(
        "**Global Internet Usage & Events:** This graph shows global internet usage trends (2000-2023) alongside key historical events. Hover over points to see internet usage percentages and related events.")

    # Spacer for better visual separation
    st.markdown("---")

    # Graph 2: Average Growth % of Internet Usage per Continent with Historical Events
    st.components.v1.html(
        open("Workbook/ContLine.html", "r", encoding="utf-8").read(),
        height=400
    )
    st.markdown(
        "**Average Growth % of Internet Usage per Continent with Historical Events (2001-2023):** This graph displays the percentage of internet usage across continents over time, highlighting key historical events that shaped digital adoption. Hover over points to see exact usage percentages and event annotations. Use zoom to explore trends in more detail.")

    # Spacer for better visual separation
    st.markdown("---")

    # Graph 3: Annual Growth % of Internet Usage with Historical Events
    st.components.v1.html(
        open("Workbook/indepth.html", "r", encoding="utf-8").read(),
        height=400
    )
    st.markdown(
        "**Annual Growth % of Internet Usage per Continent with Historical Events (2001-2023):** This graph visualizes the annual percentage growth of internet usage across continents, overlaid with key historical events that influenced digital trends. Hover over points to see specific growth percentages and event annotations. Use zoom to explore trends in more detail.")

    # Spacer for better visual separation
    st.markdown("---")

    # Graph 4: Internet Usage by Country Over Time
    st.components.v1.html(
        open("Workbook/Globe.html", "r", encoding="utf-8").read(),
        height=700
    )
    st.markdown(
        "**Internet Usage by Country Over Time:** This interactive map displays internet usage percentages across countries from 2000 onward. Darker shades indicate higher usage rates. Hover over a country to see detailed statistics, including internet usage percentage, growth trends, and years of available data. Use the time slider or play button to observe trends over time.")

# Country Tab content
if country_tab:
    st.header("Analysis of Internet Usage by Country:")

    # Graph 1: Internet Usage Trends by Country
    st.components.v1.html(
        open("Workbook/CountryLine.html", "r", encoding="utf-8").read(),
        height=450
    )
    st.markdown(
        "**Internet Usage Trends by Country (2000-2023):** This graph shows internet usage trends (2000-2023) by country. Hover to see details, click a country to highlight, double-click to isolate, and use the slider to adjust the number of displayed countries.")

    # Spacer for better visual separation
    st.markdown("---")

    # Graph 2: Internet Usage Comparison (2000 vs 2022)
    st.components.v1.html(
        open("Workbook/ScatterCountry.html", "r", encoding="utf-8").read(),
        height=450
    )
    st.markdown(
        "**Internet Usage Comparison (2000 vs 2022):** This scatter plot compares internet usage in 2000 and 2022 across countries. Hover to see details, with colors representing different continents.")
