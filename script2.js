const map = L.map('map').setView([0, 0], 2);  // Set the initial view of the map

// Add a tile layer (you can use different tile layers as per your preference)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// Define a function to create curves (parabola-like)
function createParabolicCurve(start, end, color) {
    const midpoint = [(start[0] + end[0]) / 2, (start[1] + end[1]) / 2];
    const controlPoint = [midpoint[0] + (end[0] - start[0]) * 0.1, midpoint[1] + (start[1] - end[1]) * 0.2];
    
    const latlngs = [
        'M', [start[0], start[1]],
        'Q', controlPoint,
        [end[0], end[1]]
    ];
    
    return L.curve(latlngs, { color: color, weight: 2 }).addTo(map);
}

// Define shipping routes
const routes = [
    {
        name: "Taiwan to Los Angeles",
        color: "red",
        points: [
            [22.6273, 120.3014],  // Kaohsiung, Taiwan
            [33.7408, -118.259]  // Los Angeles, USA
        ]
    },
    {
        name: "Taiwan to Rotterdam",
        color: "blue",
        points: [
            [22.6273, 120.3014],  // Kaohsiung, Taiwan
            [51.9244, 4.4777]     // Rotterdam, Netherlands
        ]
    },
    {
        name: "Taiwan to Sydney",
        color: "green",
        points: [
            [22.6273, 120.3014],  // Kaohsiung, Taiwan
            [-33.8688, 151.2093]  // Sydney, Australia
        ]
    },
    {
        name: "Taiwan to Singapore",
        color: "orange",
        points: [
            [22.6273, 120.3014],  // Kaohsiung, Taiwan
            [1.3521, 103.8198]    // Singapore
        ]
    },
    {
        name: "Taiwan to Hamburg",
        color: "purple",
        points: [
            [22.6273, 120.3014],  // Kaohsiung, Taiwan
            [53.5511, 9.9937]     // Hamburg, Germany
        ]
    },
    {
        name: "Taiwan to New York",
        color: "yellow",
        points: [
            [22.6273, 120.3014],  // Kaohsiung, Taiwan
            [40.7128, -74.0060]   // New York, USA
        ]
    },
    {
        name: "Taiwan to Dubai",
        color: "cyan",
        points: [
            [22.6273, 120.3014],  // Kaohsiung, Taiwan
            [25.276987, 55.296249] // Dubai, UAE
        ]
    },
    {
        name: "Taiwan to Durban",
        color: "magenta",
        points: [
            [22.6273, 120.3014],  // Kaohsiung, Taiwan
            [-29.8587, 31.0218]   // Durban, South Africa
        ]
    },
    {
        name: "Taiwan to Buenos Aires",
        color: "brown",
        points: [
            [22.6273, 120.3014],  // Kaohsiung, Taiwan
            [-34.6037, -58.3816]  // Buenos Aires, Argentina
        ]
    },
    {
        name: "Taiwan to Vancouver",
        color: "lime",
        points: [
            [22.6273, 120.3014],  // Kaohsiung, Taiwan
            [49.2827, -123.1207]  // Vancouver, Canada
        ]
    }
];

// Add routes to the map
routes.forEach(route => {
    createParabolicCurve(route.points[0], route.points[1], route.color).bindPopup(route.name);
});

// Add a legend
const legend = L.control({ position: 'bottomright' });

legend.onAdd = function(map) {
    const div = L.DomUtil.create('div', 'info legend');
    const labels = [
        "Taiwan to Los Angeles",
        "Taiwan to Rotterdam",
        "Taiwan to Sydney",
        "Taiwan to Singapore",
        "Taiwan to Hamburg",
        "Taiwan to New York",
        "Taiwan to Dubai",
        "Taiwan to Durban",
        "Taiwan to Buenos Aires",
        "Taiwan to Vancouver"
    ];
    const colors = ["red", "blue", "green", "orange", "purple", "yellow", "cyan", "magenta", "brown", "lime"];

    for (let i = 0; i < labels.length; i++) {
        div.innerHTML += `<i style="background:${colors[i]}"></i> ${labels[i]}<br>`;
    }
    return div;
};

legend.addTo(map);
