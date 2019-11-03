from IPython.display import HTML
HTML('''
<style>
.ik_container {
    position: absolute;
    top: 0;
    display: flex;
    left: 20px;
}
.ik-toggle-btn {
    cursor: pointer;
    margin-top: 10px;
    margin-right: 20px;
}
.ik-toggle-btn:hover {
    text-decoration: underline;
}
.ik-hidden {
    display: none !important;
}
div.code_cell {
    padding-top: 40px;
}
div.text_cell {
    padding-top: 20px;
}
</style>
<script>
function add_toggle_btn() {
    $('#notebook-container > .cell').each(function(key, value) {
        var display_input = $(this).find('.js-toggle-display'),
            display_output = $(this).find('.js-toggle-display'),
            ik_container = $(this).find('.ik_container'),
            input = '';
        if(ik_container.find('.input').length == 1) {
            input = 'input';
        }
        else {
            input = 'prompt';
        }
        if(ik_container.length == 0) {
            $(this).append('<div class="ik_container"></div>');
            $(this).find('.ik_container').append('<div data-type="'+input+'" class="ik-toggle-btn js-toggle-display"><span>hide</span> input</div>');
            $(this).find('.ik_container').append('<div data-type="output_wrapper" class="ik-toggle-btn js-toggle-display"><span>hide</span> output</div>');
        }
    }) 
}
function toggle_display() {
    $('.js-toggle-display').click(function() {
        var type_display = $(this).data('type'),
            cell = $(this).closest('.cell'),
            cur_item = cell.find('.'+type_display);
        if(cur_item.hasClass('ik-hidden')){
            cur_item.removeClass('ik-hidden');
            $(this).find('span').html('hide');
        }
        else {
            cur_item.addClass('ik-hidden');
            $(this).find('span').html('show');
        }
        
    })
}
add_toggle_btn();
toggle_display();
$('#insert_above_below').click(function(){
    add_toggle_btn();
    toggle_display();
})
</script>

''')

##################################################### 1
from IPython.display import display, HTML
display(HTML('''
<style>
.ik_btn {
    cursor: pointer;
    display: inline-block;
    padding: 2px 8px;
    border: 1px solid #ddd;
    border-radius: 2px;
    color: #333 !important;
    background-color: #fff;
    float: right;
}
.ik_btn:hover {
    background-color: #e6e6e6;
    border-color: #adadad;
}
.ik_btn:active { 
    -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
    box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.ik_btn span:first-child {
    display: inline-block;
}
.ik_btn span:last-child {
    display: none;
}
.ik-hidden {
    display: none !important;
}
.ik-btn-active span:first-child {
    display: none;
}
.ik-btn-active span:last-child {
    display: inline-block;
}
.ik_list_header {
    position: relative;
}

.ik_list_header > .fa {
    position: absolute;
    display: none;
}
.ik_list_header ul {
    display: none;
    position: absolute;
    width: 310px;
    background: #fff;
    list-style: none;
    padding: 20px 0;
    left: -40px;
    text-align: left;
    list-style: none;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid #ccc;
    border: 1px solid rgba(0, 0, 0, 0.15);
    border-radius: 2px;
    -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
    
}
.ik_list_header.active ul,
.ik_list_header.active > .fa{
    display: block;
}

.ik_list_header ul li > a {
    display: block;
    padding: 3px 20px;
    clear: both;
    font-weight: 400;
    line-height: 1.42857143;
    color: #333333;
}
.ik_list_header ul li > a:hover {
    background-color: #f5f5f5;
    text-decoration: none;
}
</style>
<script>
var notebook = $('#notebook'),
    panel = $('#maintoolbar-container'),
    ik_btn = $('.ik_btn'),
    list_header = $('.ik_list_header');

function close_list_header() {
    $('.js-ik_list_item').click(function() {
        list_header.removeClass('active')
    })
}

if(ik_btn.length == 0) {
    panel.append('<a class="js-ik_btn ik_btn btn-group"><span>Скрыть код</span><span>Показать код</span></a>');
}
if(list_header.length == 0) {
    panel.append('<div class="js-ik_list_header ik_list_header ik_btn btn-group">Перейти к заголовку<ul></ul></div>');
}

$('.ik_btn').unbind().click(function(e) {
    e.preventDefault();
    notebook.find('.input').toggleClass('ik-hidden');
    $(this).toggleClass('ik-btn-active');
})
$('.ik_list_header').unbind().click(function(e) {
    if(e.target.className.indexOf('ik_list_header') != -1) {
        var ul = $(this).find('ul');
        ul.html('');
        $(this).toggleClass('active');
        notebook.find('.cell h1, .cell h2, .cell h3').each(function() {
            ul.append('<li><a class="js-ik_list_item" href="#'+$(this).prop('id')+'">'+$(this).contents().get(0).nodeValue+'</a></li>');
        })
    }
    else {
        $(this).removeClass('active');
    }
})


</script>
'''))
print('Тут скрипт для кнопки')

