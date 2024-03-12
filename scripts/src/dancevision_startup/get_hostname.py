import subprocess

def get_hostname():
    return bytes.decode(subprocess.check_output(["hostname", "-I"])).strip()