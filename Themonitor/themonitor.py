from flask import Flask, render_template, url_for, jsonify
from flask_restful import Resource, Api
import dns.resolver
import logging
import json
from time import gmtime, strftime
from fabric.api import local, settings, abort, run, cd, env, execute, sudo
from fabric.contrib.console import confirm
from os import path

# flask initialisation
app = Flask(__name__)
api = Api(app)

# This method determines which CChost is the master
def which_CCHost():
    # use the settings method from fabric.api to get return codes for silent fails
    # to allow for error handeling and nicer error messages.
    try:
        with settings(warn_only=True):
            ret = run("/usr/bin/sudo /usr/sbin/pcs status")
            if ret.return_code == 0:
                _, keyword, after = ret.partition("Current DC")
                activeCCHost = after[0:30].strip(": ")
                return activeCCHost
            elif p.return_code > 0:
                print "Something went wrong... Check that Pacemaker is ok..."
                return 1
            else:
                print "Something went even more wrong..."
                return 2
    except Exception as e:
        logging.exception(e)
        return 3


# api call to get active site. Return Json with response code and custom response header
class ActiveSite(Resource):
    def get(self):
        cname, nodes = nslookup()
        return {'Active_site': cname.labels[0]}, 200, {'Datacenter': cname}

class ActiveCC(Resource):
    def get(self, *args, **kwargs):
        ret = which_CCHost()
        if ret == 1:
            return {'Error': 'Check that Pacemaker is ok'}, 500, {'CCHost': "Error"}
        elif ret == 2:
            return {'Error': 'Something went wrong...'}, 500, {'CCHost': "Error"}
        elif ret == 3:
            return {'Error': 'Farbic could not process remote SSH command, check logs for error... time reference: {}'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime()))}, 500, {'CCHost': "Error"}
        else:
            return {'Active_CC_host': ret}, 200, {'CCHost': ret}

# api end points
api.add_resource(ActiveCC, '/api/v1.0/host')
api.add_resource(ActiveSite, '/api/v1.0/site')

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html', text="Always watching, never breaking eye contact...")

@app.route('/host')
def ccHost():
    ret=str(which_CCHost())
    return render_template('lookup.html', cname=ret)

@app.route('/site')
def lookup():
    cname, nodes = nslookup()
    return render_template('lookup.html', cname=cname)


def nslookup():
    data = None
    unittest_mypath = path.join(path.dirname(__file__), 'server_lists')

    with open(unittest_mypath +'/stage') as server_list:
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

# Fabric globals
_, nodes = nslookup()
env.host_string = nodes[0]['Node1']['server_name']
print env.host_string
env.port = ''
env.user = ''
env.password = ''
env.sudo_user = ''
env.sudo_password = ''
env.key_filename = ''
env.use_ssh_config = True
# env.always_use_pty = False

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True, port=5050)

