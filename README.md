[![Build Status](https://travis-ci.org/V3ckt0r/TheMonitor.svg?branch=master)](https://travis-ci.org/V3ckt0r/TheMonitor)

{::nomarkdown}
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="99" height="20">
    <linearGradient id="b" x2="0" y2="100%">
        <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
        <stop offset="1" stop-opacity=".1"/>
    </linearGradient>
    <mask id="a">
        <rect width="99" height="20" rx="3" fill="#fff"/>
    </mask>
    <g mask="url(#a)">
        <path fill="#555" d="M0 0h63v20H0z"/>
        <path fill="#4c1" d="M63 0h36v20H63z"/>
        <path fill="url(#b)" d="M0 0h99v20H0z"/>
    </g>
    <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
        <text x="31.5" y="15" fill="#010101" fill-opacity=".3">coverage</text>
        <text x="31.5" y="14">coverage</text>
        <text x="80" y="15" fill="#010101" fill-opacity=".3">95%</text>
        <text x="80" y="14">95%</text>
    </g>
</svg>
{:/}

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

