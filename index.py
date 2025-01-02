import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
import base64
from pathlib import Path
from streamlit_pills import pills
from PIL import Image
import webbrowser

# Lottie Files

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder = load_lottie(r"https://lottie.host/f1824c04-c2e3-4190-942e-89bc7028a163/LEB3P705dH.json")

# Studying Lottie
study_lottie = load_lottie(r"https://lottie.host/9a28a239-0f79-4afa-bda9-6efe44b47e4d/TWbQQlAANL.json") 

# Projects Images
project1 = Image.open("static/Investology.png")
project2 = Image.open("static/Malware Class.png")

# Personal
st.set_page_config(page_title="Nagendra Puram", page_icon=":wave:", layout="wide")

# Header Section
st.markdown("""
            <style>
                .header-container {
                    text-align: center;
                    margin-top: -50px;
                    align-items: center;
                }
                .headrer-container h1{
                    text-align: center;
                }
                .header-image {
                    width: 120px;
                    height: 120px;
                    border-radius: 50%;
                    margin-bottom: 10px;
                }
                .header-buttons a {
                    text-decoration: none;
                    display: inline-block;
                    color: white;
                    padding: 10px 20px;
                    border-radius: 5px;
                    font-size: 14px;
                    margin: 5px;
                }
                .download-cv {
                    background-color: black;
                }
                .hire-me {
                    background-color: #4CAF50;
                }
                .about-container {
                    display: flex;
                    justify-content: space-between;
                    gap: 30px;
                    margin-top: 30px;
                }
                .about-box, .bio-box {
                    padding: 20px;
                    background: white;
                    border-radius: 10px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                    width: 48%;
                }
                h2 {
                    color: #333333;
                    margin-bottom: 10px;
                }
            </style>
            <div class='header-container'>
                    <h1>Nagendra Puram</h1>
                    <p style='color: gray;'>Data Scientist and DevOps Engineer</p>
                    </div>
            </div>""", unsafe_allow_html=True)

# Social Media Links
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .links {
            display: flex; 
            justify-content: center; 
            gap: 15px; 
            margin-top: 20px;
        }
        .links a {
            text-decoration: none; 
            color: white; 
            padding: 10px 15px; 
            border-radius: 50%; 
            font-size: 30px; 
            display: inline-flex; 
            justify-content: center; 
            align-items: center;
        }
        a:hover {
            opacity: 0.8;
        }
        .links a {
            text-decoration: none; /* Remove underline from links */
        }

        .links .linkedin i {
            color: #0077b5; /* Default LinkedIn color */
        }

        .links .github i {
            color: #000000;
            background: #ffffff;
            border-radius: 40px;
        }

        .links .instagram i {
            color: #e4405f; /* Default Instagram color */
        }
        @media (prefers-color-scheme: dark) {
            .links .linkedin i {
                color: #0e76a8; /* Dark mode LinkedIn color */
            }

            .links .github i {
                color: #ffffff;
                background: black;
                border-radius: 30px;
            }

            .links .instagram i {
                color: #ff6f61; /* Dark mode Instagram color */
            }
        }
    </style>
    <div class="links">
        <!-- LinkedIn -->
        <a href="https://www.linkedin.com/in/puramnagendra2" target="_blank" class="linkedin">
            <i class="fa-brands fa-linkedin"></i>
        </a>
        <!-- GitHub -->
        <a href="https://www.github.com/puramnagendra2" target="_blank" class="github">
            <i class="fa-brands fa-github"></i>
        </a>
        <!-- Instagram -->
        <a href="https://www.instagram.com" target="_blank" class="instagram">
            <i class="fa-brands fa-instagram"></i>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# Summary Section
