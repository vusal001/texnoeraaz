
$(document).ready(function(){
  $('.owl-carousel').owlCarousel({
    loop:true,
    margin: 10,
    autoPlay: 1000,
    responsiveClass:true,
    autoplay:true,
    
    responsive:{
        0:{
            items:1.2,
            nav:true,
            
        },
    }
});
})