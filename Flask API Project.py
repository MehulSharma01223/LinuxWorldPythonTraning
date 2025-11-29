from flask import Flask

app = Flask(__name__)

@app.route("/")
def resume():
    return """
    <style>
        body {
            font-family: Arial;
            background: #f4f4f4;
            padding: 30px;
        }
        .resume-box {
            background: white;
            max-width: 700px;
            margin: auto;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
        }
        h1 { text-align: center; }
        h2 { color: #444; border-bottom: 2px solid #ddd; padding-bottom: 5px; }
        ul { padding-left: 20px; }
        p, li { font-size: 16px; }
    </style>

    <div class="resume-box">
        <h1>Resume - Mainak</h1>

        <h2>Personal Information</h2>
        <p><b>Name:</b> Mainak</p>
        <p><b>Mobile:</b> 3249387656</p>
        <p><b>Email:</b> sjhasgetr@gmail.com</p>

        <h2>Skills</h2>
        <ul>
            <li>Python</li>
            <li>Flask</li>
            <li>HTML & CSS</li>
            <li>AI & Machine Learning (Basic)</li>
        </ul>

        <h2>Projects</h2>
        <ul>
            <li>Smart Attendance System using Face Recognition</li>
            <li>AI-based Virtual Health Assistant</li>
            <li>Lundery Managment System</li>
            <li>Health check system</li>
        </ul>

        <h2>Education</h2>
        <p>B.Tech in Computer Science — Vivekananda Global University, Jaipur</p>

        <h2>Summary</h2>
        <p>Motivated CSE student with skills in Python, web development, 
           and AI. Passionate about building real-world projects.</p>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
