
        $('.sw-btn-next').click(function(){
            if($('.nav-item')[1].classList.value === 'nav-item done' && $('.nav-item')[2].classList.value === 'nav-item active') {
                var al_products = $('.prodValue');
                for(var i = 0 ; i < al_products.length; i++) {
                    console.log('id: ' + al_products[i].id + ' value: ' + al_products[i].value);
                }
            };
        })
    }, 1000);
})
//