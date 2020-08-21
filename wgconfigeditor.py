import os, subprocess, configparser, random, fabric

class Configuration():
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
    def __init__(self):
        self.sections = []
        self.filename = 'test'
        self.publickey = ""
        self.privatekey = ""
        self.config = configparser.ConfigParser()

    def parse_wg_config(self, sectionname):
        """Parses Interface or peer sections. """
        with open(self.filename) as wgconfig:
            line = wgconfig.readline()
            while line:
                if line.strip() == '[' + sectionname + ']':
                    self.sections.append(line.strip())
                line = wgconfig.readline()


    # def parse_sections(self):
    #     """  Load all sections into array function. """
    #
    #     # In this function, we need to get the wireguard sections.
    #     # In order to do that, we first need to get all of the sections,
    #     # the number of sections, and then we can parse those.
    #
    #     with open('test') as file:
    #         line = file.readline()
    #         lineNumberCount = 1
    #         while line:
    #             #print(line.strip())
    #             if line.strip().startswith('[') and line.strip().endswith(']'):
    #                 self.sections.append(line.strip())
    #             line = file.readline()

    def parse_peers(self):
        """Parse all peers in config file. """
        self.parse_wg_config('Interface')

    def parse_interface(self):
        self.parse_section('Interface')

    #def add_peer_endpoint(self, interfacename, peername, endpoint):
    # def add_peer_endpoint(self):
    #     with open(self.filename, 'a') as configfile:
    #         configfile.write('[Peer]')
    #         self.publickey = os.system('cat ~/publickey')
    #         configfile.write('Public Key = ' + self.publickey)

    def generate_wireguard_keys(self):
        """Generates wireguard private and public keys into home directory. """
        os.system("cd && wg genkey | tee privatekey | wg pubkey > publickey")

        self.publickey = os.system('cat ~/publickey')
        self.privatekey = os.system('cat ~/privatekey')

    def add_server_peer(self, publickey):
         with open(self.filename, 'a') as configfile:
             configfile.write('[Peer]' + '\n')
             configfile.write(publickey + '\n')

    def add_server_interface(self, publickey, ipaddress):
        """Add interface for wireguard servers (not peers). """

        with open(self.filename, 'a') as configfile:
            configfile.write('[Interface]\n')
            configfile.write('Address' + ipaddress + '\n')
            configfile.write('PrivateKey = ' + ipaddress + '\n')
            configfile.write('ListenPort = ' + str(random.randint(8000,38888)) + '\n')

    def save_config(self):

        # Create sections if they don't exist (If they do it will ignore)

        self.config.add_section('clients')
        self.config.add_section('endpoints')





