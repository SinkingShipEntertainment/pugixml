name = "pugixml"

version = "1.14.sse.1.0.0"

description = \
    """
    Light-weight, simple and fast XML parser for C++ with XPath support
    """

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
]

variants = [
]

build_system = "cmake"
uuid = "repository.pugixml"


def pre_build_commands():

    info = {}
    with open("/etc/os-release", 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line_info = line.replace('\n', '').split('=')
            if len(line_info) != 2:
                continue
            info[line_info[0]] = line_info[1].replace('"', '')
    linux_distro = info.get("NAME", "centos")
    print("Using Linux distro: " + linux_distro)

    if linux_distro.lower().startswith("centos"):
        command("source /opt/rh/devtoolset-6/enable")
    elif linux_distro.lower().startswith("rocky"):
        pass

def commands():
    env.PUGIXML_LOCATION = "{root}"
    env.pugixml_ROOT = "{root}"
    env.pugixml_INCLUDE_DIR = "{root}/include"
    env.pugixml_LIBRARY_DIR = "{root}/lib64"

    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
