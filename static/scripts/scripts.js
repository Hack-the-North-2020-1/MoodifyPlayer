var imageContainer = document.getElementById("image-container");
var image = document.getElementById("image-placeholder");
var songnameContainer = document.getElementById("songname");
var artistnameContainer = document.getElementById("artistname");

function subscribeToImages(updateImage){
    //connect to the hashtag namespace
    const socket = io();
    socket.emit("subscribeToImages", "someuserid");
    socket.on("imageData", data => updateImage(data));
}

function updateImage(data){
    console.log(data);
    image.src = data;
}

function playsong(event){
    songname = songnameContainer.value;
    artistname = artistnameContainer.value;

    token = "BQAw4Mnaa1B0s_7jgPmQ9fu85rvkmD4qHnW2qZ8Gr9E2gef9iVNI1HF4ICRjVOdz8PnYZn1dQDc5FgbLvEWTX1EK8mLLNOdaoMfOl2Gsmwh6sw7nYXtpHg3XAbOwPmqMMXcqMamX1Utt7QOVA8VRvgHtUqyGcbe3soJsM_AK894"
    
    fetch(`/artist:${artistname}&song:${songname}`, {
        method: 'GET',
        headers: {
            'Content-Type' : 'application/json',
            'Authorization' : 'Bearer ' + token
        }
    })
    .then(res=>res.text())
    .then(data=> {
        console.log(data);
     }
    )
    .catch(err=>{
        console.log(err);
    })
}

subscribeToImages(updateImage);
console.log("subscribeToImages");