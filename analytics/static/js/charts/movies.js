const endpoint = '/charts/imdb'
const bgClolors = [
    'rgba(255, 99, 132, 0.5)',
    'rgba(54, 162, 235, 0.5)',
    'rgba(255, 206, 86, 0.5)',
    'rgba(75, 192, 192, 0.5)',
    'rgba(153, 102, 255, 0.5)',
    'rgba(255, 159, 64, 0.5)',
]
const borderColors = [
    'rgba(255, 99, 132, 1)',
    'rgba(54, 162, 235, 1)',
    'rgba(255, 206, 86, 1)',
    'rgba(75, 192, 192, 1)',
    'rgba(153, 102, 255, 1)',
    'rgba(255, 159, 64, 1)',
]

$(document).ready(() => {
    $.ajax({
        method: 'GET',
        url: endpoint,
        success: (response) => initChart(response),
        error: (error) => {
            alert('Error')
        },
    })
})

const initChart = (response) => {
    const { data, labels } = response
    const ctx = document.getElementById('ratingsChart').getContext('2d')
    const chart = makeChart(ctx, data, labels)
}

const makeChart = (ctx, data, labels) => {
    const chart = new Chart(ctx, {
        type: 'horizontalBar',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Rating',
                    data: data,
                    backgroundColor: bgClolors,
                    borderColor: borderColors,
                    borderWidth: 1,
                },
            ],
        },
        options: {
            title: {
                display: true,
                text: 'IMDb Ratings',
                fontSize: 25,
            },
            legend: {
                display: false,
            },
        },
    })

    return chart
}
