"""
Return config on servers to start for codeserver

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import shutil

def setup_app():
    # Make sure codeserver is in $PATH
    def _app_command(port):
       
        return ['app.sh', '{port}'] 
        
    return {
        'command': _app_command,
        'timeout': 20,
        'launcher_entry': {
            'title': 'Domino App',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      'icons', 'vscode.svg')
        }
    }
