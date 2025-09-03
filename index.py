import requests
from bs4 import BeautifulSoup
import os
import re

# ========== Step 1: Scrape KNAPP Logo & Description ==========
url = 'https://www.knapp.com/en/company/about-us/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Logo scraping
logo_img = soup.find('img')
logo_url = logo_img['src'] if logo_img else ''
if logo_url and logo_url.startswith('/'):
    logo_url = 'https://www.knapp.com' + logo_url
"""
# Scrape first substantial paragraph
paragraphs = soup.find_all('p')
company_description = "Company description not found."
for p in paragraphs:
    text = p.get_text(strip=True)
    if len(text) > 50:  # first substantial paragraph
        company_description = text
        break


def scrape_about_page(url, save_images=True, img_folder="company_images"):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all paragraphs and headings
    content = []
    for tag in soup.find_all(["h1", "h2", "h3", "p"]):
        text = tag.get_text(strip=True)
        if text:
            content.append(text)

    # Extract a few images
    images = []
    if save_images:
        os.makedirs(img_folder, exist_ok=True)
        for img_tag in soup.find_all("img"):
            img_url = img_tag.get("src")
            if img_url and ("logo" not in img_url.lower()):  # avoid logos/icons
                if not img_url.startswith("http"):
                    img_url = url.rstrip("/") + "/" + img_url.lstrip("/")
                try:
                    img_data = requests.get(img_url).content
                    file_name = os.path.join(img_folder, os.path.basename(img_url.split("?")[0]))
                    with open(file_name, "wb") as f:
                        f.write(img_data)
                    images.append(file_name)
                except Exception as e:
                    print(f"Failed to download {img_url}: {e}")

    return {
        "text_content": "\n".join(content),
        "images": images
    }

# Example usage
result = scrape_about_page("https://www.cyngn.com/about")
print(result["text_content"][:1000])  # Print preview
print("Downloaded images:", result["images"])
"""
# ========== Step 2: Static Content ==========
# ========== Step 2: Static Content ==========

company_description = (
    "KNAPP is a global leader in warehouse automation and intelligent intralogistics systems, "
    "founded in 1952 and now operating with 8,300 employees across 49 locations worldwide. "
    "The company develops end-to-end solutions combining robotics, automation, logistics software, "
    "and digitalization. KNAPP partners with industry leaders such as Walmart to deliver "
    "Next Generation Fulfillment Centers, setting benchmarks for efficiency, scalability, "
    "and sustainability in logistics."
)

scope_content = (
    "Scope of KNAPP's work includes designing and maintaining warehouse automation systems, "
    "robotics integration, logistics software (WMS, WCS, SRC), and intelligent intralogistics solutions "
    "for industries ranging from healthcare to e-commerce. "
    "The McCordsville facility in particular focuses on high-performance distribution center operations, "
    "software reliability, and continuous optimization of automated workflows."
)

culture_content = (
    "KNAPP fosters a culture of innovation, collaboration, and continuous learning. "
    "As a family-owned company with global reach, it values diversity, teamwork, and creative problem-solving. "
    "Employees are encouraged to embrace sustainability, adapt to emerging technologies, "
    "and contribute to future-ready logistics solutions while thriving in a supportive, high-performance environment."
)

motivation_content = (
    "I am drawn to KNAPP’s ability to combine innovation with real-world impact. "
    "Their leadership in warehouse automation and partnerships with global companies like Walmart "
    "align with my goal to solve complex logistics challenges using data, AI, and scalable automation. "
    "The McCordsville facility represents a unique opportunity to contribute directly to cutting-edge software operations "
    "that power next-generation distribution systems."
)

fit_reason = (
    "With a strong background in autonomous systems, AI-driven analytics, and full-stack software development, "
    "I bring both technical expertise and practical problem-solving experience. "
    "Through my research and industry projects, I have developed skills in high-pressure troubleshooting, "
    "data-driven optimization, and cross-functional collaboration. "
    "I am adaptable, detail-oriented, and thrive in fast-paced environments — qualities that make me a strong fit "
    "for KNAPP’s mission of delivering intelligent, reliable, and sustainable logistics solutions."
)

