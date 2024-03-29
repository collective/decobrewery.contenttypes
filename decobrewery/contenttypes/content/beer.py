"""This file contains a page type using Deco and Blocks
"""

from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.blocks.layoutbehavior import ILayoutAware
from plone.namedfile.field import NamedImage
from plone.namedfile.interfaces import IImageScaleTraversable

class IBeer(form.Schema):
    """Beer schema"""
    
    price = schema.Float(
            title=u"Price",
            required=False,
        )
    alcohol_percentage = schema.Float(
            title=u"Alcohol percentage",
            required=False,
        )
    ingredients = schema.TextLine(
            title=u"Ingredients",
            required=False,
        )
    image = NamedImage(
            title=u"Picture",
            required=False,
        )


class Beer(dexterity.Container):
    grok.implements(IBeer, IImageScaleTraversable)


class View(grok.View):
    grok.context(IBeer)
    grok.require('zope2.View')

    def render(self):
        """
        Render the contents of the "content" field coming from 
        the plone.app.layoutbehavior behavior. 
        This result is supposed to be transformed by plone.app.blocks.
        """
        return ILayoutAware(self.context).content
