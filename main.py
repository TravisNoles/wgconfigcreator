# Wireguard Configuration Creator
import fire
from wgconfigeditor import WGConfig

class WireguardServer(object):
    def new(self, ipaddress, interface_name):
        """ Create new Wireguard Server config. """
        new_wg = WGConfig()
        new_wg.gen_wireguard_keys()
        new_wg.add_server_interface(new_wg.publickey, ipaddress)


class WireguardClient(object):
    def __init__(self):
        WireguardServer()

    def new(self):
        """ Create new wireguard client config. """
        print('test')


class Pipeline(object):
    def __init__(self):
        self.server = WireguardServer()
        self.client = WireguardClient()





if __name__ == '__main__':
    fire.Fire(Pipeline)