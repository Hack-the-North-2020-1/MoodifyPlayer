var imageContainer = document.getElementById("image-container");
var image = document.getElementById("image-placeholder");

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

subscribeToImages(updateImage);
console.log("subscribeToImages");