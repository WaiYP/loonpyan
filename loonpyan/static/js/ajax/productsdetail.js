$(function () {
    $(document).ajaxStart($.blockUI).ajaxStop($.unblockUI);

    getProductGroup();

    function getProductGroup() {
        $.ajax({
            url: "api/products/get_productgroup/", // the endpoint
            type: "GET", // http method
            // handle a successful response
            success: function (data) {

                var sel;
                var pid=$("#pgroup").val();

                // alert(pid);
                $("#pgroup").html('');
                for (var i = 0; i < data.length; i++) {
                    pgroup = data[i];
                    if(i==0)
                        {
                            sel=pgroup.id;
                        }
                    if(pid==pgroup.id)
                    {
                        sel = pgroup.id;
                        // alert('in selected');
                        $("#pgroup").append(
                            '<option value="' + pgroup.id + '" selected>'
                            + pgroup.name
                            + '</option>'
                        );
                    }
                    else{
                        // alert(pgroup.id);
                        $("#pgroup").append(
                        $('<option/>', {
                            value: pgroup.id,
                            html: pgroup.name
                        }));
                    }

                }
                $("#pgroup").val(sel);
                getProductSubGroup(sel);
            },
            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }

    $('#pgroup').change(function () {
        //alert('In change');
        // alert($('#pgroup').val());

        getProductSubGroup($('#pgroup').val());
        // getProSubGroup($('#pgroup').val());//updated by SSM to use the text input search in product sub group4/5/2018
    });


    //updated by SSM to make text search input in Product Sub Group 4/5/2018
    function getProductSubGroup(id) {
        $.ajax({

            url: "api/products/get_productsubgroup/" + id, // the endpoint
            type: "GET", // http method
            // handle a successful response
            success: function (data) {
                // alert('hello success');
                var psid=$("#psgroup").val();
                // alert(psid);
                $('#psgroup').html(' ');
                var sel;
                for (var i = 0; i < data.length; i++) {
                   // alert(i);
                    psgroup = data[i];
                   // alert(psgroup.id);
                    if (i == 0)
                        sel = psgroup.id;
                     if(psid==psgroup.id)
                    {
                        sel = psgroup.id;
                        // alert('in selected');
                        $("#psgroup").append(
                            '<option value="' + psgroup.id + '" selected>'
                            + psgroup.name
                            + '</option>'
                        );
                    }
                    else{
                        // alert(psgroup.id);
                        $("#psgroup").append(
                        $('<option/>', {
                            value: psgroup.id,
                            html: psgroup.name
                        }));
                    }

                    // $("#psgroup").append(
                    //     $('<option/>', {
                    //         value: psgroup.id,
                    //         html: psgroup.name
                    //     }));
                }
                $("#psgroup").val(sel);
                // getProduct(sel);
                // getProductLength(sel);
            },
            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }


    $('#psgroup').change(function () {
        // alert('In change sub group');
        // alert($('#pgroup').val());
        // getProduct($('#psgroup').val());
        // getProductLength($('#psgroup').val());
    });


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});