##################################################### 2


from IPython.display import display, HTML
display(HTML('''
<style>
.ik_btn {
    cursor: pointer;
    display: inline-block;
    padding: 2px 8px;
    border: 1px solid #ddd;
    border-radius: 2px;
    color: #333 !important;
    background-color: #fff;
    float: right;
}
.ik_btn:hover {
    background-color: #e6e6e6;
    border-color: #adadad;
}
.ik_btn:active { 
    -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
    box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.ik_btn span:first-child {
    display: inline-block;
}
.ik_btn span:last-child {
    display: none;
}
.ik-hidden .cell .input {
    display: none !important;
}
.ik-btn-active span:first-child {
    display: none;
}
.ik-btn-active span:last-child {
    display: inline-block;
}
.ik_list_header {
    position: relative;
}

.ik_list_header > .fa {
    position: absolute;
    display: none;
}
.ik_list_header ul {
    display: none;
    position: absolute;
    width: 310px;
    background: #fff;
    list-style: none;
    padding: 20px 0;
    left: -40px;
    text-align: left;
    list-style: none;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid #ccc;
    border: 1px solid rgba(0, 0, 0, 0.15);
    border-radius: 2px;
    -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
    
}
.ik_list_header.active ul,
.ik_list_header.active > .fa{
    display: block;
}

.ik_list_header ul li > a {
    display: block;
    padding: 3px 20px;
    clear: both;
    font-weight: 400;
    line-height: 1.42857143;
    color: #333333;
}
.ik_list_header ul li > a:hover {
    background-color: #f5f5f5;
    text-decoration: none;
}
</style>
<script>
var notebook = $('#notebook'),
    panel = $('#maintoolbar-container'),
    ik_btn = $('.ik_btn'),
    list_header = $('.ik_list_header');

if(ik_btn.length == 0) {
    panel.append('<a class="js-ik_btn ik_btn btn-group"><span>Скрыть код</span><span>Показать код</span></a>');
}
if(list_header.length == 0) {
    panel.append('<div class="js-ik_list_header ik_list_header ik_btn btn-group">Перейти к заголовку<ul></ul></div>');
}

$('.ik_btn').unbind().click(function(e) {
    e.preventDefault();
    notebook.toggleClass('ik-hidden');
    $(this).toggleClass('ik-btn-active');
})
$('.ik_list_header').unbind().click(function(e) {
    if(e.target.className.indexOf('ik_list_header') != -1) {
        var ul = $(this).find('ul');
        ul.html('');
        $(this).toggleClass('active');
        notebook.find('.cell h1, .cell h2, .cell h3').each(function() {
            ul.append('<li><a class="js-ik_list_item" href="#'+$(this).prop('id')+'">'+$(this).contents().get(0).nodeValue+'</a></li>');
        })
    }
    else {
        $(this).removeClass('active');
    }
})


</script>
'''))
print('Тут скрипт для кнопки')
##################################################### 3
from IPython.display import display, HTML
display(HTML('''
<style>
.ik_btn {
    cursor: pointer;
    display: inline-block;
    padding: 2px 8px;
    border: 1px solid #ddd;
    border-radius: 2px;
    color: #333 !important;
    background-color: #fff;
    float: right;
}
.ik_btn:hover {
    background-color: #e6e6e6;
    border-color: #adadad;
}
.ik_btn:active { 
    -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
    box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.ik_btn span:first-child {
    display: inline-block;
}
.ik_btn span:last-child {
    display: none;
}
.ik-hidden .cell .input {
    display: none !important;
}
.ik-btn-active span:first-child {
    display: none;
}
.ik-btn-active span:last-child {
    display: inline-block;
}
.ik_list_header {
    position: relative;
}

.ik_list_header > .fa {
    position: absolute;
    display: none;
}
.ik_list_header ul {
    display: none;
    position: absolute;
    width: 310px;
    background: #fff;
    list-style: none;
    padding: 20px 0;
    left: -40px;
    text-align: left;
    list-style: none;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid #ccc;
    border: 1px solid rgba(0, 0, 0, 0.15);
    border-radius: 2px;
    -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
    
}
.ik_list_header.active ul,
.ik_list_header.active > .fa{
    display: block;
}

.ik_list_header ul li > a {
    display: block;
    padding: 3px 20px;
    clear: both;
    font-weight: 400;
    line-height: 1.42857143;
    color: #333333;
}
.ik_list_header ul li > a:hover {
    background-color: #f5f5f5;
    text-decoration: none;
}
</style>
<script>
var notebook = $('#notebook'),
    panel = $('#maintoolbar-container'),
    ik_btn = $('.ik_btn'),
    list_header = $('.ik_list_header');

if(ik_btn.length == 0) {
    panel.append('<a class="js-ik_btn ik_btn btn-group"><span>Скрыть код</span><span>Показать код</span></a>');
}
if(list_header.length == 0) {
    panel.append('<div class="js-ik_list_header ik_list_header ik_btn btn-group">Перейти к заголовку<ul></ul></div>');
}

$('.ik_btn').unbind().click(function(e) {
    e.preventDefault();
    notebook.toggleClass('ik-hidden');
    $(this).toggleClass('ik-btn-active');
})
$('.ik_list_header').unbind().click(function(e) {
    if(e.target.className.indexOf('ik_list_header') != -1) {
        var ul = $(this).find('ul');
        ul.html('');
        $(this).toggleClass('active');
        notebook.find('.cell h1, .cell h2, .cell h3').each(function() {
            ul.append('<li><a class="js-ik_list_item" href="#'+$(this).prop('id')+'">'+$(this).contents().get(0).nodeValue+'</a></li>');
        })
    }
    else {
        $(this).removeClass('active');
    }
})


</script>
'''))
print('Тут скрипт для кнопки')
################
from IPython.display import display, HTML
def set_script() :
    global is_set_script
    is_set_script = True
    display(HTML('''
    <style>
    .ik_btn {
        cursor: pointer;
        display: inline-block;
        padding: 2px 8px;
        border: 1px solid #ddd;
        border-radius: 2px;
        color: #333 !important;
        background-color: #fff;
        float: right;
    }
    .ik_btn:hover {
        background-color: #e6e6e6;
        border-color: #adadad;
    }
    .ik_btn:active { 
        -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
        box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
    }
    .ik_btn span:first-child {
        display: inline-block;
    }
    .ik_btn span:last-child {
        display: none;
    }
    .ik-hidden .cell .input {
        display: none !important;
    }
    .ik-btn-active span:first-child {
        display: none;
    }
    .ik-btn-active span:last-child {
        display: inline-block;
    }
    .ik_list_header {
        position: relative;
    }

    .ik_list_header > .fa {
        position: absolute;
        display: none;
    }
    .ik_list_header ul {
        display: none;
        position: absolute;
        width: 310px;
        background: #fff;
        list-style: none;
        padding: 20px 0;
        left: -40px;
        text-align: left;
        list-style: none;
        background-color: #fff;
        background-clip: padding-box;
        border: 1px solid #ccc;
        border: 1px solid rgba(0, 0, 0, 0.15);
        border-radius: 2px;
        -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);

    }
    .ik_list_header.active ul,
    .ik_list_header.active > .fa{
        display: block;
    }

    .ik_list_header ul li > a {
        display: block;
        padding: 3px 20px;
        clear: both;
        font-weight: 400;
        line-height: 1.42857143;
        color: #333333;
    }
    .ik_list_header ul li > a:hover {
        background-color: #f5f5f5;
        text-decoration: none;
    }	
    </style>
    <script>
    var notebook = document.getElementById('notebook'),
        panel = document.getElementById('maintoolbar-container'),
        btn_display_code = document.getElementById('btn_display_code'),
        btn_list_headers = document.getElementById('btn_list_headers');
    function toggle_notebook_display(e) {
        console.log(e.target.tagName)
        notebook.classList.toggle("ik-hidden");
        btn_display_code.classList.toggle("ik-btn-active");
    }
    if(!btn_display_code) {
        btn_display_code = document.createElement('a');
        btn_display_code.id = 'btn_display_code';
        btn_display_code.className = 'js-ik_btn ik_btn btn-group';
        btn_display_code__span1 = document.createElement('span');
        btn_display_code__span1.innerHTML = 'Скрыть код';
        btn_display_code__span2 = document.createElement('span');
        btn_display_code__span2.innerHTML = 'Показать код';
        btn_display_code.append(btn_display_code__span1)
        btn_display_code.append(btn_display_code__span2)
        panel.append(btn_display_code)
    }
    btn_display_code.addEventListener('click', toggle_notebook_display)
    </script>
    '''))
