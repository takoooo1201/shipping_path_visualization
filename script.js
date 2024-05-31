const map = L.map('map').setView([0, 0], 2);  // Set the initial view of the map

// Add a tile layer (you can use different tile layers as per your preference)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// Define shipping routes
const routes = [
    {
        name: "Route 1",
        color: "red",
        points: [
            [35.6895, 139.6917],  // Tokyo
            [37.7749, -122.4194], // San Francisco
            [51.5074, -0.1278]    // London
        ]
    },
    {
        name: "Route 2",
        color: "blue",
        points: [
            [22.3964, 114.1095],  // Hong Kong
            [1.3521, 103.8198],   // Singapore
            [-33.8688, 151.2093]  // Sydney
        ]
    }
];

// Add routes to the map
routes.forEach(route => {
    L.polyline(route.points, { color: route.color }).addTo(map).bindPopup(route.name);
});

L.polyline(route.points, { color: route.color })
    .addTo(map)
    .bindPopup(`<b>${route.name}</b><br>More info about this route.`);


const legend = L.control({ position: 'bottomright' });

legend.onAdd = function(map) {
    const div = L.DomUtil.create('div', 'info legend');
    const routes = ["Route 1", "Route 2"];
    const colors = ["red", "blue"];
    
    for (let i = 0; i < routes.length; i++) {
        div.innerHTML += `<i style="background:${colors[i]}"></i> ${routes[i]}<br>`;
    }
    return div;
};

legend.addTo(map);



