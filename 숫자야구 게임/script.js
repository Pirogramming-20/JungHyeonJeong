let leftover = 9;
const answer = [];
let flag = true;
let finish = false;

while(answer.length < 3){
    let num = Math.floor(Math.random() * 10);
    if(!answer.includes(num)) answer.push(num);
}

function check_numbers(){
    //입력값 받아오고 3개가 모두 다 들어왔는지 확인
    let num1 = document.getElementById("number1").value;
    let num2 = document.getElementById("number2").value;
    let num3 = document.getElementById("number3").value;
    if(num1 === '' || num2 === '' || num3 === '') flag = false;
    else flag = true;


    //if 입력값 3개가 모두 들어왔다면 결과 확인 시작
    if(flag){
        num1 = Number(document.getElementById("number1").value);
        num2 = Number(document.getElementById("number2").value);
        num3 = Number(document.getElementById("number3").value);

        let arr = [num1, num2, num3];
        let s = 0;
        let b = 0;
        console.log(answer);
        console.log(arr);

        //s와 b의 값 업데이트
        for(let i = 0; i < 3; i++){
            if(arr[i] === answer[i]) s++;
            else if(answer.includes(arr[i])) b++;
        }

        if(s === 3) finish = true;
        //console.log(finish);

        if(s === 0 && b === 0){
            const resultDisplayDiv = document.querySelector('.result-display');
            resultDisplayDiv.className = 'result-display';
            const checkResultDiv = document.createElement('div');
            checkResultDiv.className = 'check-result';
            checkResultDiv.innerHTML = `
                <div class="left">${num1} ${num2} ${num3}</div>
                :
                <div class="right">
                    <div class="out num-result">O</div>
                </div>
            `;
            resultDisplayDiv.appendChild(checkResultDiv);
        }
        else{
            const resultDisplayDiv = document.querySelector('.result-display');
            resultDisplayDiv.className = 'result-display';
            const checkResultDiv = document.createElement('div');
            checkResultDiv.className = 'check-result';
            checkResultDiv.innerHTML = `
                    <div class="left">${num1} ${num2} ${num3}</div>
                    :
                    <div class="right">
                        ${s} <div class="strike num-result">S</div>
                        ${b} <div class="ball num-result">B</div>
                    </div>
            `;
            resultDisplayDiv.appendChild(checkResultDiv);
        }
    }

    leftover--;
    console.log(leftover);

    if(finish){
        document.getElementById('game-result-img').setAttribute('src', './success.png');
    }
    else if(!finish && leftover === 0){
        document.getElementById('game-result-img').setAttribute('src', './fail.png');
    }

    //확인하기 누른 후 : 입력창 비우기
    document.getElementById("number1").value = '';
    document.getElementById("number2").value = '';
    document.getElementById("number3").value = '';

    setTimeout(function reset(){document.getElementById('game-result-img').setAttribute('src', '');}, 5000);
    
}