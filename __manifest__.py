{
    'name': "my_website",
    'summary': "My Website",
    'author': "Jake Cornelia",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'website', 'portal', 'website_form', 'website_blog', 'crm', 'website_mass_mailing'],
    # always loaded
    'data': [
        'views/backend/common.xml',
        'views/views.xml',
        'views/assets.xml',
        'views/website_builder_snippet.xml',
        'views/homepage.xml',
        'views/templates.xml',
        'views/footer.xml',
        'views/snippets.xml',
        'views/pages/contactus.xml',
        'data/pages.xml',
        'data/fields.xml',
    ],
}
# -*- coding: utf-8 -*-
