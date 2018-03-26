import json
import re

WIDGET_FILE = 'widget_data.json'

class Widget(object):
    def __init__(self, wg_file=WIDGET_FILE):
        self.widget_data = self._load_json(wg_file)
        self.wg_file = wg_file

    def _load_json(self,path):
        widget_data = json.loads(open(path).read())
        return widget_data
    
    def search(self, wname, wvalue):
        if not re.match('^[a-zA-Z0-9_]*$', wname) or not re.match('^[a-zA-Z0-9_]*$', wvalue):
            return 'Invalid character'
        wname = wname.lower()
        wvalue = wvalue.lower()
        search_result = []
        if wname == '' or wvalue == '':
            return 'Cannot search'
        for i in self.widget_data:
            if wname in self.widget_data[i]:
                if wname == 'device' and wvalue == 'all':
                    search_result.append(i)
                elif wname == 'device' and (self.widget_data[i][wname] == 'all' or self.widget_data[i][wname] == wvalue):
                    search_result.append(i)
                elif wname == 'site' and wvalue == 'all':
                    search_result.append(i)
                elif wname == 'site' and (self.widget_data[i][wname] == 'all' or wvalue in self.widget_data[i][wname]):
                    search_result.append(i)                                        
        return ','.join(search_result)

class WidgetError(Exception):
    pass