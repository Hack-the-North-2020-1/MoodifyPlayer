var access_token = "BQDkFkUCakGWxCwtvWyvDct7b-NTbUNHwoRJa18S6qI5XUyn7uTWmpJORw6cEJuViyH6SQeRDsXcYzrrnv53Jkwcq-VCwrlmNUDzlWJO6j69oaq72IfSjT6VyvWBGL27dL5Fc_I73_eEFXMisY9HOjinltTpksCK2h8rY7lHpkNN0pj4XFsb2Tg"

window.onSpotifyWebPlaybackSDKReady = () => {
    player = new Spotify.Player({
      name: 'Web Playback SDK Quick Start Player',
      getOAuthToken: cb => { cb(access_token); },
      volume: 0.1
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
        spotify_uri: 'spotify:track:7xGfFoTpQ2E7fRF5lN10tr'
      });
    });

    // Connect to the player!
    player.connect();
  }