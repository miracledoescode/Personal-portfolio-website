import streamlit as st
from PIL import Image
import base64

# Page configuration
st.set_page_config(
	page_title="Miracle Mathew - Portfolio",
	page_icon="🚀",
	layout="wide",
	initial_sidebar_state="collapsed"
)


# Custom CSS for styling
def load_css():
	st.markdown("""
    <style>
    /* Import fonts */
    @import url('https://fonts.googleapis.com/css2?family=Segoe+UI:wght@300;400;500;600;700;800&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');

    /* Root variables */
    :root {
        --primary: #80cfff;
        --primary-dark: #48a9ff;
        --bg-dark: #121212;
        --bg-light: #1b1b1b;
        --text: #e0e0e0;
        --text-muted: #b0bec5;
        --card-bg: rgba(27, 27, 27, 0.7);
    }

    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Main app styling */
    .stApp {
        background: linear-gradient(45deg, #121212, #1a1a1a, #242424);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: var(--text);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Hero section */
    .hero-container {
        background: rgba(27, 27, 27, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 4rem 2rem;
        margin: 2rem 0;
        position: relative;
        overflow: hidden;
    }

    .hero-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(128, 207, 255, 0.1), transparent);
        z-index: 1;
    }

    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(45deg, var(--primary), var(--primary-dark));
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        animation: fadeIn 1s ease-out;
    }

    .hero-subtitle {
        font-size: 1.5rem;
        color: var(--text-muted);
        margin-bottom: 1.5rem;
        animation: fadeIn 1s ease-out 0.5s both;
    }

    .hero-description {
        font-size: 1.1rem;
        color: var(--text-muted);
        animation: fadeIn 1s ease-out 1s both;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Profile image */
    .profile-image {
        width: 280px;
        height: 280px;
        border-radius: 50%;
        border: 3px solid var(--primary);
        box-shadow: 0 0 20px rgba(128, 207, 255, 0.3);
        animation: float 6s ease-in-out infinite;
        margin: 0 auto;
        display: block;
    }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }

    /* Section titles */
    .section-title {
        text-align: center;
        margin: 3rem 0;
        position: relative;
    }

    .section-title h2 {
        font-size: 2.5rem;
        color: var(--primary);
        margin-bottom: 1rem;
    }

    .section-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 60px;
        height: 3px;
        background: var(--primary);
        border-radius: 2px;
    }

    /* Project cards */
    .project-card {
        background: rgba(27, 27, 27, 0.7);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        border: 1px solid rgba(128, 207, 255, 0.2);
    }

    .project-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        border-color: var(--primary);
    }

    .project-title {
        font-size: 1.25rem;
        color: var(--primary);
        margin-bottom: 1rem;
        font-weight: 600;
    }

    .project-description {
        color: var(--text-muted);
        margin-bottom: 1.5rem;
        line-height: 1.6;
    }

    .project-link {
        display: inline-block;
        padding: 0.8rem 1.5rem;
        background: transparent;
        border: 2px solid var(--primary);
        color: var(--primary);
        border-radius: 25px;
        text-decoration: none;
        transition: all 0.3s ease;
        font-weight: 500;
    }

    .project-link:hover {
        background: var(--primary);
        color: var(--bg-dark);
        text-decoration: none;
    }

    /* Skills */
    .skill-item {
        background: rgba(27, 27, 27, 0.7);
        padding: 1rem 2rem;
        border-radius: 25px;
        border: 2px solid var(--primary);
        color: var(--primary);
        font-weight: 500;
        margin: 0.5rem;
        display: inline-block;
        transition: all 0.3s ease;
    }

    .skill-item:hover {
        background: var(--primary);
        color: var(--bg-dark);
        transform: translateY(-5px);
    }

    /* Contact section */
    .contact-container {
        text-align: center;
        padding: 2rem;
        background: rgba(27, 27, 27, 0.7);
        border-radius: 15px;
        margin: 2rem 0;
    }

    .contact-button {
        display: inline-block;
        padding: 1rem 2rem;
        background: var(--primary);
        color: var(--bg-dark);
        border-radius: 30px;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s ease;
        margin: 1rem;
    }

    .contact-button:hover {
        background: var(--primary-dark);
        transform: translateY(-5px);
        text-decoration: none;
    }

    .social-links {
        margin-top: 2rem;
        display: flex;
        justify-content: center;
        gap: 2rem;
    }

    .social-link {
        color: var(--primary);
        font-size: 1.5rem;
        transition: all 0.3s ease;
        text-decoration: none;
    }

    .social-link:hover {
        color: var(--primary-dark);
        transform: translateY(-5px);
        text-decoration: none;
    }

    /* Navigation */
    .nav-container {
        background: rgba(31, 31, 31, 0.95);
        backdrop-filter: blur(10px);
        padding: 1rem 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .logo {
        font-size: 1.5rem;
        font-weight: 700;
        background: linear-gradient(45deg, var(--primary), var(--primary-dark));
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Responsive design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }

        .hero-subtitle {
            font-size: 1.2rem;
        }

        .profile-image {
            width: 200px;
            height: 200px;
        }

        .section-title h2 {
            font-size: 2rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def create_navigation():
	st.markdown("""
    <div class="nav-container">
        <div class="logo">Miracle's Personal Portfolio</div>
    </div>
    """, unsafe_allow_html=True)


def create_hero_section():
	st.markdown("""
    <div class="hero-container">
    """, unsafe_allow_html=True)
	
	col1, col2 = st.columns([2, 1])
	
	with col1:
		st.markdown("""
        <div style="position: relative; z-index: 2;">
            <h1 class="hero-title">Miracle Mathew</h1>
            <h2 class="hero-subtitle">AI/ML Student dev & Software developer</h2>
            <p class="hero-description">Hello! I'm a passionate software developer specializing in building clean, performant digital experiences and AI applications tailored to your needs.</p>
        </div>
        """, unsafe_allow_html=True)
	
	with col2:
		# Create a placeholder profile image
		st.markdown("""
        <div style="text-align: center; position: relative; z-index: 2;">
            <div class="profile-image" style="background: linear-gradient(45deg, #80cfff, #48a9ff); display: flex; align-items: center; justify-content: center; font-size: 4rem; font-weight: bold; color: #121212;">
                MM
            </div>
        </div>
        """, unsafe_allow_html=True)
	
	st.markdown("</div>", unsafe_allow_html=True)


def create_projects_section():
	st.markdown("""
    <div class="section-title">
        <h2>Projects</h2>
    </div>
    """, unsafe_allow_html=True)
	
	col1, col2, col3 = st.columns(3)
	
	projects = [
		{
			"title": "Currency Converter",
			"description": "A real-time currency converting application built for traders, forex experts, businesses and foreign exchange.",
			"link": "#"
		},
		{
			"title": "Weather App",
			"description": "A real-time weather application with location-based forecasts and dynamic backgrounds powered by a OpenWeather API.",
			"link": "#"
		},
		{
			"title": "Todo App",
			"description": "A simple yet powerful to-do list application with local storage support and intuitive user interface, using streamlit as the UI.",
			"link": "#"
		}
	]
	
	for i, (col, project) in enumerate(zip([col1, col2, col3], projects)):
		with col:
			st.markdown(f"""
            <div class="project-card">
                <h3 class="project-title">{project['title']}</h3>
                <p class="project-description">{project['description']}</p>
                <a href="{project['link']}" target="_blank" class="project-link">View Project</a>
            </div>
            """, unsafe_allow_html=True)


def create_skills_section():
	st.markdown("""
    <div class="section-title">
        <h2>Skills</h2>
    </div>
    """, unsafe_allow_html=True)
	
	skills = [
		"HTML5", "CSS3", "JavaScript", "React", "Node.js",
		"C++", "SAAS", "Python", "Django", "AI/ML", "Data Science"
	]
	
	# Create skills grid
	skills_html = '<div style="text-align: center; margin: 2rem 0;">'
	for skill in skills:
		skills_html += f'<span class="skill-item">{skill}</span>'
	skills_html += '</div>'
	
	st.markdown(skills_html, unsafe_allow_html=True)


def create_contact_section():
	st.markdown("""
    <div class="section-title">
        <h2>Contact Me</h2>
    </div>
    """, unsafe_allow_html=True)
	
	st.markdown("""
    <div class="contact-container">
        <p style="color: var(--text-muted); margin-bottom: 2rem; font-size: 1.1rem;">
            If you'd like to get in touch, feel free to connect via social media.
        </p>
        <div class="social-links">
            <a href="https://github.com/miracledoescode" class="social-link" target="_blank">
                <i class="fab fa-github"></i>
            </a>
            <a href="https://www.linkedin.com/in/miracle-mathew-8b0137354/" class="social-link" target="_blank">
                <i class="fab fa-linkedin"></i>
            </a>
            <a href="https://twitter.com/miraclesayscode" class="social-link" target="_blank">
                <i class="fab fa-twitter"></i>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)


def create_footer():
	st.markdown("""
    <div style="text-align: center; padding: 2rem; color: var(--text-muted); margin-top: 3rem;">
        <p>&copy; 2025 GreyCode. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)


def main():
	# Load custom CSS
	load_css()
	
	# Create navigation
	create_navigation()
	
	# Create sections
	create_hero_section()
	create_projects_section()
	create_skills_section()
	create_contact_section()
	create_footer()


if __name__ == "__main__":
	main()
