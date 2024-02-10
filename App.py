import json
import os
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from dotenv import load_dotenv
import utils
from streamlit_option_menu import option_menu

load_dotenv()

with open('assets/data.json') as file:
    my_info = json.loads(file.read())

with open('assets/Resume.pdf', 'rb') as file:
    pdf_data = file.read()

lottie_animation = 'https://assets10.lottiefiles.com/packages/lf20_O2ci8jA9QF.json'
lottie_getintouch = 'https://assets5.lottiefiles.com/private_files/lf30_T12D5w.json'
HR = Image.open('images/HR.webp')
walmart = Image.open('images/walmart.webp')
img_photo = Image.open('images/my_photo-modified.png')
real = Image.open('images/realmart.webp')
bank = Image.open('images/bank.webp')
datascience = Image.open('images/datascience.webp')
kaggle = Image.open('images/kaggle.webp')

st.set_page_config(page_title='MADHAN KUMAR M', page_icon='😎', layout='wide')
st.markdown(utils.local_css('style/style.css'), unsafe_allow_html=True)



st.markdown("""
    <style>
        h1, h2  {
            color: #008080;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        }
    </style>
        """, unsafe_allow_html=True)


with st.container():
    left, right = st.columns((2, 3), gap='small')

    with right:
        st.subheader(my_info['header'])
        st.title(my_info['title'])
        st.write(my_info['about_me'])

        st.download_button(
                label=" 📄 Download Resume",
                data=pdf_data,
                file_name='madhankumarm.pdf',
                mime="application/octet-stream",
            )

    with left:
        st.image(img_photo, width=340)
    st.markdown('---')

with st.container():
    option = option_menu(
        menu_title=None,
        options=['Home', 'Skills', 'Interests', 'Projects', 'Contact'],
        icons=['person', 'code-slash', 'book', 'book', 'phone'],
        orientation='horizontal'
    )
if option == 'Home':

    
    st.markdown("# Career Objective")

    career_objective = """
    As an AI Cognitive Developer, my objective is to apply my skills in artificial intelligence and cognitive computing to contribute to cutting-edge projects. I am enthusiastic about leveraging technology to solve complex problems and drive innovation. My goal is to continuously learn and adapt to emerging trends, contributing to advancements in the field of artificial intelligence.
    """

    st.write(career_objective)

    # Education Section
    st.markdown("# Education")

    # Single degree information
    degree_info = {
        "degree": "Bachelor of Technology in Information Technology",
        "university": "Chennai Institute of Technology",
        "year": "2026",
    }
    
    # Display education details
    st.markdown(f"#### {degree_info['degree']}")
    st.write(f"**University:** {degree_info['university']}")
    st.write(f"**Year:** {degree_info['year']}")

    st.markdown("# INTERNSHIP")

    # Single degree information
    inter_info = {
        "Company": "Agri Tech CMSD",
        "Position": "App Developer",
        "year": "2023",
    }
    
    # Display education details
    st.markdown(f"**Company** {inter_info['Company']}")
    st.write(f"**Position:** {inter_info['Position']}")
    st.write(f"**Year:** {inter_info['year']}")

    st.markdown("# ACHEIVEMENTS ")

    # Single degree information
    inter_info = {
        "competition": "HARYANA POLICE HACKATHON",
        "Position": "App Developer",
        "year": "2024",
    }
    
    # Display education details
    st.markdown(f"**Competition** {inter_info['competition']}")
    st.write(f"**Position:** {inter_info['Position']}")
    st.write(f"**Year:** {inter_info['year']}")

        # Languages and Proficiency
    languages = [
            {"name": "Tamil", "proficiency": 80},
            {"name": "English", "proficiency": 90},
            {"name": "Kannada", "proficiency": 60},
        ]

        # Display proficiency meters
    
    st.markdown("# Language Proficiency")

    for language in languages:
            st.markdown(f"## {language['name']}")

            # Proficiency meter
            st.progress(language['proficiency'] / 100.0)

