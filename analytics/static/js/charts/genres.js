const endpoint = '/charts/genres'
const bgColors = [
    'rgba(255, 99, 132, 0.5)',
    'rgba(54, 162, 235, 0.5)',
    'rgba(255, 206, 86, 0.5)',
    'rgba(75, 192, 192, 0.5)',
    'rgba(153, 102, 255, 0.5)',
    'rgba(215, 19, 34, 0.5)',
    'rgba(135, 29, 112, 0.5)',
    'rgba(154, 122, 155, 0.5)',
    'rgba(255, 126, 86, 0.5)',
    'rgba(75, 123, 12, 0.5)',
    'rgba(233, 12, 255, 0.5)',
    'rgba(235, 139, 64, 0.5)',
]

$(document).ready(() => {
    $.ajax({
        method: 'GET',
        url: endpoint,
        success: (response) => initCharts(response),
        error: (error) => {
            alert(error)
        },
    })
})

const initCharts = (response) => {
    const { data, labels } = response
    const chartData = {
        labels: labels,
        datasets: [
            {
                data: data,
                backgroundColor: bgColors,
                borderWidth: 1,
            },
        ],
    }
    let ctx = document.getElementById('genresPieChart').getContext('2d')
    const pieChart = makePieChart(ctx, chartData)
    ctx = document.getElementById('genresBarChart').getContext('2d')
    const barChart = makeBarChart(ctx, chartData)
}

const makePieChart = (ctx, chartData) => {
    const chart = new Chart(ctx, {
        type: 'pie',
        data: chartData,
        options: {
            title: {
                display: false,
                text: '',
                fontSize: 25,
            },
            legend: {
                display: true,
                position: 'right',
            },
        },
    })

    return chart
}

const makeBarChart = (ctx, chartData) => {
    const chart = new Chart(ctx, {
        type: 'bar',
        data: chartData,
        options: {
            legend: {
                display: false,
            },
            scales: {
                yAxes: [
                    {
                        ticks: {
                            beginAtZero: true,
                        },
                    },
                ],
            },
        },
    })

    return chart
}
