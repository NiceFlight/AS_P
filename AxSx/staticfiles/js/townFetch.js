import { map } from "./map.js";

let geojsonLayer = null;
const townSelect = document.getElementById("selectedTown");

document.getElementById("selectedTown").addEventListener("change", function () {
  var filterTown = townSelect.value.split("(")[1].substring(0, 3);
  // console.log(townSelect.value.slice(-4, -1))
  // 異步請求，將選擇的資料送到後端伺服器查詢
  fetch("api/views_AxSx/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      // 以下二擇一
      "X-CSRFToken": window.csrfToken, // Django template 渲染時注入的變數{{ csrf_token }}
      // "X-CSRFToken": csrf_token(), // 從 document.cookie 找出名為 csrftoken 的值
    },
    body: JSON.stringify({ filterTown: filterTown }),
  })
    .then((response) => response.json()) // 後端伺服器回傳查詢結果並 Json 格式化
    .then((data) => {
      // 在地圖上標記
      if (data.status === "success") {
        var coordinates = data.coordinates;
        var filterData = data.filterData;

        // 清除geojsonLayer
        if (geojsonLayer) {
          map.removeLayer(geojsonLayer);
        }

        geojsonLayer = L.geoJSON(filterData, {
          style: function () {
            return {
              color: "#ff0000",
              weight: 3,
            };
          },
        }).addTo(map);

        // 更新邊界
        var bounds = geojsonLayer.getBounds();
        map.fitBounds(bounds);

        // 清除標記
        map.eachLayer(function (layer) {
          if (layer instanceof L.Marker) {
            map.removeLayer(layer);
          }
        });
        coordinates.forEach(function (coord) {
          var marker = L.marker([coord.lat, coord.lng]).addTo(map).bindPopup(`<h3>${coord.name}</h3>`);
          marker.on("mouseover", function () {
            this.openPopup();
          });
          marker.on("mouseout", function () {
            this.closePopup();
          });
          // 列出標記
          const locationList = document.getElementById("location-list");
          locationList.innerHTML = "";
          data.coordinates.forEach((location) => {
            const listItem = document.createElement("li");
            listItem.textContent = `${location.name}`;
            locationList.appendChild(listItem);
          });
        });
      } else {
        console.error("error:", data.error);
      }
    })
    .catch((error) => console.error("Error:", error));
});