if option == "Skills":

    # Container layout
    with st.container():
        st.markdown('---')

        # Left side for skills
        st.markdown("# Skills")

        # Introduction
        st.markdown("""
            Welcome to my Skills page! As a passionate AI Cognitive Developer, I have gained expertise in various areas.
            Below are some of the key skills I bring to the table.
        """)

        # Overall proficiency progress bar
        overall_proficiency = 85  # Adjust overall proficiency value
        st.markdown("## Overall Proficiency")
        st.progress(overall_proficiency / 100.0)

        # Skills Section
        st.markdown("## Technical Skills")

        # Programming Languages
        st.markdown("## Programming Languages")
        programming_languages = [
            {"language": "Python (TensorFlow, PyTorch, scikit-learn)", "proficiency": 90},
            {"language": "R", "proficiency": 80},
            {"language": "C++", "proficiency": 75},
            {"language": "php", "proficiency": 65},
        ]
        
        for lang in programming_languages:
            st.markdown(f"- {lang['language']}")
        st.markdown("#### Programming Languages Proficiency")
        st.progress(lang['proficiency'] / 100.0)
        st.markdown("---")

        #web development
        st.markdown("## Web Development")
        web = ['html','css','bootsrap','tailwind css','javascript','typescript','reactjs','nodejs']
        for w in web:
            st.markdown(f"- {w}")
        st.markdown("#### Web development Proficiency")
        st.progress(65 / 100.0)
        st.markdown('---')

        # Machine Learning
        st.markdown("## Machine Learning")
        ml_skills = [
            "Supervised and Unsupervised Learning",
            "Deep Learning",
            "Reinforcement Learning",
        ]
        
        for skill in ml_skills:
            st.markdown(f"- {skill}")
        ml_proficiency = 85  # Adjust proficiency value
        st.markdown("#### Machine Learning Proficiency")
        st.progress(ml_proficiency / 100.0)
        st.markdown('---')

        # Natural Language Processing (NLP)
        st.markdown("## Natural Language Processing (NLP)")
        nlp_skills = [
            "Named Entity Recognition (NER)",
            "Sentiment Analysis",
            "Text Classification",
            "Language Modeling",
        ]
        
        for skill in nlp_skills:
            st.markdown(f"- {skill}")
        nlp_proficiency = 80  # Adjust proficiency value
        st.markdown("#### NLP Proficiency")
        st.progress(nlp_proficiency / 100.0)
        
        # Tools and Frameworks without progress bars
        st.markdown("## Tools and Frameworks")
        tools_frameworks = [
            "TensorFlow",
            "PyTorch",
            "Keras",
            "NLTK",
            "SpaCy",
        ]
        for tool in tools_frameworks:
            st.markdown(f"- {tool}")
        st.markdown("#### Tools and Frameworks Proficiency")
        tools = 76
        st.progress(tools / 100.0)

        # Database Systems
        st.markdown("## Database Systems")
        database_systems = [
            "SQL",
            "MongoDB",
        ]
        
        for system in database_systems:
            st.markdown(f"- {system}")
        db_proficiency = 80  # Adjust proficiency value
        st.markdown("#### Database Systems Proficiency")
        st.progress(db_proficiency / 100.0)
        st.markdown('---')

        st.markdown("## App development")
        database_systems = [
            "Flutter",
            "React Native",
        ]
        
        for system in database_systems:
            st.markdown(f"- {system}")
        db_proficiency = 47  # Adjust proficiency value
        st.markdown("#### App development Proficiency")
        st.progress(db_proficiency / 100.0)
        st.markdown('---')

        # Software Development
        st.markdown("## Software Development")
        software_dev_skills = [
            "Agile and Scrum methodologies",
            "Version control (Git)",
        ]
        
        for skill in software_dev_skills:
            st.markdown(f"- {skill}")
        dev_proficiency = 85  # Adjust proficiency value
        st.markdown("#### Software Development Proficiency")
        st.progress(dev_proficiency / 100.0)
        st.markdown('---')

    # Right side for connect section
    with st.container():
        st.markdown('<h2 style="color:#008080;">Connect with Me</h2>', unsafe_allow_html=True)
        st.markdown("""
            I'm excited to connect with you! Feel free to reach out through the following platforms.
        """)

        st.markdown(f'[🌐 GitHub]({my_info["github"]})', unsafe_allow_html=True)
        st.markdown(f'[💼 Medium]({my_info["med"]})', unsafe_allow_html=True)
        st.markdown(f'[🐦 Twitter]({my_info["twitter"]})', unsafe_allow_html=True)
        st.markdown(f'[🔗 LinkedIn]({my_info["linkedin"]})', unsafe_allow_html=True)

