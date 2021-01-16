function subscribeToImages(cb){
    //connect to the hashtag namespace
    const socket = io();
    socket.emit("subscribeToImages", "someuserid");
    socket.on("imageData", data => cb(data));
}

function cb(data){
    console.log(data);
}

subscribeToImages(cb);
console.log("subscribeToImages");