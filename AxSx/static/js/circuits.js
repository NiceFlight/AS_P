// 設定下拉選單
const circuitSelect = document.getElementById("selectedCircuit");

// 有一個 JSON 資料結構，填充選項
fetch("/circuits_json/")
    .then((response) => response.json())
    .then((data) => {
        const circuits = data['features'];

        // 動態填充選項
        circuits.forEach((circuit) => {
            var option = document.createElement("option");
            option.value = circuit.properties.id;
            option.text = circuit.properties.Name;
            circuitSelect.appendChild(option);
        });
        document.getElementById("selectedCircuit").addEventListener('change', function () {
            var selectedCircuit = circuitSelect.value
            console.log(selectedCircuit);
            var filterCircuit = {
                'type': 'FeatureCollection',
                'features': data.features.filter(function (feature) {
                    return (
                        feature.properties.id === selectedCircuit
                    );
                }),
            };
            console.log(filterCircuit);
            var geojsonLayer;
            if (geojsonLayer) {
                map.removeLayer(geojsonLayer)
            }
            geojsonLayer = L.geoJSON(filterCircuit, {
                style: function () {
                    return {
                        color: "#ff0000",
                        weight: 3,
                    };
                },
            }).addTo(map);
            if (filterCircuit.features.length > 0) {
                // 選取中的鄉鎮(列表)，fitBounds()
                var bounds = geojsonLayer.getBounds();
                map.fitBounds(bounds);
            };
        });
    });

// 初始化地圖
const map = L.map("map").setView([0, 0], 3);  // 中心座標

// 添加底圖
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

// fetch("/circuits_json/").then((response) => response.json()).then((data) => {
//     L.geoJSON(data, {
//         style: function () {
//             return {
//                 color: "#ff0000",
//                 weight: 3,
//             };
//         },
//     }).addTo(map);
//     // console.log(data)
// }).catch(error => console.error(error));
