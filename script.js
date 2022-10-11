$(document).ready(function(){
    $(window).scroll(function(){
        if(this.scrollY >20){
            $('.topnav').addClass("sticky");
        }else{
            $('.topnav').removeClass("sticky");
        }
    });
    //toggle menu/topnav
    $('.menu-btn').click(function(){
        $('.topnav .menu').toggleClass("active");
        

    })
});