elif option == 'Interests':
    st.markdown("""
    <style>
        h1 {
            color: #008080;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

    # Container layout
    with st.container():
        st.write('---')
        
        # Left side for text
        interests, animation = st.columns((2,3), gap='small')
        with interests:
        # Text content
            st.markdown("# MY Interests")
            st.markdown("""
                Welcome to my Interests page! As an AI Cognitive Developer, I am passionate about various aspects of artificial intelligence and cognitive computing.
                Below are some of my key interests that drive my enthusiasm in this field.
            """)

        # Interests Section with color
        st.markdown("""
            <style>
                h2 {
                    color: #008080;
                }
            </style>
        """, unsafe_allow_html=True)

        st.markdown("## Key Interests")

        # List of interests
        interests_list = [
            "Machine Learning Applications in Healthcare",
            "Natural Language Processing (NLP) for Conversational AI",
            "Ethical AI and Responsible AI Practices",
            "AI in Autonomous Systems and Robotics",
            "Cognitive Computing for Decision Support Systems",
        ]
       
        # Display interests
        for interest in interests_list:
            st.markdown(f"- {interest}")
        
        with animation:
            st_lottie(
                utils.load_data_from_url(lottie_animation),
                height=300,
                key='animation'
            )
        

        # Recent Readings with color
        st.markdown("""
            <style>
                h2 {
                    color: #008080;
                }
            </style>
        """, unsafe_allow_html=True)

        st.markdown("## Recent Readings")

        # Display recent readings
        st.markdown("""
            1. **"Artificial Intelligence: A Guide for Thinking Humans"** by Melanie Mitchell
            2. **"Human Compatible: Artificial Intelligence and the Problem of Control"** by Stuart Russell
            3. **"AI Superpowers: China, Silicon Valley, and the New World Order"** by Kai-Fu Lee
        """)

        # AI Community Involvement with color
        st.markdown("""
            <style>
                h2 {
                    color: #008080;
                }
            </style>
        """, unsafe_allow_html=True)

        st.markdown("## AI Community Involvement")

        # Display community involvement
        st.markdown("""
            - Regular participant in AI conferences and meetups
            - Contributing to open-source AI projects on GitHub
            - Active member of AI forums and discussion groups
        """)

        # Conclusion with color
        st.markdown("""
            <style>
                h2 {
                    color: #008080;
                }
            </style>
        """, unsafe_allow_html=True)

        st.markdown("## Conclusion")

        st.markdown("""
            These are some of my key interests as an AI Cognitive Developer. I am dedicated to staying informed about the latest developments in artificial intelligence and contributing to the community.
            If you share similar interests or have insights to share, I would love to connect!
        """)

        # Contact Information with color
        st.markdown("""
            <style>
                h2 {
                    color: #008080;
                }
            </style>
        """, unsafe_allow_html=True)

        
elif option == 'Projects':
    tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["HR Analytics", "Walmart Dashboard","RealMart Dashboard","bank","datascience website","kaggle"])
        # HR Analytics Dashboard in Power BI
    with tab1:
        with st.container():
            st.image(HR, use_column_width=True)

            hr_content = """
            🚀 **HR Analytics Dashboard in Power BI:**
            - **Overview:** Transformed raw HR data into actionable insights, empowering HR teams.
            - **Features:** Metrics, visualizations, and a user-friendly interface.
            - **Focus Areas:** Talent, performance, retention, and diversity & inclusion metrics.
            - **Value:** Data-driven decisions, time efficiency, and strategic planning.
            """
            st.markdown(hr_content)

        # Separator between tabs
        st.markdown("---")
    with tab2:
        # Walmart Dashboard in Tableau
        with st.container():
            st.image(walmart, use_column_width=True)

            walmart_content = """
            🚀 **Walmart Dashboard in Tableau:**
            - **Overview:** Developed an insightful Walmart Dashboard for retail analytics.
            - **Features:** Sales metrics, inventory management, customer behavior, and geospatial analysis.
            - **Focus Areas:** Product performance, supply chain optimization, customer segmentation, and competitive benchmarking.
            - **Value:** Data-driven decision-making, operational efficiency, and customer-centric strategies.
            """
            st.markdown(walmart_content)
    
    with tab3:
    # Power BI Dashboard
        with st.container():
            st.image(real, use_column_width=True)

            realmart_content = """
            🚀 **Real Mart Dashboard in Power BI:**
            - **Overview:** Created a dynamic Power BI Dashboard to revolutionize retail analytics.
            - **Features:** Uncover detailed insights on sales metrics, streamline inventory management, understand customer behavior, and perform geospatial analysis.
            - **Focus Areas:** Dive deep into product performance analytics, optimize the supply chain for efficiency, create targeted customer segmentation, and stay ahead with competitive benchmarking.
            - **Value:** Empowering data-driven decision-making, enhancing operational efficiency, and crafting customer-centric strategies for sustainable growth.
            """
            st.markdown(realmart_content)
    
    with tab4:
    # Bank Management Dashboard
        with st.container():
            st.image(bank, use_column_width=True)

            bank_project_content = """
            🚀 **Bank Management System:**
            - **Overview:** This was my first year project.
            - **Features:**
            - **Deposit:** Easily deposit funds into your account for convenient transactions.
            - **Withdraw:** Seamlessly withdraw money based on your financial needs.
            - **Check Balance:** Get real-time updates on your account balance for better financial management.
            - **Login and Logout:** Securely access your account with a user-friendly login/logout system.
            - **Messaging System:** Send and receive messages to/from other users for efficient communication.
            - **Focus Areas:** Enhance user experience, ensure security in transactions, and promote effective communication within the banking system.
            - **Value:** Facilitating financial transactions, providing account transparency, and fostering seamless communication for an improved banking experience.
            - **Teck Stack:** php, html, css, Mysql database.
            """
            st.markdown(bank_project_content)

    with tab5:
        # datascience
        with st.container():
            st.image(datascience, use_column_width=True)

            streamlit_project_content = """
            🚀 **Streamlit Website Project:**
            - **Overview:** Developed a versatile Streamlit website offering a range of features for data exploration and interaction.
            - **Features:**
            - **Creating ML Models:** Build and deploy machine learning models seamlessly within the platform.
            - **Data Visualization:** Visualize data using interactive charts and graphs for better insights.
            - **Tableau Integration:** Connect and embed Tableau dashboards to enhance data presentation.
            - **Sending Mail:** Incorporate an email functionality to facilitate communication and notifications.
            - **Stock Dashboard:** Explore real-time stock data with a dedicated dashboard for financial analysis.
            - **Focus Areas:** Empower users with machine learning capabilities, enhance data exploration, leverage Tableau for advanced visualization, streamline communication through email, and provide comprehensive stock market analytics.
            - **Value:** Enabling users to perform end-to-end data-related tasks, fostering informed decision-making, and creating a centralized platform for diverse data functionalities.
            """
            st.markdown(streamlit_project_content)

    with tab6:
        #kaggle
        with st.container():
            st.image(kaggle, use_column_width=True)

            streamlit_project_content = """
            🚀 **datascience ML models Project:**
            - I have created more than 12 Machine learning models in the kaggle account
            - take a view of my kaggle account
            """
            
            st.markdown(streamlit_project_content)
            st.markdown(f'[🔗 Kaggle]({my_info["kaggle"]})')



        
        
        

elif option == 'Contact':
    with st.container():
        st.write('---')
        st.header('Get in touch with me...')
        contact_form = f'''
        <form action="https://formsubmit.co/madhankumarbusiness@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <input type="text" name="service" placeholder="What kind of service you are looking for..." required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        '''
        form, empty = st.columns(2)
        with form:
            st.markdown(contact_form, unsafe_allow_html=True)
        with empty:
            st_lottie(
                utils.load_data_from_url(lottie_getintouch),
                height=300,
                key='getintouch'
            )
