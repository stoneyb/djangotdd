var lists_init = function () { 
        $("input[name='text']").on({
        'keypress': function() { console.log("keypress"); $('.has-error').hide(); },
        'click': function() { console.log("click"); $('.has-error').hide(); }
    });
};

lists_init();
