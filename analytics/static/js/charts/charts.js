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
    const labels = chartData.labels
    const dataset = {
        data: chartData.data,
        backgroundColor: backgrounds,
        borderWidth: 1,
    }
    return makeChart(ctx, 'pie', labels, dataset, options)
}

const verticalBarChart = (ctx, chartData) => {
    const options = {
        legend: {
            display: false,
        },
        scales: {
            xAxes: [{ gridLines: { drawOnChartArea: false } }],
            yAxes: [
                {
                    ticks: { beginAtZero: true },
                    gridLines: { drawOnChartArea: false },
                },
            ],
        },
    }
    const labels = chartData.labels
    const dataset = {
        data: chartData.data,
        backgroundColor: backgrounds,
        borderWidth: 1,
    }
    return makeChart(ctx, 'bar', labels, dataset, options)
}

const horizontalBarChart = (ctx, chartData) => {
    const options = {
        legend: {
            display: false,
        },
        scales: {
            xAxes: [
                {
                    ticks: { beginAtZero: true },
                    gridLines: { drawOnChartArea: false },
                },
            ],
            yAxes: [{ gridLines: { drawOnChartArea: false } }],
        },
    }
    const labels = chartData.labels
    const dataset = {
        data: chartData.data,
        backgroundColor: backgrounds,
        borderWidth: 1,
    }
    return makeChart(ctx, 'horizontalBar', labels, dataset, options)
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
                    ticks: { beginAtZero: true },
                    gridLines: { drawOnChartArea: false },
                },
            ],
            yAxes: [{ gridLines: { drawOnChartArea: false } }],
        },
    }
    const labels = chartData.labels
    const dataset = {
        data: chartData.data,
        backgroundColor: backgrounds[3],
        borderWidth: 3,
        borderColor: backgrounds[3],
        fill: false,
    }
    return makeChart(ctx, 'line', labels, dataset, options)
}

function makeChart(ctx, type, label, dataset, options) {
    return new Chart(ctx, {
        type: type,
        data: {
            labels: label,
            datasets: [dataset],
        },
        options: options,
    })
}
