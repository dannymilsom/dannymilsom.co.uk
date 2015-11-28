from dannywebsite.settings import *

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-progressive',
    '--progressive-bar-filled=4',
    '--progressive-function-color=4',
    '--with-coverage',
    '--cover-erase',
    '--cover-html',
    '--cover-html-dir=coverage_html',
    '--logging-level=CRITICAL'
]