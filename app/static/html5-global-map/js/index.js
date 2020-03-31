let list = getParamValue("list");
filledList(list);

function getParamValue()
{
    var url = window.location.search.substring(1); //get rid of "?" in querystring
    var pArr = url.split('='); //split key and value
    var param = pArr[1].split("%2C");
    return param;
}

function filledList(list) {
    for (let i = 0; i < list.length; i++) {
        filled(list[i]);
    }
}

function filled(country) {
    let x = document.getElementById(country);
    let a = x.getAttribute("fill");
    x.setAttribute("fill", "#477cb2");
    let b = x.getAttribute("fill");
}

