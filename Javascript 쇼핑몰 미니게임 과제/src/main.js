//json 파일에서 아이템들을 받아옴
function loadItems(){
    return fetch('./data/data.json')
    .then(response => response.json())
    .then(json => json.items)
}

loadItems()
.then(items =>{
    console.log(items);
    //displayItems(items);
    //setEventListeners(items)
})
.catch(console.log)