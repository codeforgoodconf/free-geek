/**
 * Created by emanuel on 7/31/17.
 */

function checkBothPasswords() {
    console.log(document.getElementById("password").value);
    console.log(document.getElementById("password_check").value);
}

function sanitizeThis() {
    //Using regex to make sure that the input >= 10 <= 100000
    //If there are decimals it needs at least one number after the decimal point.
    const regex = /^([1-9][0-9]{1,4})(\.[0-9]{1,2})?$/g;
    const currFrequency = $('#frequency_number').val();
    var message = $('#message_bro');

    if (!!currFrequency.match(regex) == false){

        message.html("INVALID! example: 500 or 325.23");
        message.css("color", "red");
        sanitized = false;
    } else{
        message.css("color", "greenyellow");
        message.html("VALID INPUT");
        sanitized = true;
    }
}
