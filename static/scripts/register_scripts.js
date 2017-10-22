/**
 * Created by emanuel on 7/31/17.
 */
function checkBothPasswords() {
    //This function serves two purposes.
    //The first is to verify that the password falls within certain parameters
    var pWordOne = document.getElementById('password').value;
    var pWordTwo = document.getElementById('password_check').value;

    document.getElementById('register_button').disabled = false;
    document.getElementById('password_error').innerHTML='';
    if (pWordOne !== pWordTwo) {
	document.getElementById('register_button').disabled = true;
	document.getElementById('password_error').innerHTML += 'Passwords must be equal.<br>';
    }
    if (pWordOne.length < 5) {
	document.getElementById('register_button').disabled = true;
	document.getElementById('password_error').innerHTML +=('Password must be at least 5 characters.<br>');
    }

}


$(function() {
function check_if_username_exists() {
    console.log("function check_if_username_exists()");
    $.ajax({
            url : "check_if_username_exists/", // the endpoint
                type: "POST", // http method
                data : { proposed_username : $('#form_username').val() }, // data sent with the post request

                // handle a successful response
                success : function(json) {
                    console.log(json); // log the returned json to the console
                    $("#username_error").html(json.username_exists_message); // for now, show True/False if username does/does not exist in database already
                    $("#register_button").prop('disabled',json.username_exists);
                    console.log("Should have set username_error to True/False by now.") // so we know to look for it
                },
                error : function(xhr,errmsg,err) {
                    $("#username_error").html(errmsg);
                    console.log(xhr.status + ": " + xhr.responseText); // more error info for the console 
                }
    });
};

$('#form_username').on('keyup', function(event){
        event.preventDefault();
        console.log("keyup detected");
        check_if_username_exists();
    }  
 );


// Following is taken from https://github.com/realpython/django-form-fun
// How to give proper credit???

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
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                        // Send the token to same-origin, relative URLs only.                                                                                                  
                        // Send the token only if the method warrants CSRF protection                                                                                          
                        // Using the CSRFToken value acquired earlier                                                                                                          
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });


});