with st.container():
    selected = option_menu(
        menu_title=None,
        options=["Summary"],
        orientation='horizontal',
        menu_icon="cast",
        styles={
            "container": { "width": "20%"},  # Background of the entire menu
            "nav-link": {
                "font-size": "20px",
                "font-family": "cursive",
                "text-align": "center",
                "color": "white",
                "cursor": "default"
            },
            "nav-link-selected": {"background-color": "#008cba", "color": "white", "cursor": "default"},  # Background for selected item
        },
    )
    st.markdown("""
                <style>
                    .container1 {
                        border-radius: 8px;
                        padding: 10px;
                        text-align: center;
                        margin: auto;
                        justify-content: center;
                        width: 80%;
                    }
                </style>
                <div class='container1'> 
                    <p style="font-family: cursive;">Passionate MCA graduate with expertise in Python, machine learning, and deep learning, eager to transform 
                        complex data into actionable insights. With strong problem-solving and collaboration skills, I aim to bring 
                        fresh ideas and analytical skills to a dynamic data science team, driving innovation and growth.
                    </p>
                </div>""", unsafe_allow_html=True)


st.divider()

# Education Tab
with st.container():
    selected = option_menu(
        menu_title=None,
        options=["Education"],
        icons=["mortarboard-fill"],
        orientation='horizontal',
        menu_icon="cast",
        styles={
            "container": { "width": "20%"},  # Background of the entire menu
            "nav-link": {
                "font-size": "20px",
                "font-family": "cursive",
                "text-align": "center",
                "color": "white",
                "cursor": "default"
            },
            "nav-link-selected": {"background-color": "#008cba", "color": "white", "cursor": "default"},  # Background for selected item
        },
    )
    col1, col2 = st.columns([3, 1])

    # First column with two rows
    with col1:
        year, mca = st.columns([2, 7], gap="small")
        with year:
            st.markdown("""
            <div style='display: flex; align-items: center; justify-content: center; 
                            border: 4px solid #6c5ce7; border-radius: 20px; text-align: center; 
                            height: 100%; margin-top:70px;'>
                    <h4 style='color:#0984e3; margin: 0;'>2022 - 2024</h4>
            </div>""", unsafe_allow_html=True)
        with mca:
            st.markdown("""
                <div style='border: 4px solid #6c5ce7; border-radius: 20px; text-align: center; margin-bottom: 10px; margin-top:50px;'>
                    <h4 style='color:#6c5ce7;'>Master of Computer Applications (MCA) </h4>
                    <h5>Madanapalle Institute of Technology & Science - Madanapalle</h5>
                </div>
            """, unsafe_allow_html=True)
        year, bca = st.columns([2, 7], gap="small")
        with year:
            st.markdown("""
            <div style='display: flex; align-items: center; justify-content: center; 
                        border: 4px solid #0984e3; border-radius: 20px; text-align: center; 
                        height: 100%; margin-top:20px;'>
                <h4 style='color:#0984e3; margin: 0;'>2018 - 2021</h4>
            </div>
            """, unsafe_allow_html=True)
        with bca:
            st.markdown("""
            <div style='border: 4px solid #0984e3; border-radius: 20px; text-align: center; margin-bottom: 10px;'>
                <h4 style='color:#0984e3;'>Bachelor of Computer Applications (BCA) </h4>
                <h5>SJES College of Management Studies - Bangalore</h5>
            </div>
        """, unsafe_allow_html=True)

    # Second column with one row
    with col2:
        st_lottie(study_lottie, height=300, reverse=True)
    

st.divider()

