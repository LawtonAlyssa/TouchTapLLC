function is_user_mode() {
    return window.user_mode == true;
}

// allow html pages to include html scripts in '/components'
load_html_count = 0
nav_bar_loaded_callbacks = []
$(function() {
    console.log("Including html files...")
    var includes = $('[data-include]')
    $.each(includes, function() {
        var base_file_name = $(this).data('include');
        var file = 'components/' + base_file_name + '.html'

        load_html_count += 1
        $(this).load(file, function() {
            load_html_count -= 1

            if (load_html_count == 0) {
                console.log("HTML File Loaded")

                console.log("Setting active item in menu")
                var url = window.location.href;

                // passes on every "a" tag
                $("#h_menu a").each(function() {
                    // checks if its the same on the address bar
                    if (url == (this.href)) {
                        $(this).closest("li").addClass("active");
                    }
                });

                // passes on every "a" tag
                $("#v_menu a").each(function() {
                    // checks if its the same on the address bar
                    if (url == (this.href)) {
                        $(this).closest("li").addClass("active");
                    }
                });
            }

        })

    })
})