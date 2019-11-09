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
if(!notebook) {
    var notebook = $('#notebook'),
        panel = $('#maintoolbar-container'),
        btn_display_code = $('#btn_display_code');

    if(btn_display_code.length == 0) {
        panel.append('<a id="btn_display_code" class="js-ik_btn ik_btn btn-group"><span>Скрыть код</span><span>Показать код</span></a>');
    }

    $('#btn_display_code').click(function(e) {
        e.preventDefault();
        notebook.toggleClass('ik-hidden');
        $(this).toggleClass('ik-btn-active');
    })
}
</script>
'''))