try:
    is_set_script
    print('oh')
except:
    print('first run')
    set_script()

########################################
from IPython.display import display, HTML
display(HTML('''
<style>
.ik_btn {
    cursor: pointer;
    display: inline-block;
    padding: 2px 8px;
    border: 1px solid #ddd;
    border-radius: 2px;
    color: #333 !important;
    background-color: #fff;
    float: right;
}
.ik_btn:hover {
    background-color: #e6e6e6;
    border-color: #adadad;
}
.ik_btn:active { 
    -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
    box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.ik_btn span:first-child {
    display: inline-block;
}
.ik_btn span:last-child {
    display: none;
}
.ik-hidden .cell .input {
    display: none !important;
}
.ik-btn-active span:first-child {
    display: none;
}
.ik-btn-active span:last-child {
    display: inline-block;
}
.ik_list_header {
    position: relative;
}

.ik_list_header > .fa {
    position: absolute;
    display: none;
}
.ik_list_header ul {
    display: none;
    position: absolute;
    width: 310px;
    background: #fff;
    list-style: none;
    padding: 20px 0;
    left: -40px;
    text-align: left;
    list-style: none;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid #ccc;
    border: 1px solid rgba(0, 0, 0, 0.15);
    border-radius: 2px;
    -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);

}
.ik_list_header.active ul,
.ik_list_header.active > .fa{
    display: block;
}

.ik_list_header ul li > a {
    display: block;
    padding: 3px 20px;
    clear: both;
    font-weight: 400;
    line-height: 1.42857143;
    color: #333333;
}
.ik_list_header ul li > a:hover {
    background-color: #f5f5f5;
    text-decoration: none;
}	
</style>
<script>
console.log(notebook)
if(!notebook) {
    var notebook = document.getElementById('notebook'),
        panel = document.getElementById('maintoolbar-container'),
        btn_display_code = document.getElementById('btn_display_code'),
        btn_list_headers = document.getElementById('btn_list_headers');
    if(!btn_display_code) {
        btn_display_code = document.createElement('a');
        btn_display_code.id = 'btn_display_code';
        btn_display_code.className = 'js-ik_btn ik_btn btn-group';
        btn_display_code__span1 = document.createElement('span');
        btn_display_code__span1.innerHTML = 'Скрыть код';
        btn_display_code__span2 = document.createElement('span');
        btn_display_code__span2.innerHTML = 'Показать код';
        btn_display_code.append(btn_display_code__span1)
        btn_display_code.append(btn_display_code__span2)
        panel.append(btn_display_code)
    }
    function toggle_notebook_display(e) {
        notebook.classList.toggle("ik-hidden");
        btn_display_code.classList.toggle("ik-btn-active");
    }
    btn_display_code.addEventListener('click', toggle_notebook_display)
}
</script>
'''))
#########
from IPython.display import display, HTML
display(HTML('''
<style>
.ik_btn {
    cursor: pointer;
    display: inline-block;
    padding: 2px 8px;
    border: 1px solid #ddd;
    border-radius: 2px;
    color: #333 !important;
    background-color: #fff;
    float: right;
}
.ik_btn:hover {
    background-color: #e6e6e6;
    border-color: #adadad;
}
.ik_btn:active { 
    -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
    box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.ik_btn span:first-child {
    display: inline-block;
}
.ik_btn span:last-child {
    display: none;
}
.ik-hidden .cell .input {
    display: none !important;
}
.ik-btn-active span:first-child {
    display: none;
}
.ik-btn-active span:last-child {
    display: inline-block;
}
.ik_list_header {
    position: relative;
}

.ik_list_header > .fa {
    position: absolute;
    display: none;
}
.ik_list_header ul {
    display: none;
    position: absolute;
    width: 310px;
    background: #fff;
    list-style: none;
    padding: 20px 0;
    left: -40px;
    text-align: left;
    list-style: none;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid #ccc;
    border: 1px solid rgba(0, 0, 0, 0.15);
    border-radius: 2px;
    -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);

}
.ik_list_header.active ul,
.ik_list_header.active > .fa{
    display: block;
}

.ik_list_header ul a {
    display: block;
    padding: 3px 20px;
    clear: both;
    font-weight: 400;
    line-height: 1.42857143;
    color: #333333;
}
.ik_list_header ul a:hover {
    background-color: #f5f5f5;
    text-decoration: none;
}	
</style>
<script>
if(!notebook) {
    var notebook = document.getElementById('notebook'),
        panel = document.getElementById('maintoolbar-container'),
        btn_display_code = document.getElementById('btn_display_code'),
        btn_list_headers = document.getElementById('btn_list_headers'),
        btn_list_headers_list = document.getElementById('btn_list_headers_list');
        
    function toggle_notebook_display(e) {
        notebook.classList.toggle("ik-hidden");
        btn_display_code.classList.toggle("ik-btn-active");
    }
    
    function show_list_headers(e) {
        if(e.target.className.indexOf('ik_list_header') != -1) {
            btn_list_headers_list.innerHTML = '';
            btn_list_headers.classList.toggle("active");
            notebook.querySelectorAll(".cell h1, .cell h2, .cell h3").forEach(function(elem) {
                var link_item = document.createElement('a');
                link_item.setAttribute('href', "#"+elem.id);
                link_item.innerText = elem.innerText;
                btn_list_headers_list.append(link_item);
            })
        }
        else {
            btn_list_headers.classList.toggle("active");
        }       
    }
    
    if(!btn_display_code) {
        btn_display_code = document.createElement('a');
        btn_display_code.id = 'btn_display_code';
        btn_display_code.className = 'js-ik_btn ik_btn btn-group';
        btn_display_code__span1 = document.createElement('span');
        btn_display_code__span1.innerHTML = 'Скрыть код';
        btn_display_code__span2 = document.createElement('span');
        btn_display_code__span2.innerHTML = 'Показать код';
        btn_display_code.append(btn_display_code__span1);
        btn_display_code.append(btn_display_code__span2);
        panel.append(btn_display_code);
        btn_display_code.addEventListener('click', toggle_notebook_display);
    }

    if(!btn_list_headers) {
        btn_list_headers = document.createElement('div');
        btn_list_headers.className = 'js-ik_list_header ik_list_header ik_btn btn-group';
        btn_list_headers.innerHTML = 'Навигация';
        btn_list_headers.id = 'btn_list_headers';
        btn_list_headers_list = document.createElement('ul');
        btn_list_headers_list.id = 'btn_list_headers_list';
        btn_list_headers.append(btn_list_headers_list);
        panel.append(btn_list_headers);
        btn_list_headers.addEventListener('click', show_list_headers);
    }
}
</script>
'''))
##########################
from IPython.display import display, HTML
display(HTML('''
<style>
.ik_btn {
    cursor: pointer;
    display: inline-block;
    padding: 2px 8px;
    border: 1px solid #ddd;
    border-radius: 2px;
    color: #333 !important;
    background-color: #fff;
    float: right;
}
.ik_btn:hover {
    background-color: #e6e6e6;
    border-color: #adadad;
}
.ik_btn:active { 
    -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
    box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.ik_btn span:first-child {
    display: inline-block;
}
.ik_btn span:last-child {
    display: none;
}
.ik-hidden .cell .input {
    display: none !important;
}
.ik-btn-active span:first-child {
    display: none;
}
.ik-btn-active span:last-child {
    display: inline-block;
}
.ik_list_header {
    position: relative;
}

.ik_list_header > .fa {
    position: absolute;
    display: none;
}
.ik_list_header ul {
    display: none;
    position: absolute;
    width: 310px;
    background: #fff;
    list-style: none;
    padding: 20px 0;
    left: -40px;
    text-align: left;
    list-style: none;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid #ccc;
    border: 1px solid rgba(0, 0, 0, 0.15);
    border-radius: 2px;
    -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
    
}
.ik_list_header.active ul,
.ik_list_header.active > .fa{
    display: block;
}

.ik_list_header ul li > a {
    display: block;
    padding: 3px 20px;
    clear: both;
    font-weight: 400;
    line-height: 1.42857143;
    color: #333333;
}
.ik_list_header ul li > a:hover {
    background-color: #f5f5f5;
    text-decoration: none;
}
</style>
<script>
if(!notebook) {
    var notebook = $('#notebook'),
        panel = $('#maintoolbar-container'),
        btn_display_code = $('#btn_display_code'),
        list_header = $('#btn_list_headers');

    if(btn_display_code.length == 0) {
        panel.append('<a id="btn_display_code" class="js-ik_btn ik_btn btn-group"><span>Скрыть код</span><span>Показать код</span></a>');
    }
    if(list_header.length == 0) {
        panel.append('<div id="btn_list_headers" class="js-ik_list_header ik_list_header ik_btn btn-group">Перейти к заголовку<ul></ul></div>');
    }

    $('#btn_display_code').click(function(e) {
        e.preventDefault();
        notebook.toggleClass('ik-hidden');
        $(this).toggleClass('ik-btn-active');
    })
    $('#btn_list_headers').click(function(e) {
        if(e.target.className.indexOf('ik_list_header') != -1) {
            var ul = $(this).find('ul');
            ul.html('');
            $(this).toggleClass('active');
            notebook.find('.cell h1, .cell h2, .cell h3').each(function() {
                ul.append('<li><a class="js-ik_list_item" href="#'+$(this).prop('id')+'">'+$(this).contents().get(0).nodeValue+'</a></li>');
            })
        }
        else {
            $(this).removeClass('active');
        }
    })
}
</script>
'''))