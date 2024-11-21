# 1. Create the Teacher's Settings File:

# {
#     "extensions.autoUpdate": false,
#     "extensions.autoCheckUpdates": false,
#     "extensions.gallery": {
#         "serviceUrl": "",
#         "cacheUrl": "",
#         "itemUrl": ""
#     },
#     "extensions.path": "/home/x/.vscode/extensions", # important
#     "editor.fontSize": 14,
#     "editor.tabSize": 4,
#     "files.autoSave": "afterDelay"
# }

# 2. Create Symbolic Links for User Settings
for user in $(ls /home); do
    mkdir -p /home/$user/.vscode
    ln -sf /opt/vscode/shared-config/settings.json /home/$user/.vscode/settings.json
    chown -h $user:$user /home/$user/.vscode/settings.json
done
