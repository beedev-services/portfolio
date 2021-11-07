$(document).ready(function() {
    $('#showMenu').click(function() {
        $('#hideMenu').animate( {
            width: 'toggle'
        })
        $('#hideMenu').css({
            'display': 'flex',
            'flex-direction': 'column',
            'justify-content': 'center',
            'align-items': 'center'
        })
    })
    $('#showSubMenu').click(function() {
        $('#hideSubMenu').animate( {
            width: 'toggle'
        })
        $('#hideSubMenu').css({
            'display': 'flex',
            'flex-direction': 'column',
            'justify-content': 'center',
            'align-items': 'center'
        })
    })
})