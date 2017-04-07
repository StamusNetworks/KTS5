import elasticsearch
import json
import sys

if len(sys.argv) != 2:
    print >>sys.stderr, 'Syntax: %s [dashboard name]' % sys.argv[0]
    sys.exit(1)

index_name = ".kibana"
doc_type_name = "dashboard"
dashboard_name = sys.argv[1]

es_server = "elasticsearch:9200"

es = elasticsearch.Elasticsearch(es_server)

# get from ES
dashboard_doc = ""
dashboard_doc = es.get(index=index_name, doc_type=doc_type_name, id=dashboard_name)
dashboard_doc_src = dashboard_doc['_source']
panel = json.loads(dashboard_doc_src['panelsJSON'])
sorted_panel = sorted(panel, cmp=lambda x,y: cmp(x['row'], y['row']))
panelsJSON = json.dumps(sorted_panel)
dashboard_doc_src['panelsJSON'] = panelsJSON

# put into ES
#sys.stdout.write(json.dumps(dashboard_doc_src) + "\n")
es.index(index=index_name, doc_type=doc_type_name, id=dashboard_name, body=dashboard_doc_src)
