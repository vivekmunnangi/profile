import requests
from bs4 import BeautifulSoup

# Step 1: Scrape company info
url = 'https://www.knapp.com/en/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract company description (example: first meaningful paragraph on homepage)
# Adjust this selector if needed for better content extraction
company_description = soup.find('p').get_text() if soup.find('p') else "Company description not found."

# Step 2: Your detailed skills and experience
your_skills_experience = """
<ul>
  <li><strong>Programming Languages:</strong> Python, C++, R, SQL, ROS2</li>
  <li><strong>Data Science & Machine Learning:</strong> TensorFlow, PyTorch, Scikit-Learn, NLTK, OpenCV, Pandas, NumPy, Matplotlib</li>
  <li><strong>AI & HPC:</strong> LLMs, AutoGen, Semantic Kernel, CREW AI, NVIDIA GPUs (A100, V100, H100)</li>
  <li><strong>Web Development:</strong> MERN stack, API development, SQL databases</li>
  <li><strong>Visualization & BI Tools:</strong> Power BI, Tableau</li>
  <li><strong>Databases & Cloud:</strong> MySQL, MongoDB, AWS S3</li>
  <li><strong>Mechanical Engineering Tools:</strong> MATLAB, Ansys, SolidWorks, Fusion 360, CAD/CAM</li>
</ul>

<p><strong>Experience Highlights:</strong></p>
<ul>
  <li>Autonomous vehicle state estimation and control improving real-world performance.</li>
  <li>Designed fail-safe trajectory modules using real-time sensor fusion.</li>
  <li>ML-based 3D medical image registration with 97% accuracy.</li>
  <li>Built ETL pipelines and AI dashboards for healthcare data analytics.</li>
  <li>Developed full-stack web apps with cloud deployment.</li>
  <li>Mechanical design of high-efficiency BLDC motors and vehicle drivetrain.</li>
</ul>
"""

# Step 3: Your fit reason (can be customized)
your_fit_reason = "Passion for efficient supply chains matches Knapp's mission and innovative spirit."

# Step 4: Create personalized HTML content with basic inline CSS
about_me_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>About Me for Knapp</title>
<style>
  body {{
    font-family: Arial, sans-serif;
    max-width: 900px;
    margin: 2rem auto;
    padding: 1rem;
    background-color: #f9faff;
    color: #333;
  }}
  h1, h2 {{
    color: #0055a5;
    border-bottom: 2px solid #0055a5;
    padding-bottom: 0.3rem;
  }}
  ul {{
    line-height: 1.6;
  }}
</style>
</head>
<body>
  <h1>About Knapp</h1>
  <p>{company_description}</p>

  <h2>Why I'm a Great Fit</h2>
  <p>{your_fit_reason}</p>

  <h2>Skills and Experience</h2>
  {your_skills_experience}
</body>
</html>
"""

# Step 5: Save to file
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(about_me_html)


# Imagine you scraped the color from the company website's CSS or meta tags
primary_color = "#0070f3"  # for example, Knapp's blue

custom_css = f"""
body {{
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f0f4f8;
  color: #333;
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem;
}}

h1, h2, a {{
  color: {primary_color};
}}

h2 {{
  border-bottom: 3px solid {primary_color};
}}

a:hover {{
  border-color: {primary_color};
}}
"""

with open("style.css", "w") as f:
    f.write(custom_css)
print("Personalized About Me page generated as 'index.html'")