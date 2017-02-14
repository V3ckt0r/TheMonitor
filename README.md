[![Build Status](https://travis-ci.org/V3ckt0r/TheMonitor.svg?branch=master)](https://travis-ci.org/V3ckt0r/TheMonitor)
##The Monitor

The Monitor is an app to help you determine operational logistics of Zenoss Resource Manager.

###Quickstart

Get the active datacenter:

    curl -X GET localhost:5050/api/v1.0/site

    {
        "Active_site": "zenoss-b"
    }

Notice that the response header returned from the server also includes a custom header "Datacenter":

    curl -X GET localhost:5050/api/v1.0/site -I

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 34
    Datacenter: zenoss-b.stage.tools.bbc.co.uk.
    Server: Werkzeug/0.11.15 Python/2.7.10
    Date: Tue, 14 Feb 2017 10:21:13 GMT

