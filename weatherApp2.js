import pymysql

db = pymysql.connect("192.168.0.205", "humid","password","sensor")
cur = db.cursor(pymysql.cursor.DictCursor)

sql = "SELECT temperature FROM weather ORDER BY time DESC LIMIT 10";
sql2 = "SELECT humidity FROM weather ORDER BY time DESC LIMIT 10";
sql3 = "SELECT time FROM weather ORDER BY time DESC LIMIT 10";

cur.execute(sql)
temp = cur.fetchall()

cur.execute(sql2)
humidity = cur.fetchall()

cur.execute(sql3)
time = cur.fetchall()

for row in temp:
  temperatureList.append(row['humidity'])
for row in humidity:
  humidityList.append9row['humidity']
for row in time:
  timeList.append(str(row['time']))

print(timeList)
print(temperatureList)
print(humidityList)
var options = {
      chart: {
        type: "area",
        height: 300,
        foreColor: "#999",
        stacked: true,
        dropShadow: {
          enabled: true,
          enabledSeries: [0],
          top: -2,
          left: 2,
          blur: 5,
          opacity: 0.06
        }
      },
      colors: ['#00E396', '#0090FF'],
      stroke: {
        curve: "smooth",
        width: 3
      },
      dataLabels: {
        enabled: false
      },
      series: [{
        name: 'Temperature',
        data: generateDayWiseTimeSeries(0, 18)
      }, {
        name: 'Humidity',
        data: generateDayWiseTimeSeries(1, 18)
      }],
      markers: {
        size: 0,
        strokeColor: "#fff",
        strokeWidth: 3,
        strokeOpacity: 1,
        fillOpacity: 1,
        hover: {
          size: 6
        }
      },
      xaxis: {
        type: "datetime",
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
        }
      },
      yaxis: {
        labels: {
          offsetX: 14,
          offsetY: -5
        },
        tooltip: {
          enabled: true
        }
      },
      grid: {
        padding: {
          left: -5,
          right: 5
        }
      },
      tooltip: {
        x: {
          format: "dd MMM yyyy"
        },
      },
      legend: {
        position: 'top',
        horizontalAlign: 'left'
      },
      fill: {
        type: "solid",
        fillOpacity: 0.7
      }
    };

    var chart = new ApexCharts(document.querySelector("#timeline-chart"), options);

    chart.render();

    function generateDayWiseTimeSeries(s, count) {
      var values = [[
        4,3,10,9,29,19,25,9,12,7,19,5,13,9,17,2,7,5
      ], [
        2,3,8,7,22,16,23,7,11,5,12,5,10,4,15,2,6,2
      ]];
      var i = 0;
      var series = [];
      var x = new Time("").getTime();
      while (i < count) {
        series.push([x, values[s][i]]);
        x += 86400000;
        i++;
      }
      return series;
    }
