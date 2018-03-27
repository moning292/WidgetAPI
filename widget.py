import json
import re

#Config data file here
WIDGET_FILE = 'widget_data.json'
BACKUP_FILE = 'backup.json'

class Widget(object):
    def __init__(self, wg_file=WIDGET_FILE):
        self.widget_data = self._load_json(wg_file)
        #self.widget_data = None
        self.wg_file = wg_file

    def _load_json(self,path):
        #Load JSON file
        try:
            widget_data = json.loads(open(path).read())
            with open(BACKUP_FILE,'w') as f:
                json.dump(widget_data, f)
        except WidgetError as err:
            print('ERROR: %s' % err)
            return None
        return widget_data

    def search(self, wname, wvalue):
        if wname is None or wvalue is None:
            return 'Search text is none'
        #Check empty string
        if wname == '' or wvalue == '':
            return 'Cannot search'
        #Check if a string does not contain special characters
        reg_text = r'^[a-zA-Z0-9_\s]*$'
        if not re.match(reg_text, wname) or not re.match(reg_text, wvalue):
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
                elif wname == 'site' and (self.widget_data[i][wname] == 'all' or wvalue in self.widget_data[i][wname]):
                    search_result.append(i)
            else:
                return 'Property \'%s\' is not found' % wname
        return ','.join(search_result)
    
    #incomplete - can search device only
    def search_with_filters(self, **kwargs):
        search_result = []
        for name, value in kwargs.items():
            name = name.lower()
            value = value.lower()
            for i in self.widget_data:
                if name in self.widget_data[i]:
                    if i not in search_result:
                        if value == 'all':                      
                            search_result.append(i)
                        elif (self.widget_data[i][name] == 'all' or self.widget_data[i][name] == value):
                            search_result.append(i)
                else:
                    return 'Property \'%s\' is not found' % wname
        return ','.join(search_result)

class WidgetError(Exception):
    pass