# Skills Section
with st.container():
    selected = option_menu(
        menu_title=None,
        options=["Skills"],
        icons=["card-list"],
        orientation='horizontal',
        menu_icon="cast",
        styles={
            "container": { "width": "20%"},  # Background of the entire menu
            "nav-link": {
                "font-size": "20px",
                "font-family": "cursive",
                "text-align": "center",
                "color": "white",
                "cursor": "default"
            },
            "nav-link-selected": {"background-color": "#008cba", "color": "white", "cursor": "default"},  # Background for selected item
        },
    )
    col1, col2, col3 = st.columns([1, 2, 1], gap='small')
    with col1:
        pass
    with col2:
        # Function to encode image to base64
        def image_to_base64(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode("utf-8")

        # Paths to your local images
        images = [
            "static/linux.png",
            "static/git.png",
            "static/ansible.png",
            "static/azure-devops.png",
            "static/docker.png",
            "static/terraform.png",
            "static/kubernetes.png",
        ]

        # Encode images to base64
        encoded_images = [image_to_base64(image) for image in images]

        # Generate the HTML with embedded images
        html_code = """
        <style>
        .logo-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            margin-top: 10px;
            margin-left: 0px;
        }

        .logo-container img {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }

        .logo-container img:hover {
            transform: scale(1.1);
        }
        </style>
        <div class="logo-container">
        """

        # Add each image to the HTML
        for encoded_image in encoded_images:
            html_code += f'<img src="data:image/png;base64,{encoded_image}" alt="Logo">'

        html_code += "</div>"

        # Display the HTML in Streamlit
        st.markdown(html_code, unsafe_allow_html=True)
    with col3:
        pass


    # Data Science
    col1, col2, col3 = st.columns([1, 2, 1], gap='small')
    with col1:
        pass
    with col2:
        # Function to encode image to base64
        def image_to_base64(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode("utf-8")

        # Paths to your local images
        images = [
            "static/python.png",
            "static/numpy.png",
            "static/pandas.png",
            "static/matplotlib.png",
            "static/seaborn.png",
            "static/plotly.png",
            "static/scikit.png",
            "static/tensorflow.png",
            "static/streamlit.png"
        ]

        # Encode images to base64
        encoded_images = [image_to_base64(image) for image in images]

        # Generate the HTML with embedded images
        html_code = """
        <style>
        .logo-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            margin-top: 60px;
            margin-left: 0px;
        }

        .logo-container img {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }

        .logo-container img:hover {
            transform: scale(1.1);
        }
        </style>
        <div class="logo-container">
        """

        # Add each image to the HTML
        for encoded_image in encoded_images:
            html_code += f'<img src="data:image/png;base64,{encoded_image}" alt="Logo">'

        html_code += "</div>"

        # Display the HTML in Streamlit
        st.markdown(html_code, unsafe_allow_html=True)
    with col3:
        pass

    # Full Stack
    # Data Science
    col1, col2, col3 = st.columns([1, 2, 1], gap='small')
    with col1:
        pass
    with col2:
        # Function to encode image to base64
        def image_to_base64(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode("utf-8")

        # Paths to your local images
        images = [
            "static/html.png",
            "static/css.png",
            "static/js.png",
            "static/django.png",
            "static/postgresql.png",
            "static/mongodb.png",
            "static/api.png"
        ]

        # Encode images to base64
        encoded_images = [image_to_base64(image) for image in images]

        # Generate the HTML with embedded images
        html_code = """
        <style>
        .logo-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            margin-top: 60px;
            margin-left: 0px;
        }

        .logo-container img {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }

        .logo-container img:hover {
            transform: scale(1.1);
        }
        </style>
        <div class="logo-container">
        """

        # Add each image to the HTML
        for encoded_image in encoded_images:
            html_code += f'<img src="data:image/png;base64,{encoded_image}" alt="Logo">'

        html_code += "</div>"

        # Display the HTML in Streamlit
        st.markdown(html_code, unsafe_allow_html=True)
    with col3:
        pass

# End of Skills Section

st.divider()

# Navigation Menu

with st.container():
    selected = option_menu(
        menu_title=None,
        options=["Projects", "Blogs"],
        icons=['code', "book"],
        orientation='horizontal',
        menu_icon="cast",
        styles={
            "container": {"padding": "5px", "background-color": "#000000", "width": "40%"},  # Background of the entire menu
            "nav-link": {
                "font-size": "20px",
                "font-family": "cursive",
                "text-align": "center",
                "margin": "2px",
                "color": "white",
            },
            "nav-link-selected": {"background-color": "#008cba", "color": "white"},  # Background for selected item
        },
    )

# Start of Projects Section

if selected == 'Projects':
    st.write("##")

    # Project 1
    image_col, text_column = st.columns((1, 2))
    with image_col:
        st.image(project1)
    with text_column:
        st.subheader("A Web-based Stock Price Projection using GRU and Django")
        st.write(
            """
             Developed a web-based system for predicting stock prices using deep learning and 
            Django. The system provides stock price forecasts with a user-friendly interface for inputting stock 
            symbols and visualizing past and projected price trends.

            """
        )
        if st.button("Source Code", type="primary", icon="💻"):
            webbrowser.open("https://github.com/puramnagendra2/investology-project")
    
    # Project 2
    image_col, text_column = st.columns((1, 2))
    with image_col:
        st.image(project2)
    with text_column:
        st.subheader("Malware Classification Using Stacking CLassifier and Autoencoders")
        st.write(
            """
             Developed a web-based system for predicting stock prices using deep learning and 
            Django. The system provides stock price forecasts with a user-friendly interface for inputting stock 
            symbols and visualizing past and projected price trends.

            """
        )
        if st.button("Source Code", type="primary", icon="🔗"):
            webbrowser.open("https://github.com/puramnagendra2/malware-classification")

# End of Projects Section

# Start of Blogs Section

elif selected == "Blogs":
    st.write("##")

    image_col1, image_col2, image_col3 = st.columns((1, 1, 1))
    with image_col1:
        st.image(project2)
        st.subheader("Malware Classification Using Stacking CLassifier and Autoencoders")
        st.write(
            """
             Developed a web-based system for predicting stock prices using deep learning and 
            Django. The system provides stock price forecasts with a user-friendly interface for inputting stock 
            symbols and visualizing past and projected price trends.

            """
        )
    with image_col2:
        st.image(project2)
        st.subheader("Malware Classification Using Stacking CLassifier and Autoencoders")
        st.write(
            """
             Developed a web-based system for predicting stock prices using deep learning and 
            Django. The system provides stock price forecasts with a user-friendly interface for inputting stock 
            symbols and visualizing past and projected price trends.

            """
        )
    with image_col3:
        st.image(project2)
        st.subheader("Malware Classification Using Stacking CLassifier and Autoencoders")
        st.write(
            """
             Developed a web-based system for predicting stock prices using deep learning and 
            Django. The system provides stock price forecasts with a user-friendly interface for inputting stock 
            symbols and visualizing past and projected price trends.

            """
        )


st.divider()

# Contact Section
with st.container():
    selected = option_menu(
        menu_title=None,
        options=["Contact Us"],
        icons=["envelope-arrow-down-fill"],
        orientation='horizontal',
        menu_icon="cast",
        styles={
            "container": { "width": "20%"},  # Background of the entire menu
            "nav-link": {
                "font-size": "20px",
                "font-family": "cursive",
                "text-align": "center",
                "color": "white",
                "cursor": "default"
            },
            "nav-link-selected": {"background-color": "#008cba", "color": "white", "cursor": "default"},  # Background for selected item
        },
    )
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');
        .container {
            width: 80%; 
            background: #fff; 
            border-radius: 6px; 
            padding: 20px 60px 30px 40px;
            border-left: 4px solid #3e2093;
            border-right: 4px solid #3e2093;
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2); 
            margin: 40px auto; /* Center the container horizontally */
            display: flex; /* Use flexbox to align items */
            flex-direction: column; /* Align items vertically */
            align-items: center; /* Center items horizontally within the flex container */
        }
        .container .content{
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .container .content .left-side{
            width: 25%;
            height: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-top: 15px;
            position: relative;
        }
        .content .left-side::before{
            content: '';
            position: absolute;
            height: 70%;
            width: 2px;
            right: -15px;
            top: 50%;
            transform: translateY(-50%);
            background: #afafb6;
        }
        .content .left-side .details{
            margin: 14px;
            text-align: center;
        }
        .content .left-side .details i{
            font-size: 30px;
            color: #3e2093;
            margin-bottom: 10px;
        }
        .content .left-side .details .topic{
            font-size: 18px;
            font-weight: 500;
        }
        .content .left-side .details .text-one,
        .content .left-side .details .text-two{
            font-size: 14px;
            color: #afafb6;
        }
        .container .content .right-side{
            width: 75%;
            margin-left: 75px;
        }
        .content .right-side .topic-text{
            font-size: 23px;
            font-weight: 600;
            color: #3e2093;
        }
        .right-side .input-box{
            height: 50px;
            width: 100%;
            margin: 12px 0;
        }
        .right-side .input-box input,
        .right-side .input-box textarea{
            height: 100%;
            width: 100%;
            border: none;
            outline: none;
            font-size: 16px;
            background: #F0F1F8;
            border-radius: 6px;
            padding: 0 15px;
            resize: none;
        }
        .right-side .message-box{
            min-height: 110px;
        }
        .right-side .input-box textarea{
            padding-top: 6px;
        }
        .right-side .button{
            display: inline-block;
            margin-top: 12px;
        }
        .right-side .button input[type="button"]{
            color: #fff;
            font-size: 18px;
            outline: none;
            border: none;
            padding: 8px 16px;
            border-radius: 6px;
            background: #3e2093;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .button input[type="button"]:hover{
            background: #5029bc;
        }

        @media (max-width: 950px) {
            .container{
                width: 90%;
                padding: 30px 40px 40px 35px ;
            }
            .container .content .right-side{
            width: 75%;
            margin-left: 55px;
            }
        }
        @media (max-width: 820px) {
            .container{
                margin: 40px 0;
                height: 100%;
            }
            .container .content{
                flex-direction: column-reverse;
            }
            .container .content .left-side{
            width: 100%;
            flex-direction: row;
            margin-top: 40px;
            justify-content: center;
            flex-wrap: wrap;
            }
            .container .content .left-side::before{
            display: none;
            }
            .container .content .right-side{
            width: 100%;
            margin-left: 0;
            }
        }
    </style>
    <div class="container">
        <div class="content">
        <div class="left-side">
            <div class="address details">
                <i class="fa-brands fa-linkedin"></i>
                <div class="topic">Address</div>
                <div class="text-one">linkedin.com/in/puramnagendra2</div>
            </div>
            <div class="phone details">
                <i class="fas fa-phone-alt"></i>
                <div class="topic">Phone</div>
                <div class="text-one">+91 6302463724</div>
            </div>
            <div class="email details">
                <i class="fas fa-envelope"></i>
                <div class="topic">Email</div>
                <div class="text-one">puramnagendra2@gmail.com</div>
            </div>
        </div>
        <div class="right-side">
            <div class="topic-text"><h2>Send me a query</h2></div>
            <p>If you have any work from me or any types of quries related to my tutorial, you can send me message from here. It's my pleasure to help you.</p>
            <form action="#">
                <div class="input-box">
                    <input type="text" placeholder="Enter your name">
                </div>
                <div class="input-box">
                    <input type="text" placeholder="Enter your email">
                </div>
                <div class="input-box message-box">
                    <input type="text" placeholder="Enter your message">
                </div>
                <div class="button">
                <input type="button" value="Send Now" >
                </div>
            </form>
        </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# Footer Section
footer = """
<style>
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #f8f9fa;
    color: #6c757d;
    text-align: center;
    padding: 10px;
    font-size: 14px;
    font-family: cursive;
    border-top: 1px solid #e7e7e7;
}
</style>
<div class="footer">
    © 2025 Puram Nagendra | All Rights Reserved.
</div>
"""
st.markdown(footer, unsafe_allow_html=True)