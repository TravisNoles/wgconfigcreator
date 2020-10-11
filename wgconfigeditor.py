import os, subprocess, configparser, random, fabric, getpass

class AppConfig():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.createconfig() # Creates config if file doesn't exist

    def save(self):
        """Save file wgconfigcreator's configuration (ini) """
        with open('servers.ini', 'w') as inifile:
            self.config.write(inifile)

    def load(self):
        """Loads wgconfigcreator's configuration (inifile) """
        print("stub")

    def add_client(self, ip_address, endpoint):
        self.config['clients'][ip_address] = endpoint

    def createconfig(self):
        """If wgconfigcreator's config doesn't exist create it. """
        self.config.add_section('clients')
        self.config.add_section('endpoints')
        self.config.add_section('system')

class WGConfig():
    def __init__(self, interfacename):
        self.filename = interfacename + '.conf'

        self.section_total = 0
        self.section_locations = []

        self.publickey = ""
        self.privatekey = ""
        self.config = configparser.ConfigParser()
        #self.gen_wireguard_keys()


    def get_section(self, name):
        """Get section and the line number of the section. """
        with open(self.filename) as wgconfig:
            line = wgconfig.readline()
            while line:
                if line.strip() == '[' + name + ']':
                    self.sections.append(line.strip())
                    self.section_locations.append(line.index())
                line = wgconfig.readline()

    def get_peers(self):
        self.get_section('Peer')

    def get_interfaces(self):
        self.get_section('Interface')

    def gen_wireguard_keys(self):
        os.system("cd && wg genkey | tee privatekey | wg pubkey > publickey")
        username = getpass.getuser()

        publickey = subprocess.check_output(['cat', '/home/' + username + '/publickey'])
        privatekey = subprocess.check_output(['cat', '/home/' + username + '/privatekey'])
        self.publickey = publickey.decode().strip() #strips all endline characters
        self.privatekey = privatekey.decode().strip()

    def add_endpoint(self):
        with open(self.filename, 'a') as configfile:
            configfile.write('[Peer]' + '\n')
            configfile.write('PublicKey = ' + self.publickey + '\n')

    def add_server_peer(self, publickey):
         with open(self.filename, 'a') as configfile:
             configfile.write('[Peer]' + '\n')
             configfile.write(publickey + '\n')
             configfile.close()

    def add_server_interface(self, publickey, ipaddress):
        """Add interface for wireguard servers (not peers). """
        with open(self.filename, 'a') as configfile:
            configfile.write('[Interface]\n')
            configfile.write('Address' + ipaddress + '\n')
            configfile.write('PrivateKey = ' + ipaddress + '\n')
            configfile.write('ListenPort = ' + str(random.randint(8000,38888)) + '\n')

    def create_file(self, interface_name):
        """Creates new wireguard file with new pub/private keys. """
        with open(self.filename, 'w') as configfile:
            self.gen_wireguard_keys()


class ConfigFile():
    def __init__(self, filename):
        self.filename = filename
        self.config = configparser.ConfigParser()
        self.wireguard

    def add_wireguard_interface(self, interface):
        self.config['']

    def new(self):
        """ Create new local config file for tracking wireguard configs. """
        with open(self.filename, 'w') as configfile:
            configfile.write('')

    def save(self):
        """ Save changes to config. ""
        

    def append_line(self, line):
        """ Append line to file. """
        with open(self.filename)





