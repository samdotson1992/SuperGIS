# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1512914119.0798166
_enable_loop = True
_template_filename = 'themes/zen/templates/arusahni_helper.tmpl'
_template_uri = 'arusahni_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_feedlinks', 'html_translations', 'html_sourcelink', 'html_tags', 'html_navigation_links', 'html_title', 'html_stylesheets', 'late_load_js', 'html_headstart']


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
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_rss = context.get('generate_rss', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            for langname in translations.keys():
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('                <a href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('" rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('">\n                ')
                    __M_writer(str(messages("LANGUAGE", langname)))
                    __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('        &nbsp;&nbsp;|&nbsp;&nbsp;\n        <a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.tags:
            __M_writer('        <div itemprop="keywords" class="tags">\n        <ul>\n        ')
            __M_writer(str(messages("Tags")))
            __M_writer('&nbsp;:&nbsp;\n')
            for tag in post.tags:
                __M_writer('           <li><a class="tag p-category" href="')
                __M_writer(str(_link('tag', tag)))
                __M_writer('" rel="tag">')
                __M_writer(str(tag))
                __M_writer('</a></li>\n')
            __M_writer('        </ul>\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        navigation_links = context.get('navigation_links', UNDEFINED)
        rel_link = context.get('rel_link', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for url, text, icon in navigation_links[lang]:
            if rel_link(permalink, url) == "#":
                __M_writer('            <li><a href="')
                __M_writer(str(url))
                __M_writer('" title="')
                __M_writer(str(text))
                __M_writer('"><i class="')
                __M_writer(str(icon))
                __M_writer('"></i></a></li>\n')
            else:
                __M_writer('            <li><a href="')
                __M_writer(str(url))
                __M_writer('" title="')
                __M_writer(str(text))
                __M_writer('"><i class="')
                __M_writer(str(icon))
                __M_writer('"></i></a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <h1 class="p-name entry-title" itemprop="headline name">')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_cdn = context.get('use_cdn', UNDEFINED)
        annotations = context.get('annotations', UNDEFINED)
        post = context.get('post', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        notes = context.get('notes', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <link href=\'//fonts.googleapis.com/css?family=Bitter:400,400italic,700\' rel=\'stylesheet\' type=\'text/css\'>\n            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            if use_cdn:
                __M_writer("            <link href='//fonts.googleapis.com/css?family=Bitter:400,400italic,700' rel='stylesheet' type='text/css'>\n")
            else:
                __M_writer('            <link href="/assets/css/bitter.css" rel="stylesheet" type="text/css">\n')
            __M_writer('        <link href="/assets/css/main.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer('        ')
            __M_writer(str(notes.css()))
            __M_writer('\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer('        ')
            __M_writer(str(notes.css()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_cdn = context.get('use_cdn', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>\n            <script src="//cdnjs.cloudflare.com/ajax/libs/jquery-timeago/1.1.0/jquery.timeago.min.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/all-nocdn.js" type="text/javascript"></script>\n')
        else:
            if use_cdn:
                __M_writer('            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>\n            <script src="//cdnjs.cloudflare.com/ajax/libs/jquery-timeago/1.1.0/jquery.timeago.min.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/jquery-1.10.2.min.js" type="text/javascript"></script>\n            <script src="/assets/js/jquery.timeago.js" type="text/javascript"></script>\n')
        __M_writer('    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        title = context.get('title', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        description = context.get('description', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        striphtml = context.get('striphtml', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        blog_title = context.get('blog_title', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html\n')
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']) or (comment_system == 'facebook'):
            __M_writer("prefix='")
            if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
                __M_writer('og: http://ogp.me/ns# ')
            if use_open_graph:
                __M_writer('article: http://ogp.me/ns/article# ')
            if comment_system == 'facebook':
                __M_writer('fb: http://ogp.me/ns/fb# ')
            __M_writer("'")
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n    <head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(str(description))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width">\n    <title>')
        __M_writer(striphtml(str(title)))
        __M_writer(' | ')
        __M_writer(striphtml(str(blog_title)))
        __M_writer('</title>\n\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n')
        if permalink:
            __M_writer('      <link rel="canonical" href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        __M_writer('\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="/assets/js/html5.js"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "arusahni_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 57, "22": 85, "23": 105, "24": 119, "25": 129, "26": 143, "27": 150, "28": 161, "29": 168, "35": 107, "44": 107, "45": 108, "46": 109, "47": 109, "48": 109, "49": 110, "50": 111, "51": 112, "52": 113, "53": 113, "54": 113, "55": 113, "56": 113, "57": 115, "58": 116, "59": 116, "60": 116, "66": 152, "74": 152, "75": 153, "76": 154, "77": 155, "78": 156, "79": 156, "80": 156, "81": 156, "82": 156, "83": 157, "84": 157, "90": 163, "97": 163, "98": 164, "99": 165, "100": 166, "101": 166, "102": 166, "103": 166, "109": 132, "115": 132, "116": 133, "117": 134, "118": 136, "119": 136, "120": 137, "121": 138, "122": 138, "123": 138, "124": 138, "125": 138, "126": 140, "132": 121, "140": 121, "141": 122, "142": 123, "143": 124, "144": 124, "145": 124, "146": 124, "147": 124, "148": 124, "149": 124, "150": 125, "151": 126, "152": 126, "153": 126, "154": 126, "155": 126, "156": 126, "157": 126, "163": 146, "169": 146, "170": 147, "171": 148, "172": 148, "173": 148, "179": 59, "189": 59, "190": 60, "191": 61, "192": 62, "193": 64, "194": 65, "195": 67, "196": 68, "197": 69, "198": 70, "199": 71, "200": 73, "201": 76, "202": 77, "203": 80, "204": 81, "205": 81, "206": 81, "207": 82, "208": 83, "209": 83, "210": 83, "216": 87, "223": 87, "224": 88, "225": 89, "226": 90, "227": 92, "228": 93, "229": 95, "230": 96, "231": 97, "232": 99, "233": 100, "234": 104, "235": 104, "236": 104, "242": 3, "265": 3, "266": 7, "267": 8, "268": 9, "269": 10, "270": 12, "271": 13, "272": 15, "273": 16, "274": 18, "275": 21, "276": 22, "277": 25, "278": 25, "279": 25, "280": 28, "281": 29, "282": 29, "283": 29, "284": 31, "285": 32, "286": 32, "287": 32, "288": 32, "289": 34, "290": 34, "291": 35, "292": 35, "293": 36, "294": 37, "295": 37, "296": 37, "297": 39, "298": 40, "299": 41, "300": 42, "301": 42, "302": 42, "303": 42, "304": 42, "305": 42, "306": 42, "307": 45, "308": 46, "309": 47, "310": 47, "311": 47, "312": 49, "313": 50, "314": 51, "315": 52, "316": 53, "317": 55, "318": 56, "319": 56, "325": 319}, "filename": "themes/zen/templates/arusahni_helper.tmpl"}
__M_END_METADATA
"""
