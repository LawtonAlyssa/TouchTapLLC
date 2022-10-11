// import updatePopover from './setup.js';
import {Service, generateTable, getData, setData} from './setup.js';
// import getData from './setup.js';
// import setData from './setup.js';
// import generateTable from './setup.js';

window.addEventListener('load', loadEvent)

function loadEvent() {
    console.log("html loaded!")

    window.onload = setupLocalStorage();

    $("button").click(function () {
        // console.log($('[data-toggle="popover"]'))
        $('[data-toggle="popover"]').popover("hide");
        var html = document.getElementById(this.id).innerHTML;
        var o_m_svcs_sel = getData("o_m_svcs_sel");
        // console.log("services" + o_m_svcs_sel)
        if (html === 'Select') {
            $(this).html('Selected');
            var service = document.getElementById("h5-" + this.id).innerHTML;
            var cost = document.getElementById("cost-" + this.id).innerHTML;

            if (!containsObject(o_m_svcs_sel, this.id)) {
                // $("#tbody-cart").append("<tr id=\"row-" + this.id + "\"> <td scrope=\"col\">" + service + "</td> <td scrope=\"col\">" + cost + "</td> </tr>");
                o_m_svcs_sel.push(new Service(this.id, service, cost));
            }
            console.log("added:" + o_m_svcs_sel)
        } else {
            $(this).html('Select');
            // console.log("remove:",this.id)
            removeVal(o_m_svcs_sel, this.id);
            // $('table#cart-table tr#row-' + this.id).remove();
            // if (o_m_svcs_sel.length == 0) $("#dark-row").remove();
            console.log("removed:" + o_m_svcs_sel)
        }

        
        // if (o_m_svcs_sel.length == 0) {
        //     $("#sum-cart").text("$0");
        // } else {
        //     updateSum('cart-table', o_m_svcs_sel);
        // }
        setData("o_m_svcs_sel", o_m_svcs_sel);
        generateTable('cart-table', o_m_svcs_sel);
        console.log(o_m_svcs_sel);
    });

}

function removeVal(arr, val) {
    // console.log("Array")
    // console.log("index:" + getIndex(val, arr))
    arr.splice(getIndex(val, arr), 1);
}

function getIndex(objId, arr) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i].id === objId) {
            return i;
        }
    }
    return -1;
}

function setupLocalStorage() {
    console.log("getdata:" , getData)
    var o_m_svcs_sel = getData("o_m_svcs_sel");

    console.log("services:" + o_m_svcs_sel)

    if (o_m_svcs_sel === undefined) {
        console.log("undefined")
    } else {
        if (o_m_svcs_sel === null) {
            o_m_svcs_sel = [];
            setData("o_m_svcs_sel", o_m_svcs_sel);
        } else {
            console.log("LEN:" + o_m_svcs_sel.length)
            if (o_m_svcs_sel.length === 0) {
                return;
            }
            o_m_svcs_sel.forEach(function (svc) {
                let svcID = svc.id;
                var html = document.getElementById(svcID).innerHTML;

                // let service = document.getElementById("h5-" + svc).innerHTML;
                // let cost = document.getElementById("cost-" + svc).innerHTML;
                // console.log("HERE:" + $("#tbody-cart"))
                // $("#tbody-cart").append("<tr id=\"row-" + svc + "\"> <td scrope=\"col\">" + service + "</td> <td scrope=\"col\">" + cost + "</td> </tr>");
                if (html === 'Select') {
                    document.getElementById(svcID).click();
                    document.getElementById(svcID).innerHTML = 'Selected';
                }
            });
            generateTable('cart-table', o_m_svcs_sel);
            // updatePopover();
        }
    }
}



function containsObject(obj, arr) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === obj) {
            return true;
        }
    }
    return false;
}



