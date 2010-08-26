"""This file contains a page type using Deco and Blocks
"""

from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.layoutbehavior import ILayout

class INewsItem(form.Schema):
    """NewsItem schema"""

    source = schema.TextLine(
            title=u"Source",
            required=False,
        )


class NewsItem(dexterity.Container):
    grok.implements(INewsItem)


class View(grok.View):
    grok.context(INewsItem)
    grok.require('zope2.View')

    def render(self):
        """
        Render the contents of the "content" field coming from 
        the plone.app.layoutbehavior behavior. 
        This result is supposed to be transformed by plone.app.blocks.
        """
        return ILayout(self.context).content
