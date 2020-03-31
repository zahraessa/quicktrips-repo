let countryList = getParamValue(0);
let ratingList = getParamValue(1);
filledList(countryList, ratingList);

function getParamValue(n)
{
    // n = 0 get the country while n = 1 get the rate
    var url = window.location.search.substring(1); //get rid of "?" in querystring
    var qArray = url.split('&'); //get key-value pairs
    var pArr = qArray[n].split('='); //split key and value
    var param = pArr[1].split("%2C");
    return param

}

function filledList(countryList, ratingList) {
    for (let i = 0; i < countryList.length; i++) {
        filled(countryList[i], ratingList[i]);
    }
}

function filled(country, rating) {
    let x = document.getElementById(country);
    if (rating === "0") {
        x.setAttribute("fill", "rgba(89,184,255,0.59)");
    }
    else if (rating === "1") {
        x.setAttribute("fill", "rgba(83,173,238,0.7)");
    }
    else if (rating === "2") {
        x.setAttribute("fill", "rgba(81,160,223,0.75)");
    }
    else if (rating === "3") {
        x.setAttribute("fill", "rgba(78,148,208,0.8)");
    }
    else if (rating === "4") {
        x.setAttribute("fill", "rgba(63,126,192,0.9)");
    }
    else if (rating === "5") {
        x.setAttribute("fill", "#477cb2");
    }
}