# ========== Step 3: Experience Boxes with slideshow ==========
experience_boxes = f"""
<div class="experience-box" data-title="Research Engineer, VAIL IU">
    <h3>Research Engineer, VAIL IU</h3>
    <div class="slideshow-preview">
        <img src="../images/s_withcar.jpg" alt="Vehicle Model"/>
        <img src="../images/group_withcar.jpg" alt="Team"/>
        <img src="../images/grip_analysis.png" alt="Dashboard"/>
    </div>
    <p>State estimation, vehicle dynamics, and control development for IU Luddy Racing’s autonomous Indy Autonomous Challenge car.</p>
    <div class="full-content">
        <h3>Research Engineer, Vehicle Autonomy and Intelligence Lab – IU Luddy Racing</h3>
        <div class="image-row">
            <figure>
                <img src="../images/s_withcar.jpg" alt="Vehicle Model"/>
                <figcaption>Dallara AV-24 – IU Luddy Racing Racecar</figcaption>
            </figure>
            <figure>
                <img src="../images/group_withcar.jpg" alt="Team"/>
                <figcaption>IU Luddy Racing Team – Laguna Seca Race Weekend</figcaption>
            </figure>
        </div>

        <p>
            I joined the team in <strong>August 2024</strong>, about seven months into development, shortly after
            IU Luddy Racing announced its participation in the <strong>Indy Autonomous Challenge (IAC)</strong>.
            My focus was on <strong>state estimation and vehicle dynamics</strong>, working alongside the
            controller and localization leads to solve state-related problems and refine the dynamics model.
        </p>

        <p>
            After onboarding, I identified the need for a more advanced dynamics model and proposed a
            <strong>grip prediction module</strong> to estimate traction limits. This allowed us to design
            safer, more aggressive <strong>velocity profiles</strong> using offline planners. I also analyzed
            <strong>engine performance data</strong>, building strategies for <strong>optimal gear shifting</strong>
            based on ECU and dynamometer data to adapt power delivery to track demands.
        </p>

        <p>
            Our first dynamic module control tests took place at <strong>Las Vegas Motor Speedway (LVMS) in January 2025</strong>,
            showing promising results. Over the next months, we prepared for <strong>multi-car racing</strong>, updating the
            stack for robustness and safety. In <strong>July 2025</strong>, we competed at <strong>Laguna Seca Raceway</strong>
            against eight international teams. Despite a late practice crash that forced speed adjustments,
            we achieved <strong>4th place overall</strong> – a strong showing for our first-ever road course race
            and only our third competition as a new team.
        </p>

        <div class="image-row">
            <figure>
                <img src="../images/grip_analysis.png" alt="Dashboard"/>
                <figcaption>Grip Prediction and Race Data Analysis</figcaption>
            </figure>
        </div>

        <p>
            These milestones gave us valuable data on vehicle dynamics, localization, and controller behavior.
            Going forward, I continue developing new modules to push performance and safety, helping
            IU Luddy Racing compete at the cutting edge of autonomous motorsport.
        </p>

        <p><a href="https://vail-robotics.net/pages/people#" target="_blank">My Research Profile</a></p>
    </div>
</div>


<div class="experience-box" data-title="Partner & AI Head, DentalMatrix.ai">
    <h3>AI Head, DentalMatrix.ai</h3>
    <div class="slideshow-preview">
        <img src="../images/writeoff_description.png" alt="Dashboard"/>
        <img src="../images/writeoff_distribution.png" alt="Distribution"/>
    </div>
    <p>Co-founded and developed a unified dental platform with real-time ETL pipelines and a fine-tuned AI agent for actionable practice insights.</p>

    <div class="full-content">
        <h3>AI Head, DentalMatrix.ai</h3>

        <p>
            At DentalMatrix.ai, we built a platform to help dental clinics unify their patient and lead data. 
            Clinics often manage patient records in OpenDental and track new inquiries in GoHighLevel CRM. 
            Our solution integrates these systems into a single database, allowing clinics to track existing patients 
            and potential leads in one place. This unified data enables clinics to target marketing campaigns, convert 
            potential patients into real appointments, and improve overall operational efficiency. So with this I started working on sync operations using API on <strong>September 2024</strong>
        </p>

        <p>
            We also developed a domain-specific <strong>AI Agent</strong> to interact with clinic staff. Unlike generic 
            chatbots, this agent is fine-tuned on dental terminology, CRM data structures, and official dental abbreviations. 
            It provides answers to natural-language questions with either <strong>textual explanations or data visualizations</strong>. 
            Examples of queries include: 
            <em>"Which procedures have the highest write-offs?"</em> or 
            <em>"Show conversion rates for new patient inquiries this month."</em>
        </p>

        <p>
            The AI Agent uses a <strong>Qwen-3 base model</strong> for its multilingual capabilities, 
            allowing clinics to translate campaigns and communications into languages like Spanish automatically. 
            Fine-tuning was performed on <strong>2× H100 GPUs</strong> using <strong>DeepSpeed, Fully Sharded Data Parallel (FSDP), and parallel computing</strong> 
            to accelerate training and optimize performance.
        </p>

        <p>
            The backend includes a robust <strong>ETL pipeline</strong> that extracts and synchronizes structured data 
            from OpenDental and the CRM into a centralized relational database. This enables real-time CRUD operations 
            and ensures all patient and lead information is immediately up-to-date.
        </p>
        <p> When asked about <em>"Which procedures have the highest write-offs?"</em>, the agent reaponse as text was <em> "The WriteOff is calculated as: (Sum of all fees on procedures - Sum of all insurance estimates and insurance payments received) + WriteoffsAlreadySent.  It's not just a simple sum of all writeoffs.  The user can never directly edit this field, but it is possible to set it blank.  If the WriteOff value is higher than the WriteOffEst, then we show the WriteOff value in color red.  This means that it has been manually altered from the estimate. We don't currently track who changed it."</em>, and the visual response as shown below </p>
        <div class="image-row">
            <figure>
                <img src="../images/writeoff_description.png" alt="Dashboard"/>
                <figcaption>AI Agent visualization: Patient write-off insights</figcaption>
            </figure>
            <figure>
                <img src="../images/writeoff_distribution.png" alt="Distribution"/>
                <figcaption>AI Agent visualization: Distribution of total write-offs amount</figcaption>
            </figure>
        </div>

        <p>
            This platform provides dental clinics with a unified view of all contacts, actionable insights for resource planning, 
            marketing, and patient management, and an intelligent assistant designed specifically for dental operations. 
            With this foundation, clinics can better understand patient needs, optimize marketing efforts, 
            and deliver higher quality care efficiently.
        </p>
    </div>
</div>


<div class="experience-box" data-title="Research Assistant">
    <h3>Research Assistant, Frontiers of Optical Imaging and Biology Lab</h3>
    
    <div class="slideshow-preview">
        <img src="../images/lab_logo.png" alt="Lab Logo"/>
        <img src="../images/Mice_Eye_3D.png" alt="3D Eye Scan"/>
        <img src="../images/is_after.png" alt="Registered Eye Scan"/>
    </div>
    
    <p>Developed a dynamic 3D image registration pipeline to correct cellular-level motion in high-resolution eye scans across multiple subjects.</p>
    
    <div class="full-content">
        <h3>Research Assistant, Frontiers of Optical Imaging and Biology Lab</h3>
        <p>
            In this research, I worked on aligning 3D eye scan datasets from humans, mice, and bovine subjects. 
            Each scan captures cellular structures at <strong>2 µm focus</strong>, where even small biological motions 
            or scanner delays cause misalignment. The goal was to dynamically correct drift while preserving the natural movement of cells.
        </p>
        
        <p>
            The workflow included:
            <ul>
                <li><strong>Pixel classification:</strong> Identified cell bodies, nuclei, and background pixels using intensity distribution and pooling. Noise pixels were removed.</li>
                <li><strong>Dynamic registration:</strong> Sequentially aligned frames by tracking drift and adjusting each frame relative to the first, while allowing live cells to move naturally.</li>
                <li><strong>Subject-agnostic design:</strong> The code works across different species and datasets without manual tuning.</li>
            </ul>
        </p>
        <div class="image-row">
            <figure>
                <img src="../images/sv_before_drift.png" alt="Side view before"/>
                <figcaption>Side view before registration</figcaption>
            </figure>
            <figure>
                <img src="../images/sv_after_drift.png" alt="Side view after"/>
                <figcaption>Side view after registration</figcaption>
            </figure>
        </div>

        <div class="image-row">
            <figure>
                <img src="../images/sv_before.png" alt="Front view before"/>
                <figcaption>Front view before registration</figcaption>
            </figure>
            <figure>
                <img src="../images/sv_after.png" alt="Front view after"/>
                <figcaption>Front view after registration</figcaption>
            </figure>
        </div>

        <p>
            The registration consistently produced highly quality alignment with 97% and at  6.5 MB/s processing speed, making cellular structures clearly visible 
            in top, front, and side views, and enabling downstream analysis of cell motion and behavior.
        </p>
        

        <div class="image-row">
            <figure>
                <img src="../images/is_before.png" alt="Top view before"/>
                <figcaption>Top view before registration (3D stack)</figcaption>
            </figure>
            <figure>
                <img src="../images/is_after.png" alt="Top view after"/>
                <figcaption>Top view after registration (3D stack)</figcaption>
            </figure>
        </div>
        <div class="image-row">
            <figure>
                <img src="../images/Mice_Eye_3D.png" alt="Top view before"/>
                <figcaption>Mice Eye constructed as 3D image from scan</figcaption>
            </figure>
        </div>
        <p><a href="https://blogs.iu.edu/tankamlab/people/" target="_blank">My Research Profile</a></p>
    </div>
</div>

<div class="experience-box" data-title="Consultant, EDD chat assistant">
    <h3>Consultant, EDD chat assistant</h3>

    <div class="slideshow-preview">
        <img src="../images/edd_logo.png" alt="CEDS Dashboard"/>
        <img src="../images/ceds_template.png" alt="AI Integration"/>
        <img src="../images/edd_region.png" alt="AI Integration"/>
    </div>

    <p>Developed an AI-driven tool to assist Economic Development Districts (EDDs) in creating Comprehensive Economic Development Strategies (CEDS).</p>

    <div class="full-content">
        <h3>Consultant, EDD chat assistant</h3>

        <p>
            From August 2024 to January 2025, I worked on integrating AI into the **CEDS creation process** for under-resourced Economic Development Districts (EDDs). 
            The CEDS is a strategic plan used to drive regional economic growth and is critical for securing federal funding through the Economic Development Administration (EDA). 
            Many EDDs face challenges in creating strong CEDS documents due to limited resources, expertise, and access to data.
        </p>
        <div class="image-row">
            <figure>
                <img src="../images/edd_region.png" alt="Top view before"/>
                <figcaption>Interactive map of Economic Development District - EDD Zones</figcaption>
            </figure>

        <p>
            <strong>Problem:</strong> Creating a robust CEDS is time-intensive and requires data analysis, stakeholder engagement, and alignment with EDA guidelines. Smaller districts often struggle to meet these requirements, delaying funding and limiting economic development opportunities.
        </p>

        <p>
            <strong>Solution:</strong> The project aimed to develop an AI-driven CEDS generator that leverages generative AI and transformer-based models to automate key parts of the process. Key features include:
            <ul>
                <li><strong>Structured Input Interface:</strong> Predefined fields for entering regional data to ensure alignment with EDA guidelines.</li>
                <li><strong>LLM Integration:</strong> Large language models process inputs and generate region-specific strategies using historical CEDS data.</li>
                <li><strong>SWOT Automation:</strong> AI-assisted SWOT analyses and strategic recommendations based on regional data.</li>
                <li><strong>Evaluation Framework Alignment:</strong> Automated feedback to ensure generated CEDS meets EDA evaluation criteria.</li>
                <li><strong>Scalability:</strong> Modular design allowing use across multiple EDDs with regional customization.</li>
            </ul>
        </p>
        <div class="image-row">
            <figure>
                <img src="../images/ceds_template.png" alt="Top view before"/>
                <figcaption>Basic CEDS Template</figcaption>
            </figure>
            <figure>
                <img src="../images/inital_proposal.png" alt="Top view after"/>
                <figcaption>Initial Proposal</figcaption>
            </figure>
        <p>
            <strong>Implementation Strategy:</strong> 
            - Built a prototype integrating AI( used VLLM mistral architecture with mutiple Lora adaptors targeting different layers of base model) with SWOT analysis and draft CEDS generation.  
            - Used cosine similarity to compare generated content against approved CEDS documents, focusing on areas like climate resilience and equity.  
            - Incorporated feedback loops for planners to iteratively refine inputs and outputs.  
            - Designed front-end mockups and modular agent frameworks for user-friendly interaction.
        </p>

        <p>
            <strong>Impact:</strong> This project demonstrated the potential for AI to streamline CEDS creation, automate labor-intensive tasks, and improve document quality and compliance. The prototype empowered planners to create data-backed, EDA-compliant strategies more efficiently.  
            While I paused working on this project after January 2025 due to time constraints, the foundation provides a scalable framework for future AI-assisted economic development tools.
        </p>

        <div class="image-row">
            <figure>
                <img src="../images/pn_analysis.png" alt="CEDS Dashboard"/>
                <figcaption>Positive and negative statment analysis per topics</figcaption>
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
<title>Portfolio</title>
<style>
body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin:0; padding:0; background:#f0f4f8; color:#333; }}
header {{ display:flex; align-items:center; padding:1rem 2rem; background:#fff; border-bottom:2px solid #ccc; }}
header img {{ height:60px; margin-right:20px; }}
main {{ max-width:1000px; margin:2rem auto; padding:0 2rem; }}
h1,h2,h3 {{ color:#0055a5; }}
h2 {{ border-bottom:2px solid #0055a5; padding-bottom:0.3rem; margin-bottom:1rem; }}
section {{ margin-bottom:3rem; }}

.experience-grid {{
  display: grid;
  gap: 1.5rem;
}}

/* Mobile: 1 per row */
@media (max-width: 600px) {{
  .experience-grid {{
    grid-template-columns: 1fr;
  }}
}}

/* Tablet: 2 per row */
@media (min-width: 601px) and (max-width: 1000px) {{
  .experience-grid {{
    grid-template-columns: repeat(2, 1fr);
  }}
}}

/* Desktop: 3 per row */
@media (min-width: 1001px) {{
  .experience-grid {{
    grid-template-columns: repeat(3, 1fr);
  }}
}}

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
    <h1>Career</h1>
</header>
<main>
    <section><h2>Company Description</h2><p>{company_description}</p></section>
    <section><h2>Scope</h2><p>{scope_content}</p></section>
    <section><h2>Work Culture</h2><p>{culture_content}</p></section>
    <section><h2>Motivation to Join KNAPP</h2><p>{motivation_content}</p></section>
    <section><h2>Why I am a Great Fit</h2><p>{fit_reason}</p></section>
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
