
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", document.getElementById('csrfmiddlewaretoken').value);
        }
    }
});

function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


function getAllList()
{
    $.ajax({
        url:'/getAllRegions/',
        type:'GET',
        success: function(response){
            $("#region").append($("<option>").text('Select the Region').attr('value', 0));
            if(response.length > 0) {
                $.each(response, function (i, value) {
                    if (value != "") {
                        $("#region").append($("<option>").text(value).attr('value', value));
                    }
                });
            }
        }
    });
     $.ajax({
        url:'/getAllTempTypes/',
        type:'GET',
        success: function(response){
            $("#tempType").append($("<option>").text('Select the Temp Type').attr('value', 0));
            if(response.length > 0) {
                $.each(response, function (i, value) {
                    if (value != "") {
                        $("#tempType").append($("<option>").text(value).attr('value', value));
                    }
                });
            }
        }
    });

      $.ajax({
        url:'/getAllYears/',
        type:'GET',
        success: function(response){
            $("#year").append($("<option>").text('Select the year').attr('value', 0));
            if(response.length > 0) {
                $.each(response, function (i, value) {
                    if (value != "") {
                        $("#year").append($("<option>").text(value).attr('value', value));
                    }
                });
            }
        }
    });

}


function drawGraph(){
    $("#msgDiv").empty();
    var region = document.getElementById('region').value;
    var type = document.getElementById('tempType').value;
    var year = document.getElementById('year').value;
    if(region != 0 && type != 0 && year != 0) {
        $.get('/getDataForChart/?region=' + region + '&type=' + type+ '&year=' + year, function (d) {
          $('#dashChart').empty();
          console.log(d['month']);
           console.log(d['data']);
           var marray=[];
           var dataarray=[];
           for(i=0;i<=d.length;i++)
           {
              marray[i] = d[i].month;
              dataarray[i] = d[i].data;
           }
          var chart = c3.generate({
            bindto: '#dashChart',
            data: {
                columns: [
                    marray,
                    dataarray
                ],
                type: 'line',

            },
              bar: {
                width: {
                    ratio: 0.5
                }
              },

        });
        });
    }
    else{
        $("#msgDiv").append('<div class="alert alert-warning alert-dismissable"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>ERROR : Please select Region and Type and Year of weather.</div>');
    }

}