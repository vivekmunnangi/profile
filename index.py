import os
import requests
from bs4 import BeautifulSoup

# ========== Step 1: Scrape KNAPP Logo & Description ==========
url = 'https://www.knapp.com/en/company/about-us/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Logo scraping
logo_img = soup.find('img')
logo_url = logo_img['src'] if logo_img else ''
if logo_url and logo_url.startswith('/'):
    logo_url = 'https://www.knapp.com' + logo_url

# Scrape first substantial paragraph
paragraphs = soup.find_all('p')
company_description = "Company description not found."
for p in paragraphs:
    text = p.get_text(strip=True)
    if len(text) > 50:  # first substantial paragraph
        company_description = text
        break

# ========== Step 2: Static Content ==========
scope_content = "Scope of KNAPP's work includes warehouse automation, robotics, logistics software, and intelligent intralogistics systems."
culture_content = "KNAPP fosters innovation, teamwork, and continuous learning, focusing on sustainability and future-ready logistics solutions."
motivation_content = "I'm drawn to KNAPP’s blend of innovation and purpose. Their leadership in automation aligns with my goal to solve impactful logistics challenges using data and AI."
fit_reason = "With hands-on experience in autonomous systems, AI, and full-stack development, I bring both the technical depth and adaptability KNAPP values."

# ========== Step 3: Experience Boxes with slideshow ==========
experience_boxes = f"""
<div class="experience-box" data-title="Research Engineer, VAIL IU">
    <h3>Research Engineer</h3>
    <div class="slideshow-preview">
        <img src="../images/s_withcar.jpg" alt="Vehicle Model"/>
        <img src="../images/group_withcar.jpg" alt="Team"/>
        <img src="../images/grip_analysis.png" alt="Dashboard"/>
    </div>
    <p>Developed state estimation and autonomous control for race vehicles.</p>
    <div class="full-content">
        <div class="image-row">
            <figure>
                <img src="../images/s_withcar.jpg" alt="Vehicle Model"/>
                <figcaption>Dallara AV24 IU Luddy Racecar</figcaption>
            </figure>
            <figure>
                <img src="../images/group_withcar.jpg" alt="Trajectory Plot"/>
                <figcaption>IU Luddy Team at Laguna Sega Race weekend</figcaption>
            </figure>
        </div>
        <p>I worked on state estimation algorithms for autonomous racecars, using Kalman filtering and sensor fusion to refine vehicle positioning. The controller modules used MPC for high-speed path planning. The system improved lap times by dynamically adjusting for road friction.</p>
        <div class="image-row">
            <figure>
                <img src="../images/grip_analysis.png" alt="Dashboard"/>
                <figcaption>Grip Analysis on Race data</figcaption>
            </figure>
        </div>
        <p><a href="https://vail-robotics.net/pages/people#" target="_blank">My Research Profile</a></p>
    </div>
</div>

<div class="experience-box" data-title="AI Head, dentalmatrix.ai">
    <h3>Research Engineer</h3>
    <div class="slideshow-preview">
        <img src="../images/writeoff_description.png" alt="Dashboard"/>
        <img src="../images/writeoff_distribution.png" alt="Distribution"/>
    </div>
    <p>Built real-time ETL pipelines and deployed LLM-powered analytics tools for dental practice intelligence.</p>
    <div class="full-content">
        <p>Created an API to integrate OpenDental with CRM platforms, building an ETL pipeline to extract and sync structured data into a centralized relational database. Utilized SQL for querying and transforming patient and billing data, enabled seamless CRUD operations and 100% real-time synchronization. Using unstructured text and relative fields in database, and with custom build agent (Qwen3 architecture) to answer questions and create workforce-analytics dashboards.</p>
        <div class="image-row">
            <figure>
                <img src="../images/writeoff_description.png" alt="Dashboard"/>
                <figcaption>Visualization output from Agent</figcaption>
            </figure>
            <figure>
                <img src="../images/writeoff_distribution.png" alt="Dashboard"/>
                <figcaption>Visualization output from Agent</figcaption>
            </figure>
        </div>
    </div>
</div>
"""

