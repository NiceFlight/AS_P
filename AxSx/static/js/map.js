// 設定下拉選單
const citySelect = document.getElementById("selectedCity");
const townSelect = document.getElementById("selectedTown");

// 假設有一個 JSON 資料結構，包含縣市與鄉鎮的對應關係
fetch("static/js/city_town_ID.json")
  .then((response) => response.json())
  .then((data) => {
    const cityTowns = data;
    // console.log(cityTowns)

    // 動態填充縣市選項
    for (const city in cityTowns) {
      // console.log(city);
      const option = document.createElement("option");
      option.value = city;
      option.textContent = city;
      citySelect.appendChild(option);
    }

    // 監聽縣市選項的變化
    citySelect.addEventListener("change", () => {
      const selectedCity = citySelect.value;
      const towns = cityTowns[selectedCity];

      // 清空鄉鎮選項
      townSelect.innerHTML = '<option value="">請選擇鄉鎮</option>';

      // 動態填充鄉鎮選項
      towns.forEach((town) => {
        const option = document.createElement("option");
        option.value = town;
        option.textContent = town;
        townSelect.appendChild(option);
      });
      townSelect.disabled = false;
    });
  })
  .catch((error) => console.error("Error:", error));

// 初始化地圖
const map = L.map("map").setView([23.97565, 120.9738819], 8); // 台灣的中心座標

// 添加底圖
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

// 加載外部 GeoJSON 文件
var geojsonLayer;

function updateMap(selectedTown) {
  fetch("/static/js/town.geojson")
    .then((response) => response.json())
    .then((data) => {
      var filteredData = {
        type: "FeatureCollction",
        features: data.features.filter(function (feature) {
          try {
            return (
              feature.properties.TOWNID === selectedTown.split("(")[1].substring(0, 3)
            );
          } catch (e) {
            console.log(e);
          }
        }),
      };
      console.log(filteredData);
      if (geojsonLayer) {
        map.removeLayer(geojsonLayer);
      }
      geojsonLayer = L.geoJSON(filteredData, {
        style: function () {
          return {
            color: "#ff0000",
            weight: 3,
          };
        },
      }).addTo(map);

      // 更新地圖中心點
      if (filteredData.features.length > 0) {
        // 選取中的鄉鎮(列表)，fitBounds()
        var bounds = geojsonLayer.getBounds();
        map.fitBounds(bounds);
      };
    })
    .catch((error) => console.error("Error loading GeoJSON:", error));
}

// 當下拉選單的值改變時，更新地圖
document.getElementById("selectedTown").addEventListener("change", function (e) {
  var selectedTown = e.target.value;
  updateMap(selectedTown);
});
