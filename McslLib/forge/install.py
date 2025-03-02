import os
import requests
import McslLib.forge.install
import McslLib.forge.utils

def install_forge(version, path, name):
    URL=f"https://bmclapi2.bangbang93.com/forge/minecraft/{version}"
    json=requests.get(URL).json()[0]
    print(json)
    build=json["build"]
    forge_version=json["version"]
    URL=f"https://bmclapi2.bangbang93.com/maven/net/minecraftforge/forge/{version}-{forge_version}/forge-{version}-{forge_version}-installer.jar"
    os.makedirs(f"{path}/servers/{name}", exist_ok=True)
    McslLib.forge.utils.download_progress(url=URL, path=f"{path}/temps/forge-{version}-{forge_version}-installer.jar",p2=f"{path}/servers/{name}")