# Tiny Django Project from Scratch

Shout out to
[Vitor Freitas](https://simpleisbetterthancomplex.com/about/) for his wonderful
article,
[A Minimal Django Application](https://simpleisbetterthancomplex.com/article/2017/08/07/a-minimal-django-application.html),
from which this little experiment was taken!

This creates a minimal Django project "from scratch", without using the
template in
[django.conf.project_template](https://github.com/django/django/tree/main/django/conf/project_template). Instead,
the minimal requirements to get a running application are written from scratch.


## Usage

Run:
``` 
django-admin runserver --pythonpath=. --settings=tinyapp 0:8000
``` 
and point your browser at the host system on port ``8000``.


## Resources

* [The Django template language: for Python programmers](https://docs.djangoproject.com/en/dev/ref/templates/api/)
