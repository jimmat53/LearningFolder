import os
import sys

from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

settings.configure(DEBUG=DEBUG, SECRET_KEY=SECRET_KEY,
	ROOT_URLCONF=__name__,
	MIDDLEWARE_CLASSES=('django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',),)

application = get_wsgi_application()

def index(request):
    return HttpResponse('Hello World')

urlpatterns = (
        url(r'^$', index),
        )

if __name__ == "__main__":
	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)
