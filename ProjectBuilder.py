import webbrowser

class Project:

    def __init__(self, label : str, describe : str):
        self.json = {"label": label, "describe": describe, "data": {}, "custom": 'function custom() {}'}

    def Page(self, func):
        self.json['data'][func.__name__.replace(' ', '')] = {"png": [], "chapter": [], "link": []}
        return func(func.__name__)
    
    def AddPng(self, page_name : str, src : str):
        self.json['data'][page_name]['png'].append({"src": src})

    def AddChapter(self, page_name : str, label : str, text : str):
        self.json['data'][page_name]['chapter'].append({"label": label, "text": text})

    def AddLink(self, page_name : str, text : str, href : str):
        self.json['data'][page_name]['link'].append({"href": href, "text": text})

    def SetCustom(self, code : str):
        self.json['custom'] = code

class Builder:
    
    def __init__(self):
        self.css = '$fonts$ #label { padding-left:10%; margin-bottom:0px; margin-top:0px; font-size:650%; } #sublabel { padding-left:10%; margin-bottom:0px; margin-top:0px; font-size:450%; } #menu { text-align:center; } #png { padding-top:1%; text-align:center; } #link { text-align:center; } button { font-size:300%; } .chptname { text-align:center; font-size:350%; } .chptdescribe { text-align:justify; padding-left:15%; padding-right:15%; font-size:250%; } a { font-size:200%; } img { height:200px; width:300px; margin-top:20px;} img:hover { height:220px; width:320px; margin-top:0px;}'
        self.javascript = 'var unerror_veriable=undefined; function CssEditLoading(){ $cssswap$ } function Page(ipng, ichapter, ilink){return {png:ipng,chapter:ichapter,link:ilink}} var curr_page; $page_data$ function setPage(data){const png=document.getElementById("png"),chapter=document.getElementById("chapter"),link=document.getElementById("link");let innerHTML="";for(let i=0;i<data.png.length;i++){innerHTML+=`<img src="${data.png[i]}">`}png.innerHTML=innerHTML;innerHTML="";for(let i=0;i<data.chapter.length;i++){innerHTML+=`<h1 class="chptname">${data.chapter[i][0]}</h1>`;innerHTML+=`<h2 class="chptdescribe">${data.chapter[i][1]}</h2>`}chapter.innerHTML=innerHTML;innerHTML="";for(let i=0;i<data.link.length;i++){innerHTML+=`<a href="${data.link[i][1]}">${data.link[i][0]}</a>`}link.innerHTML=innerHTML;curr_page=data; CssEditLoading(); document.getElementById("custom").innerHTML=""; } $button_click$ $load_start_page$ CssEditLoading()'
        self.html = '<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><style>$css$</style><title></title></head><body><h1 id="label">$label$</h1><h2 id="sublabel">$sublabel$</h2><hr><div id="menu">$menu$</div><div id="png"></div><br><div id="chapter"></div><br><element id="custom"></element><br><div id="link"></div><script>$javascript$</script><script>$custom$</script></body></html>'
        self.flname, self.cssswaps, self.fonts = '', '', ''

    def AddFont(self, font_family : str, font : str):
        self.fonts += f'@font-face [ font-family: {font_family}; src: url("{font}"); ]'.replace('[', '{').replace(']', '}')

    def SetCss(self, idifer: str, key : str, item : str):
        if idifer.find('.') != -1:
            self.cssswaps += f'document.querySelectorAll("{idifer}").forEach(element => [element.style.{key}="{item}";]);'.replace('[', '{').replace(']', '}')
        elif idifer.find('#') != -1:
            self.cssswaps += f'document.querySelector("{idifer}").style.{key}="{item}";'
        else:
            self.cssswaps += f'document.querySelectorAll("{idifer}").forEach(element => [element.style.{key}="{item}";]);'.replace('[', '{').replace(']', '}')
    
    def _DollarInsert(self, string : str, key: str, item : str):
        return string.replace(f'${key}$', item)

    def _fileFormat(self):
        open(f'{self.flname}.html', 'w', encoding='utf-8').write(self.html)
        webbrowser.open(f'{self.flname}.html')

    def _PageConfigure(self, project : Project, start_function : str):
        self.javascript = self._DollarInsert(self.javascript, 'load_start_page', f'setPage({start_function}_page);')
        self.html = self._DollarInsert(self.html, 'label', project.json['label'])
        self.html = self._DollarInsert(self.html, 'sublabel', project.json['describe'])
        self.css = self._DollarInsert(self.css, 'fonts', self.fonts)
        self.html = self._DollarInsert(self.html, 'css', self.css)
        self.html = self._DollarInsert(self.html, 'javascript', self.javascript)

    def _PageEventListenerBuilder(self, project : Project):
        if len(list(project.json['data'].keys())) >= 2:
            event_listener = ''
            for page in list(project.json['data'].keys()):
                event_listener += 'document.getElementById("$page$_btn").addEventListener("click", function() {setPage($page$_page)});'.replace('$page$', page)
            return event_listener
        return ''

    def _PageMenuBuilder(self, project : Project):
        if len(list(project.json['data'].keys())) >= 2:
            menu_div = ''
            for page in list(project.json['data'].keys()):
                menu_div += f'<button id="{page}_btn">{page}</button>'
            return menu_div
        return ''

    def _PageArrayBuilder(self, project : Project):
        output_arrays = ''
        for page in list(project.json['data'].keys()):
            png_list = []
            for img in project.json['data'][page]['png']:
                png_list.append(img['src'])

            chapter_list = []
            for chapter in project.json['data'][page]['chapter']:
                chapter_list.append([chapter['label'], chapter['text']])

            link_list = []
            for chapter in project.json['data'][page]['link']:
                link_list.append([chapter['text'], chapter['href']])

            output_arrays += f'{page}_page = Page({png_list}, {chapter_list}, {link_list});'.replace(']', ')').replace('[', 'new Array(')
        return output_arrays

    def BuildProject(self, project : Project, index_func, start_function : str = 'home'):
        index_func()
        self.javascript = self._DollarInsert(self.javascript, 'page_data', self._PageArrayBuilder(project))
        self.html = self._DollarInsert(self.html, 'menu', self._PageMenuBuilder(project))

        self.javascript = self._DollarInsert(self.javascript, 'button_click', self._PageEventListenerBuilder(project))
        self.html = self._DollarInsert(self.html, 'custom', project.json["custom"])
        self.javascript = self._DollarInsert(self.javascript, 'cssswap', self.cssswaps)

        self._PageConfigure(project, start_function)
        self._fileFormat()

    def Generation(self, func):
        self.flname = func.__name__
        return func