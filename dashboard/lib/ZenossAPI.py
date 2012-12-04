import json
import urllib
import urllib2

ROUTERS = { 'EventsRouter': 'evconsole' }

class ZenossAPI():
    def __init__(self, ZENOSS_INSTANCE, ZENOSS_USERNAME, ZENOSS_PASSWORD):
        """
        Initialize the API connection, log in, and store authentication cookie
        """
        
        # Use the HTTPCookieProcessor as urllib2 does not save cookies by default
        self.urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        self.reqCount = 1
        self.ZENOSS_INSTANCE = ZENOSS_INSTANCE

        # Contruct POST params and submit login.
        loginParams = urllib.urlencode(dict(
                        __ac_name = ZENOSS_USERNAME,
                        __ac_password = ZENOSS_PASSWORD,
                        submitted = 'true',
                        came_from = ZENOSS_INSTANCE + '/zport/dmd'))
        try:
            self.urlOpener.open(ZENOSS_INSTANCE + '/zport/acl_users/cookieAuthHelper/login',
                                loginParams)
        except urllib2.URLError, e:
            print "Unable to connect to " + ZENOSS_INSTANCE 

    def _router_request(self, router, method, data=[]):
        if router not in ROUTERS:
            raise Exception('Router "' + router + '" not available.')

        req = urllib2.Request(self.ZENOSS_INSTANCE + '/zport/dmd/' +
                              ROUTERS[router] + '_router')

        req.add_header('Content-type', 'application/json; charset=utf-8')

        reqData = json.dumps([dict(
                    action=router,
                    method=method,
                    data=data,
                    type='rpc',
                    tid=self.reqCount)])

        self.reqCount += 1

        return json.loads(self.urlOpener.open(req, reqData).read())

    def get_events(self, device=None, component=None, eventClass=None):
        data = dict(start=0, limit=100, dir='DESC', sort='severity')
        data['params'] = dict(severity=[5,4,3,2], eventState=[0,1])

        if device: data['params']['device'] = device
        if component: data['params']['component'] = component
        if eventClass: data['params']['eventClass'] = eventClass

        return self._router_request('EventsRouter', 'query', [data])['result']
