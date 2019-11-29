$(document).ready(function () {
    $('.animated-card').each(function () {

        // animate on enter
        $(this).on('mouseenter', function (evt) {
            $(this).find('.sliding-card').css({
                'top': '0px',
                'height': '337.5px'
            });
            $(this).find('.slides-up').css('visibility', 'visible');
            $(this).find('img').css('filter', 'blur(5px)');
        })

        //animate on exit
        $(this).on('mouseleave', function (evt) {
            $(this).find('.sliding-card').css({
                'top': '225px',
                'height': '168.75px'
            });
            $(this).find('.slides-up').css('visibility', 'hidden');
            $(this).find('img').css('filter', 'blur(0px)');
        })
    })

})