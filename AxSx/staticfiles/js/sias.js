// 初始化地圖
const map = L.map('map', {
    center: [23.58, 120.58], // 中心座標
    crs: L.CRS.EPSG3857, // 使用 EPSG:3857 坐標系
    zoom: 7,
    worldCopyJump: true, // 無限滾動
    zoomSnap: 0.25, // 更小的縮放步長
    zoomDelta: 1, // 更小的縮放增量
    inertia: true, // 啟用慣性滾動
    inertiaDeceleration: 3000, // 慣性滾動減速
    inertiaMaxSpeed: 1500 // 慣性滾動最大速度
})
// 添加底圖
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    className: 'grayscale'
}).addTo(map)

const citySelect = document.getElementById("selectedCity");

// 假設有一個 JSON 資料結構，包含縣市與鄉鎮的對應關係
fetch('/static/js/city_town_ID.json')
    .then((response) => response.json())
    .then((data) => {
        const cityTowns = data
        // console.log(cityTowns)

        // 動態填充縣市選項
        for (const city in cityTowns) {
            // console.log(city);
            const option = document.createElement('option')
            option.value = city
            option.textContent = city
            citySelect.appendChild(option)
        }
    })

function getCsrfToken() {
    return document.cookie.split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}


// 傳遞縣市到後端
let geojsonLayer;

document.getElementById('selectedCity').addEventListener('change', function () {
    var filterCity = citySelect.value
    // console.log(filterCity)
    fetch('/api/sias_json/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken(), // CSRF token
        },
        body: JSON.stringify({ filterCity: filterCity }), // 傳遞縣市到後端
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.status == 'success') {
                var siases = JSON.parse(data.sias_json)
                var selectedCity = data.selectedCity_json
                // console.log(selectedCity)

                if (geojsonLayer) {
                    map.removeLayer(geojsonLayer)
                }

                try {
                    geojsonLayer = L.geoJSON(selectedCity, {
                        style: function () {
                            return {
                                color: '#ff0000',
                                weight: 3,
                                fillOpacity: 0
                            }
                        }
                    }).addTo(map)
                } catch (e) {
                    console.error("JSON 解析失敗：", e);
                }
                // 更新邊界
                var bounds = geojsonLayer.getBounds()
                map.fitBounds(bounds)

                map.eachLayer(function (layer) {
                    if (layer instanceof L.Marker) {
                        map.removeLayer(layer)
                    }
                })
                // 創建一個空的 bounds 來存儲所有座標
                var bounds = L.latLngBounds();

                siases.forEach(function (as) {
                    if (as.lat && as.lng) {
                        // 顯示 marker
                        var marker = L.marker([as.lat, as.lng]).addTo(map)
                        marker.bindPopup(`<b>Name: ` + as.name + `</b><br><b>Code: ` + as.code + `</b><br><b>Culture type: ` + as.culture_type + `</b><br><b>Era: ` + as.era + `</b><br><b>Year: ` + as.year + `</b><br><b>Rating: ` + as.rating + `</b>`)
                        marker.on('mouseover', function (e) {
                            this.openPopup()
                        })
                        marker.on('mouseout', function (e) {
                            this.closePopup()
                        })
                        bounds.extend([as.lat, as.lng]);
                    }
                })
                // if (siases.length > 0) {
                // map.fitBounds(bounds);
                // }
            } else {
                console.error('Error:', data.message)
            }
        })
        .catch((error) => console.error('Error:', error))
})


// 加載外部 GeoJSON 文件
//let geojsonLayer

// function updateMap(selectedCity) {
//     if (selectedCity.includes('台')) {
//         selectedCity = selectedCity.replace('台', '臺')
//     }
//     fetch('/static/js/city.geojson')
//         .then((response) => response.json())
//         .then((data) => {
//             var filteredData = {
//                 type: 'FeatureCollection',
//                 features: data.features.filter(function (feature) {
//                     try {
//                         return feature.properties.COUNTYNAME === selectedCity
//                     } catch (e) {
//                         console.log(e)
//                     }
//                 })
//             }
//             // console.log(filteredData)
//             if (geojsonLayer) {
//                 map.removeLayer(geojsonLayer)
//             }
//             geojsonLayer = L.geoJSON(filteredData, {
//                 style: function () {
//                     return {
//                         color: '#ff0000',
//                         weight: 3,
//                         fill: false
//                     }
//                 }
//             }).addTo(map)

//             // 更新地圖中心點
//             if (filteredData.features.length > 0) {
//                 // 選取中的鄉鎮(列表)，fitBounds()
//                 var bounds = geojsonLayer.getBounds()
//                 map.fitBounds(bounds)
//             }
//         })
//         .catch((error) => console.error('Error loading GeoJSON:', error))
// }

// // 當下拉選單的值改變時，更新地圖
// document.getElementById('selectedCity').addEventListener('change', function (e) {
//     var selectedCity = e.target.value
//     updateMap(selectedCity)
// })