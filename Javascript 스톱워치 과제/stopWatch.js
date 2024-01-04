const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const resetBtn = document.getElementById("resetBtn");
const screen = document.getElementById("clockScreen");
let second = 0, millisecond = 0;
let intervalId;
let resultSecond = 0;
let resultMillisecond = 0;

startBtn.addEventListener("click", function(){
    intervalId = setInterval(start, 10);
});

stopBtn.addEventListener("click", function() {
    clearInterval(intervalId);
    record();
});

resetBtn.addEventListener("click", reset);

function reset() {
    let div = document.getElementById("time");
    div.innerText = "00:00";
    second = 0;
    millisecond = 0;
}

function start(){
    let div = document.getElementById("time");
    if(!div){
        div = document.createElement("div");
        div.setAttribute("id", "time");
        screen.appendChild(div);
    }

    millisecond++;
    if (millisecond >= 100) {
        millisecond = 0;
        second++;
    }

    if (second === 0) {
        resultSecond = "00";
    }
    else {
        if (second > 9) {
            resultSecond = second;
        }
        else {
            resultSecond = "0" + second;
        }
    }


    if (millisecond > 9) {
        resultMillisecond = millisecond;
    }
    else {
        resultMillisecond = "0" + millisecond;
    }
    div.innerText = resultSecond + ":" + resultMillisecond;
}

function record(){
    const recordList = document.getElementById("recordList");
    const recordItem = document.createElement("li");

    const checkIcon = document.createElement("i");
    checkIcon.classList.add("fa-regular", "fa-circle");

    const trashIcon = document.createElement("i");
    trashIcon.classList.add("fa-solid", "fa-trash", "none");

    const div = document.createElement("div");
    div.innerText = resultSecond + ":" + resultMillisecond;

    recordItem.appendChild(checkIcon);
    recordItem.appendChild(div);
    recordItem.appendChild(trashIcon);

    recordList.appendChild(recordItem);
}

