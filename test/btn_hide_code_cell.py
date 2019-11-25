<style>
.ik_container_b {
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
            ik_container = $(this).find('.ik_container_b'),
            input = '';
        if(ik_container.find('.input').length == 1) {
            input = 'input';
        }
        else {
            input = 'prompt';
        }
        if(ik_container.length == 0) {
            $(this).append('<div class="ik_container_b"></div>');
            $(this).find('.ik_container_b').append('<div data-type="'+input+'" class="ik-toggle-btn js-toggle-display"><span>hide</span> input</div>');
            $(this).find('.ik_container_b').append('<div data-type="output_wrapper" class="ik-toggle-btn js-toggle-display"><span>hide</span> output</div>');
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