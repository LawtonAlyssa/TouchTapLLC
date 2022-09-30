window.addEventListener('load', loadEvent)


function loadEvent() {
    console.log("html loaded!")

    $(function() {
        $('.datepicker').datepicker({
            format: '   mm/dd/yyyy'

        });
    });

    $(".datepicker").on("change", function() {
        let pickedDate = $("input").val();

        console.log(pickedDate);
        // $("#showdate").text(
        // `You picked this ${pickedDate} Date`);
    });


    // $('.datepicker').datepicker(function() {
    //     console.log($(this).attr('id'));
    //     console.log(this.id);

    //     var jsDate = $('#date-picker-appt').data('DateTimePicker').date();
    //     // if (jsDate !== null) { // if any date selected in datepicker
    //     //     jsDate instanceof Date; // -> true
    //     //     jsDate.getDate();
    //     //     jsDate.getMonth();
    //     //     jsDate.getFullYear();
    //     // }
    //     console.log(jsDate);
    // });
}
// var date = new Date();
// date.setDate(date.getDate() - 1);

// $('#date-picker-appt').datepicker({
//     startDate: date
// });