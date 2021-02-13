function realtimeClock(){
    var rtClock = new Date();

    var hours = rtClock.getHours();
    var minutes = rtClock.getMinutes();
    var seconds = rtClock.getSeconds();

    hours = ("0" + hours).slice(-2);
    minutes = ("0" + minutes).slice(-2);
    seconds = ("0" + seconds).slice(-2);

    if(hours >= 6 && hours < 10){
        document.getElementById("clock").innerHTML = hours + ":" + minutes + ":" + seconds + "  Gunaydin"
        var t = setTimeout(realtimeClock, 500);
    }
    
    else if(hours >= 10 && hours < 17){
        document.getElementById("clock").innerHTML = hours + ":" + minutes + ":" + seconds + "  Iyi gunler"
        var t = setTimeout(realtimeClock, 500);
    }
    
    else if(hours >= 17 && hours < 20){
        document.getElementById("clock").innerHTML = hours + ":" + minutes + ":" + seconds + "  Iyi aksamlar"
        var t = setTimeout(realtimeClock, 500);
    }

    else if(hours >= 20 && hours < 24){
        document.getElementById("clock").innerHTML = hours + ":" + minutes + ":" + seconds + "  Iyi geceler"
        var t = setTimeout(realtimeClock, 500);
    }

    else if(hours < 6 && hours >= 0){
        document.getElementById("clock").innerHTML = hours + ":" + minutes + ":" + seconds + "  Esenlikler dilerim"
        var t = setTimeout(realtimeClock, 500);
    }
    
}