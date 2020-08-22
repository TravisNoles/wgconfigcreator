# wgconfigcreator
Wireguard CLI Configuration Creator 

#Overview
WGConfigCreator was created in order to make deploying wireguard easier in my homelab environment, rather than creating all 
of the wireguard configuration manually, this will automatically create the files needed in order
to have a working wireguard environment up and running quicker. 

Not completely working, app is still in heavy development. Almost to working state, working on having an
working version by 29th of August 2020. 

Semi working state, is able to generate private/public keys and export them to the home directory. 
Working on generating the wireguard config and keeping track of the changes inside an internal
.ini configuration. 

This app uses a custom wireguard configuration editor, built from scratch since the built in config editor doesn't work with
Wireguard configuration because of the duplicate sections. 

# Features
* Create Wireguard Server
* Add wireguard peer
* Add wireguard endpoint




# Feature Roadmap
* Remove wireguard peers
* Remove wireguard endpoints
* Edit wireguard endpoints
* Edit wireguard peers
* Push changes to clients/server
* Generate QR codes, display in terminal or popup webpage