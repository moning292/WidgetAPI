from widget import Widget, WidgetError

class WidgetLibrary(object):
    def __init__(self):
        self._widget = Widget()
        self._result = ''

    def search(self, wname, wvalue):
        if wname == 'EMPTY':
            wname = ''        
        if wvalue == 'EMPTY':
            wvalue = ''
        self._result = self._widget.search(wname, wvalue)
    
    def result_should_be(self, expected_result):
        if expected_result != self._result:
            raise AssertionError("Expected result to be '%s' but was '%s'."
                                 % (expected_result, self._result))