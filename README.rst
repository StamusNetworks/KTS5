===============================
Kibana 5 Templates for Suricata
===============================

Templates/Dashboards for Kibana 5 to use with Suricata IDPS and the ELK stack

This repository provides 13 templates for the Kibana 5.x and Elasticsearch 5.x
for use with Suricata IDS/IPS - Intrusion Detection and Prevention System.

These dashboards are for use with Suricata and ELK - Elasticsearch, Logstash, 
Kibana and comprise of more than 140 visualizations and 11 searches.

The dashboards are:

 - ALL  
 - ALERTS 
 - DNS  
 - FILE Transactions  
 - FLOW  
 - HTTP  
 - IDS
 - OVERVIEW
 - SMTP
 - SSH  
 - TLS
 - VLAN
 - STATS

How to use
==========

::

     apt-get install git-core
     git clone https://github.com/StamusNetworks/KTS5.git
     cd KTS5
     
Load the dashboards in Kibana:

Load the dashboards: ::

 ./load.sh

**NOTE:**  
This may delete any custom dashboards you already have in place.

**NOTE:**  
In order to use the full HTTP logging dashboard template you need to set up Suricata as
explained here - http://www.pevma.blogspot.se/2014/06/http-header-fields-extended-logging.html  

**NOTE:**  
If the traffic you are inspecting contains vlans - in order to use the VLAN template, make sure you have enabled vlan tracking in ``suricata.yaml`` -

     vlan:
       use-for-tracking: true

**NOTE:**  
For best user experience use with 1680 x 1050 screen resolution!!  

Do not hesitate to test,feedback and contribute !
