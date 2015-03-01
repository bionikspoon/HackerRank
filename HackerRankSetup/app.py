import ConfigParser
import os

config = ConfigParser.SafeConfigParser()
config.read('config.cfg')

project = os.path.abspath(config.get('HackerRank', 'Root'))
workspace = os.path.relpath(config.get('HackerRank', 'Workspace'), project)
assets = os.path.relpath(config.get('HackerRank', 'Assets'), project)

print project, workspace, assets