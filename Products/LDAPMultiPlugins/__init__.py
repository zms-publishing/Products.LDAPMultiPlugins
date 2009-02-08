##############################################################################
#
# Copyright (c) 2005-2009 Jens Vagelpohl and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" LDAPMultiPlugin product initialization

$Id$
"""

from AccessControl.Permissions import add_user_folders
from Products.PluggableAuthService.PluggableAuthService import \
        registerMultiPlugin
from LDAPMultiPlugin import LDAPMultiPlugin, \
                            manage_addLDAPMultiPlugin, \
                            addLDAPMultiPluginForm
from ActiveDirectoryMultiPlugin import ActiveDirectoryMultiPlugin, \
                            manage_addActiveDirectoryMultiPlugin, \
                            addActiveDirectoryMultiPluginForm

def initialize(context):
    """ Initialize the LDAPMultiPlugin """
    registerMultiPlugin(LDAPMultiPlugin.meta_type)
    registerMultiPlugin(ActiveDirectoryMultiPlugin.meta_type)

    context.registerClass( LDAPMultiPlugin
                         , permission=add_user_folders
                         , constructors=( addLDAPMultiPluginForm
                                        , manage_addLDAPMultiPlugin
                                        )
                         , icon='www/ldapmultiplugin.png'
                         , visibility=None
                         )

    context.registerClass( ActiveDirectoryMultiPlugin
                         , permission=add_user_folders
                         , constructors=( addActiveDirectoryMultiPluginForm
                                     , manage_addActiveDirectoryMultiPlugin
                                     )
                         , icon='www/admultiplugin.png'
                         , visibility=None
                         )
