from flask import Flask
import mysql.connector

app = Flask(__name__)

# Database connection details
DB_CONFIG = {
    "host": "db",
    "port": "3306",
    "user": "root",
    "password": "memoyasser2004.",
    "database": "team_data",
}


# Function to fetch team members from database
def get_team_members():

        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM team_members ORDER BY cgpa ASC")
        team_members = cursor.fetchall()
        return team_members


# Homepage with a button to navigate to the database page
@app.route("/")
def home():
    # Dynamic greeting message based on the time of the day
    import datetime

    current_time = datetime.datetime.now()
    greeting = (
        "Good morning"
        if current_time.hour < 12
        else "Good afternoon" if current_time.hour < 18 else "Good evening"
    )

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Homepage</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-image: url('https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?q=80&w=1744&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
                background-position: center;
                background-size: cover;
                background-color: #000000;
                color: #ffffff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .homepage-container {{
                max-width: 800px;
                padding: 40px;
                background-color: rgba(0, 0, 0, 0.8);
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
                border-radius: 10px;
                text-align: center;
                animation: fadeInUp 1s ease forwards;
            }}
            h1 {{
                margin-bottom: 20px;
            }}
            p {{
                margin-bottom: 30px;
            }}
            .btn {{
                display: inline-block;
                padding: 15px 30px;
                background-color: #007bff;
                color: #ffffff;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s ease;
                font-size: 1.2rem;
                border: none;
                cursor: pointer;
                outline: none;
            }}
            .btn:hover {{
                background-color: #0056b3;
            }}
            @keyframes fadeInUp {{
                from {{
                    opacity: 0;
                    transform: translateY(-50px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}
        </style>
    </head>
    <body>
        <div class="homepage-container">
            <h1>{greeting}, welcome to our website!</h1>
            <p>Explore our team members and get to know us better.</p>
            <a href="/team-members" class="btn">Meet the Team</a>
        </div>
    </body>
    </html>
    """


# Route to display team members
@app.route("/team-members")
def team_members():
    team_members = get_team_members()
    if team_members:
        table_rows = "".join(
            [
                "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(
                    member["name"], member["student_id"], member["age"], member["cgpa"]
                )
                for member in team_members
            ]
        )
        table_html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Team Members</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-image: url('https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?q=80&w=1744&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
                    background-size: cover;
                    background-position: center;
                    color: #ffffff;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}
                .container {{
                    max-width: 1200px;
                    padding: 40px;
                    background-color: rgba(0, 0, 0, 0.8);
                    box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
                    border-radius: 10px;
                    text-align: center;
                    animation: fadeInUp 1s ease forwards;
                }}
                h1 {{
                    color: #007bff;
                    margin-bottom: 30px;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                }}
                th, td {{
                    padding: 15px;
                    border: 1px solid #ddd;
                    text-align: left;
                }}
                th {{
                    background-color: #007bff;
                }}
                tr:nth-child(even) {{
                    background-color: translateY(0);
                }}
                @keyframes fadeInUp {{
                    from {{
                        opacity: 0;
                        transform: translateY(-50px);
                    }}
                    to {{
                        opacity: 1;
                        transform: translateY(0);
                    }}
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Team Members</h1>
                <table>
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Student ID</th>
                            <th>Age</th>
                            <th>CGPA</th>
                        </tr>
                    </thead>
                    <tbody>
                        {table_rows}
                    </tbody>
                </table>
            </div>
        </body>
        </html>
        """
        return table_html
    else:
        return "<h1>No team members found</h1>"


if __name__ == "__main__":
    app.run('0.0.0.0')
