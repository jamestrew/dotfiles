from libqtile.command.client import InteractiveCommandClient

client = InteractiveCommandClient()

group_info = client.group.info()
layout = group_info['layout']
