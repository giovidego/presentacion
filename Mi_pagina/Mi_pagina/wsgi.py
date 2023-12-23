"""
WSGI config for Mi_pagina project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
#from pathlib import Path
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
#BASE_DIR = Path(__file__).resolve().parent
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mi_pagina.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join('/opt/render/project/src/Mi_pagina', '/staticfiles'))
