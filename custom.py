import requests
from bs4 import BeautifulSoup

# Step 1: Scrape logo and description
url = 'https://www.knapp.com/en/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

logo_img = soup.find('img')
logo_url = logo_img['src'] if logo_img else ''
if logo_url and logo_url.startswith('/'):
    logo_url = 'https://www.knapp.com' + logo_url

company_description = soup.find('p').get_text(strip=True) if soup.find('p') else "Company description not found."

# Step 2: Add your content
scope_content = "Scope of KNAPP's work includes warehouse automation, robotics, logistics software, and intelligent intralogistics systems."
culture_content = "KNAPP fosters innovation, teamwork, and continuous learning, focusing on sustainability and future-ready logistics solutions."
motivation_content = "I'm drawn to KNAPP’s blend of innovation and purpose. Their leadership in automation aligns with my goal to solve impactful logistics challenges using data and AI."
fit_reason = "With hands-on experience in autonomous systems, AI, and full-stack development, I bring both the technical depth and adaptability KNAPP values."

experiences = [
    {
        "title": "Research Engineer",
        "summary": "Developed state estimation and autonomous control for race vehicles, improving average lap speed by 20mph."
    },
    {
        "title": "AI Partner, dentalmatrix.ai",
        "summary": "Built real-time ETL pipelines and deployed LLM-powered analytics tools for dental practice intelligence."
    },
    {
        "title": "Research Assistant, Imaging Lab",
        "summary": "Designed neural networks to register 3D eye scan volumes without reference points, achieving 97% accuracy."
    }
]

# Step 3: Build HTML
experience_boxes = ""
for exp in experiences:
    experience_boxes += f"""
    <div class="experience-box">
      <h3>{exp['title']}</h3>
      <p>{exp['summary']}</p>
    </div>
    """

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>About Me & KNAPP</title>
  <style>
    body {{
      font-family: 'Segoe UI', Tahoma, sans-serif;
      background-color: #f0f4f8;
      color: #333;
      margin: 0;
      padding: 0;
    }}
    header {{
      display: flex;
      align-items: center;
      padding: 1rem 2rem;
      background-color: white;
      border-bottom: 2px solid #ccc;
    }}
    header img {{
      height: 60px;
      margin-right: 20px;
    }}
    main {{
      max-width: 1000px;
      margin: 2rem auto;
      padding: 0 2rem;
    }}
    section {{
      margin-bottom: 3rem;
    }}
    h1, h2, h3 {{
      color: #0055a5;
    }}
    .experience-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
    }}
    .experience-box {{
      background: white;
      padding: 1rem;
      border-left: 5px solid #0055a5;
      box-shadow: 0 0 10px rgba(0,0,0,0.05);
      transition: transform 0.3s ease;
    }}
    .experience-box:hover {{
      transform: scale(1.03);
    }}
  </style>
</head>
<body>
  <header>
    <img src="{logo_url}" alt="KNAPP Logo" />
    <h1>About KNAPP</h1>
  </header>
  <main>
    <section>
      <h2>Company Description</h2>
      <p>{company_description}</p>
    </section>

    <section>
      <h2>Scope</h2>
      <p>{scope_content}</p>
    </section>

    <section>
      <h2>Work Culture</h2>
      <p>{culture_content}</p>
    </section>

    <section>
      <h2>Motivation to Join KNAPP</h2>
      <p>{motivation_content}</p>
    </section>

    <section>
      <h2>Why I'm a Great Fit</h2>
      <p>{fit_reason}</p>
    </section>

    <section>
      <h2>Work Experience</h2>
      <div class="experience-grid">
        {experience_boxes}
      </div>
    </section>
  </main>
</body>
</html>
"""

# Step 4: Save HTML file
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ index.html generated.")



primary_color = "#0055a5"  # KNAPP-style blue

custom_css = f"""
body {{
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f0f4f8;
  color: #333;
  margin: 0;
  padding: 0;
}}

header {{
  display: flex;
  align-items: center;
  padding: 1rem 2rem;
  background-color: white;
  border-bottom: 2px solid #ccc;
}}

header img {{
  height: 60px;
  margin-right: 20px;
}}

main {{
  max-width: 1000px;
  margin: 2rem auto;
  padding: 0 2rem;
}}

section {{
  margin-bottom: 3rem;
}}

h1, h2, h3 {{
  color: {primary_color};
}}

h2 {{
  border-bottom: 2px solid {primary_color};
  padding-bottom: 0.3rem;
  margin-bottom: 1rem;
}}

.experience-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}}

.experience-box {{
  background: white;
  padding: 1rem;
  border-left: 5px solid {primary_color};
  box-shadow: 0 0 10px rgba(0,0,0,0.05);
  transition: transform 0.3s ease;
}}

.experience-box:hover {{
  transform: scale(1.03);
}}

a {{
  color: {primary_color};
  text-decoration: none;
}}

a:hover {{
  text-decoration: underline;
}}
"""

with open("style.css", "w") as f:
    f.write(custom_css)

print("✅ Updated style.css generated.")
