from repeater.views import get_time
import os


def home(default_url):
    result = dict()

    result['html'] = 'repeater/home.html'

    variables = dict()
    build_time = os.getenv('build_time', default=0)
    variables['build_time'] = get_time.string(build_time)
    deploy_time = os.getenv('deploy_time')
    variables['deploy_time'] = get_time.string(deploy_time)

    variables['default_url'] = default_url

    result['variables'] = variables

    return result
