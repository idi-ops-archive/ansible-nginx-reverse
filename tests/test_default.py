import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_nginx_service(Service):
    s = Service('nginx')

    assert s.is_enabled
    assert s.is_running


def test_endpoint_config_file(File):
    f = File('/etc/nginx/conf.d/test-endpoint.conf')

    assert f.exists
