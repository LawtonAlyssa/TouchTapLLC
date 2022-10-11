function is_user_mode() {
    return window.user_mode == true;
}

// allow html pages to include html scripts in '/components'
var load_html_count = 0
var nav_bar_loaded_callbacks = []
$(function () {
    console.log("Including html files...")
    var includes = $('[data-include]')
    $.each(includes, function () {
        var base_file_name = $(this).data('include');
        var file = 'components/' + base_file_name + '.html'

        load_html_count += 1
        $(this).load(file, function () {
            load_html_count -= 1

            if (load_html_count == 0) {
                console.log("HTML File Loaded")

                // $('#purchaseModal').modal({backdrop: 'static', keyboard: false});
                console.log("Setting active item in menu")
                var url = window.location.href;

                // passes on every "a" tag
                $("#h_menu a").each(function () {
                    // checks if its the same on the address bar
                    if (url == (this.href)) {
                        $(this).closest("li").addClass("active");
                    }
                });

                // passes on every "a" tag
                $("#v_menu a").each(function () {
                    // checks if its the same on the address bar
                    if (url == (this.href)) {
                        $(this).closest("li").addClass("active");
                    }
                });

                var o_m_svcs_sel = getData("o_m_svcs_sel");
                if (o_m_svcs_sel === null) {
                    o_m_svcs_sel = [];
                    setData("o_m_svcs_sel", o_m_svcs_sel);
                }

                generateTable('cart-table', o_m_svcs_sel);

                updatePopover();

                $('#checkout_btn').attr('name', 'value');

                console.log("button", $("button#checkout"))


            }

        })

    })

})

$(document).on('click', '#checkout_btn', function () {
    $('[data-toggle="popover"]').popover("hide");
    $('#tbody-cart').empty();
    setData("o_m_svcs_sel", []);
    updateSum([]);
    $('#purchaseModal').modal({backdrop: 'static', keyboard: false});
    $('#purchaseModal').on('shown.bs.modal', function () {
        $('#purchaseModal').focus();
    })  
    // $('#purchaseModal').trigger("focus")
    // window.location.reload();
});

$(document).on('click', '#modal_close', function () {
    window.location.reload();
});

function updatePopover() {
    if ($('[data-toggle="popover"]').length > 0) {
        $('[data-toggle="popover"]').popover({
            html: true,
            sanitize: false,
            placement: 'bottom',
            title: function () {
                return $("#popover-head").html();
            },
            content: function () {
                console.log("Pop over CONTENT in SETUP")
                return $("#popover-content").html();
            }
        }).on('shown.bs.popover', function () {

            // Trying to get date picker to show :(
            // $('#reservationDate').datepicker({
            //     format: "dd/mm/yyyy"
            // }).on('change', function() {
            //     $('.reservationDate').hide();
            // });
        });
    }
}

export class Service {
    constructor(id, name, cost) {
        this.id = id;
        this.name = name;
        this.cost = cost;
    }
}

export function generateTable(tableId, o_m_svcs_sel) {
    o_m_svcs_sel = getData("o_m_svcs_sel");
    let o_m_svcs_ids = []
    // console.log("services:" + o_m_svcs_sel)

    if (o_m_svcs_sel === null) {
        o_m_svcs_sel = [];
        setData("o_m_svcs_sel", o_m_svcs_sel);
    } else {
        $('#tbody-cart').empty()
        o_m_svcs_sel.forEach(svc => {
            let id = svc.id;
            // console.log("HERE:" + $("#tbody-cart"))
            $("#tbody-cart").append("<tr id=\"row-" + id + "\"> <td scrope=\"col\">" + svc.name + "</td> <td scrope=\"col\">" + svc.cost + "</td> </tr>");
            o_m_svcs_ids.push(id);
        });
        updateSum(o_m_svcs_sel);
        if (o_m_svcs_sel.length == 0) {
            $('button#checkout_btn').prop('disabled', true);
        } else {
            $('button#checkout_btn').prop('disabled', false);
        }
    }
    // console.log("ids",o_m_svcs_ids)
    $('input#checkout').val(o_m_svcs_ids);
}

export function updateSum(o_m_svcs_sel) {
    let sum = 0;

    o_m_svcs_sel.forEach(svc => {
        sum += parseInt((svc.cost).replace("$", ""));
        // console.log(sum)
    });

    // for (let index = 2; index < o_m_svcs_sel.length + 2; index++) {
    //     console.log("i:" + index)
    //     // console.log("CELL:" + table.rows[index].cells[1].innerHTML.replace("$",""));
    //     sum += parseInt(table.rows[index].cells[1].innerHTML.replace("$", ""));
    //     // console.log("SUM=" + sum)
    // }
    // // console.log("cell:" + document.getElementById('cart-table').rows[1].cells[0].innerHTML)
    // console.log("sum" + sum)
    $("#sum-cart").text("$" + sum);
}

export function getData(key) {
    // console.log("localStorage:", localStorage)
    const data = localStorage.getItem(key);
    if (data === null) return null;
    return JSON.parse(data);
}

export function setData(key, data) {
    localStorage.setItem(key, JSON.stringify(data));
}