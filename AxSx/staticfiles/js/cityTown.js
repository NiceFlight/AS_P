// 設定下拉選單
const citySelect = document.getElementById("selectedCity");
const townSelect = document.getElementById("selectedTown");

// 假設有一個 JSON 資料結構，包含縣市與鄉鎮的對應關係
fetch("/static/js/city_town_ID.json")
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
