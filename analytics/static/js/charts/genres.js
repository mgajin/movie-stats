import { getChart } from './main.js'

$(document).ready(() => {
    const endpoint = '/charts/genres'
    $.ajax({
        method: 'GET',
        url: endpoint,
        success: (response) => init(response),
        error: (error) => {
            alert(error)
        },
    })
})

const init = (response) => {
    const { data, labels } = response
    const chartData = { data, labels }
    let ctx = document.getElementById('genresPieChart').getContext('2d')
    const pieChart = getChart(ctx, 'pie', chartData)
    ctx = document.getElementById('genresBarChart').getContext('2d')
    const barChart = getChart(ctx, 'verticalBar', chartData)
}
