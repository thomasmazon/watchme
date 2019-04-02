
# Copyright (C) 2018-2019 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.


__version__ = "0.0.11"
AUTHOR = 'Vanessa Sochat'
AUTHOR_EMAIL = 'vsochat@stanford.edu'
NAME = 'watchme'
PACKAGE_URL = "http://www.github.com/vsoch/watchme"
KEYWORDS = 'web, changes, cron'
DESCRIPTION = "client to watch for webpage changes, and track over time"
LICENSE = "LICENSE"

INSTALL_REQUIRES = (
    ('python-crontab', {"min_version":"2.3.6"}),
)

## beautiful soup selection task

INSTALL_URLS_DYNAMIC = (
    ('beautifulsoup4', {'min_version': '4.6.0'}),
)

INSTALL_ALL = (INSTALL_REQUIRES +
               INSTALL_URLS_DYNAMIC)
