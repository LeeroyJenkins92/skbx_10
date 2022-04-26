import testinfra


def tst_os_release(host):
    assert host.file("/etc/os-release").contains("Alpine")

def is_nginx_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed
    assert nginx.version.statswith("1.18")

def is_nginx_running(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled


