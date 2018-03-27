from widget import Widget, WidgetError

class WidgetLibrary(object):
    def __init__(self):
        self._widget = Widget()
        #self._widget.load_json()
        self._result = ''

    def check_json(self):
        if self._widget.widget_data != None:
            self._result = 'JSON LOAD SUCCESS'
        else:
            self._result = 'JSON LOAD FAILED'

    def search(self, wname, wvalue):
        if wname == 'EMPTY':
            wname = ''        
        if wvalue == 'EMPTY':
            wvalue = ''
        if wname == 'NULL':
            wname = None
        if wvalue == 'NULL':
            wvalue = None
        self._result = self._widget.search(wname, wvalue)
    
    def result_should_be(self, expected_result):
        if expected_result != self._result:
            raise AssertionError("Expected result to be '%s' but was '%s'."
                                 % (expected_result, self._result))

    #incomplete - can search device only
    def search_with_filters(self, **kwargs):
        if kwargs is not None:
            self._result = self._widget.search_with_filters(**kwargs)
        else:
            self._result = 'No filter'