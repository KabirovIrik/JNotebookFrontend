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
</style>
<script>
var notebook = document.getElementById('notebook'),
    panel = document.getElementById('maintoolbar-container'),
    btn_display_code = document.getElementById('btn_display_code'),
    btn_list_headers = document.getElementById('btn_list_headers'),
    btn_list_headers_list = document.getElementById('btn_list_headers_list');
    
function toggle_notebook_display(e) {
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
    btn_display_code.append(btn_display_code__span1);
    btn_display_code.append(btn_display_code__span2);
    panel.append(btn_display_code);
    btn_display_code.addEventListener('click', toggle_notebook_display);
}
</script>
'''))