from datetime import datetime
from django.http import HttpResponse

def home(request):
    result = ""
    if 'year' in request.GET:
        try:
            birth_year = int(request.GET.get('year'))
            current_year = datetime.now().year
            age = current_year - birth_year
            result = f"You are {age} years old."
        except:
            result = "Please enter a valid year."

    html = f"""
    <html>
    <head>
        <title>Age Calculator</title>
        <style>
            body {{
                font-family: Arial;
                text-align: center;
                margin-top: 100px;
                background-color: #fff3e0;
            }}
            form {{
                display: inline-block;
                padding: 20px;
                background: #fff;
                border-radius: 10px;
                box-shadow: 0 0 10px #ccc;
            }}
            input {{
                padding: 10px;
                width: 100%;
                margin-bottom: 10px;
            }}
            input[type="submit"] {{
                background-color: #ef6c00;
                color: white;
                border: none;
            }}
            p.result {{
                font-size: 1.2em;
                color: #bf360c;
            }}
        </style>
    </head>
    <body>
        <h1>Age Calculator</h1>
        <form method="get">
            <input type="number" name="year" placeholder="Enter your birth year" required><br>
            <input type="submit" value="Calculate Age">
        </form>
        <p class="result">{result}</p>
    </body>
    </html>
    """
    return HttpResponse(html, content_type="text/html")
