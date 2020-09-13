import { backgrounds } from './constants.js'

export function getChart(ctx, type, chartData) {
    switch (type) {
        case 'pie':
            return pieChart(ctx, chartData)
        case 'horizontalBar':
            return horizontalBarChart(ctx, chartData)
        case 'verticalBar':
            return verticalBarChart(ctx, chartData)
        case 'line':
            return lineChart(ctx, chartData)
    }
}

const pieChart = (ctx, chartData) => {
    const options = {
        legend: {
            display: true,
            position: 'right',
        },
    }
    return makeChart(ctx, 'pie', chartData, options)
}

const verticalBarChart = (ctx, chartData) => {
    const options = {
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
    }
    return makeChart(ctx, 'bar', chartData, options)
}

const horizontalBarChart = (ctx, chartData) => {
    const options = {
        legend: {
            display: false,
        },
        scales: {
            xAxes: [
                {
                    ticks: {
                        beginAtZero: true,
                    },
                },
            ],
        },
    }
    return makeChart(ctx, 'horizontalBar', chartData, options)
}

const lineChart = (ctx, chartData) => {
    const options = {
        legend: {
            display: false,
        },
        fill: false,
        scales: {
            xAxes: [
                {
                    ticks: {
                        beginAtZero: true,
                    },
                },
            ],
        },
    }
    return makeChart(ctx, 'line', chartData, options)
}

function makeChart(ctx, type, chartData, options) {
    return new Chart(ctx, {
        type: type,
        data: {
            labels: chartData.labels,
            datasets: [
                {
                    data: chartData.data,
                    backgroundColor: backgrounds,
                    borderWidth: 1,
                },
            ],
        },
        options: options,
    })
}
