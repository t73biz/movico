# -*- coding: utf-8 -*-

from core.views.helpers.Helper import Helper

class Html(Helper):
    """Html Helper Class for rendering well formatted html elements"""

    charset = "UTF-8"

    tags = {
        'meta' : '<meta{0}/>',
        'metalink' : '<link href="{0}"{1}/>',
        'link' : '<a href="{0}"{0}>{2}</a>',
        'mailto' : '<a href="mailto:{0}" {1}>{2}</a>',
        'form' : '<form {1}>',
        'formend' : '</form>',
        'input' : '<input name="{0}" {1}/>',
        'textarea' : '<textarea name="{0}" {1}>{2}</textarea>',
        'hidden' : '<input type="hidden" name="{0}" {1}/>',
        'checkbox' : '<input type="checkbox" name="{0}" {1}/>',
        'checkboxmultiple' : '<input type="checkbox" name="{0}[]"{1} />',
        'radio' : '<input type="radio" name="{0}" id="{2}" {3} />{4}',
        'selectstart' : '<select name="{0}"{1}>',
        'selectmultiplestart' : '<select name="{0}[]"{1}>',
        'selectempty' : '<option value=""{0}>&nbsp;</option>',
        'selectoption' : '<option value="{0}"{1}>{2}</option>',
        'selectend' : '</select>',
        'optiongroup' : '<optgroup label="{0}"{1}>',
        'optiongroupend' : '</optgroup>',
        'checkboxmultiplestart' : '',
        'checkboxmultipleend' : '',
        'password' : '<input type="password" name="{0}" {1}/>',
        'file' : '<input type="file" name="{0}" {1}/>',
        'file_no_model' : '<input type="file" name="{0}" {1}/>',
        'submit' : '<input {0}/>',
        'submitimage' : '<input type="image" src="{0}" {1}/>',
        'button' : '<button type="{0}"{1}>{2}</button>',
        'image' : '<img src="{0}" {1}/>',
        'tableheader' : '<th{0}>{0}</th>',
        'tableheaderrow' : '<tr{0}>{1}</tr>',
        'tablecell' : '<td{0}>{1}</td>',
        'tablerow' : '<tr{0}>{1}</tr>',
        'block' : '<div{0}>{1}</div>',
        'blockstart' : '<div{1}>',
        'blockend' : '</div>',
        'tag' : '<{0}{1}>{2}</{3}>',
        'tagstart' : '<{0}{1}>',
        'tagend' : '</{0}>',
        'para' : '<p{0}>{1}</p>',
        'parastart' : '<p{0}>',
        'label' : '<label for="{0}"{1}>{2}</label>',
        'fieldset' : '<fieldset{0}>{1}</fieldset>',
        'fieldsetstart' : '<fieldset><legend>{0}</legend>',
        'fieldsetend' : '</fieldset>',
        'legend' : '<legend>{0}</legend>',
        'css' : '<link rel="{0}" type="text/css" href="{1}" {2}/>',
        'style' : '<style type="text/css"{0}>{1}</style>',
        'charset' : '<meta http-equiv="Content-Type" content="text/html; charset={0}" />',
        'ul' : '<ul{0}>{1}</ul>',
        'ol' : '<ol{0}>{1}</ol>',
        'li' : '<li{0}>{1}</li>',
        'error' : '<div{0}>{1}</div>',
        'javascriptblock' : '<script type="text/javascript"{0}>{1}</script>',
        'javascriptstart' : '<script type="text/javascript">',
        'javascriptlink' : '<script type="text/javascript" src="{0}"{1}></script>',
        'javascriptend' : '</script>'
    }

    def __init__(self, charset = "UTF-8"):
        self.charset = charset

    def tag(self, name, text = None, options = None):

        """
        Render an Html.tag that matches the name variable
        """
        if text == None:
            text = ""

        if options == None:
            options = ""
        else:
            pass

        if name in self.tags:
            print(self.tags[name].format(options, text))
