=========================
cookiecutter-saltformula
=========================

Cookiecutter template for a Salt Formula. See https://github.com/audreyr/cookiecutter.

* Free software: BSD license
* Vanilla testing setup with `unittest` and `python setup.py test`
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 2.6, 2.7, 3.3
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_

Usage
-----

Generate a salt formula project::

    cookiecutter https://github.com/westurner/cookiecutter-saltformula.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis CI account.
* Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
* Release your package the standard Python way. Here's a release checklist: https://gist.github.com/audreyr/5990987
* Also see the `network`_ and `family tree`_ for this repo. (If you find
  anything that should be listed here, please add it and send a pull request!)


.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _github comparison view: https://github.com/westurner/cookiecutter-saltformula/compare/westurner:master...master
.. _`network`: https://github.com/westurner/cookiecutter-saltformula/network
.. _`family tree`: https://github.com/westurner/cookiecutter-saltformula/network/members
