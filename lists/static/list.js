var lists_init = function () { 
        $("input[name='text']").on({
        'keypress': function() { $('.has-error').hide(); },
        'click': function() { $('.has-error').hide(); }
    });
};

lists_init();
