let weather = {

    fetchWeather: function () {
        fetch(
            "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,rain&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset&current_weather=true&timezone=Europe%2FBerlin"
        )
            .then((response) => response.json())
            .then((data) => this.displayWeather(data));
    },
    displayWeather: function (data) {
        const { name } = data;
        const { speed } = data.daily.windspeed;
        const { tempmin } = data.daily.temperature_2m_min;
        console.log(speed, tempmin)
    }
};
