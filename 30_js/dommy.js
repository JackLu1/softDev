// team - Jack Lu, Cheryl Qian
// SoftDev1 pd8
// K30 -- Sequential Progression III: Season of the Witch
// 2018-12-21

var fib = function (n){
    if (n < 2){
        return n;
    }
    else
        return fib(n-1) + fib(n-2);
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
addList.addEventListener('click', function(e){
    //console.log(e);
    var item = document.createElement("li");
    item.innerHTML = "new item";
    var ol = document.getElementById("thelist");
    ol.appendChild(item);
});

