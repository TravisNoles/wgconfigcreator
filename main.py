# Wireguard Configuration Creator
import fire
from wgconfigeditor import WGConfigEditor

class WireguardServer(object):
    def new(self, ipaddress, interface_name):
        """ Create new Wireguard Server config. """

        new_wg = WGConfigEditor()
        new_wg.generate_wireguard_keys()
        new_wg.add_server_interface(new_wg.publickey, ipaddress)








if __name__ == '__main__':
    fire.Fire(WireguardServer)