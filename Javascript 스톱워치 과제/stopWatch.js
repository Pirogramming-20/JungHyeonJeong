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
    checkIcon.addEventListener("click", function(){
        this.classList.toggle("fa-circle");
        this.classList.toggle("fa-circle-check");
    });

    const trashIcon = document.createElement("i");
    trashIcon.classList.add("fa-solid", "fa-trash", "none");

    const div = document.createElement("div");
    div.innerText = resultSecond + ":" + resultMillisecond;

    recordItem.appendChild(checkIcon);
    recordItem.appendChild(div);
    recordItem.appendChild(trashIcon);

    recordList.appendChild(recordItem);
}

document.getElementById("allCheckBtn").addEventListener("click", function(){
    const allBtn = document.getElementById("allCheckBtn");
    allBtn.classList.toggle("fa-circle");
    allBtn.classList.toggle("fa-circle-check");

    if (allBtn.classList.contains("fa-circle-check")) {
        const itemList = document.querySelectorAll('li');
        itemList.forEach(function(item){
            const checkIcon = item.querySelector(".fa-circle");
            if (checkIcon) {
                checkIcon.classList.remove("fa-circle");
                checkIcon.classList.add("fa-check-circle");
            }
        })
    }

    if (allBtn.classList.contains("fa-circle")) {
        const itemList = document.querySelectorAll('li');
        itemList.forEach(function(item){
            const checkIcon = item.querySelector(".fa-check-circle");
            if (checkIcon) {
                checkIcon.classList.add("fa-circle");
                checkIcon.classList.remove("fa-check-circle");
            }
        })
    }
});