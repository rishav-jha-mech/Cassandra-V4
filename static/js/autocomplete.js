
var x = 1;
const togAuto = () => {
    var stateText = document.getElementById('AucTu');
    var stateSwitch = document.getElementById('forma');
    if (x == 1) { stateText.innerText = "Autocomplete Turned On"; stateSwitch.setAttribute("autocomplete", "on"); x++; }
    else if (x == 2) { stateText.innerText = "Autocomplete Turned Off"; stateSwitch.setAttribute("autocomplete", "off"); x--; }
}