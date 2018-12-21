// team - Jack Lu, Cheryl Qian
// SoftDev1 pd8
// K30 -- Sequential Progression III: Season of the Witch
// 2018-12-21

var fib = function (n){
    var results = [0, 1];
    for (var i = 2; i <= n; i++){
        results.push(results[i-2]  + results[i-1]);
    }
    return results[n];
}

// display list item when hovering over it
var dlist = document.getElementById("thelist").childNodes;
for (var i = 0; i < dlist.length; i++){
    var el = dlist[i];
    el.addEventListener('mouseover', function(e){
        //console.log(e.target.innerHTML);
        document.getElementById("h").innerHTML = e.target.innerHTML;
    })
    el.addEventListener('click', function(){
        this.remove();
        document.getElementById("h").innerHTML = "Hello World!";
    })
}

// change back to "hello world" when mouse leaves list
document.getElementById("thelist").addEventListener('mouseout', function(){
    document.getElementById("h").innerHTML = "Hello World!";
})

// adds element to list when button pushed
var addList = document.getElementById("b");
addList.addEventListener('click', function(){
    //console.log(e);
    var item = document.createElement("li");
    item.innerHTML = "new item";
    var ol = document.getElementById("thelist");
    ol.appendChild(item);
    item.addEventListener('mouseover', function(e){
        //console.log(e.target.innerHTML);
        document.getElementById("h").innerHTML = e.target.innerHTML;
    })
    item.addEventListener('click', function(){
        this.remove();
        document.getElementById("h").innerHTML = "Hello World!";
    })
});

// add fib numbers in a list when fib button clicked
var fiblist = document.getElementById("fiblist");
var fbutton = document.getElementById("fb");
var counter = 1;
var f = document.getElementById("fiblist");
fbutton.addEventListener('click', function(e){
    var item = document.createElement("li");
    item.innerHTML = fib(counter++);
    f.appendChild(item);
});

