import streamlit as st
import os
import pandas as pd
import re
from io import StringIO
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

engine_llm = LLM(
    model="groq/llama-3.3-70b-versatile", 
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.0
)

st.set_page_config(page_title="Aegis BI | Elite Engine", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FDF5E6; }
    .main .block-container { padding-top: 0rem !important; margin-top: -65px !important; }
    h1 { color: #5D4037 !important; font-family: 'Segoe UI', sans-serif; font-weight: 800; font-size: 28px !important; }
    h2 { color: #8B4513 !important; font-family: 'Segoe UI', sans-serif; font-weight: 700; font-size: 22px !important; margin-bottom: 10px; }
    .insight-card { background-color: #FFF9F0; padding: 20px; border-left: 5px solid #D4AF37; border-top: 1px solid #E5D3B3; margin-bottom: 20px; font-weight: 500; font-size: 15px; color: #5D4037; line-height: 1.8; }
    
    .stButton>button { 
        background-color: #D4AF37 !important; 
        color: #FFFFFF !important; 
        font-weight: 700; 
        height: 48px; 
        border-radius: 6px; 
        border: none;
        transition: all 0.3s ease-in-out !important;
    }
    
    .stButton>button:hover { 
        background-color: #8B4513 !important; 
        color: #FDF5E6 !important;
        box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.4);
        border: 1px solid #D4AF37 !important;
    }

    .sidebar-text { font-size: 14px; font-weight: 700; color: #8B4513; margin-top: 25px; margin-bottom: 10px; }
    hr { border: 0; height: 1px; background-image: linear-gradient(to right, rgba(212, 175, 55, 0), rgba(212, 175, 55, 0.75), rgba(212, 175, 55, 0)); margin: 20px 0; }
    </style>
    """, unsafe_allow_html=True)

if 'vault' not in st.session_state: st.session_state.vault = {}
if 'page' not in st.session_state: st.session_state.page = "MAIN"

with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>AEGIS ARCHITECT</h2>", unsafe_allow_html=True)
    if st.button("NEW ANALYSIS"): st.session_state.page = "MAIN"
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown('<p class="sidebar-text">PREVIOUS RESEARCH</p>', unsafe_allow_html=True)
    for key in list(st.session_state.vault.keys()):
        display_label = " ".join(key.split()[:2]) + " ...."
        if st.button(display_label, key=key): st.session_state.page = key

if st.session_state.page == "MAIN":
    st.markdown("<h1>AEGIS BI LIGHTNING ENGINE</h1>", unsafe_allow_html=True)
    query = st.text_input("TARGET DOMAIN (2026):", placeholder="e.g., AgriTech in Tamil Nadu")
    
    if st.button("EXECUTE FAST SYNTHESIS"):
        if query:
            with st.spinner("Synthesizing Content and Architecture..."):
                try:
                    master_agent = Agent(
                        role='Elite BI Data Architect',
                        goal=f'Provide 4 brief bullet points followed by a 40-row dataset for {query}.',
                        backstory='Senior Architect at Zoho. You never omit the strategic insights. You deliver professional, brief bullet points before the data marker.',
                        llm=engine_llm
                    )

                    t1 = Task(
                        description=f'''Mandatory Sequence for {query}:
                        1. Write exactly 4 brief, one-line bullet points (no emojis).
                        2. Write the separator ###DATA### on its own line.
                        3. Provide the 40-row CSV (Category, Entity_Name, Metric, Investment_Cr, Growth_Rate_%).
                        
                        Strictly follow the order: Insights FIRST, then Marker, then CSV.''',
                        expected_output='Brief bullet points followed by marker and CSV.',
                        agent=master_agent
                    )

                    crew = Crew(agents=[master_agent], tasks=[t1], process=Process.sequential)
                    result = crew.kickoff()

                    raw_output = str(result.raw)
                    if "###DATA###" in raw_output:
                        text_part, csv_part = raw_output.split("###DATA###")
                        insights = text_part.strip()
                        clean_csv = csv_part.replace('```csv', '').replace('```', '').strip()
                        
                        df = pd.read_csv(StringIO(clean_csv))
                        
                        if "Tamil Nadu" in query or "TN" in query:
                            df = df[~df['Entity_Name'].str.contains('Thiruvananthapuram|Kochi|Kerala|Bangalore|Hyderabad', case=False, na=False)]
                        
                        df = df.drop_duplicates(subset=['Entity_Name']).head(40)
                        df['Investment_Cr'] = pd.to_numeric(df['Investment_Cr'], errors='coerce').abs().fillna(1500)
                        df['Category'] = df['Category'].str.strip()
                        df = df.sort_values(by='Category', ascending=False)
                        
                        df['Performance_Index'] = df.groupby('Category')['Investment_Cr'].transform(
                            lambda x: (((x - x.min()) / (x.max() - x.min())) * 60 + 40).round(1) if (x.max() != x.min()) else 82.5
                        ).fillna(82.5)

                        st.session_state.vault[query] = {'insights': insights, 'df': df}
                        st.session_state.page = query
                        st.rerun()
                    else:
                        st.error("Sequence Error. Retrying...")
                except Exception as e:
                    st.error(f"Engine Log: {e}")
else:
    data = st.session_state.vault[st.session_state.page]
    st.markdown(f"<h2>REPORT: {st.session_state.page.upper()}</h2>", unsafe_allow_html=True)
    
    if data['insights']:
        st.markdown('<div class="insight-card">' + data['insights'] + '</div>', unsafe_allow_html=True)
    
    st.markdown("<h3 style='color: #8B4513;'>MASTER POWER BI DATASET</h3>", unsafe_allow_html=True)
    st.dataframe(data['df'], use_container_width=True, hide_index=True)
    st.download_button(label="DOWNLOAD LOAD-READY CSV", data=data['df'].to_csv(index=False), file_name=f"aegis_master.csv", mime="text/csv")