// let access_token = "BQBxtE6zSFY3ReaOTi3OMoxeug0AHP_2e_3YjoopJtsOcLB28wuqDpQycfZueJRDsTrUTyXZYGBlzP_KYWMehNs6Ct8c-cbXQzDh39KLBStAhRk8sr1FGKmbAqxiJc46fA7FoeaIHm1GiJ7Opu9aaORwwDHvX1V1XJPAEwxPgvc56gVz8OEf5Tg";
// let player;

// //initialze player once the app starts
// window.onSpotifyWebPlaybackSDKReady = () => {
//     player = initializePlayer(access_token);
// }

// function initializePlayer(access_token){
//    player = new Spotify.Player({
//       name: 'Web Playback SDK Quick Start Player',
//       getOAuthToken: cb => { cb(access_token); },
//       volume: 0.1
//     });

//     // Error handling
//     player.addListener('initialization_error', ({ message }) => { console.error(message); });
//     player.addListener('authentication_error', ({ message }) => { console.error(message); });
//     player.addListener('account_error', ({ message }) => { console.error(message); });
//     player.addListener('playback_error', ({ message }) => { console.error(message); });

//     // Playback status updates
//     player.addListener('player_state_changed', state => { console.log(state); });

//     // Ready
//     player.addListener('ready', ({ device_id }) => {
//       console.log('Ready with Device ID', device_id);
//     });

//     // Connect to the player!
//     player.connect();

//     return player;
// }

// function play(song_id){
//     console.log("start playing the song with songid", songid);
//     //start playing the song
//     const play = ({
//       spotify_uri,
//       playerInstance: {
//         _options: {
//           getOAuthToken,
//           id
//         }
//       }
//     }) => {
//       getOAuthToken(access_token => {
//         console.log(access_token);
//         console.log(device_id);
//         fetch(`https://api.spotify.com/v1/me/player/play?device_id=${device_id}`, {
//           method: 'PUT',
//           body: JSON.stringify({ uris: [spotify_uri] }),
//           headers: {
//             'Content-Type': 'application/json',
//             'Authorization': `Bearer ${access_token}`
//           },
//         });
//       });
//     };

//     play({
//       playerInstance: player,
//       spotify_uri: `spotify:track:${song_id}`
//     });

//     // Connect to the player!
//     player.connect();
//   }