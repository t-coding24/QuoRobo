var LEVEL_MAX = 10;
var LEVEL_MIN = 0;
var currentLevelPan = 5;
var currentLevelTilt = 5;
var commandID = 0;

var TILT_MIN = 45;
var TILT_MAX = 135;
var PAN_MIN = 45;
var PAN_MAX = 135;
var current_tilt = 90;
var current_pan = 90;

function applyCustomCss(custom_css) {
    var head = document.getElementsByTagName('head')[0];
    var style = document.createElement('link');
    style.rel = "stylesheet";
    style.type = "text/css";
    style.href = custom_css;
    head.appendChild(style);
}

function initialize_webiopi() {
    applyCustomCss('../css/styles.css')
    webiopi().refreshGPIO(false);
}

$(function() {

    $("#smileBtn").click(function() {
        console.log("JS:smileBtn");
        webiopi().callMacro("eye","s");
	webiopi().callMacro("voice","konnitiwaaaaaa");
    });
    $("#blinkBtn").click(function() {
        console.log("JS:blinkBtn");
        webiopi().callMacro("eye","b");
	webiopi().callMacro("voice","tukaretayooooo");
    });
    $("#happyBtn").click(function() {
        console.log("JS:blinkBtn");
        webiopi().callMacro("eye","h");
	webiopi().callMacro("voice","hajimemasiteeee");
    });
    $("#emo1Btn").click(function() {
        webiopi().callMacro("eye","g");
	webiopi().callMacro("voice","konnitiwaaaaaaa");
    });
    $("#emo2Btn").click(function() {
        webiopi().callMacro("eye","p");
	webiopi().callMacro("voice","yaaadayoooo");
    });
    $("#emo3Btn").click(function() {
        webiopi().callMacro("eye","t");
	webiopi().callMacro("voice","pepperdesu");
    });
    $("#homeBtn").click(function() {
        console.log("JS:Home")
        while(current_tilt != 90 && current_pan != 90){
            setTimeout(1000);
            if(current_tilt > 90){
            current_tilt = current_tilt -1;
            }
            if(current_tilt < 90){
            current_tilt = current_tilt + 1;
            }
            if(current_pan > 90){
            current_pan = current_pan - 1;
            }
            if(current_pan < 90){
            current_pan = current_pan + 1;
            }
            webiopi().callMacro("move",[String(current_tilt), String(current_pan)]);
        }
    });

    $("#upBtn").click(function() {
        setTimeout(1000);
        if(current_tilt < TILT_MAX){
            current_tilt = current_tilt + 5;
            webiopi().callMacro("move",[String(current_tilt), String(current_pan)]);
        }
    });

    $("#downBtn").click(function() {
      setTimeout(1000);
        if(current_tilt > TILT_MIN){
            current_tilt = current_tilt - 5;
            webiopi().callMacro("move",[String(current_tilt), String(current_pan)]);
        }
    });

    $("#leftBtn").click(function() {
        setTimeout(1000);
        if(current_pan > PAN_MIN){
            current_pan = current_pan - 5;
            webiopi().callMacro("move",[String(current_tilt), String(current_pan)]);
        }
    });

    $("#rightBtn").click(function() {
        setTimeout(1000);
        if(current_pan < PAN_MAX){
            current_pan = current_pan + 5;
            webiopi().callMacro("move",[String(current_tilt), String(current_pan)]);
        }
    });

    $("#shotBtn").click(function() {
        $.get("http://192.168.1.37:8080/0/action/snapshot", function(data) {
            alert("Shot Success!!");
        });
    });
});
