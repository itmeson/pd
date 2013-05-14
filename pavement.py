import paver
import paver.misctasks
from paver.path import path
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()

from sphinxcontrib import paverutils

# You will want to change these for your own environment
master_url = 'http://127.0.0.1:8000'
master_app = 'runestone'


options(
    sphinx = Bunch(
        docroot=".",
        ),

    everyday = Bunch(
        outdir="static/everyday",
        sourcedir="everyday",
        builddir="static/everyday",
        confidir="everyday",
        template_args={'course_id':'everyday',
                       'login_required':'false',
                       'appname':master_app,
                       'loglevel':10,
                       'course_url':master_url }
        ),

    thinkcspy = Bunch(
        builddir="static/thinkcspy",
        sourcedir="source",
        outdir="static/thinkcspy",
        confdir="thinkcspy",
        template_args={'course_id':'thinkcspy',
                       'login_required':'false',
                       'appname':master_app,
                       'loglevel':10,
                       'course_url':master_url }

    ),

    pythonds = Bunch(
        builddir="static/pythonds",
        sourcedir="source",
        outdir="static/pythonds",
        confdir="pythonds",
        template_args={'course_id':'pythonds',
                       'login_required':'false',
                       'appname':master_app,
                       'loglevel':10,
                       'course_url':master_url }

    ),

    overview = Bunch(
        builddir="static/overview",
        sourcedir="overview",
        outdir="static/overview",
        confdir="overview",
        template_args={'course_id':'overview',
                       'login_required':'false',
                       'appname':master_app,
                       'loglevel':10,
                       'course_url':master_url }

    ),

    devcourse = Bunch(
        builddir="static/devcourse",
        sourcedir="source",
        outdir="static/devcourse",
        confdir="devcourse",
        template_args={'course_id':'devcourse',
                       'login_required':'true',
                       'appname':master_app,
                       'loglevel':10,
                       'course_url':master_url }

    ),

    pd = Bunch(
	builddir="static/pd",
	sourcedir="source",
	outdir="static/pd",
	confdir="pd",
	template_args={'course_id':'pd',
		       'login_required':'true',
		       'appname':master_app,
                       'loglevel':10,
                       'course_url':master_url }	
    )

)

@task
def everyday(options):
    paverutils.run_sphinx(options,'everyday')

@task
def thinkcspy(options):
    sh('cp %s/index.rst %s' % (options.thinkcspy.confdir,options.thinkcspy.sourcedir))

    paverutils.run_sphinx(options,'thinkcspy')

@task
def pythonds(options):
    sh('cp %s/index.rst %s' % (options.pythonds.confdir,options.pythonds.sourcedir))

    paverutils.run_sphinx(options,'pythonds')

@task
def overview(options):
    paverutils.run_sphinx(options,'overview')

@task
def devcourse(options):
    sh('cp %s/index.rst %s' % (options.devcourse.confdir,options.devcourse.sourcedir))

    paverutils.run_sphinx(options,'devcourse')

@task
def pd(options):
    sh('cp %s/index.rst %s' % (options.pd.confdir,options.pd.sourcedir))

    paverutils.run_sphinx(options,'pd')


@task
def allbooks(options):
    thinkcspy(options)
    pythonds(options)
    devcourse(options)
    overview(options)
    pd(options)
