#!/usr/bin/python2
import sys
import json
from copy import copy

if len(sys.argv) != 3:
    print >>sys.stderr, 'Syntax: %s [index1.json] [index2.json]' % sys.argv[0]
    exit(1)

class KibanaIndex(object):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, 'r')
        raw = f.read()
        f.close()
        self.data = json.loads(raw)
        self.fields = json.loads(self.data['fields'])
        self.fields_name = [f['name'] for f in self.fields]
    
    def title(self):
        return self.data['title']

    def merge(self, other):
        for field in other.fields:
            if field['name'] in self.fields_name:
                continue
            print >>sys.stderr, 'New field: %s' % field['name']
            self.fields.append(field)
            self.fields_name.append(field['name'])

    def show(self):
        fields = json.dumps(self.fields, separators= (',', ':'))
        data = copy(self.data)
        data['fields'] = fields
        print json.dumps(data, separators= (',', ':'))

kib1 = KibanaIndex(sys.argv[1])
kib2 = KibanaIndex(sys.argv[2])

print >>sys.stderr, '%s : %s %i' % (kib1.filename, kib1.title(), len(kib1.fields))
print >>sys.stderr, '%s : %s %i' % (kib2.filename, kib2.title(), len(kib2.fields))
kib2.merge(kib1)
print >>sys.stderr, '%s : %s %i' % (kib2.filename, kib2.title(), len(kib2.fields))
kib2.show()
