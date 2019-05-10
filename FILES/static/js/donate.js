// JavaScript source code
$(document).ready(function () {
    $("#donate").on("show.bs.modal", function (e) {
        var button = $(e.relatedTarget);
        var row = button.parents("tr");
        var firstname = row.find(".FirstName").text();
        var lastname = row.find(".LastName").text();
        var day = row.find(".Day").text();
        var room = row.find(".Room").text();
        var shift = row.find(".Shift").text();
        var slot = row.find(".Slot").text();


        $(this).find(".first_input").val(firstname);
        $(this).find(".last_input").val(lastname);
        $(this).find(".day_input").val(day);
        $(this).find(".room_input").val(room);
        $(this).find(".shift_input").val(shift);
        $(this).find(".slot_input").val(slot);




       
       
    });
});