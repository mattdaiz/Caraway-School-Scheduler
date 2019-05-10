// JavaScript source code
//initiaize the kalendaes
var date; 
var year;
var month;
var day;
var room;

var red = new Kalendae("Red", {
    blackout: function (date) {
        return [1, 0, 0, 0, 0, 0, 1][Kalendae.moment(date).day()];
    }
});
var blue = new Kalendae("Blue", {
    blackout: function (date) {
        return [1, 0, 0, 0, 0, 0, 1][Kalendae.moment(date).day()];
    }
});
var purple = new Kalendae("Purple", {
    blackout: function (date) {
        return [1, 0, 0, 0, 0, 0, 1][Kalendae.moment(date).day()];
    }
});
var green = new Kalendae("Green", {
    blackout: function (date) {
        return [1, 0, 0, 0, 0, 0, 1][Kalendae.moment(date).day()];
    }
});
var grey = new Kalendae("Grey", {
    blackout: function (date) {
        return [1, 0, 0, 0, 0, 0, 1][Kalendae.moment(date).day()];
    }
});


//if click on  kalendae it will alert of the date and open modal with date passed to it
red.subscribe('change', function (date) {
    date = this.getSelected()
    year = date.split("-")[0];
    month = date.split("-")[1];
    day = date.split("-")[2];
    room = 'Red';
    document.getElementById("Year").value = year;
    document.getElementById("Month").value = month;
    document.getElementById("Day").value = day;
    document.getElementById("Room").value = room;
    $("#myModal").modal("show");
    $('.YearSelected').html(year);
    $('.MonthSelected').html(month);
    $('.DaySelected').html(day);
    $('.RoomSelected').html(room);
});

//if click on  kalendae it will alert of the date and open modal with date passed to it
blue.subscribe('change', function (date) {
    date = this.getSelected()
    year = date.split("-")[0];
    month = date.split("-")[1];
    day = date.split("-")[2];
    room = 'Blue';
    document.getElementById("Year").value = year;
    document.getElementById("Month").value = month;
    document.getElementById("Day").value = day;
    document.getElementById("Room").value = room;
    $("#myModal").modal("show");
    $('.YearSelected').html(year);
    $('.MonthSelected').html(month);
    $('.DaySelected').html(day);
    $('.RoomSelected').html(room);

});

//if click on  kalendae it will alert of the date and open modal with date passed to it
purple.subscribe('change', function (date) {
    date = this.getSelected()
    year = date.split("-")[0];
    month = date.split("-")[1];
    day = date.split("-")[2];
    room = 'Purple';
    document.getElementById("Year").value = year;
    document.getElementById("Month").value = month;
    document.getElementById("Day").value = day;
    document.getElementById("Room").value = room;
    $("#myModal").modal("show");
    $('.YearSelected').html(year);
    $('.MonthSelected').html(month);
    $('.DaySelected').html(day);
    $('.RoomSelected').html(room);
});

//if click on  kalendae it will alert of the date and open modal with date passed to it
green.subscribe('change', function (date) {
    date = this.getSelected()
    year = date.split("-")[0];
    month = date.split("-")[1];
    day = date.split("-")[2];
    room = 'Green';
    document.getElementById("Year").value = year;
    document.getElementById("Month").value = month;
    document.getElementById("Day").value = day;
    document.getElementById("Room").value = room;
    $("#myModal").modal("show");
    $('.YearSelected').html(year);
    $('.MonthSelected').html(month);
    $('.DaySelected').html(day);
    $('.RoomSelected').html(room);
});

grey.subscribe('change', function (date) {
    date = this.getSelected()
    year = date.split("-")[0];
    month = date.split("-")[1];
    day = date.split("-")[2];
    room = 'Grey';
    document.getElementById("Year").value = year;
    document.getElementById("Month").value = month;
    document.getElementById("Day").value = day;
    document.getElementById("Room").value = room;
    $("#myModal").modal("show");
    $('.YearSelected').html(year);
    $('.MonthSelected').html(month);
    $('.DaySelected').html(day);
    $('.RoomSelected').html(room);
});