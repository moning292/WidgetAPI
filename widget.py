import json
import re

#Config data file here
WIDGET_FILE = 'widget_data.json'

class Widget(object):
    def __init__(self, wg_file=WIDGET_FILE):
        self.widget_data = self._load_json(wg_file)
        #self.widget_data = None
        self.wg_file = wg_file

    def _load_json(self,path):
        #Load JSON file
        try:
            widget_data = json.loads(open(path).read())
        except Exception as e:
            #print('Invalid JSON: %s' %e)
            return None
        return widget_data

    def search(self, wname, wvalue, **kwargs):
        if kwargs is not None:
            for name, value in kwargs.items():
            #print('%s:%s' % (key, kwargs[key]))
        #Check null
            #if name == 'arg':
                return name
        if wname is None or wvalue is None:
            return 'Search text is none'
        #Check empty string
        if wname == '' or wvalue == '':
            return 'Cannot search'
        #Check if a string does not contain special characters
        if not re.match('^[a-zA-Z0-9_]*$', wname) or not re.match('^[a-zA-Z0-9_]*$', wvalue):
            return 'Invalid character'
        #Convert string to lower case
        wname = wname.lower()
        wvalue = wvalue.lower()
        search_result = []
        for i in self.widget_data:
            if wname in self.widget_data[i]:
                if wvalue == 'all':
                    search_result.append(i)
                elif wname == 'device' and (self.widget_data[i][wname] == 'all' or self.widget_data[i][wname] == wvalue):
                    search_result.append(i)
                #elif wname == 'site' and wvalue == 'all':
                #    search_result.append(i)
                elif wname == 'site' and (self.widget_data[i][wname] == 'all' or wvalue in self.widget_data[i][wname]):
                    search_result.append(i)
                #elif wvalue == 'all':
                #    search_result.append(i)
            else:
                return 'Property \'%s\' is not found' % wname
        return ','.join(search_result)

class WidgetError(Exception):
    pass