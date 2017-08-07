/**
 * Created by emanuel on 7/31/17.
 */

function checkBothPasswords() {
    //This function serves two purposes.
    //The first is to verify that the password falls within certain parameters
    var pWordOne = document.getElementById('password').value;
    var pWordTwo = document.getElementById('password_check').value;
    if (pWordOne === pWordTwo && pWordOne.length >= 5) {
        document.getElementById('register_button').disabled = false;
    } else {
        document.getElementById('register_button').disabled = true;
    }
}