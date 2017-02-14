from flask import Flask, render_template, url_for
from flask_restful import Resource, Api
import dns.resolver
import json


app = Flask(__name__)
api = Api(app)

# api call to get active site. Return Json with response code and custom response header
class ActiveSite(Resource):
    def get(self):
        cname, nodes = nslookup()
        return {'Active_site': cname.labels[0]}, 200, {'Datacenter': cname}

api.add_resource(ActiveSite, '/api/v1.0/site')

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html', text="Always watching, never breaking eye contact...")

@app.route('/lookup')
def lookup():
    cname, nodes = nslookup()
    return render_template('lookup.html', cname=cname)


def nslookup():
    data = None

    with open('./server_lists/stage') as server_list:
        data = json.load(server_list)

    resolve = dns.resolver.query('zenoss.stage.tools.bbc.co.uk')
    canonicalName = resolve.canonical_name
    site = canonicalName[0]
    nodes = []
    count = 0

    for i in data[u'DC'][site]:
        count += 1
        print "Server name {}, IP is {}".format(i[u'Node' + str(count)][u'server_name'],i[u'Node' + str(count)][u'ip'])
        nodes.append(i)

    return canonicalName, nodes

if __name__ == '__main__':
    app.run(debug=True, port=5050)

