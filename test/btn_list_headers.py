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
    var notebook = document.getElementById('notebook'),
        panel = document.getElementById('maintoolbar-container'),
        btn_list_headers = document.getElementById('btn_list_headers'),
        btn_list_headers_list = document.getElementById('btn_list_headers_list');
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
</script>
'''))