"use strict";


//your MapBox access tokne
mapboxgl.accessToken = 'pk.eyJ1IjoiY2FzZXlsdW0iLCJhIjoiY2l6eXJ6dzV3MDMzMTJwcXFocThtNzNsbiJ9.pmpavQkzgLOo-I41M0PacA';

/**
 * Handles responses from the fetch() API.
 * The iTunes API always returns JSON, even for
 * status codes >= 400.
 * @param {Response} response 
 * @returns {Promise}
 */
function handleResponse(response) {
    if (response.ok) {
        return response.json();
    } else {
        return response.json()
            .then(function(err) {
                throw new Error(err.errorMessage);
            });
    }
}

let map = new mapboxgl.Map({
    container: "map",
    style: "mapbox://styles/mapbox/streets-v9",
    center: [-122.3321, 47.6062], 
    zoom: 12
});

map.addControl(new mapboxgl.NavigationControl()); 
    
navigator.geolocation.getCurrentPosition(onCurrentPos, onErrorCurrentPos, {enableHighAccuracy: true});

function onCurrentPos(position) {
   console.log(position);
   let lnglat = [position.coords.longitude, position.coords.latitude];
   map.flyTo({center: lnglat, zoom: 14});

   let div = document.createElement("div");
   div.className = "current-location-marker";
   let marker = new mapboxgl.Marker(div);
   marker.setLngLat(lnglat).addTo(map);
}

function onErrorCurrentPos(error) {
    console.error(error);
    alert(error.message);
}

function addMarker(record) {
    let elem = document.createElement("div");
    elem.className = "data-marker";
    let marker = new mapboxgl.Marker(elem);
    let lnglat = [record.longitude, record.latitude];
    marker.setLngLat(lnglat);
    marker.addTo(map);
    let popup = new mapboxgl.Popup();
    let eventDate = new Date(record.event_clearance_date);
    popup.setText(record.event_clearance_description + " (" + eventDate.toLocaleDateString() + ")");
    marker.setPopup(popup);
}

fetch(dataURL) 
    .then(handleResponse)
    .then(data => {
        console.log(data);
        for (let i = 0; i < data.length; i++) {
            addMarker(data[i]);
        }
    })
    .catch(err => console.error(err));