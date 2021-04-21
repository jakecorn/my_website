# -*- coding: utf-8 -*-
{
    'name': "my_website",
    'summary': "My Website",
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'website', 'portal'],
    # always loaded
    'data': [
        'views/views.xml',
        'views/assets.xml',
        'views/homepage.xml',
        'views/templates.xml',
        'views/footer.xml',
        'views/pages/contactus.xml',
    ],
}
