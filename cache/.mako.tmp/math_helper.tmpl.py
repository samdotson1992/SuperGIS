# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1512933235.3371181
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/math_helper.tmpl'
_template_uri = 'math_helper.tmpl'
_source_encoding = 'ascii'
_exports = ['math_scripts_ifposts', 'math_styles', 'math_styles_ifpost', 'math_scripts', 'math_scripts_ifpost', 'math_styles_ifposts']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_scripts_ifposts(context,posts):
    __M_caller = context.caller_stack._push_frame()
    try:
        any = context.get('any', UNDEFINED)
        def math_scripts():
            return render_math_scripts(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if any(post.is_mathjax for post in posts):
            __M_writer('        ')
            __M_writer(str(math_scripts()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_styles(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_katex = context.get('use_katex', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_katex:
            __M_writer('        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/katex.min.css" integrity="sha384-wITovz90syo1dJWVh32uuETPVEtGigN07tkttEqPv+uR2SE/mbQcG7ATL28aI9H0" crossorigin="anonymous">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_styles_ifpost(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        def math_styles():
            return render_math_styles(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.is_mathjax:
            __M_writer('        ')
            __M_writer(str(math_styles()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_scripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        katex_auto_render = context.get('katex_auto_render', UNDEFINED)
        use_katex = context.get('use_katex', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_katex:
            __M_writer('        <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/katex.min.js" integrity="sha384-/y1Nn9+QQAipbNQWU65krzJralCnuOasHncUFXGkdwntGeSvQicrYkiUBwsgUqc1" crossorigin="anonymous"></script>\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/contrib/auto-render.min.js" integrity="sha256-ExtbCSBuYA7kq1Pz362ibde9nnsHYPt6JxuxYeZbU+c=" crossorigin="anonymous"></script>\n')
            if katex_auto_render:
                __M_writer('            <script>\n                renderMathInElement(document.body,\n                    {\n                        ')
                __M_writer(str(katex_auto_render))
                __M_writer('\n                    }\n                );\n            </script>\n')
            else:
                __M_writer('            <script>\n                renderMathInElement(document.body);\n            </script>\n')
        else:
            __M_writer('        <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML" integrity="sha256-SDRP1VVYu+tgAGKhddBSl5+ezofHKZeI+OzxakbIe/Y=" crossorigin="anonymous"></script>\n')
            if mathjax_config:
                __M_writer('        ')
                __M_writer(str(mathjax_config))
                __M_writer('\n')
            else:
                __M_writer('        <script type="text/x-mathjax-config">\n        MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$latex \',\'$\'], [\'\\\\(\',\'\\\\)\']]}});\n        </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_scripts_ifpost(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        def math_scripts():
            return render_math_scripts(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.is_mathjax:
            __M_writer('        ')
            __M_writer(str(math_scripts()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_styles_ifposts(context,posts):
    __M_caller = context.caller_stack._push_frame()
    try:
        any = context.get('any', UNDEFINED)
        def math_styles():
            return render_math_styles(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if any(post.is_mathjax for post in posts):
            __M_writer('        ')
            __M_writer(str(math_styles()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"130": 56, "131": 57, "132": 58, "133": 58, "134": 58, "140": 134, "16": 0, "21": 30, "22": 36, "23": 42, "24": 48, "25": 54, "26": 60, "32": 44, "39": 44, "40": 45, "41": 46, "42": 46, "43": 46, "49": 32, "54": 32, "55": 33, "56": 34, "62": 50, "68": 50, "69": 51, "70": 52, "71": 52, "72": 52, "78": 2, "85": 2, "86": 3, "87": 4, "88": 6, "89": 7, "90": 10, "91": 10, "92": 14, "93": 15, "94": 19, "95": 21, "96": 22, "97": 23, "98": 23, "99": 23, "100": 24, "101": 25, "107": 38, "113": 38, "114": 39, "115": 40, "116": 40, "117": 40, "123": 56}, "uri": "math_helper.tmpl", "source_encoding": "ascii", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/math_helper.tmpl"}
__M_END_METADATA
"""
