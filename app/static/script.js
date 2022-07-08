// get song details from API, if none then put placeholder image
let getSong = async () => {
    let response = await fetch('/artwork');
    spotifyImg = 'https://developer.spotify.com/assets/branding-guidelines/icon3@2x.png';

    try {
        if (response.status == 200) {
            let json = await response.json()
            artist = json['item']['artists'][0]['name']
            song = json['item']['name']
            img = json['item']['album']['images'][0]['url']

            document.getElementById("artistSong").innerHTML = `<h2>Now playing:</h2><p>${artist}: ${song}</p>`
            document.getElementById("artwork").innerHTML = `<img src=${img} alt="artwork for ${song} by ${artist}" />`
        }
    }
    catch {
        document.getElementById("artistSong").innerHTML = ''
        document.getElementById("artwork").innerHTML = `<img src=${spotifyImg} alt="Spotify logo"/>`
    }
}

// get song details on load
getSong()

// refresh song details every 5 secs
setInterval(() => {
    getSong(); 
}, 5000);