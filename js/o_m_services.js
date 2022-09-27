window.addEventListener('load', loadEvent)

function loadEvent(){
    console.log("html loaded!")
    window.onload = setupLocalStorage();

    $("button").click(function() {
        var html = document.getElementById(this.id).innerHTML;
        var o_m_svcs_sel = JSON.parse(localStorage.getItem("o_m_svcs_sel"));
        if (html === 'Select') {
            $(this).html('Selected');
            if(!o_m_svcs_sel.includes(this.id)) o_m_svcs_sel.push(this.id);
        } else {
            $(this).html('Select');
            removeVal(o_m_svcs_sel, this.id);
        }
        localStorage.setItem("o_m_svcs_sel",JSON.stringify(o_m_svcs_sel));
        console.log(localStorage.o_m_svcs_sel);
    });

}

function removeVal(array, val) {
    const index = array.indexOf(val);
    if (index > -1) {
        array.splice(index, 1);
    }
}

function setupLocalStorage () {
    if (localStorage.getItem("o_m_svcs_sel")===null) {
        var o_m_svcs_sel = [];
        localStorage.setItem("o_m_svcs_sel",JSON.stringify(o_m_svcs_sel));
    } else {
        var o_m_svcs_sel = JSON.parse(localStorage.getItem("o_m_svcs_sel"));
        o_m_svcs_sel.forEach(elem_id => {
            var html = document.getElementById(elem_id).innerHTML;
            if (html === 'Select') {
                document.getElementById(elem_id).click();
                document.getElementById(elem_id).innerHTML = 'Selected';
            }
        });
    }
}