# ========== Step 4: Full HTML ==========
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>About Me & KNAPP</title>
<style>
body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin:0; padding:0; background:#f0f4f8; color:#333; }}
header {{ display:flex; align-items:center; padding:1rem 2rem; background:#fff; border-bottom:2px solid #ccc; }}
header img {{ height:60px; margin-right:20px; }}
main {{ max-width:1000px; margin:2rem auto; padding:0 2rem; }}
h1,h2,h3 {{ color:#0055a5; }}
h2 {{ border-bottom:2px solid #0055a5; padding-bottom:0.3rem; margin-bottom:1rem; }}
section {{ margin-bottom:3rem; }}
.experience-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:1.5rem; }}
.experience-box {{
    background:#fff; padding:1rem; border-left:5px solid #0055a5; box-shadow:0 0 10px rgba(0,0,0,0.05);
    cursor:pointer; display:flex; flex-direction:column; justify-content:space-between; aspect-ratio:1/1; position:relative;
}}
.experience-box h3 {{ margin-top:0; text-align:center; }}
.experience-box p {{ text-align:center; margin-top:0.5rem; }}
.experience-box .full-content {{ display:none; }}
.slideshow-preview {{ position:relative; width:100%; flex:1; margin:0.5rem 0; overflow:hidden; }}
.slideshow-preview img {{
    position:absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; opacity:0; transition:opacity 1s;
}}
.slideshow-preview img.active {{ opacity:1; }}
a {{ color:#0055a5; text-decoration:none; }}
a:hover {{ text-decoration:underline; }}
.modal {{ display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.7); justify-content:center; align-items:center; z-index:1000; }}
.modal-content {{ background:#fff; padding:2rem; max-width:800px; width:90%; max-height:90%; overflow-y:auto; position:relative; border-radius:8px; }}
.modal-close {{ position:absolute; top:1rem; right:1rem; font-size:1.5rem; cursor:pointer; color:#0055a5; }}
.image-row {{ display:flex; gap:1rem; flex-wrap:wrap; justify-content:center; margin-bottom:1rem; }}
.image-row figure {{ flex:1 1 200px; text-align:center; margin:0; }}
.image-row img {{ width:100%; height:auto; object-fit:contain; }}
</style>
</head>
<body>
<header>
    <img src="{logo_url}" alt="KNAPP Logo"/>
    <h1>About KNAPP</h1>
</header>
<main>
    <section><h2>Company Description</h2><p>{company_description}</p></section>
    <section><h2>Scope</h2><p>{scope_content}</p></section>
    <section><h2>Work Culture</h2><p>{culture_content}</p></section>
    <section><h2>Motivation to Join KNAPP</h2><p>{motivation_content}</p></section>
    <section><h2>Why I'm a Great Fit</h2><p>{fit_reason}</p></section>
    <section><h2>Work Experience</h2>
        <div class="experience-grid">
            {experience_boxes}
        </div>
    </section>
</main>

<div class="modal" id="modal">
    <div class="modal-content" id="modal-content">
        <span class="modal-close" id="modal-close">&times;</span>
        <div id="modal-inner"></div>
    </div>
</div>

<script>
const boxes = document.querySelectorAll('.experience-box');
const modal = document.getElementById('modal');
const modalInner = document.getElementById('modal-inner');
const modalClose = document.getElementById('modal-close');

// Small preview slideshow
boxes.forEach(box => {{
    const previewImgs = box.querySelectorAll('.slideshow-preview img');
    if(previewImgs.length > 0){{
        let current = 0;
        previewImgs[current].classList.add('active');
        setInterval(()=>{{
            previewImgs[current].classList.remove('active');
            current = (current+1) % previewImgs.length;
            previewImgs[current].classList.add('active');
        }},3000);
    }}
}});

// Modal logic
boxes.forEach(box => {{
    box.addEventListener('click', () => {{
        const content = box.querySelector('.full-content');
        if(content) {{
            modalInner.innerHTML = content.innerHTML;
            modal.style.display = 'flex';
        }}
    }});
}});

modalClose.addEventListener('click', () => {{ modal.style.display = 'none'; }});
window.addEventListener('click', (e) => {{ if(e.target == modal) modal.style.display = 'none'; }});
</script>
</body>
</html>
"""

# ========== Step 5: Write HTML ==========
output_dir = "./knapp"
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("✅ index.html generated.")
