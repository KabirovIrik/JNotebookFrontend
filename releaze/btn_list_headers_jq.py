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
    overflow-y: scroll;
    max-height: 500px;
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
        list_header = $('#btn_list_headers');

    if(list_header.length == 0) {
        panel.append('<div id="btn_list_headers" class="js-ik_list_header ik_list_header ik_btn btn-group">Перейти к заголовку<ul></ul></div>');
    }

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