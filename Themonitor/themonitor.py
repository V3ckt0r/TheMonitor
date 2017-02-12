from flask import Flask, render_template, url_for
import socket
import subprocess
import dns.resolver



app = Flask(__name__)

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html', text="Always watching, never breaking eye contact...")

@app.route('/lookup')
def nslookup():
    resolve = dns.resolver.query('zenoss.stage.tools.bbc.co.uk')
    canonicalName = resolve.canonical_name
    return 

def main():
    nslookup()

if __name__ == '__main__':
    app.run(debug=True)
