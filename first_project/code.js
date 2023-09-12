let saveEl = document.getElementById("save-el");
let countEl = document.getElementById("count-el");
let count = 0;
let previousEntries = "";

function increment() {
  count += 1;
  countEl.innerText = count;
}

function save() {
  let countStr = count + " - ";
  previousEntries += countStr;
  saveEl.textContent = "Previous entries:" + previousEntries;
  console.log(count);
  count = 0;
  countEl.innerText = count;
}
