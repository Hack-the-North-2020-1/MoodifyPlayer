const imageContainer = document.getElementById("image-container");
const image = document.getElementById("image-placeholder");
const songnameContainer = document.getElementById("songname");
const artistnameContainer = document.getElementById("artistname");

let access_token = "BQAI-Tsf0ME13IfHCeRI96kNjTnK0CM5pmvqJfw3kfQU2whMvFj5oPgO3cWwudaQaTqU3agVF0-h0h9v6gkJKjKPEe25FRdcMhCqYFxLIPmLjwn-lv9MmWoIikYDqUloUnpZ1ixMj1nDtg3GpbPp7LT_txteGFw0";
let player;
let device_id;

function startSong(song_id){
    console.log("starting song...");
    player = new Spotify.Player({
    name: 'Web Playback SDK Quick Start Player',
        getOAuthToken: cb => { cb(access_token); }
    });

    // Error handling
    player.addListener('initialization_error', ({ message }) => { console.error(message); });
    player.addListener('authentication_error', ({ message }) => { console.error(message); });
    player.addListener('account_error', ({ message }) => { console.error(message); });
    player.addListener('playback_error', ({ message }) => { console.error(message); });

    // Playback status updates
    player.addListener('player_state_changed', state => { console.log(state); });

    // Ready
    player.addListener('ready', ({ device_id }) => {
    console.log('Ready with Device ID', device_id);
    
    //start playing the song
    const play = ({
        spotify_uri,
        playerInstance: {
        _options: {
            getOAuthToken,
            id
         }
        }
    }) => {
        getOAuthToken(access_token => {
        console.log(access_token);
        console.log(device_id);
        fetch(`https://api.spotify.com/v1/me/player/play?device_id=${device_id}`, {
            method: 'PUT',
            body: JSON.stringify({ uris: [spotify_uri] }),
            headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${access_token}`
            },
         });
        });
    };

    play({
        playerInstance: player,
        spotify_uri: `spotify:track:${song_id}`
    });
    });

    // Connect to the player!
    player.connect();
}


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
        event.preventDefault();
        songname = songnameContainer.value;
        artistname = artistnameContainer.value;

        song_id = "7xGfFoTpQ2E7fRF5lN10tr";
        
        fetch(`/artist:${artistname}&song:${songname}`, {
            method: 'GET',
            headers: {
                'Content-Type' : 'application/json',
                'Authorization' : 'Bearer ' + access_token
            }
        })
        .then(res=>res.text())
        .then(data=> {
            startSong(data);
        }
        )
        .catch(err=>{
            console.log(err);
        })
    }

subscribeToImages(updateImage);
console.log("subscribeToImages");